# this import is used to handle password hashing and verification in the application. The CryptContext class from the passlib library provides a convenient way to manage multiple hashing algorithms and their configurations.
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from jose import jwt
from datetime import datetime, timedelta

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256" # this is the algorithm used for encoding and decoding JWT tokens. HS256 stands for HMAC with SHA-256, which is a widely used algorithm for secure token generation.

ACCESS_TOKEN_EXPIRE_MINUTES = 30 # this variable defines the expiration time for access tokens in minutes. In this case, access tokens will expire after 30 minutes, which helps to enhance security by limiting the time window during which a token can be used.

# this line initializes a CryptContext object with the bcrypt hashing algorithm. The deprecated="auto" argument allows the context to automatically handle any deprecated algorithms in the future, ensuring that the application remains secure as hashing standards evolve.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # this function takes a plain text password as input and returns a hashed version of the password using the CryptContext object initialized earlier. The hash function applies the bcrypt algorithm to securely hash the password, making it suitable for storage in a database.
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # this function takes a plain text password and a hashed password as input and verifies whether the plain text password matches the hashed password. It uses the verify method of the CryptContext object to perform this check, returning True if the passwords match and False otherwise.
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    # this to_encode variable is a copy of the input data dictionary, which will be used to create the payload for the JWT token
    to_encode = data.copy()

    # this line calculates the expiration time for the token by adding the defined number of minutes to the current UTC time.
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 

    # this line adds the expiration time to the payload dictionary under the "exp" key, which is a standard claim in JWT tokens that indicates when the token should expire.
    to_encode.update({"exp": expire}) 

    # this line encodes the payload into a JWT token using the specified secret key and algorithm. The resulting token can be used for authentication and authorization purposes in the application.
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) 