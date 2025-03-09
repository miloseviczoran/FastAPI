from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/TodoApplicationDatabase"
SQLALCHEMY_DATABASE_URL = "postgresql://deploy_database_postgresql_user:yQduYz1qaQE1jrcGthOOdt98SIgCqniB@dpg-cv6qjta3esus73e8vepg-a.frankfurt-postgres.render.com/deploy_database_postgresql"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()