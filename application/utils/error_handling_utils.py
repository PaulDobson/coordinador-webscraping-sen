from domain.scraping_exception import ScrapingException

class ErrorHandlingUtils:

    @staticmethod
    def application_error(error_message: str, exception: Exception) -> ScrapingException:
        if isinstance(exception, ScrapingException):
            return ScrapingException(exception.message)
        else:
            return ScrapingException(error_message)