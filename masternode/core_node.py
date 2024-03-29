"""Module to handle communication with wallet/node daemon"""

import requests, json, configparser, itertools

class CoreNodeRPCClient(object):
	def __init__(self, host = "127.0.0.1", port = 25522, username = None, password = None):
		self.host = host
		self.port = int(port)
		self.username = username
		self.password = password

	def call(self, method, params = []):
		if self.username or self.password:
			url = "http://%s:%s@%s:%s" % (self.username, self.password, self.host, self.port)
		else:
			url = "http://%s:%s/" % (self.host, self.port)

		headers = {
			'content-type': 'application/json'
			}
		payload = {
			"method": method,
			"params": params,
			"jsonrpc": "1.0",
			"id": 0
		}
		response = requests.post(url, data=json.dumps(payload), headers=headers)
		try:
			if 'error' in response.json() and response.json()['error'] != None:
				return response.json()	#False

			if 'result' in response.json():
				return response.json()['result']

		except:
			return response.text

class CoreNodeConfigParser(object):
	# Default values for core config options go here
	defaults = {
		'rpchost': '127.0.0.1',
		'rpcport': '5493',
	}

	def __init__(self):
		self.parser = configparser.ConfigParser()
		self.parser['DEFAULT'] = self.defaults

	def parse(self, config_path):
		# A trick to parse the config file without a header section
		with open(config_path) as fp:
			self.parser.read_file(itertools.chain(['[core]'], fp), source=config_path)

		return dict(self.parser['core'])


