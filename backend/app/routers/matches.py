# class MatchBase(BaseModel):
#     date: date
#     home_team: int
#     away_team: int
#     home_team_score: int
#     away_team_score: int


# class MatchResponse(BaseModel):
#     id: int
#     date: date
#     home_team_name: str
#     away_team_name: str
#     home_team_score: int
#     away_team_score: int

#     class Config:
#         from_attributes = True

# @app.post("/matches/")
# async def create_match(match: MatchBase, db: db_dependency):
#     home_team = db.query(models.Team).filter(models.Team.id == match.home_team).first()
#     away_team = db.query(models.Team).filter(models.Team.id == match.away_team).first()
    
#     if not home_team:
#         raise HTTPException(status_code=404, detail=f"Drużyna domowa o ID {match.home_team} nie istnieje")
    
#     if not away_team:
#         raise HTTPException(status_code=404, detail=f"Drużyna wyjazdowa o ID {match.away_team} nie istnieje")

#     if match.home_team == match.away_team:
#         raise HTTPException(status_code=400, detail="Drużyna domowa i wyjazdowa muszą być różne")
    
#     db_match = models.Match(
#         date=match.date,
#         home_team=match.home_team,
#         away_team=match.away_team,
#         home_team_score=match.home_team_score,
#         away_team_score=match.away_team_score,
#     )
#     db.add(db_match)
#     db.commit()
#     db.refresh(db_match)
#     return db_match


# @app.get("/matches/", response_model=List[MatchResponse])
# async def read_matches(db: db_dependency):
#     HomeTeam = aliased(models.Team)
#     AwayTeam = aliased(models.Team)
    
#     results = (
#         db.query(
#             models.Match.id,
#             models.Match.date,
#             HomeTeam.name.label("home_team_name"),
#             AwayTeam.name.label("away_team_name"),
#             models.Match.home_team_score,
#             models.Match.away_team_score,
#         )
#         .join(HomeTeam, models.Match.home_team == HomeTeam.id)
#         .join(AwayTeam, models.Match.away_team == AwayTeam.id)
#         .all()
#     )
    
#     return results