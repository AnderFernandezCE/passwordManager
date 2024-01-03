import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from src.config import settings
from src.models import get_Base


def main():
    try:
        dsn = str(settings.DATABASE_URL)
        dsn = dsn.replace('+aiomysql', '', 1)
        print(dsn)
        engine = create_engine(dsn, echo = True)
        Base = get_Base()
        Base.metadata.create_all(engine)
    except OperationalError as e:
        print('Base de datos fuera de servicio')
        raise
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()