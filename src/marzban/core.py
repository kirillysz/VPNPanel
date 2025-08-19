from marzban import Panel

class Core:
    def __init__(self, panel: Panel):
        """
        Wrapper around the 'Panel' API for interacting with the core system

        Args:
            panel (Panel): An instance of the `Panel` API client.
            core_prefix (str): API endpoint prefix for core-related requests.
        """
        self.panel = panel
        self.core_prefix = "core"

    async def get_core_stats(self) -> dict:
        """Retrieve core statistics such as version and uptime.

        Returns:
            dict: Core statistics and status data from the server.
        """
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}",
            method="GET"
        )
        return response

    async def restart_core(self) -> str:
        """
        Restart the core system.

        Returns:
            str: Server response indicating success of the restart.
        """
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}/restart",
            method="POST"
        )
        return "success"

    async def get_core_config(self) -> dict:
        """Get the current core configuration.

        Returns:
            dict: Core configuration data.
        """
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}/config",
            method="GET"
        )
        return response

    async def modify_core_config(self, config: dict) -> str:
        """Modify the core configuration and restart the core.

        Args:
            config (dict): Dictionary containing configuration keys and values to update.

        Returns:
            str: Server response indicating success of the restart with updated config.
        """
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}/config",
            method="PUT",
            data=config
        )
        return "success"
