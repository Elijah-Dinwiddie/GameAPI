from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✨ This is your connection string
# Replace with your actual username/password
DATABASE_URL = "postgresql://postgres:carry$$tart!@localhost:5432/mygameapi"

# 🔌 This connects SQLAlchemy to PostgreSQL
engine = create_engine(DATABASE_URL)

# 🧱 This creates sessions that will talk to the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🧬 This is the base class your models will inherit from
Base = declarative_base()
