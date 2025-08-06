from sqlalchemy import (
    Column, Integer, String, Boolean, Enum, ForeignKey, Text
)
from sqlalchemy.orm import declarative_base, relationship
import enum

# 1. Base class for all models
# This is a base "class factory" that SQLAlchemy uses to register your models and map them to tables.
Base = declarative_base()

# 2. Enum for status field
# Python enum to represent the status options in user_games table.
class StatusEnum(enum.Enum):
    wishlist = "wishlist"
    playing = "playing"
    completed = "completed"

# 3. User model class
# This represents the 'users' table in your DB.
class User(Base):
    __tablename__ = "users"  # Name of the table in the database

    # Columns correspond to table columns:
    id = Column(Integer, primary_key=True)  # Primary key column, auto-increment by default
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    # password_hash = Column(Text)  # For future use

    # Optional: relationships to other tables (like user_games)
    # user_games = relationship("UserGame", back_populates="user")

# 4. VideoGame model class for video_games table
class VideoGame(Base):
    __tablename__ = "video_games"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    est_length = Column(Integer)  # Estimated playtime in hours
    released = Column(Boolean)

    # Optional relationships to game_consoles, user_games etc.

# 5. Console model class
class Console(Base):
    __tablename__ = "consoles"

    id = Column(Integer, primary_key=True)
    console_name = Column(String, unique=True, nullable=False)

# 6. GameConsole model (many-to-many link between games and consoles)
class GameConsole(Base):
    __tablename__ = "game_consoles"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("video_games.id"))
    console_id = Column(Integer, ForeignKey("consoles.id"))

# 7. UserGame model
class UserGame(Base):
    __tablename__ = "user_games"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("video_games.id"))
    excitement = Column(Integer)
    purchased = Column(Boolean)
    status = Column(Enum(StatusEnum), default=StatusEnum.wishlist)
    rating = Column(Integer)
    review = Column(Text)

