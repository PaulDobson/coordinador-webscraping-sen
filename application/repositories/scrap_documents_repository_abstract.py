from abc import ABC, abstractmethod
import typing

from domain.eaf_document import EAFDocument
from domain.page_document_pagination import PageDocumentPagination
from domain.pdf_document import PdfDocument
from domain.year_folder import YearFolder


class ScrapWebDocumentRepositoryAbstract(ABC):
    @abstractmethod
    def get_documents_by_year(self, year) -> typing.List[EAFDocument]:
        """Get all documents of a year"""

    @abstractmethod
    def get_all_years(self) -> typing.List[YearFolder]:
        """Get a list of year in web page"""
    
    @abstractmethod
    def get_pagination(self,year) -> PageDocumentPagination:
        """Get a list of page from pagination in web page"""

    @abstractmethod
    def download_pdf(self,eafDocument:EAFDocument) -> PdfDocument:
        """Download PDF"""
        