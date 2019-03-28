import json
import tempfile
import unittest
from unittest import mock

from modelforge import slogging

from lookout.style.cloner import Cloner
from lookout.style.format.tests.test_quality_report import Capturing

downloaded_repos = []


def fake_clone(repo, git_dir: str):
    downloaded_repos.append(repo)


def fake_exists(path: str) -> bool:
    if path == "existing_repo":
        return True
    if path != "downloaded_repo" and path.endswith("downloaded_repo"):
        return True
    return False


class FakePool:
    def __init__(self, proc):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    map = map


class ClonerTests(unittest.TestCase):
    @mock.patch("multiprocessing.Pool", side_effect=FakePool)
    @mock.patch("os.path.exists", side_effect=fake_exists)
    @mock.patch("dulwich.porcelain.clone", side_effect=fake_clone)
    def test_cloner(self, f1, f2, f3):
        slogging.setup("DEBUG", True)
        with Capturing() as output:
            with tempfile.TemporaryDirectory() as tmp_dir:
                cloner = Cloner(tmp_dir)
                cloner.clone(
                    ["repo1", "repo2", "repo3", "existing_repo", "downloaded_repo"])
        expected_log = [
            "start cloning 5 repositories",
            "repo1 was cloned to",
            "repo2 was cloned to",
            "repo3 was cloned to",
            "existing_repo exists",
            "downloaded_repo was found at",
            "successfully cloned 5/5 repositories",
        ]
        for expected_msg, log_entry in zip(expected_log, output):
            self.assertEqual(expected_msg, json.loads(log_entry)["msg"][:len(expected_msg)])

        self.assertEqual(set(downloaded_repos), {"repo1", "repo2", "repo3"})

    def test_get_repo_name(self):
        self.assertEqual(Cloner.get_repo_name("https://github.com/src-d/style-analyzer"),
                         "src-d-style-analyzer")
        self.assertEqual(Cloner.get_repo_name("src-d/style-analyzer"), "src-d-style-analyzer")
        self.assertEqual(Cloner.get_repo_name("style-analyzer"), "style-analyzer")


if __name__ == "__main__":
    unittest.main()
