from adapter.spi.repositories_factory import RepositoriesFactory
from adapter.spi.scraping.http.http_connection import HttpConnection
from application.repositories.scrap_documents_repository_abstract import ScrapWebDocumentRepositoryAbstract
from application.usecasses.scraping.download_document_usecase import DownloadDocumentUseCase
from application.usecasses.scraping.get_all_documents_by_year_usecase import GetAllDocumentsByYearUseCase
from application.usecasses.scraping.get_all_pages_from_pagination_by_year_usecase import GetAllPagesFromPaginationByYearUseCase
from application.usecasses.scraping.get_all_year_usecase import GetAllYearFromWebUseCase
from domain.eaf_document import EAFDocument

print("inicio de proceso WebScraping")

http_connection: HttpConnection = HttpConnection()
repositories_factory = RepositoriesFactory( http_connection)
webScrapRepository: ScrapWebDocumentRepositoryAbstract = repositories_factory.get_repository("web_scraping_repository")

get_all_years_usecase:GetAllYearFromWebUseCase = GetAllYearFromWebUseCase(webScrapRepository)
get_all_document_by_year_usecase:GetAllDocumentsByYearUseCase = GetAllDocumentsByYearUseCase(webScrapRepository)
get_all_page_by_year_usecase:GetAllPagesFromPaginationByYearUseCase = GetAllPagesFromPaginationByYearUseCase(webScrapRepository)
download_pdf_usecase:DownloadDocumentUseCase = DownloadDocumentUseCase(webScrapRepository)

#list_years = get_all_years_usecase.execute()
#year = list_years[0]
#print("buscando por año: " + year.year)
#pagination = get_all_page_by_year_usecase.execute(year.link)

#for page in pagination:
#    print(page)
#for year in list_years:
#    print(year.year)
#    document_list = get_all_document_by_year_usecase.execute(year.link)

document:EAFDocument = EAFDocument(
    "EAF 486/2022 SEN",
    "EAF-486-2022.pdf",
    "2022",
    "https://www.coordinador.cl/wp-content/uploads/2023/01/EAF-486-2022.pdf",
    None,None,None,None
)

download_pdf_usecase.execute(document)



print("termino de proceso WebScraping")