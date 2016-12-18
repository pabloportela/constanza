import requests

'''
handle contacts date from some google drive.
'''

class ContactsManager:
    url = "https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pub?gid=0&single=true&output=csv"
    headers = ['firstname', 'lastname', 'street', 'zip', 'city', 'image']

    def get(self):
        r = requests.get(self.url)
        return self.process_csv(r.text)

    def process_csv(self, csv):
        results = []
        rows = csv.splitlines()
        for r in rows[1:]:
            fields = r.split(',')
            result = {}
            for i,f in enumerate(fields[0:len(self.headers)]):
                result[self.headers[i]] = f.strip()

            results.append(result)
                
        return results
        
        
