from adapter.spi.scraping.http.http_connection import HttpConnection
from adapter.spi.scraping.web_scraping_repository import WebScrapingRepository

class RepositoriesFactory:
    def __init__(self,http_connection: HttpConnection) -> None:
        self.__repositories: dict = {
            "web_scraping_repository": WebScrapingRepository(http_connection,"https://www.coordinador.cl/operacion/documentos/estudios-operacionales/estudios-de-analisis-de-falla/")
        }
    
    def get_repository(self,repository_name:str):
        if repository_name in self.__repositories:
            return self.__repositories[repository_name]
        else:
            raise Exception("Repository does not exist")