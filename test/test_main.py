import os
import pytest
from main import *  # Importing all from the source module, add_numbers
def test_dummy():
	assert True
# Test generated using Keploy
def test_add_numbers_positive_integers():
    result = add_numbers(3, 5)
    assert result == 8, "Expected sum of 3 and 5 to be 8"
# Test generated using Keploy
def test_serve_homepage_file_not_found(monkeypatch):
    # Mock os.getcwd to return a temporary directory
    monkeypatch.setattr("os.getcwd", lambda: "/tmp")
    # Mock the open function to raise a FileNotFoundError
    def mock_open(file_path, mode):
        raise FileNotFoundError("File not found")
    monkeypatch.setattr("builtins.open", mock_open)
    try:
        serve_homepage()
    except FileNotFoundError as e:
        assert str(e) == "File not found"