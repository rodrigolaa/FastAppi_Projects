from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine(
'postgresql://postgres:rodrigo.1@localhost/Blx',
echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_bd():
    Base.metadata.create_all(bind=engine)