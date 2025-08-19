from src.marzban.panel import Panel
from src.marzban.models.hosts_model import ModifyHostsRequest

class System:
    def __init__(self, panel: Panel):
        self.panel = panel

        self.system_prefix = "system"
        self.inbounds_prefix = "inbounds"
        self.hosts_prefix = "hosts"

    async def get_system_info(self):
        response = await self.panel.request(
            endpoint=f"{self.system_prefix}",
            method="GET"
        )
        return response

    async def get_all_inbounds(self):
        response = await self.panel.request(
            endpoint=f"{self.inbounds_prefix}",
            method="GET"
        )
        return response
    
    async def get_hosts(self):
        response = await self.panel.request(
            endpoint=f"{self.hosts_prefix}",
            method="GET"
        )
        return response

    async def modify_hosts(self, hosts: ModifyHostsRequest):
        response = await self.panel.request(
            endpoint=f"{self.hosts_prefix}",
            method="PUT",
            data=hosts.dict()
        )