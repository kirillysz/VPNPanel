from marzban import Panel
from marzban.models.user_model import UserModel

class User:
    def __init__(self, panel: Panel):
        self.panel = panel
        self.user_prefix = "user"
        self.users_prefix = "users"

    async def add_user(self, user: UserModel):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}",
            method="POST",
            data=user.dict()
        )
        return response

    async def get_user(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}",
            method="GET"
        )
        return response

    async def modify_user(self, username: str, user: UserModel):
        data = {k: v for k, v in user.dict().items() if v is not None}
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}",
            method="PUT",
            data=data
        )
        return response

    async def remove_user(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}",
            method="DELETE"
        )
        return response

    async def reset_user_data_usage(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/reset",
            method="POST"
        )
        return response

    async def remoke_user_subscription(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/revoke_sub",
            method="POST"
        )
        return response
        
    async def get_user_usage(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/usage",
            method="GET"
        )
        return response

    async def active_next_user_plan(self, username: str):
        response = await self.panel.request(
            endpoint=f"{self.user_prefix}/{username}/active-next",
            method="POST"
        )
    

    async def get_users(self):
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}",
            method="GET"
        )
        return response

    async def reset_users_data_usage(self):
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/reset",
            method="POST"
        )
        return response

    async def get_users_usage(self):
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/usage",
            method="GET"
        )
        return response

    async def set_owner_for_user(self, username: str, admin_username: str):
        data = {"admin_username": admin_username}
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/{username}/set-owner",
            method="POST",
            data=data
        )
        return response

    async def get_expired_users(self):
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/expired",
            method="GET"
        )
        return response

    async def delete_expired_users(self):
        response = await self.panel.request(
            endpoint=f"{self.users_prefix}/expired",
            method="DELETE"
        )
        return response

    