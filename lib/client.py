import json
import requests

class Client:

	def __init__(self, key_id, key_secret):
		self.key_id = key_id
		self.key_secret = key_secret
		self.base_url = "https://api.onename.com/v1"

	def _get_request(self, url):
		response = requests.get(url, auth=(self.key_id, self.key_secret), verify=False)
		return json.loads(response.text)

	def _post_request(self, url, payload):
		response = requests.post(url, data=payload, auth=(self.key_id, self.key_secret), verify=False)
		return json.loads(response.text)


	def get_user(self, username):
		url = self.base_url + "/users/" +  username
		return self._get_request(url)

	def get_search(self, query):
		url = self.base_url + "/search?query=" + query
		return self._get_request(url)

	def get_stats(self):
		url = self.base_url + "/users"
		return self._get_request(url)

	def get_address(self, address):
		url = self.base_url + "/addresses/" + address
		return self._get_request(url)

	def register_user(self, payload):
		url = self.base_url + "/users"
		return self._post_request(url, payload)

	def broadcast_transaction(self, payload):
		url = self.base_url +  "/transactions"
		return self._post_request(url, payload)



