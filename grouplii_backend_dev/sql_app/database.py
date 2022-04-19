import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:groupliiroot@localhost:3306/grouplii"

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:db_groupliitest2022@localhost:3306/grouplii?unix_socket=/cloudsql/groupliitest:us-east1:dbgroupliitest"

'''
SQLALCHEMY_DATABASE_URL = sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username="root",  # e.g. "my-database-user"
            password="db_groupliitest2022",  # e.g. "my-database-password"                        
            database="grouplii",  # e.g. "my-database-name"
            query={
            "unix_socket": "/cloudsql/groupliitest:us-east1:dbgroupliitest"
            }
        ),
'''

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#pass_root = "groupliiroot"