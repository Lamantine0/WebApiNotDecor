from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase





class Settings_DB:

    def __init__(self, DATABASE_URL):

        self.DATABASE_URL = DATABASE_URL

        self.engine = self.CreateEngine()

        self.session = self.CreateSession()



    def CreateEngine(self):

        self.engine = create_engine(
            self.DATABASE_URL,
            connect_args = {"check_same_thread" : False }
        )

        return self.engine
    

    def CreateSession(self):

        self.session = sessionmaker(autoflush="False", bind=self.engine)

        return self.session()


class Base(DeclarativeBase):

    pass


setting = Settings_DB("sqlite:///:memory:")



setting.CreateEngine()

setting.CreateSession()

            


