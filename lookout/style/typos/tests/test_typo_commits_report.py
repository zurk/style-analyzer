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

    # def check_candidate(self, candidate: Candidate):
    #     self.assertIsInstance(candidate, Candidate)
    #     self.assertIsInstance(candidate.token, str)
    #     self.assertGreater(len(candidate.token), 0)
    #     self.assertGreater(candidate.confidence, 0)
    #
    # def check_typo_fix(self, typo_fix: TypoFix):
    #     content = typo_fix.content.splitlines()
    #     self.assertIsInstance(typo_fix, TypoFix)
    #     self.assertIsInstance(typo_fix.path, str)
    #     self.assertNotEqual(typo_fix.path, "")
    #     self.assertGreater(typo_fix.line_number, 0)
    #     self.assertIn(typo_fix.identifier, content[typo_fix.line_number - 1])
    #     self.assertIn(typo_fix.identifier, content[typo_fix.line_number - 1])
    #     for candidate in typo_fix.candidates:
    #         self.check_candidate(candidate)
    #
    # def test_run(self):
    #     dataservice = FakeDataService(
    #         self.bblfsh_client, files=self.head_files,
    #         changes=[Change(base=self.base_files[0], head=self.head_files[0])])
    #     model = TyposAnalyzerSpy.train(ptr=self.ptr, config={}, data_service=dataservice)
    #     analyzer = TyposAnalyzerSpy(model=model, url=self.ptr.url, config=dict(
    #         model=MODEL_PATH, confidence_threshold=0.0, n_candidates=3))
    #     typo_fixes = list(analyzer.run(ptr=self.ptr, data_service=dataservice))
    #     self.assertGreater(len(typo_fixes), 0)
    #     for typo_fix in typo_fixes:
    #         self.check_typo_fix(typo_fix)
    #
    # def test_analyze(self):
    #     dataservice = FakeDataService(
    #         self.bblfsh_client, files=self.head_files,
    #         changes=[Change(base=self.base_files[0], head=self.head_files[0])])
    #     model = TyposAnalyzerSpy.train(ptr=self.ptr, config={}, data_service=dataservice)
    #     analyzer = TyposAnalyzerSpy(model=model, url=self.ptr.url, config=dict(
    #         model=MODEL_PATH, confidence_threshold=0.0, n_candidates=3))
    #     comments = analyzer.analyze(ptr_from=self.ptr, ptr_to=self.ptr, data_service=dataservice)
    #     self.assertGreater(len(comments), 0)
    #     for comment in comments:
    #         self.assertIsInstance(comment, Comment)
    #         typo_fix_dict = json.loads(comment.text)
    #         for token in typo_fix_dict["candidates"]:
    #             typo_fix_dict["candidates"][token] = [Candidate(*candidate) for candidate in
    #                                                   typo_fix_dict["candidates"][token]]
    #         typo_fix_dict["identifier_candidates"] = [
    #             Candidate(*candidate) for candidate in typo_fix_dict["identifier_candidates"]]
    #         typo_fix = TypoFix(**typo_fix_dict)
    #         self.check_typo_fix(typo_fix)
    #
    # @mock.patch("lookout.core.helpers.analyzer_context_manager.AnalyzerContextManager.review",
    #             side_effect=fake_review)
    # def test_trigger_review_event(self, func):
    #     with TypoCommitsReporter() as reporter:
    #         dataset_row = {"repo": "", "commit": ""}
    #         typos_fix = reporter._trigger_review_event(dataset_row)
    #         self.assertEqual(len(typos_fix), 1)
    #         self.assertEqual(typos_fix[0].identifier, "triggered")
    #
    # def test_finalize(self):
    #     pass

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
             {}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="end",
                     candidates=[Candidate("ends", 0.9)], identifiers_number=4),
             {}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("lenght", 0.9), Candidate("length", 0.9)],
                     identifiers_number=4),
             {}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("length", 0.9)], identifiers_number=4),
             {}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("length", 0.9)], identifiers_number=4),
             {}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("length", 0.9)], identifiers_number=4),
             {}
             ),
            (TypoFix(content="start lenght end", path="test", line_number=1, identifier="lenght",
                     candidates=[Candidate("length", 0.9)], identifiers_number=4),
             {}
             ),
        ]
        for fix, correct_scores in fixes_and_res:
            scores = json.loads(reporter.generate_commit_dataset_report(dataset_row, [fix]))

            import pprint
            pprint.pprint(scores)

        scores_for_empty = json.loads(reporter.generate_commit_dataset_report(dataset_row, []))


if __name__ == "__main__":
    unittest.main()
