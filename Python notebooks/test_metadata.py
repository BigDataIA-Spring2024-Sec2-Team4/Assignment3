from pydantic import BaseModel, ValidationError
import pytest

class MetaDataPDF(BaseModel):
    file_name: str
    language: str
    version: int
    encoding: str
    file_size: int

    class Config:
        validate_assignment = True

class MetaDataPDFClass:
    def __init__(self, file_name, language, version, encoding, file_size):
        # Use the Pydantic model for validation during object creation
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

# Test cases for successful validation
def test_successful_validation_file_name():
    # Valid file_name (string)
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    metadata_instance.display_metadata()

def test_successful_validation_version():
    # Valid version (integer)
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 2,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    metadata_instance.display_metadata()

def test_successful_validation_language():
    # Valid language (string)
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    metadata_instance.display_metadata()

def test_successful_validation_encoding():
    # Valid encoding (string)
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    metadata_instance.display_metadata()

def test_successful_validation_file_size():
    # Valid file_size (integer)
    valid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    metadata_instance = MetaDataPDFClass(**valid_data)
    metadata_instance.display_metadata()

# Test cases for failed validation
def test_failed_validation_file_name():
    # Invalid file_name (not a string)
    invalid_data = {
        'file_name': 123,
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    try:
        metadata_instance = MetaDataPDFClass(**invalid_data)
        metadata_instance.display_metadata()
    except ValueError as e:
        print(f"Error: {e}")

def test_failed_validation_version():
    # Invalid version (not an integer)
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 'invalid',
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    try:
        metadata_instance = MetaDataPDFClass(**invalid_data)
        metadata_instance.display_metadata()
    except ValueError as e:
        print(f"Error: {e}")

def test_failed_validation_language():
    # Invalid language (not a string)
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 123,
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 53543
    }

    try:
        metadata_instance = MetaDataPDFClass(**invalid_data)
        metadata_instance.display_metadata()
    except ValueError as e:
        print(f"Error: {e}")

def test_failed_validation_encoding():
    # Invalid encoding (not a string)
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 123,
        'file_size': 53543
    }

    try:
        metadata_instance = MetaDataPDFClass(**invalid_data)
        metadata_instance.display_metadata()
    except ValueError as e:
        print(f"Error: {e}")

def test_failed_validation_file_size():
    # Invalid file_size (not an integer)
    invalid_data = {
        'file_name': "../Datasets/Grobid/Grobid_RR_2024_l1_combined.xml",
        'language': 'en',
        'version': 1,
        'encoding': 'UTF-8',
        'file_size': 'invalid'
    }

    try:
        metadata_instance = MetaDataPDFClass(**invalid_data)
        metadata_instance.display_metadata()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pytest.main()
