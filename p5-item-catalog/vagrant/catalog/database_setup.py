import os
import sys
from sqlalchemy import Column, Foreign Key, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# class
## __tablename__

### mappers



engine = create_engine('sqlite:///'database_name.db)


Base.metadata.create_all(engine)