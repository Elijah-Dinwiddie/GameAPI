from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace these with your Postgres credentials & DB name
DATABASE_URL = "postgresql://postgres:SSA76P!Eva!44884!4196573@localhost/games_api_db"

# Create an engine — this manages the connection pool to your database
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session inside routes
def get_db():
    db = SessionLocal()
    try:
        yield db  # provide session to caller
    finally:
        db.close()  # close session after use
