class YearFolder:
    def __init__(self, year, link) -> None:
        self.year = year
        self.link = link

    def __str__(self) -> str:
        return f"{self.year}, {self.link}"