import typing
from application.utils.error_handling_utils import ErrorHandlingUtils
from application.repositories.scrap_documents_repository_abstract import ScrapWebDocumentRepositoryAbstract
from domain.eaf_document import EAFDocument

class DownloadDocumentUseCase:
    def __init__(self, repository:ScrapWebDocumentRepositoryAbstract) -> None:
        self.repository = repository

    def execute(self, document:EAFDocument) -> typing.Iterable[str]:
        try:
            return self.repository.download_pdf(document)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error(f"Error al descargar documento {document.name}" , exception)