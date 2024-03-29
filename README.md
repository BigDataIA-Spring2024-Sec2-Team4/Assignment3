# Assignment3
## Live application Links


[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=15TX801JmThAB60DlI9FU_bpRoIJUoFUyyn1WPdTcb7M#0)


## Problem Statement

This project aims to design, validate, and process data schemas for  CFA Institute’s website and PDF files using Grobid/PyPDF2 for extraction. The challenge involves ensuring data integrity through schema validation using Pydantic, DBT transformation, and efficient Snowflake storage

## Project Goals

1. Design `URLClass` to validate CFA webpages.
2. Create `MetaDataPDFClass` and `ContentPDFClass` for Grobid output.
3. Implement data and schema validation using Pydantic.
4. Develop a Snowflake schema for storing validated data.
5. Process "clean" CSV files from validated data.
6. Utilize DBT with Snowflake for data transformation.
7. Ensure robust testing with Pytest, demonstrating both success and failure cases

 ## Technologies Used

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![GROBID](https://img.shields.io/badge/GROBID-FFFFFF?style=for-the-badge&logo=GROBID&logoColor=black)](https://grobid.readthedocs.io/en/latest/Introduction/)
[![Snowflake](https://img.shields.io/badge/snowflake-0000FF?style=for-the-badge&logo=snowflake&logoColor=white)](https://docs.snowflake.com/ )
[![DBT](https://img.shields.io/badge/DBT-861121?style=for-the-badge)](https://www.getdbt.com/)



## Data Sources
- [CFA Website](https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending)
- Three PDF files processed through Grobid


## Prerequisites
1. Python 3.8+
2. Pip for Python package management
3. Snowflake account and setup
4. DBT setup and account

Install PyDantic using pip:
```⁠ bash
pip install pydantic
```

Install PyTest using pip:
```
pip install pytest
```

## Project Structure
```⁠ bash
.DS_Store
.gitignore
DBT-Snowflake.txt
Datasets
   |-- CFA.csv
   |-- Grobid
   |   |-- Grobid_RR_2024_l1_combined.txt
   |   |-- Grobid_RR_2024_l1_combined.xml
   |   |-- Grobid_RR_2024_l2_combined.txt
   |   |-- Grobid_RR_2024_l2_combined.xml
   |   |-- Grobid_RR_2024_l3_combined.txt
   |   |-- Grobid_RR_2024_l3_combined.xml
   |   |-- metadata.csv
   |   |-- metadata_enhanced.csv
   |-- PyPDF
   |   |-- PyPDF_RR_2024_l1_combined.txt
   |   |-- PyPDF_RR_2024_l2_combined.txt
   |   |-- PyPDF_RR_2024_l3_combined.txt
   |-- Sample_PDFs
   |   |-- 2024-l1-topics-combined-2.pdf
   |   |-- 2024-l2-topics-combined-2.pdf
   |   |-- 2024-l3-topics-combined-2.pdf
   |-- final_output.csv
README.md
analyses
   |-- .gitkeep
dbt_project.yml
images
   |-- .DS_Store
   |-- Architecture Diagram.png
   |-- Pydantic.png
   |-- csv.png
   |-- dbt.png
   |-- pytest.png
   |-- snowflake.png
macros
   |-- .gitkeep
models
   |-- split_subheadings.sql
   |-- summary_table.sql
   |-- summary_table.yml
notebooks
   |-- Architecture_Diagram.ipynb
   |-- CFA.json
   |-- ContentPDFClass File.ipynb
   |-- S3 to snowflake.ipynb
   |-- URLClass.ipynb
   |-- Validated data to snoflake.ipynb
   |-- architecture_diagram.png
   |-- metadata.csv
   |-- test_metadata_validation.py
   |-- validated_CFA.csv
seeds
   |-- .gitkeep
snapshots
   |-- .gitkeep
tests
   |-- .gitkeep
validated data
   |-- validated_CFA.csv
   |-- validated_metadata_output.csv
validated_CFA.csv
```

## How to Run Application Locally
1. Clone the repository to your local machine.
2. Install required Python packages using 
3. Set up your Snowflake and DBT accounts, configuring the necessary credentials.
4. Follow DBT documentation to set up and run transformation jobs against your Snowflake data warehouse.


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
   '''
   python url_model_validation.py
   '''
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


## Metadata Validator

This Python script validates metadata from a CSV file using Pydantic models and generates a new CSV file with cleaned data.


## Usage

1. Clone the repository:

   '''
   git clone https://github.com/your-username/your-repo.git
   '''

2. Navigate to the project directory:
    '''
    cd metadata-validator
    '''

3. Run the script:
    '''
    python metadata_validator.py
    '''

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

## ContentPDFClass: Validation and CSV Processing
ContentPDFClass is designed to encapsulate and validate the structured content extracted from PDF files, focusing on the headings, subheadings, and the count of occurrences for each subheading.

## Pydantic Model - ContentPDFClass
The Pydantic model ContentPDFClass is defined with the following fields to represent and validate the structured content:
- file_name: String representing the name of the PDF file.
- topics: List of strings, each representing a main main headings in the document.
- subheadings: List of subheadings under that heading.
- subheading_counts: Count of occurrences of subheading within the document.

# Upload to Amazon S3

This script allows you to upload a CSV file from your local machine to an Amazon S3 bucket.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed (version 3.x)
- AWS account with S3 bucket
- AWS Access Key ID and Secret Access Key

## Setup

1. Clone the repository:

    ''''
    git clone https://github.com/your-username/your-repository.git
    ''''

2. Install required Python packages:

    '''
    pip install -r requirements.txt
    '''

3. Set up your environment variables:

    Create a `.env` file with the following content:

    '''
    access_id=your-aws-access-key-id
    secret_key=your-aws-secret-access-key
    ''''

    Replace `your-aws-access-key-id` and `your-aws-secret-access-key` with your AWS credentials.

## Usage

1. Ensure you have the CSV file (`validated_CFA.csv`) in the same directory as the script.

2. Run the script:

    '''
    python upload_to_s3.py
    '''

3. The script will upload the CSV file to the root of your S3 bucket (`validateddata`).

## DBT
Transform and summarize the cleaned CSV data using DBT in conjunction with Snowflake.
* Connection of snowflake with dbt
* Creation of models for asked schema
* Generated test
* Deployed to test and prod
## STEPS:
- Data Loading: Import the cleaned CSV data into Snowflake.
- DBT Project: Create a DBT project to define transformation workflows.



## References

- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [DBT Documentation](https://docs.getdbt.com/)
- [Snowflake Documentation](https://docs.snowflake.com/)

## Learning Outcomes

- Proficiency in data extraction and processing using Grobid.
- Schema design and validation using Pydantic.
- Data transformation and analytics with Snowflake and DBT.
- Comprehensive testing with Pytest to ensure data integrity.

## Conclusion

This project demonstrates a robust approach to processing, validating, and storing PDF content, leveraging modern tools like Pydantic for data validation, Snowflake for data storage, and Pytest for testing. It also introduces you to advanced data transformation and deployment strategies by introducing test and prod env concepts. Through meticulous schema design and testing, the project lays the foundation for various applications to leverage processed PDF data efficiently and reliably.

## Team Information and Contribution

| Name       | Contribution % | Contributions                             |
|------------|----------------|-------------------------------------------|
| Riya Singh  | 33%            | ContentPDFClass, Schema design, Pydantic validation, Testing with Pytest, Architecture Diagram, README |
| Nidhi Nitin Kulkarani   | 37%            | URLClass, DBT transformation, Schema design, Pydantic validation, Testing with Pytest |
| Deepakraja Rajendran   | 30%            | MetaDataPDFClass, Snowflake Integration, Pydantic validation, Testing with Pytest, README |

