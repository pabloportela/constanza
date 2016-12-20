import requests
import csv

class GDocsContactsManager:
    """Fetches and processes contacts csv data from some google drive."""

    url = 'https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pub?gid=0&single=true&output=csv'
    headers = ('firstname', 'lastname', 'street', 'zip', 'city', 'image')

    def get(self):
        return self.process_input(self.fetch_input())

    def fetch_input(self):
        r = requests.get(self.url)
        return r.text

    def process_input(self, text):
        # skip headers
        rows = text.splitlines()[1:]
        return [{header: field.strip() for header, field in zip(self.headers, fields)} for fields in csv.reader(rows)]

