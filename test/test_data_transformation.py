from src.exception.exception import customexception
import pytest
from src.data.data_transformation import *  # Importing all from the source module, DataTransformation
def test_dummy():
	assert True
# Test generated using Keploy
def test_initialize_data_transformation_missing_train_file(tmp_path):
    # Arrange
    test_csv = tmp_path / "test.csv"
    test_csv.write_text("Feature1,Feature2,Price\n4,D,400\n5,E,500")
    data_transformation = DataTransformation()
    # Act & Assert
    with pytest.raises(customexception):
        data_transformation.initialize_data_transformation(
            train_path="non_existent_train.csv", test_path=str(test_csv)
        )
# Test generated using Keploy
def test_initialize_data_transformation_missing_target_column(tmp_path):
    # Arrange
    train_csv = tmp_path / "train.csv"
    test_csv = tmp_path / "test.csv"
    train_csv.write_text("Feature1,Feature2\n1,A\n2,B\n3,C")
    test_csv.write_text("Feature1,Feature2,Price\n4,D,400\n5,E,500")
    data_transformation = DataTransformation()
    # Act & Assert
    with pytest.raises(customexception):
        data_transformation.initialize_data_transformation(
            train_path=str(train_csv), test_path=str(test_csv)
        )
# Test generated using Keploy
def test_initialize_data_transformation_missing_numerical_columns(tmp_path):
    # Arrange
    train_csv = tmp_path / "train.csv"
    test_csv = tmp_path / "test.csv"
    train_csv.write_text("Feature1,Feature2,Price\nA,B,100\nC,D,200")
    test_csv.write_text("Feature1,Feature2,Price\nE,F,300\nG,H,400")
    data_transformation = DataTransformation()
    # Act & Assert
    with pytest.raises(customexception):
        data_transformation.initialize_data_transformation(
            train_path=str(train_csv), test_path=str(test_csv)
        )