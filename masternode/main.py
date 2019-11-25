"""Example main module."""


def main(core_node_service):
    """Authenticate user and upload photo."""
    print(core_node_service.command('getbalance'))