from typing import Dict, Iterable, Iterator, Optional, Sequence, Tuple, Union, Any, Type  # noqa F401

from lookout.sdk.service_data_pb2 import File
from sortedcontainers import SortedDict

from lookout.style.format.annotations.annotations import Annotation, LanguageAnnotation, \
    PathAnnotation, UASTAnnotation


class NoIntersection(Exception):
    """Raises by AnnotatedData.find_intersect() if there is no intersection."""


class AnnotationsSlice(dict):
    """
    Annotations collection for a specific range.
    """

    def __init__(self, start, stop, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self._range = (start, stop)
        self._start = start
        self._stop = stop

    start = property(lambda self: self._start)

    stop = property(lambda self: self._stop)

    range = property(lambda self: self._range)


class AnnotatedData:
    """
    Class that couples annotations and data together.

    All special utilities to work with annotations should be implemented in this class
    List of methods that should be implemented can be found here:
    https://uima.apache.org/d/uimafit-current/api/org/apache/uima/fit/util/JCasUtil.html
    """

    def __init__(self, content: str):
        """
        Init.

        :param content: Data to annotate. It is expected to be string but actually can be any type
        with __getitem__() defined for int and slice input arguments.
        """
        self._content = content

        self._range_to_annotations = SortedDict()  # type: SortedDict[(int, int), Dict[Type[Annotation], Annotation]]  # noqa E501
        self._type_to_annotations = {}  # type: Dict[Type[Annotation], SortedDict[(int, int), Annotation]]  # noqa E501

    content = property(lambda self: self._content)

    def __getitem__(self, item: Union[int, slice, Tuple[int, int]]) -> Any:
        if isinstance(item, tuple):
            item = slice(*item)
        if isinstance(item, slice) and item.step is not None:
            raise KeyError("slice.step is not supported.")
        return self._content[item]

    def add(self, annotation: Annotation) -> None:
        """
        Add annotation.
        """
        annotation_id = type(annotation)
        # TODO(zurk): Add a check that there is no overlapping annotations of one type.
        if annotation.range not in self._range_to_annotations:
            self._range_to_annotations[annotation.range] = {}
        if annotation_id not in self._type_to_annotations:
            self._type_to_annotations[annotation_id] = SortedDict()
        self._range_to_annotations[annotation.range][annotation_id] = annotation
        self._type_to_annotations[annotation_id][annotation.range] = annotation

    def update(self, annotations: Iterable[Annotation]) -> None:
        """
        Update with annotations.
        """
        for annotation in annotations:
            self.add(annotation)

    def iget(self, annotation_type: Type[Annotation], index: int) -> Annotation:
        """
        Return an annotation and for given type and index.
        """
        return self._type_to_annotations[annotation_type].peekitem(index)[1]

    def iter_annotation(self, name: str, start_offset: Optional[int] = None,
                        stop_offset: Optional[int] = None) -> Iterator[Annotation]:
        """
        Iterate through specific annotation atomic_tokens, ys, files, etc.

        Returns slice of RawData and its annotation.
        """
        if start_offset is not None or stop_offset is not None:
            raise NotImplementedError()

        for value in self._type_to_annotations[name].values():
            yield value

    def iter_annotations(self, types: Sequence[Type[Annotation]],
                         start_offset: Optional[int] = None, stop_offset: Optional[int] = None,
                         ) -> Iterator[AnnotationsSlice]:
        """
        Iterate through annotations with specified type.

        :return: Requested annotations slice.
        """
        if start_offset is not None or stop_offset is not None:
            raise NotImplementedError()

        types_set = frozenset(types)
        for annotation0 in self.iter_annotation(types[0]):
            # Annotations with the same range
            same_range_annotations = self._range_to_annotations[annotation0.range]
            same_range_names = set(same_range_annotations.keys())
            common = types_set & same_range_names
            missing = types_set - same_range_names
            annotations = dict()
            for type in missing:
                try:
                    annotations[type] = self.find_intersect(type, *annotation0.range)
                except NoIntersection:
                    pass
            annotations.update({type: same_range_annotations[type] for type in common})
            yield AnnotationsSlice(*annotation0.range, annotations)

    def iter_items(self, types: Sequence[Type[Annotation]], start_offset: Optional[int] = None,
                   stop_offset: Optional[int] = None,
                   ) -> Iterator[Tuple[str, AnnotationsSlice]]:
        """
        Iterate through annotations with specified type.

        :return: Annotated data slice with requested annotations.
        """
        for annotations in self.iter_annotations(types, start_offset, stop_offset):
            yield self[annotations.range], annotations

    def find_intersect(self, name: str, start: int, stop: int) -> Annotation:
        """
        Find an annotation of given type that intersects the interval [start, stop).

        raises NoIntersection exception if there is no such annotation.

        :param name: Annotation type.
        :param start: start of interval.
        :param stop: end of interval.
        :return: requested Annotation.
        """
        try:
            annotation_layer = self._type_to_annotations[name]
        except KeyError:
            raise NoIntersection("There is no annotation layer %s" % name)
        search_start = max(0, annotation_layer.bisect_left((start, start)) - 1)
        search_stop = annotation_layer.bisect_right((stop, stop))
        for range in annotation_layer.islice(search_start, search_stop):
            if self._check_interval_crossing(start, stop, *range):
                # assuming that there is only one such annotation
                return annotation_layer[range]
        raise NoIntersection("There is no annotation %s from %d to %d" % (name, start, stop))

    @classmethod
    def _check_interval_crossing(cls, start1: int, stop1: int, start2: int, stop2: int) -> bool:
        # TODO(zurk): explain logic with [x, x) intervals.
        if start1 == stop1:
            if start2 == stop2:
                return start1 == start2
            else:
                return start2 < start1 < stop2
        else:
            if start2 == stop2:
                return start1 < start2 < stop1
            else:
                return (start1 <= start2 < stop1 or
                        start1 < stop2 < stop1 or
                        start2 <= start1 < stop2)

    def subiter_annotation(self, name: str, covering_annotation: Annotation):
        """TODO."""
        raise NotImplementedError()

    def sub_iter_annotations(self, names: Sequence[str], covering_annotation: Annotation):
        """TODO."""
        raise NotImplementedError()

    @classmethod
    def from_file(cls, file: File) -> "AnnotatedData":
        """
        Create AnnotatedData instance from File.

        :param file: file.content will be used as data to be annotated with \
                     file.path, file.language and file.uast.
        :return: new AnnotatedData instance.
        """
        raw_data = file.content.decode("utf-8", "replace")
        annotated_data = AnnotatedData(raw_data)
        annotated_data.add(PathAnnotation(0, len(raw_data), file.path))
        annotated_data.add(UASTAnnotation(0, len(raw_data), file.uast))
        annotated_data.add(LanguageAnnotation(0, len(raw_data), file.language))
        return annotated_data
