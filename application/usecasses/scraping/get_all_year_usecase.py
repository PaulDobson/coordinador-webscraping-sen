import typing
from application.utils.error_handling_utils import ErrorHandlingUtils
from application.repositories.scrap_documents_repository_abstract import ScrapWebDocumentRepositoryAbstract

class GetAllYearFromWebUseCase:
    def __init__(self, repository:ScrapWebDocumentRepositoryAbstract) -> None:
        self.repository = repository

    def execute(self) -> typing.Iterable[str]:
        try:
            return self.repository.get_all_years()
        except Exception as exception:
            raise ErrorHandlingUtils.application_error("Error al ejecutar consulta para obtener listado de años desde la Web" , exception)