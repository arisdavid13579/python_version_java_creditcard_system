from abc import ABC, abstractclassmethod
from pymysql.connections import Connection
from pymysql.err import OperationalError
import configparser
import pandas as pd


class AbstractDAO(ABC):
    def __init__(self):
        self.connection: Connection = None
        self.__database: str = None

    def connect(self):
        try:
            file = open('../database_config.ini', 'r')
            file.close()
            connection_config = configparser.ConfigParser()
            connection_config.read('../database_config.ini')
            connection_config = connection_config['Settings']
            host = connection_config['Host']
            username = connection_config['Username']
            password = connection_config['Password']
            port = connection_config.getint('Port')
            self.__database = connection_config['Database']
            self.connection = Connection(host=host, user=username, password=password,
                                         port=port, database=self.__database)
        except IOError:
            print("Error: The database configuration file cannot be found or is not accessible. Please make sure that"
                  "\n the database's login and server details are in the 'database_config.ini' file")
            return

        except OperationalError as error:
            print('Error: Cannot connect to database\n')
            print(error)

    def disconnect(self):
        self.connection.close()
        print(f"\nDisconnected from {self.__database}")
        del self.__database
