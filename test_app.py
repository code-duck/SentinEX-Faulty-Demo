import unittest
from types import SimpleNamespace
from unittest.mock import patch

from app import run_command


class RunCommandTests(unittest.TestCase):
    @patch("app.subprocess.run")
    def test_runs_argument_list_without_a_shell(self, run):
        run.return_value = SimpleNamespace(stdout="ok\n")
        self.assertEqual(run_command(["echo", "ok"]), "ok")
        run.assert_called_once_with(
            ["echo", "ok"],
            shell=False,
            check=True,
            capture_output=True,
            text=True,
        )


if __name__ == "__main__":
    unittest.main()
