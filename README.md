# Assignment3
# Metadata Validator

This Python script validates metadata from a CSV file using Pydantic models and generates a new CSV file with cleaned data.

## Prerequisites

- Python 3.x
- Install required packages using `pip install -r requirements.txt`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git

2. Navigate to the project directory:
    ```bash
    cd metadata-validator

3. Run the script:
    ```bash
    python metadata_validator.py

The script will read the input CSV file, perform validation, and generate a new CSV file (validated_output.csv) with cleaned data.

## File Structure
* metadata_validator.py: Main script for metadata validation.
* metadata.csv: Input CSV file containing metadata.
* validated_output.csv: Output CSV file with cleaned metadata.

## Configuration
* Update input_csv_file and output_csv_file variables in the script to change file paths.

## Tests
The script includes pytest tests to ensure the correct functionality. You can run the tests using:

pytest metadata_validator.py

