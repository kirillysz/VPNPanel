from marzban import Panel
from marzban.models.user_template_model import UserTemplateConfig

class UserTemplate:
    def __init__(self, panel: Panel):
        self.panel = panel
        self.user_template_prefix = "user_template"

    async def add_user_template(self, template: UserTemplateConfig):
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}",
            method="GET",
            data=template.dict()
        )
        return response

    async def get_user_templates(self):
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}",
            method="GET"
        )
        return response

    async def get_user_template_endpoint(self, template_id: int):
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}/{template_id}",
            method="GET"
        )
        return response

    async def modify_user_template(self, template_id: int, template: UserTemplateConfig):
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}/{template_id}",
            method="PUT",
            data=template.dict()
        )
        return response

    async def remove_user_template(self, template_id: int):
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}/{template_id}",
            method="DELETE"
        )
        return response

