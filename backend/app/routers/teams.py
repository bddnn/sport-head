from typing import List, Optional

from app import models
from app.deps import db_dependency, user_dependency
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix='/teams',
    tags=['teams']
)

class TeamBase(BaseModel):
    name: str


class TeamResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
        
@router.post("/teams/", response_model=TeamResponse)
async def create_team(team: TeamBase, db: db_dependency):
    existing_team = db.query(models.Team).filter(models.Team.name == team.name).first()
    if existing_team:
        raise HTTPException(status_code=400, detail=f"Drużyna o nazwie '{team.name}' już istnieje")
    
    db_team = models.Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


@router.get("/teams/", response_model=List[TeamResponse])
async def read_teams(db: db_dependency):
    result = db.query(models.Team).all()
    return result


@router.get("/teams/{team_id}", response_model=TeamResponse)
async def read_team(team_id: int, db: db_dependency):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail=f"Drużyna o ID {team_id} nie istnieje")
    return team

# @router.delete("/")
# def delete_team()