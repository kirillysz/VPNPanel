from marzban import Panel

class Subscription:
    def __init__(self, panel: Panel, subscription_prefix: str):
        self.panel = panel
        self.subscription_prefix = subscription_prefix

    async def get_user_subscription(self, token: str):
        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}"
        )
        return response

    async def get_user_subscription_info(self, token: str):
        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}/info"
        )
        return response

    async def get_user_subscription_usage(self, token: str):
        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}/usage"
        )
        return response

    async def get_user_subscription_with_client(self, token: str, client_type: str):
        if client_type not in ["sing-box", "clash-meta", "clash", "outline", "v2ray", "v2ray-json"]:
            raise Exception(f"Request failed: Client type not in avaiables")

        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}/{client_type}"
        )
        return response
    
