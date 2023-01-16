import typing
from application.utils.error_handling_utils import ErrorHandlingUtils
from domain.eaf_document import EAFDocument
from application.repositories.scrap_documents_repository_abstract import ScrapWebDocumentRepositoryAbstract
from domain.page_document_pagination import PageDocumentPagination

class GetAllPagesFromPaginationByYearUseCase:
    def __init__(self, repository:ScrapWebDocumentRepositoryAbstract) -> None:
        self.repository = repository

    def execute(self, year) -> typing.Iterable[PageDocumentPagination]:
        try:
            return self.repository.get_pagination(year)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Error al ejecutar consulta de paginas por el criterio pagina="+year , exception)