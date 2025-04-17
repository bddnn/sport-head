import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass

engine = sa.create_engine(
    "postgresql://postgres:2404@localhost:5432/sportshub", echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
