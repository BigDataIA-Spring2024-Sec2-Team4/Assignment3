# Assignment3
## Live application Links


[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1Zo7Izg-QxwYVgBzZWhqhnRQnYeTOEthq2rflQl-ytnQ#0)

# URLModel Validation

## Overview

URLModel Validation is a Python script that utilizes Pydantic to validate and clean data related to URLs, specifically for a predefined schema. It performs validations on fields such as year, level, and URL domains. The validated data is then saved to a CSV file.

## Prerequisites

Ensure you have Python installed on your machine. You can download it from python.org.

## Setup
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/URLModel-Validation.git

2. Navigate to the project directory:
   ```bash
   cd URLModel-Validation
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Place your JSON data file (CFA.json) in the project directory.
2. Run the script:
   ```bash
   python url_model_validation.py
3. View the validated data in the generated CSV file ('validated_CFA.csv').

## Pydantic Model - URLModel
The 'URLModel' Pydantic model is defined with the following fields:
* Name_of_the_topic
* Year
* Level
* Introduction_Summary
* Learning_Outcomes
* Link_to_the_Summary_Page
* Link_to_the_PDF_File

## Field Validation
* Year: Validates integer or string containing digits within a specific range (2010 to current year).
* Level: Converts Roman numerals to integers and validates the level field.
* URL Domain: Checks if the URL domain is from "www.cfainstitute.org".
* PDF URL Domain and Extension: Checks if the PDF URL domain is from "www.cfainstitute.org" and has a ".pdf" extension.

## Test Cases
Positive and negative test cases are included to ensure proper validation.

## Conclusion
URLModel Validation provides a reliable solution for validating and cleaning data related to URLs. It ensures data integrity and adherence to the specified schema.

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
   ```bash
   pytest metadata_validator.py
   ```

# Upload to Amazon S3

This script allows you to upload a CSV file from your local machine to an Amazon S3 bucket.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed (version 3.x)
- AWS account with S3 bucket
- AWS Access Key ID and Secret Access Key

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:

    Create a `.env` file with the following content:

    ```env
    access_id=your-aws-access-key-id
    secret_key=your-aws-secret-access-key
    ```

    Replace `your-aws-access-key-id` and `your-aws-secret-access-key` with your AWS credentials.

## Usage

1. Ensure you have the CSV file (`validated_CFA.csv`) in the same directory as the script.

2. Run the script:

    ```bash
    python upload_to_s3.py
    ```

3. The script will upload the CSV file to the root of your S3 bucket (`validateddata`).
