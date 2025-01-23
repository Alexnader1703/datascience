import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class WorkPDB:
    def __init__(self, user, password, host, port):
        try:
            self.__user = user
            self.__password = password
            self.__host = host
            self.__port = port

            self.connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            print(f"Ошибочка {error}")

    def PrintInfoDB(self):
        try:
            info = "Информация о сервере\n"
            info += str(self.connection.get_dsn_parameters()) + "\n"

            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()

            info += f"Вы подключены к - {record}\n"
            return info
        except (Exception, Error) as error:
            return str(error)
