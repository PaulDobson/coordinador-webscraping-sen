class PdfDocument:
    def __init__(self, name, link, date_downloaded, path)->None:
        self.name=name
        self.link =link
        self.date_downloaded = date_downloaded
        self.path=path