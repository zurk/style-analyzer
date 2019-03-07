import unittest

from lookout.style.format.annotations.annotated_data import AnnotatedData, AnnotationsSlice
from lookout.style.format.annotations.annotations import PathAnnotation, TokenAnnotation


class AnnotationsTests(unittest.TestCase):
    def test_annotations(self):
        code = "0123456789"
        annotated_data = AnnotatedData(code)
        token_annotations = [TokenAnnotation(0, 3), TokenAnnotation(3, 3), TokenAnnotation(3, 4)]
        path_annotation = PathAnnotation(0, len(code), "1")
        annotated_data.update(token_annotations)
        annotated_data.add(path_annotation)
        annotations = list(annotated_data.iter_items([TokenAnnotation, PathAnnotation]))
        res = list(zip(("012", "", "3"),
                       (AnnotationsSlice(0, 3, {TokenAnnotation: token_annotations[0],
                                                PathAnnotation: path_annotation}),
                        AnnotationsSlice(3, 3, {TokenAnnotation: token_annotations[1],
                                                PathAnnotation: path_annotation}),
                        AnnotationsSlice(3, 4, {TokenAnnotation: token_annotations[2],
                                                PathAnnotation: path_annotation}))))
        self.assertEqual(annotations, res)

    def test_check_interval_crossing(self):
        data = [
            ((9, 19), (19, 20), False),
            ((19, 20), (9, 19), False),
            ((1, 3), (2, 4), True),
            ((2, 4), (1, 3), True),
            ((-2, 4), (1, 3), True),
            ((-2, 3), (1, 3), True),
            ((1, 3), (1, 3), True),
            ((1, 3), (6, 7), False),
            ((10, 30), (6, 7), False),
            ((10, 10), (10, 10), True),
            ((10, 30), (10, 10), False),
            ((10, 10), (10, 30), False),
            ((10, 10), (5, 30), True),
            ((5, 30), (10, 10), True),
        ]
        for i, (interval1, interval2, res) in enumerate(data):
            self.assertEqual(AnnotatedData._check_interval_crossing(*interval1, *interval2),
                             res, "Case # %d" % i)


if __name__ == "__main__":
    unittest.main()
