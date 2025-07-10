import subprocess
import sys


def test_html_clean():
    cmd = ["tidy", "-q", "-errors", "index.html"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert result.stdout.strip() == "", f"tidy reported issues:\n{result.stdout}"

