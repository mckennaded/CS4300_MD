import pytest
from src.task6 import count_words

def test_count_words(tmp_path):
    # Create temporary file with known content
    file = tmp_path / "testfile.txt"
    file.write_text("This is a test file with nine words total.")
    assert count_words(str(file)) == 9
