from db.session import SessionLocal

# this function is a dependency that can be used in FastAPI routes to get a database session. It creates a new session using the SessionLocal factory, yields it for use in the route, and then ensures that the session is closed after the route is finished, even if an error occurs. This helps to manage database connections efficiently and prevents potential issues with open connections.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()