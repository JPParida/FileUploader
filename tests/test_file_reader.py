"""Test File Reader"""

import pytest
from uploader.file_reader import FileReader

def test_file_reader(tmp_path):
    """
    Test case for FileReader.get_files method

    Args:
        tmp_path(pathlib.Path): Temporary directory path provided by pytest.
    """

    # create temporary directory and file
    file_dir = tmp_path / "test_path"
    file_dir.mkdir()
    file_path = file_dir / "test_file.txt"
    file_path.write_text("test_content")

    file_reader = FileReader(file_path)
    files = file_reader.get_files()

    assert len(files) == 1
    assert files[0] == str(file_path)