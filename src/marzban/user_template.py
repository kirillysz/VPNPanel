from marzban import Panel
from marzban.models.user_template_model import UserTemplateConfig

class UserTemplate:
    def __init__(self, panel: Panel):
        """
        A UserTemplate wrapper for a user interface panel.

        Args:
            panel (Panel): The panel instance associated with this user template.
        """
        self.panel = panel
        self.user_template_prefix = "user_template"

    async def add_user_template(self, template: UserTemplateConfig) -> dict:
        """
        Add a new user template.

        Args:
            template (UserTemplateConfig): User template configuration to create.

        Returns:
            dict: Created template's data.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}",
            method="POST",
            data=template.dict()
        )
        return response

    async def get_user_templates(self) -> dict:
        """
        Get a list of user templates (with optional pagination if supported).

        Returns:
            dict: A dictionary containing templates' data.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}",
            method="GET"
        )
        return response

    async def get_user_template_endpoint(self, template_id: int) -> dict:
        """
        Get information about a specific user template by ID.

        Args:
            template_id (int): The ID of the user template.

        Returns:
            dict: The template's data.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}/{template_id}",
            method="GET"
        )
        return response

    async def modify_user_template(self, template_id: int, template: UserTemplateConfig) -> dict:
        """
        Update an existing user template.

        Args:
            template_id (int): The ID of the user template to update.
            template (UserTemplateConfig): The updated user template configuration.

        Returns:
            dict: The updated template's data.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}/{template_id}",
            method="PUT",
            data=template.dict()
        )
        return response

    async def remove_user_template(self, template_id: int) -> dict:
        """
        Delete a user template by ID.

        Args:
            template_id (int): The ID of the user template to remove.

        Returns:
            dict: The API response after deletion.
        """
        response = await self.panel.request(
            endpoint=f"{self.user_template_prefix}/{template_id}",
            method="DELETE"
        )
        return response
