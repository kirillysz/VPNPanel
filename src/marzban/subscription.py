from marzban import Panel

class Subscription:
    def __init__(self, panel: Panel, subscription_prefix: str):
        """
        Wrapper around the 'Panel' API for managing user subscriptions.

        Args:
            panel (Panel): An instance of the `Panel` API client.
            subscription_prefix (str): API endpoint prefix for subscription-related requests.
        """
        self.panel = panel
        self.subscription_prefix = subscription_prefix

    async def get_user_subscription(self, token: str):
        """
        Provides a subscription link based on the user agent (Clash, V2Ray, etc.).

        Args:
            token (str): Subscription Token (https://example.com/TOKEN_HERE/sub_id)

        Returns:
            any: Subscription link based on the user agent
        """
        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}"
        )
        return response

    async def get_user_subscription_info(self, token: str) -> dict:
        """
        Retrieves detailed information about the user's subscription.

        Args:
            token (str): Subscription Token (https://example.com/TOKEN_HERE/sub_id)

        Returns:
            dict: Detailed subscription information
        """
        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}/info"
        )
        return response

    async def get_user_subscription_usage(self, token: str):
        """
        Fetches the usage statistics for the user within a specified date range.

        Args:
            token (str): Subscription Token (https://example.com/TOKEN_HERE/sub_id)

        Returns:
            any: Usage statistics
        """
        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}/usage"
        )
        return response

    async def get_user_subscription_with_client(self, token: str, client_type: str):
        """
        Provides a subscription link based on the specified client type (e.g., Clash, V2Ray).

        Args:
            token (str): Subscription Token (https://example.com/TOKEN_HERE/sub_id)
            client_type (str): Client type. Must be one of:
                ["sing-box", "clash-meta", "clash", "outline", "v2ray", "v2ray-json"].

        Raises:
            Exception: If client_type is not in the allowed list.

        Returns:
            any: Subscription data formatted for the client
        """
        if client_type not in ["sing-box", "clash-meta", "clash", "outline", "v2ray", "v2ray-json"]:
            raise Exception(f"Request failed: Client type not in avaiables")

        response = await self.panel.request_subscription(
            endpoint=f"{self.subscription_prefix}/{token}/{client_type}"
        )
        return response
    
