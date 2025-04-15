from datetime import date
from typing import Annotated

import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class TeamBase(BaseModel):
    name: str


class MatchBase(BaseModel):
    date: date
    home_team: int
    away_team: int
    home_team_score: int
    away_team_score: int


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/matches/")
async def get_matches(match: MatchBase, db: db_dependency):
    db_matches = models.Match(
        date=match.date,
        home_team=match.home_team,
        away_team=match.away_team,
        home_team_score=match.home_team_score,
        away_team_score=match.away_team_score,
    )
    db.add(db_matches)
    db.commit()
    db.refresh(db_matches)


@app.get("/matches/")
async def read_matches(db: db_dependency):
    result = db.query(models.Match).all()
    return result


@app.post("/teams/")
async def get_teams(team: TeamBase, db: db_dependency):
    db_teams = models.Team(name=team.name)
    db.add(db_teams)
    db.commit()
    db.refresh(db_teams)


@app.get("/teams/")
async def read_teams(db: db_dependency):
    result = db.query(models.Team).all()
    return result
