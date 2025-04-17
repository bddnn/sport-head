from datetime import date

from sqlalchemy import DATE, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
class Match(Base):
    __tablename__ = "matches"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(DATE, nullable=False)
    home_team: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    away_team: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    home_team_score: Mapped[int] = mapped_column(default=0)
    away_team_score: Mapped[int] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Match(id={self.id!r}, date={self.date!r}, home_team={self.home_team!r}, away_team={self.away_team!r}, home_team_score={self.home_team_score!r}, away_team_score={self.away_team_score!r})"

class Team(Base):
    __tablename__ = "teams"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Team(id={self.id!r}, name={self.name!r})"
