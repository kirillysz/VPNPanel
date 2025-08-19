from marzban import Panel
from marzban.models.user_model import UserModel

class User:
    def __init__(self, panel: Panel):
        """
        Initialize the `User` manager for interacting with user-related endpoints.

        Args:
            panel (Panel): An instance of the Panel API client.
        """
        self.panel = panel
        self.user_prefix = "user"
        self.users_prefix = "users"

    async def add_user(self, user: UserModel) -> dict:
        """
        Add a new user.

        Args:
            user (UserModel): The user model containing user details.

        Returns:
            dict: API response containing details of the created user.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}",
            method="POST",
            data=user.dict()
        )
        return response

    async def get_user(self, username: str) -> dict:
        """
        Retrieve information about a specific user.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            dict: User information.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}",
            method="GET"
        )
        return response

    async def modify_user(self, username: str, user: UserModel) -> dict:
        """
        Modify an existing user's information.

        Args:
            username (str): The username of the user to modify.
            user (UserModel): The user model with updated information.

        Returns:
            dict: Updated user information.
        """
        data = {k: v for k, v in user.dict().items() if v is not None}
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}",
            method="PUT",
            data=data
        )
        return response

    async def remove_user(self, username: str) -> dict:
        """
        Remove a user.

        Args:
            username (str): The username of the user to remove.

        Returns:
            dict: Response from the API after deletion.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}",
            method="DELETE"
        )
        return response

    async def reset_user_data_usage(self, username: str) -> str:
        """
        Reset a user's data usage.

        Args:
            username (str): The username of the user.

        Returns:
            str: "success" if the operation was successful.
        """
        await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/reset",
            method="POST"
        )
        return "success"

    async def revoke_user_subscription(self, username: str) -> dict:
        """
        Revoke a user's subscription (including subscription link and proxies).

        Args:
            username (str): The username of the user.

        Returns:
            dict: Updated user information.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/revoke_sub",
            method="POST"
        )
        return response
        
    async def get_user_usage(self, username: str) -> dict:
        """
        Retrieve usage statistics for a user.

        Args:
            username (str): The username of the user.

        Returns:
            dict: User's usage data.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/usage",
            method="GET"
        )
        return response

    async def activate_next_user_plan(self, username: str) -> dict:
        """
        Activate the next plan for a user.

        Args:
            username (str): The username of the user.

        Returns:
            dict: Response from the API.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/active-next",
            method="POST"
        )
        return response

    async def get_users(self) -> dict:
        """
        Retrieve all users.

        Returns:
            dict: List of all users.
        """
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}",
            method="GET"
        )
        return response

    async def reset_users_data_usage(self) -> str:
        """
        Reset data usage for all users.

        Returns:
            str: "success" if the operation was successful.
        """
        await self.panel.request(
            endpoint=f"{self.users_prefix}/reset",
            method="POST"
        )
        return "success"

    async def get_users_usage(self) -> dict:
        """
        Retrieve usage statistics for all users.

        Returns:
            dict: Usage data for all users.
        """
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/usage",
            method="GET"
        )
        return response

    async def set_owner_for_user(self, username: str, admin_username: str) -> dict:
        """
        Assign an admin as the owner of a specific user.

        Args:
            username (str): The username of the user.
            admin_username (str): The username of the admin to assign.

        Returns:
            dict: Response from the API.
        """
        data = {"admin_username": admin_username}
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/{username}/set-owner",
            method="POST",
            data=data
        )
        return response

    async def get_expired_users(self) -> dict:
        """
        Retrieve all expired users.

        Returns:
            dict: List of expired users.
        """
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/expired",
            method="GET"
        )
        return response

    async def delete_expired_users(self) -> dict:
        """
        Delete all expired users.

        Returns:
            dict: Response from the API.
        """
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/expired",
            method="DELETE"
        )
        return response
