class EAFDocument:
    def __init__(self, id, name, year, link_download,publish_date,fail_date, fail_hour, description) -> None:
        self.id = id
        self.name = name
        self.year = year
        self.publish_date = publish_date
        self.description = description
        self.fail_date = fail_date
        self.fail_hour = fail_hour
        self.link_download = link_download