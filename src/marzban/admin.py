from marzban import Panel

class Admin:
    def __init__(self, panel: Panel):
        """
        Initialize the Admin manager with a Panel instance.

        Args:
            panel (Panel): An instance of the Panel API client.
        """
        self.panel = panel
        self.admin_prefix = "admin"
        self.admins_prefix = "admins"

    async def get_token(self, username: str, password: str) -> dict:
        """Authenticate an admin and issue a token.

        Args:
            username (str): admin username
            password (str): admin password

        Returns:
            dict: token's dict
        """
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

    async def get_current_admin(self) -> dict:
        """Retrieve the current authenticated admin.

        Returns:
            dict: A dictionary containing current admin's information.
        """
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
    ) -> dict:
        """
        Create a new admin account. Requires sudo privileges.

        Args:
            username (str): New admin's username.
            password (str): New admin's password.
            is_sudo (bool, optional): Whether the new admin has sudo privileges. Defaults to False.
            telegram_id (int, optional): Associated Telegram ID. Defaults to 0.
            discord_webhook (str, optional): Discord webhook URL. Defaults to "string".
            users_usage (int, optional): Initial usage count for the admin. Defaults to 0.

        Returns:
            dict: A dictionary containing the newly created admin's details.
        """
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
        """
        Modify details of an existing admin.

        Args:
            username (str): Admin username to modify.
            password (str, optional): New password. Defaults to None.
            is_sudo (bool, optional): Update sudo privileges. Defaults to None.
            telegram_id (int, optional): New Telegram ID. Defaults to None.
            discord_webhook (str, optional): New Discord webhook URL. Defaults to None.

        Returns:
            dict: A dictionary with the updated admin information.
        """
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
        """
        Delete an admin account.

        Args:
            username (str): The admin's username to delete.

        Returns:
            dict: Response from the server indicating success or failure.
        """
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}",
            method="DELETE"
        )
        return response

    async def get_admins(self):
        """
        Retrieve a list of all admins.

        Returns:
            dict: A dictionary containing all admin accounts.
        """
        response = await self.panel.request(
            endpoint=f"{self.admins_prefix}",
            method="GET"
        )
        return response

    async def disable_all_active_users(self, username: str):
        """
        Disable all active users under a specific admin.

        Args:
            username (str): Admin username whose users will be disabled.

        Returns:
            dict: Response from the server.
        """
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}/users/disable",
            method="POST"
        )
        return response

    async def activate_all_disabled_users(self, username: str):
        """
        Reactivate all previously disabled users under a specific admin.

        Args:
            username (str): Admin username whose users will be activated.

        Returns:
            dict: Response from the server.
        """
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/{username}/users/activate",
            method="POST"
        )
        return response

    async def reset_admin_usage(self, username: str):
        """
        Reset usage statistics for a specific admin.

        Args:
            username (str): Admin username whose usage will be reset.

        Returns:
            dict: Response from the server.
        """
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/usage/reset/{username}",
            method="POST"
        )
        return response

    async def get_admin_usage(self, username: str):
        """
        Retrieve usage statistics for a specific admin.

        Args:
            username (str): Admin username to query.

        Returns:
            dict: A dictionary containing the admin's usage information.
        """
        response = await self.panel.request(
            endpoint=f"{self.admin_prefix}/usage/{username}",
            method="GET"
        )
        return response
