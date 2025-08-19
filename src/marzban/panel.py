from marzban.utils import extract_api_url
from aiohttp import ClientSession

class Panel:
    def __init__(self, panel_url: str, token: str = ""):
        """The `Panel` class provides the main API client for interacting with a Marzban panel.  

        Args:
            panel_url (str): Panel url
            token (str, optional): JWT Token (can be get from admin.get_token()). Defaults to "".
        """
        self.panel_url = panel_url.rstrip("/")
        self.api_url = extract_api_url(panel_url)

        self.token = token
        self.session: ClientSession | None = None

    async def start(self):
        if not self.session:
            self.session = ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def request(
        self,
        endpoint: str,
        method: str = "GET",
        data: dict = None,
        form: bool = False
    ):
        if not self.session:
            await self.start()

        url = f"{self.api_url}/api/{endpoint.lstrip('/')}"

        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        if form:
            async with self.session.request(method.upper(), url, data=data, headers=headers) as resp:
                text = await resp.text()
                if not resp.ok:
                    raise Exception(f"Request failed {resp.status}: {text}")

                await self.close()
                return await resp.json()
        else:
            async with self.session.request(method.upper(), url, json=data, headers=headers) as resp:
                text = await resp.text()
                if not resp.ok:
                    raise Exception(f"Request failed {resp.status}: {text}")

                await self.close()
                return await resp.json()

    
    async def request_subscription(self, endpoint: str):
        if not self.session:
            await self.start()

        url = f"{self.api_url}/{endpoint.lstrip('/')}"

        async with self.session.get(url) as resp:
            text = await resp.text()
            if not resp.ok:
                raise Exception(f"Subscription request failed {resp.status}: {text}")

            content_type = resp.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return await resp.json()
            return text