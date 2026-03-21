# this file is used to load environment variables from a .env file and make them accessible in the application. It uses the python-dotenv package to load the variables and then retrieves the DATABASE_URL variable from the environment. This allows you to keep sensitive information like database credentials out of your codebase and easily manage different configurations for development, testing, and production environments.

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")