from sqlalchemy import Column,JSON,Integer,String,ForeignKey,DateTime,Select,VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Project(Base):
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True,autoincrement=True)
    ring_id=Column(VARCHAR)
    p_name = Column(String)
    p_manager = Column(String)
    def __init__(self,name,manager,ring_id,id=None):
        self.id=id
        self.ring_id=ring_id
        self.p_name=name
        self.p_manager=manager


class Resource(Base):
    __tablename__ = 'resources'

    resource_id=Column(Integer, primary_key=True,autoincrement=True)
    id = Column(ForeignKey(Project.project_id))
    ring_id=Column(VARCHAR)
    r_name=Column(String)
    
# class project_resource(Base):
    
#     __tablename__ = 'combined'

#     id=Column(Integer, primary_key=True,autoincrement=True)
#     project_id = Column(ForeignKey(Project.project_id))
#     resource_id=Column(ForeignKey(Resource.resource_id))

def create_connection():
    engine = create_engine('postgresql+psycopg2://postgres:Tamilan123*@localhost:5432/postgres')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    print("session created")
    return Session()

create_connection()