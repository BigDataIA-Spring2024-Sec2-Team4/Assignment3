from pydantic import BaseModel, ValidationError
import pytest
import csv
from io import StringIO

class MetaDataPDF(BaseModel):
    file_name: str
    language: str
    version: int
    encoding: str
    file_size: int

class MetaDataPDFClass:
    def __init__(self, file_name, language, version, encoding, file_size):
        try:
            metadata = MetaDataPDF(
                file_name=file_name,
                language=language,
                version=version,
                encoding=encoding,
                file_size=file_size
            )
            self.metadata = metadata
        except ValidationError as e:
            raise ValueError(f"Invalid metadata: {e}")

    def display_metadata(self):
        print(f"File Name: {self.metadata.file_name}")
        print(f"Language: {self.metadata.language}")
        print(f"Version: {self.metadata.version}")
        print(f"Encoding: {self.metadata.encoding}")
        print(f"File Size: {self.metadata.file_size} bytes")

def csv_to_stringio(csv_data):
    return StringIO(csv_data)

def run_tests_with_csv(csv_data):
    csv_file = csv_to_stringio(csv_data)
    result_code = pytest.main(['-s', '-q', __file__])

    if result_code != 0:
        print("Some tests failed. Please check the output for details.")
    else:
        print("All tests passed successfully.")

def read_csv_file(input_file):
    with open(input_file, 'r') as csv_input:
        return csv_input.read()

def write_clean_csv(output_file, clean_data):
    with open(output_file, 'w', newline='') as csv_output:
        csv_output.write(clean_data)

input_csv_file = 'metadata.csv'
output_csv_file = 'validated_output.csv'

input_csv_data = read_csv_file("metadata.csv")

run_tests_with_csv(input_csv_data)

cleaned_data = ""
reader = csv.DictReader(csv_to_stringio(input_csv_data))
fieldnames = reader.fieldnames

for row in reader:
    print("Processing row:", row)
    try:
        metadata_instance = MetaDataPDFClass(**row)
        cleaned_data += ','.join(str(getattr(metadata_instance.metadata, field.lower())) for field in fieldnames) + '\n'
    except ValueError as e:
        print(f"Error processing row: {e}")

# Write clean data to the output CSV file
output_csv_path = "validated_output.csv" # defining absolute path + output_csv_file
try:
    write_clean_csv(output_csv_path, cleaned_data)
    print(f"Cleaned data successfully written to {output_csv_path}")
except Exception as write_error:
    print(f"Error writing cleaned data to {output_csv_path}: {write_error}")


# Test cases for successful validation
def test_successful_validation_file_name():
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    assert metadata_instance.metadata.file_name == valid_data['file_name']
    assert metadata_instance.metadata.language == valid_data['language']
    assert metadata_instance.metadata.version == valid_data['version']
    assert metadata_instance.metadata.encoding == valid_data['encoding']
    assert metadata_instance.metadata.file_size == valid_data['file_size']

def test_successful_validation_version():
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 2,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    assert metadata_instance.metadata.version == valid_data['version']

def test_successful_validation_language():
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    assert metadata_instance.metadata.language == valid_data['language']

def test_successful_validation_encoding():
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    assert metadata_instance.metadata.encoding == valid_data['encoding']

def test_successful_validation_file_size():
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    assert metadata_instance.metadata.file_size == valid_data['file_size']

# Test cases for failed validation
def test_failed_validation_file_name():
    invalid_data = {
        'file_name': 123,
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    with pytest.raises(ValueError):
        metadata_instance = MetaDataPDFClass(**invalid_data)

def test_failed_validation_version():
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 'invalid',
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    with pytest.raises(ValueError):
        metadata_instance = MetaDataPDFClass(**invalid_data)

def test_failed_validation_language():
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 123,
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    with pytest.raises(ValueError):
        metadata_instance = MetaDataPDFClass(**invalid_data)

def test_failed_validation_encoding():
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 123,
        'file_size': 53543
    }

    with pytest.raises(ValueError):
        metadata_instance = MetaDataPDFClass(**invalid_data)

def test_failed_validation_file_size():
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 'invalid'
    }

    with pytest.raises(ValueError):
        metadata_instance = MetaDataPDFClass(**invalid_data)
