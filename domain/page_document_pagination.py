class PageDocumentPagination:
    def __init__(self, max_page, link) -> None:
        self.max_page = max_page
        self.link = link
        self.__index= 0
        self.pages = []
        self.parser()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index >= len(self.pages):
            raise StopIteration

        current_page = self.pages[self.__index]
        self.__index +=1
        return current_page
    
    def __str__(self) -> str:
        return f"inicio: 1, Fin: {self.max_page}, Link:{self.link}"
    
    def parser(self):
        max_index_range = self.max_page+1
        for page in range(1,max_index_range ):
            self.pages.append(  self.link.replace(f"page={self.max_page}", f"page={page}")  )

