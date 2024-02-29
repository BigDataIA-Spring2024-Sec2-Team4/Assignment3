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

## Contributing

If you'd like to contribute, please fork the repository and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


