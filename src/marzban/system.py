from marzban import Panel
from marzban.models.hosts_model import ModifyHostsRequest

class System:
    def __init__(self, panel: Panel):
        """
        Initialize the `System` manager for interacting with system-related endpoints.

        Args:
            panel (Panel): An instance of the Panel API client.
        """
        self.panel = panel

        self.system_prefix = "system"
        self.inbounds_prefix = "inbounds"
        self.hosts_prefix = "hosts"

    async def get_system_info(self) -> dict:
        """
        Fetch system stats including memory, CPU, and user metrics.

        Returns:
           dict: System information including memory, CPU, and user statistics.
        """
        response = await self.panel.request(
            endpoint=f"{self.system_prefix}",
            method="GET"
        )
        return response

    async def get_all_inbounds(self) -> dict:
        """
        Retrieve inbound configurations grouped by protocol.

        Returns:
            dict: Inbounds
        """
        response = await self.panel.request(
            endpoint=f"{self.inbounds_prefix}",
            method="GET"
        )
        return response
    
    async def get_hosts(self) -> dict:
        """
        Get a list of proxy hosts grouped by inbound tag.

        Returns:
            dict: Hosts
        """
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