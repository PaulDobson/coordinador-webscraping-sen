from types import NoneType
import typing
from adapter.spi.scraping.http.http_connection import HttpConnection
from application.repositories.scrap_documents_repository_abstract import ScrapWebDocumentRepositoryAbstract
from domain.eaf_document import EAFDocument
from domain.page_document_pagination import PageDocumentPagination
from domain.pdf_document import PdfDocument
from domain.scraping_exception import ScrapingException
from bs4 import BeautifulSoup

from domain.year_folder import YearFolder

class WebScrapingRepository(ScrapWebDocumentRepositoryAbstract):
    def __init__(self, http_connection: HttpConnection, url:str) -> None:
        self.http_connection = http_connection
        self.url = url
    
    def get_documents_by_year(self, year) -> typing.List[EAFDocument]:
        response = self.http_connection.get(year)
        if response == None or response.text == '':
            raise ScrapingException("No se puede abrir la url:"+year)
        documents_response=[]
        htmlParsed = BeautifulSoup(response.text, "html.parser")
        documents_list = htmlParsed.find_all(class_="margin-bottom-2")
        for div_document in documents_list:
            #print(div_document)
            published_date = div_document.find(class_="cen_fecha")
            if published_date is not None:
                link_donwload = div_document.find("a")
                #print(link_donwload.get("href"))                


    def get_all_years(self) -> typing.List[YearFolder]:
        response = self.http_connection.get(self.url)
        if response == None or response.text == '':
            raise ScrapingException("No se puede abrir la url:"+self.url)
        
        years_response=[]
        htmlParsed = BeautifulSoup(response.text, "html.parser")
        documents_list = htmlParsed.find(class_="cen_list-documentos")
        for li_year in documents_list.find_all("li"): 
            year = li_year.find("span").text
            if year.isnumeric():
                link = li_year.find("a")
                yearFolder: YearFolder = YearFolder(year, link.get("href"))
                years_response.append(yearFolder)

        return years_response

    def get_pagination(self,year) -> PageDocumentPagination:
        response = self.http_connection.get(year)
        if response == None or response.text == '':
            raise ScrapingException("No se puede abrir la url:"+year)
        
        htmlParsed = BeautifulSoup(response.text, "html.parser")
        cen_pagination = htmlParsed.find(class_="cen_pagination")
        if cen_pagination is None:
            raise ScrapingException("Error al obtener elementos de la paginacion")

        pages_list = cen_pagination.find_all("li")
        link_element = pages_list.pop()
        if link_element is None:
            raise ScrapingException("Error al obtener elementos de la paginacion: "+link_element.text)

        try:
            href_element = link_element.a.get("href")
            aria_label = link_element.a.get("aria-label")
            if aria_label.lower() =="final" and "page=" in href_element:
                index_page = href_element.find("page=")
                max_number_page = href_element[index_page+5:]
                if max_number_page.isnumeric():
                    pagination: PageDocumentPagination = PageDocumentPagination(int(max_number_page), href_element)
                    return pagination
                else:
                    raise ScrapingException("Error al obtener elementos de la paginacion: "+max_number_page)        
        except:
            raise ScrapingException("Error al obtener elementos de la paginacion: "+link_element.text)
        


    def download_pdf(self, eafDocument) -> PdfDocument:
        response = self.http_connection.get(eafDocument.link_download)
        pdf = open(eafDocument.name, 'wb')
        pdf.write(response.content)
        pdf.close()
        


