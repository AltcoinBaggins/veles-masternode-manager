#!/usr/bin/env python3

"""Runs the masternode orchestration script"""

import sys, os, logging, argparse

from container import IocContainer
from masternode import core_node


if __name__ == '__main__':
	# Parse commandline arguments
	parser = argparse.ArgumentParser(description='Veles Core Masternode Daemon version {} *EXPERIMENTAL*'.format('0.17.3'))
	parser.add_argument('--conf', default='veles.conf',
			help='Specify configuration file. Relative paths will be prefixed by datadir location.')
	parser.add_argument('--datadir', default='~/.veles/',
			help='Specify data directory')
	
	args = parser.parse_args()

	# Load the core node config file
	if not os.path.isfile(args.conf):
		sys.exit('Error: Configuration file not found: {}'.format(args.conf))

	# Configure container:
	container = IocContainer(
		config={
			'core_node': core_node.CoreNodeConfigParser().parse(args.conf)
		}
	)
	container.logger().addHandler(logging.StreamHandler(sys.stdout))

	# Run application:
	container.main()