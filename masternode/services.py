"""Services module."""

#from masternode import core_node

class BaseService(object):
	"""Service base class."""

class CoreNodeService(BaseService):
	"""Service to communicate with the Veles Core daemon"""

	def __init__(self, core_node, logger):
		"""Constructor"""
		self.core_node = core_node
		self.logger = logger

	def command(self, command, args = []):
		"""For debugging porposes"""
		return self.core_node.call(command, args)
		