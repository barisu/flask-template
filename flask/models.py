import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
import database

class User(database.Base):
    __tablename__ = 'user'
    user_id = Column('id', Integer, primary_key = True)
    name = Column('name', String)
    age = Column('age',Integer)
    
    def __init__(self,val=None,reason=None):
        self.user_id = user_id
        self.name = name
        self.age = age
        return

    def __repr__(self):
        return f'<Accounting {self.user_id}>'

    def toDict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "age": self.age
        }


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=database.ENGINE)

if __name__ == "__main__":
    main(sys.argv)
