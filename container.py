"""Example of dependency injection in Python."""

import logging

from dependency_injector import containers, providers
from masternode import core_node, services, main


class IocContainer(containers.DeclarativeContainer):
    """Application IoC container."""

    config = providers.Configuration('config')
    logger = providers.Singleton(logging.Logger, name='VelesMasternode')

    # Gateways

    core_node_client = providers.Singleton(
    	core_node.CoreNodeRPCClient,
    	host=config.core_node.rpchost,
    	port=config.core_node.rpcport,
    	username=config.core_node.rpcuser,
    	password=config.core_node.rpcpassword,
    )

    # Services

    core_node_service = providers.Factory(
        services.CoreNodeService,
        core_node=core_node_client,
        logger=logger,
    )

    # Misc

    main = providers.Callable(
        main.main,
        core_node_service=core_node_service,
    )