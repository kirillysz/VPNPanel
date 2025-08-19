from src.marzban.panel import Panel

class Core:
    def __init__(self, panel: Panel):
        self.panel = panel
        self.core_prefix = "core"

    async def get_core_stats(self):
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}",
            method="GET"
        )
        return response

    async def restart_core(self):
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}/restart",
            method="POST"
        )
        return response

    async def get_core_config(self):
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}/config",
            method="GET"
        )
        return response

    async def modify_core_config(self, config: dict):
        response = await self.panel.request(
            endpoint=f"{self.core_prefix}/config",
            method="PUT",
            data=config
        )
        return response
