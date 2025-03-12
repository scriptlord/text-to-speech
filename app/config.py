import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve AWS credentials with default values
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")  # Providing a default region
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET_NAME")

# Validate required environment variables
def validate_aws_credentials():
    required_vars = {
        "AWS_ACCESS_KEY_ID": AWS_ACCESS_KEY,
        "AWS_SECRET_ACCESS_KEY": AWS_SECRET_KEY,
        "AWS_REGION": AWS_REGION,
    }
    
    missing_vars = [var for var, value in required_vars.items() if not value]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

# Validate on import
validate_aws_credentials()

# Print to verify (Remove in production)
print(f"AWS Access Key: {AWS_ACCESS_KEY}")
print(f"AWS Region: {AWS_REGION}")
