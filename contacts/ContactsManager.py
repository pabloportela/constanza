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
		rows.pop()
		for r in rows:
			fields = r.split(',')
			result = {}
			i = 0
			for f in fields:
				result[self.headers[i]] = f.strip()
				i += 1
			results.append(result)
			
		return results
		
		
