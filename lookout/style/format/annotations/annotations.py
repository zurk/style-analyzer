"""Annotations for style-analyzer."""
from typing import Optional, Tuple


class Annotation:
    """Base class for annotation."""

    def __init__(self, start: int, stop: int):
        """
        Initialization.

        :param start: Annotation start.
        :param stop: Annotation end.
        """
        self._range = (start, stop)
        self._start = start
        self._stop = stop

    start = property(lambda self: self._start)

    stop = property(lambda self: self._stop)

    range = property(lambda self: self._range)

    name = property(lambda self: type(self).__name__)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "%s[%d, %d)" % (self.name, self.start, self.stop)


class AtomicTokenAnnotation(Annotation):
    """Infrangible сode token annotation."""


class LineAnnotation(Annotation):
    """Line number annotation."""

    def __init__(self, start: int, stop: int, number: int):
        """Init."""
        super().__init__(start, stop)
        self._number = number

    number = property(lambda self: self._number)


class UASTNodeAnnotation(Annotation):
    """UAST Node annotation."""

    def __init__(self, start: int, stop: int, node: "bblfsh.Node"):
        """Init."""
        super().__init__(start, stop)
        self._node = node

    node = property(lambda self: self._node)

    @staticmethod
    def from_node(node: "bblfsh.Node") -> "UASTNodeAnnotation":
        """Create the annotation from bblfsh node."""
        return UASTNodeAnnotation(node.start_position.offset, node.end_position.offset, node)


# Should be removed when overlapping annotations of one type are allowed.
class UASTAnnotation(UASTNodeAnnotation):
    """Full UAST of the file annotation."""

    uast = property(lambda self: self._node)


class TokenAnnotation(Annotation):
    """Virtual сode token annotation."""

    def __init__(self, start: int, stop: int,
                 uast_annotation: Optional[UASTNodeAnnotation] = None):
        """
        Initialization.

        :param start: Annotation start.
        :param stop: Annotation end.
        :param uast_annotation: Related UASTNodeAnnotation Annotation if applicable.
        """
        super().__init__(start, stop)
        self._uast_annotation = uast_annotation

    uast_annotation = property(lambda self: self._uast_annotation)

    @property
    def node(self) -> "bblfsh.Node":
        """
        Get UAST Node from related UASTNodeAnnotation.

        :return: related bblfsh UAST Node. None if there is no related annotation.
        """
        return self._uast_annotation.node if self._uast_annotation else None

    @property
    def has_node(self) -> bool:
        """Check if token annotation has related UAST node annotation."""
        return self._uast_annotation is None


class LanguageAnnotation(Annotation):
    """Language of the file annotation."""

    def __init__(self, start: int, stop: int, language: str):
        """Init."""
        super().__init__(start, stop)
        self._language = language

    language = property(lambda self: self._language)


class PathAnnotation(Annotation):
    """File language annotation."""

    def __init__(self, start: int, stop: int, path: str):
        """Init."""
        super().__init__(start, stop)
        self._path = path

    path = property(lambda self: self._path)


class AccumulatedIntentationAnnotation(Annotation):
    """Accumulated indentation annotation for the spaces in the beggining of the line."""


class TargetAnnotation(Annotation):
    """Target for model prediction annotation."""

    def __init__(self, start: int, stop: int, target: Tuple[int, ...]):
        """Init."""
        super().__init__(start, stop)
        self._target = target

    target = property(lambda self: self._target)
