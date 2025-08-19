from src.marzban.panel import Panel

class AdminFunctions:
    def __init__(self, panel: Panel):
        self.panel = panel
        self.admin_prefix = "admin"
        self.admins_prefix = "admins"

    async def get_token(self, username: str, password: str):
        data = {
            "grant_type": "password",
            "username": username,
            "password": password
        }

        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/token",
            method="POST",
            data=data,
            form=True
        )
        self.panel.token = response.get("access_token")
        return response

    async def get_current_admin(self):
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}",
            method="GET"
        )
        return response

    async def create_admin(
        self,
        username: str,
        password: str,
        is_sudo: bool = False,
        telegram_id: int = 0,
        discord_webhook: str = "string",
        users_usage: int = 0
    ):
        data = {
            "username": username,
            "password": password,
            "is_sudo": is_sudo,
            "telegram_id": telegram_id,
            "discord_webhook": discord_webhook,
            "users_usage": users_usage
        }
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}",
            method="POST",
            data=data
        )
        
        return response

    async def modify_admin(
        self,
        username: str,
        password: str = None,
        is_sudo: bool = None,
        telegram_id: int = None,
        discord_webhook: str = None
    ):
        data = {k: v for k, v in {
            "password": password,
            "is_sudo": is_sudo,
            "telegram_id": telegram_id,
            "discord_webhook": discord_webhook
        }.items() if v is not None}

        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}",
            method="PUT",
            data=data
        )
        return response

    async def delete_admin(
        self,
        username: str
    ):
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}",
            method="DELETE"
        )
        return response

    async def get_admins(self):
        response = await self.panel.request(
            endpoint=f"{self.admins_prefix}",
            method="GET"
        )
        return response

    async def disable_all_active_users(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}/users/disable",
            method="POST"
        )
        return response

    async def activate_all_disabled_users(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}/users/activate",
            method="POST"
        )
        return response

    async def reset_admin_usage(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/usage/reset/{username}",
            method="POST"
        )
        return response

    async def get_admin_usage(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/usage/{username}",
            method="GET"
        )
        return response