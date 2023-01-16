import typing
from application.utils.error_handling_utils import ErrorHandlingUtils
from domain.eaf_document import EAFDocument
from application.repositories.scrap_documents_repository_abstract import ScrapWebDocumentRepositoryAbstract

class GetAllDocumentsByYearUseCase:
    def __init__(self, repository:ScrapWebDocumentRepositoryAbstract) -> None:
        self.repository = repository

    def execute(self, year) -> typing.Iterable[EAFDocument]:
        try:
            return self.repository.get_documents_by_year(year)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Error al ejecutar consulta de documentos por el criterio year="+year , exception)