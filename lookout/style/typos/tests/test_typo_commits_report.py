import json
import logging
import lzma
from pathlib import Path
import unittest
from unittest import mock

import bblfsh
from lookout.core.analyzer import ReferencePointer
from lookout.core.api.service_data_pb2 import Change, File
from lookout.sdk.service_analyzer_pb2 import Comment

from lookout.style.format.benchmarks.general_report import FakeDataService
from lookout.style.typos.analyzer import TypoFix
from lookout.style.typos.benchmarks.typo_commits_report import TypoCommitsReporter, \
    TyposAnalyzerSpy
from lookout.style.typos.tests.test_analyzer import MODEL_PATH
from lookout.style.typos.utils import Candidate


def fake_review(*args, **kwargs):
    yield Comment(text=json.dumps(TypoFix("", "", 1, "triggered", {}, [])._asdict()))


class TypoCommitsReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO)
        logging.getLogger("IdTyposAnalyzer").setLevel(logging.DEBUG)
        base = Path(__file__).parent
        # str() is needed for Python 3.5
        cls.bblfsh_client = bblfsh.BblfshClient("0.0.0.0:9432")
        with lzma.open(str(base / "test_base_file.js.xz")) as fin:
            contents = fin.read()
            uast = cls.bblfsh_client.parse("test_base_file.js", contents=contents).uast
            cls.base_files = [File(path="test_base_file.js", content=contents, uast=uast,
                                   language="Javascript")]
        with lzma.open(str(base / "test_head_file.js.xz")) as fin:
            contents = fin.read()
            uast = cls.bblfsh_client.parse("test_head_file.js", contents=contents).uast
            cls.head_files = [File(path="test_head_file.js", content=contents, uast=uast,
                                   language="Javascript")]
        cls.ptr = ReferencePointer("someurl", "someref", "somecommit")

    @classmethod
    def tearDownClass(cls):
        cls.bblfsh_client._channel.close()

    def check_candidate(self, candidate: Candidate):
        self.assertIsInstance(candidate, Candidate)
        self.assertIsInstance(candidate.token, str)
        self.assertGreater(len(candidate.token), 0)
        self.assertGreater(candidate.confidence, 0)

    def check_typo_fix(self, typo_fix: TypoFix):
        content = typo_fix.content.splitlines()
        self.assertIsInstance(typo_fix, TypoFix)
        self.assertIsInstance(typo_fix.path, str)
        self.assertNotEqual(typo_fix.path, "")
        self.assertGreater(typo_fix.line_number, 0)
        self.assertIn(typo_fix.identifier, content[typo_fix.line_number - 1])
        self.assertIn(typo_fix.identifier, content[typo_fix.line_number - 1])
        for candidate in typo_fix.candidates:
            self.check_candidate(candidate)

    def test_run(self):
        dataservice = FakeDataService(
            self.bblfsh_client, files=self.head_files,
            changes=[Change(base=self.base_files[0], head=self.head_files[0])])
        model = TyposAnalyzerSpy.train(ptr=self.ptr, config={}, data_service=dataservice)
        analyzer = TyposAnalyzerSpy(model=model, url=self.ptr.url, config=dict(
            model=MODEL_PATH, confidence_threshold=0.0, n_candidates=3))
        typo_fixes = list(analyzer.run(ptr=self.ptr, data_service=dataservice))
        self.assertGreater(len(typo_fixes), 0)
        for typo_fix in typo_fixes:
            self.check_typo_fix(typo_fix)

    def test_analyze(self):
        dataservice = FakeDataService(
            self.bblfsh_client, files=self.head_files,
            changes=[Change(base=self.base_files[0], head=self.head_files[0])])
        model = TyposAnalyzerSpy.train(ptr=self.ptr, config={}, data_service=dataservice)
        analyzer = TyposAnalyzerSpy(model=model, url=self.ptr.url, config=dict(
            model=MODEL_PATH, confidence_threshold=0.0, n_candidates=3))
        comments = analyzer.analyze(ptr_from=self.ptr, ptr_to=self.ptr, data_service=dataservice)
        self.assertGreater(len(comments), 0)
        for comment in comments:
            self.assertIsInstance(comment, Comment)
            typo_fix_dict = json.loads(comment.text)
            for token in typo_fix_dict["candidates"]:
                typo_fix_dict["candidates"][token] = [Candidate(*candidate) for candidate in
                                                      typo_fix_dict["candidates"][token]]
            typo_fix_dict["identifier_candidates"] = [
                Candidate(*candidate) for candidate in typo_fix_dict["identifier_candidates"]]
            typo_fix = TypoFix(**typo_fix_dict)
            self.check_typo_fix(typo_fix)

    @mock.patch("lookout.core.helpers.analyzer_context_manager.AnalyzerContextManager.review",
                side_effect=fake_review)
    def test_trigger_review_event(self, func):
        with TypoCommitsReporter() as reporter:
            dataset_row = {"repo": "", "commit": ""}
            typos_fix = reporter._trigger_review_event(dataset_row)
            self.assertEqual(len(typos_fix), 1)
            self.assertEqual(typos_fix[0].identifier, "triggered")

    @mock.patch("lookout.style.typos.benchmarks.typo_commits_report."
                "TypoCommitsReporter._get_package_version")
    @mock.patch("lookout.style.typos.benchmarks.typo_commits_report."
                "TypoCommitsReporter._get_commit")
    def test_finalize(self, get_fake_commit, get_fake_package_version):
        get_fake_commit.return_value = "<fake commit>"
        get_fake_package_version.return_value = "<fake version>"
        reports = [
            {'detection_false_negatives': 0.0,
             'detection_false_positive': 0.0,
             'detection_precision': 0.0,
             'detection_recall': 0.0,
             'detection_true_positive': 1.0,
             'fix_accuracy': 0.0,
             'review_time': 0.0,
             'support': 4.0,
             'top3_fix_accuracy': 1.0},
            {'detection_false_negatives': 1.0,
             'detection_false_positive': 1.0,
             'detection_precision': 0.0,
             'detection_recall': 0.0,
             'detection_true_positive': 0.0,
             'fix_accuracy': 0.0,
             'review_time': 0.0,
             'support': 4.0,
             'top3_fix_accuracy': 0.0},
            {'detection_false_negatives': 0.0,
             'detection_false_positive': 0.0,
             'detection_precision': 0.0,
             'detection_recall': 0.0,
             'detection_true_positive': 1.0,
             'fix_accuracy': 0.0,
             'review_time': 0.0,
             'support': 4.0,
             'top3_fix_accuracy': 1.0}
        ]
        reporter = TypoCommitsReporter()
        reporter._fails = {10: {"repo": "<Failed repo name>"}}
        final_report = list(reporter._finalize(json.dumps({"report": report})
                                               for report in reports))
        self.assertEqual(len(final_report), 1)
        self.assertIsInstance(final_report[0], str)

        correct_report = """
# Report for the commits with typo dataset

## Metrics

|              metric | value   |
|--------------------:|:--------|
| detection_precision | 0.667   |
|    detection_recall | 0.667   |
|        fix_accuracy | 0.000   |
|   top3_fix_accuracy | 0.667   |
|             support | 12.000  |
|         review_time | 0.000   |

Report generation failed for
10. <Failed repo name>

## Versions

* Style-analyzer package version is <fake version>
* Commit is <fake commit>
""".strip()

        self.assertEqual(correct_report, final_report[0].strip())

    def test_generate_commit_dataset_report(self):
        reporter = TypoCommitsReporter()
        reporter._review_time = 0
        dataset_row = {
            "repo": "name",
            "correct id": "length",
            "wrong id": "lenght",
        }
        fixes_and_res = [
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("length", 0.9)], identifiers_number=4),
             {'detection_false_negatives': 0.0,
              'detection_false_positive': 0.0,
              'detection_precision': 0.0,
              'detection_recall': 0.0,
              'detection_true_positive': 1.0,
              'fix_accuracy': 0.0,
              'review_time': 0.0,
              'support': 4.0,
              'top3_fix_accuracy': 1.0}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="end",
                     candidates=[Candidate("ends", 0.9)], identifiers_number=4),
             {'detection_false_negatives': 1.0,
              'detection_false_positive': 1.0,
              'detection_precision': 0.0,
              'detection_recall': 0.0,
              'detection_true_positive': 0.0,
              'fix_accuracy': 0.0,
              'review_time': 0.0,
              'support': 4.0,
              'top3_fix_accuracy': 0.0}

             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("lenght", 0.9), Candidate("length", 0.9)],
                     identifiers_number=4),
             {'detection_false_negatives': 0.0,
              'detection_false_positive': 0.0,
              'detection_precision': 0.0,
              'detection_recall': 0.0,
              'detection_true_positive': 1.0,
              'fix_accuracy': 0.0,
              'review_time': 0.0,
              'support': 4.0,
              'top3_fix_accuracy': 1.0}
             ),
        ]
        for fix, correct_scores in fixes_and_res:
            scores = json.loads(reporter.generate_commit_dataset_report(dataset_row, [fix]))
            self.assertEqual(scores, correct_scores)

        with self.assertRaises(ValueError):
            json.loads(reporter.generate_commit_dataset_report(dataset_row, []))


if __name__ == "__main__":
    unittest.main()
