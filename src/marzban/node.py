from src.marzban.panel import Panel

class Node:
    def __init__(self, panel: Panel):
        self.panel = panel
        self.node_prefix = "node"
        self.nodes_prefix = "nodes"

    async def get_node_settings(self):
        response = await self.panel.request(
            endpoint=f"{self.node_prefix}/settings",
            method="GET"
        )
        return response
    
    async def add_node(
        self,
        add_as_new_host: bool = True,
        address: str = "192.168.1.1",
        api_port: int = 62051,
        name: str = "DE node",
        port: int = 62050,
        usage_coefficient: int = 1
    ):
        data = {
            "add_as_new_host": add_as_new_host,
            "address": address,
            "api_port": api_port,
            "name": name,
            "port": port,
            "usage_coefficient": usage_coefficient
        }

        response = await self.panel.request(
            endpoint=f"{self.node_prefix}",
            method="POST",
            data=data
        )
        return response

    async def get_node(self, node_id: int):
        response = await self.panel.request(
            endpoint=f"{self.node_prefix}/{node_id}",
            method="GET"
        )
        return response

    async def modify_node(
        self,
        node_id: int,
        address: str = "192.168.1.1",
        api_port: int = 62051,
        name: str = "DE node",
        port: int = 62050,
        status: str = "disabled",
        usage_coefficient: int = 1
    ):
        data = {k: v for k, v in {
            "address": address,
            "api_port": api_port,
            "name": name,
            "port": port,
            "status": status,
            "usage_coefficient": usage_coefficient
        }.items() if v is not None}

        response = await self.panel.request(
            endpoint=f"{self.node_prefix}/{node_id}",
            method="PUT",
            data=data
        )
        return response

    async def delete_node(self, node_id: int):
        response = await self.panel.request(
            endpoint=f"{self.node_prefix}/{node_id}",
            method="DELETE"
        )
        return response

    async def get_all_nodes(self):
        response = await self.panel.request(
            endpoint=f"{self.nodes_prefix}",
            method="GET"
        )
        return response
    
    async def reconnect_to_node(self, node_id: int):
        response = await self.panel.request(
            endpoint=f"{self.node_prefix}/{node_id}/reconnect",
            method="POST"
        )
        return response
    
    async def get_node_usage(self, node_id: int):
        response = await self.panel.request(
            endpoint=f"{self.node_prefix}/{node_id}/usage",
            method="GET"
        )
        return response

