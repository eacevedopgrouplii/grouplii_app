import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:groupliiroot@localhost:3306/grouplii"

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:db_groupliitest2022@/grouplii?unix_socket=/cloudsql/groupliitest:us-east1:dbgroupliitest"

db_user = "root"
db_pass = "db_groupliitest2022"
db_name = "grouplii"
db_socket_dir = "/cloudsql"
instance_connection_name = "groupliitest:us-east1:dbgroupliitest"

engine = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username=db_user,  # e.g. "my-database-user"
        password=db_pass,  # e.g. "my-database-password"
        database=db_name,  # e.g. "my-database-name"
        query={
            "unix_socket": "{}/{}".format(
                db_socket_dir,  # e.g. "/cloudsql"
                instance_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
        }
    )
)



#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL
#)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#pass_root = "groupliiroot"