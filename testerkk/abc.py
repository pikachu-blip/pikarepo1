import os

# ENVIRONMENT = os.getenv("ENVIRONMENT")
# print(ENVIRONMENT)


# Get the environment selected in GitHub Actions
GITHUB_ENVIRONMENT = os.getenv("GITHUB_ENVIRONMENT")  # Default to dev

print(f"Running in GitHub Environment: {GITHUB_ENVIRONMENT}")

# if ENVIRONMENT=="dev":
#   env_file =".env.DEV"
# else:
#   env_file =".env.PROD"

# # Load the chosen .env file
# load_dotenv(env_file,override=True)

# print(f"PROJECT_ID: {os.getenv('PROJECT_ID')}") 
# print(f"PROJECT_NO: {os.getenv('PROJECT_NUMBER')}") 

