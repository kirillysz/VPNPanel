# 'marzban-client' Documentation

* [Panel Class](#panel-class)
* [Admin Class](#admin-class)
* [Core Class](#core-class)
* [Subscription Class](#subscription-class)
* [System Class](#system-class)
* [User Class](#user-class)
* [Templates Class](#templates-class)

## Panel Class Documentation <a id="panel-class"></a>

The `Panel` class provides the main API client for interacting with a Marzban panel.
It handles the panel URL, API endpoint extraction, authentication token, and manages the HTTP session.

---

### Class Initialization

```python
from marzban_client import Panel

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
```

**Parameters:**

* `panel (Panel)`: An instance of the `Panel` API Client

---

## Admin Class Documentation <a id="admin-class"></a>

The `Admin` class provides a wrapper around the `Panel` API for managing admin accounts and their users. It supports authentication, CRUD operations for admins, user management, and usage tracking.

---

### Class Initialization

```python
from marzban_client import Panel
from marzban_client import Admin

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
admin_manager = Admin(panel=panel)

await admin_manager.get_token(username=username, password=password)
```

### Parameters

* `panel (Panel)`: An instance of the `Panel` API client.

---

## Methods

### `get_token(username: str, password: str) -> dict`

Authenticate an admin and obtain an access token.

**Parameters:**

* `username (str)`: Admin username.
* `password (str)`: Admin password.

**Returns:**

* `dict`: Contains access token and authentication details.

---

### `get_current_admin() -> dict`

Retrieve the currently authenticated admin's details.

**Returns:**

* `dict`: Information about the current admin.

---

### `create_admin(username: str, password: str, is_sudo: bool = False, telegram_id: int = 0, discord_webhook: str = "string", users_usage: int = 0) -> dict`

Create a new admin account. Requires the current admin to have sudo privileges.

**Parameters:**

* `username (str)`: New admin's username.
* `password (str)`: New admin's password.
* `is_sudo (bool, optional)`: Grant sudo privileges. Default is `False`.
* `telegram_id (int, optional)`: Telegram ID. Default is `0`.
* `discord_webhook (str, optional)`: Discord webhook URL. Default is `"string"`.
* `users_usage (int, optional)`: Initial user usage count. Default is `0`.

**Returns:**

* `dict`: Newly created admin details.

---

### `modify_admin(username: str, password: str = None, is_sudo: bool = None, telegram_id: int = None, discord_webhook: str = None) -> dict`

Modify details of an existing admin.

**Parameters:**

* `username (str)`: Admin username to modify.
* `password (str, optional)`: New password.
* `is_sudo (bool, optional)`: Update sudo privileges.
* `telegram_id (int, optional)`: Update Telegram ID.
* `discord_webhook (str, optional)`: Update Discord webhook URL.

**Returns:**

* `dict`: Updated admin information.

---

### `delete_admin(username: str) -> dict`

Delete an admin account.

**Parameters:**

* `username (str)`: Admin username to delete.

**Returns:**

* `dict`: Server response indicating success or failure.

---

### `get_admins() -> dict`

Retrieve a list of all admins.

**Returns:**

* `dict`: Contains all admin accounts.

---

### `disable_all_active_users(username: str) -> dict`

Disable all active users under a specific admin.

**Parameters:**

* `username (str)`: Admin username whose users will be disabled.

**Returns:**

* `dict`: Server response.

---

### `activate_all_disabled_users(username: str) -> dict`

Reactivate all previously disabled users under a specific admin.

**Parameters:**

* `username (str)`: Admin username whose users will be activated.

**Returns:**

* `dict`: Server response.

---

### `reset_admin_usage(username: str) -> dict`

Reset usage statistics for a specific admin.

**Parameters:**

* `username (str)`: Admin username whose usage will be reset.

**Returns:**

* `dict`: Server response.

---

### `get_admin_usage(username: str) -> dict`

Retrieve usage statistics for a specific admin.

**Parameters:**

* `username (str)`: Admin username to query.

**Returns:**

* `dict`: Admin usage information.

---

## Core Class Documentation <a id="core-class"></a>

The `Core` class provides a wrapper around the `Panel` API for managing and interacting with the core system.
It supports retrieving core statistics, fetching and modifying configuration, and restarting the core.

---

### Class Initialization

```python
from marzban_client import Panel
from marzban_client import Core

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
core_manager = Core(panel=panel)
```

### Parameters

* `panel (Panel)`: An instance of the `Panel` API client.

---

## Methods

### `get_core_stats() -> dict`

Retrieve core statistics such as version, uptime, and status.

**Returns:**

* `dict`: Core statistics and status data from the server.

### `restart_core() -> str`

Restart the core system.

**Returns:**

* `str`: `success` if the restart request was accepted by the server, otherwise `error`.

### `get_core_config() -> dict`

Retrieve the current core configuration.

**Returns:**

* `dict`: Core configuration data from the server.

### `modify_core_config(config: dict) -> str`

Modify the core configuration and apply changes.

**Parameters:**

* `config (dict)`: Dictionary containing configuration keys and values to update.

**Returns:**

* `str`: `success` if the configuration update request was accepted by the server, otherwise `error`.

---

## Subscription Class Documentation <a id="subscription-class"></a>

The `Subscription` class provides a wrapper around the `Panel` API for managing user subscriptions. It supports fetching subscription links, detailed subscription info, usage statistics, and client-specific subscription formats.

---

### Class Initialization

```python
from marzban_client import Panel, Subscription

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
subscription_manager = Subscription(panel=panel, subscription_prefix="subscription")
```

**Parameters:**

* `panel (Panel)`: An instance of the `Panel` API client.
* `subscription_prefix (str)`: API endpoint prefix for subscription-related requests.

---

## Methods

### `get_user_subscription(token: str)`

Provides a subscription link based on the user agent (Clash, V2Ray, etc.).

**Parameters:**

* `token (str)`: Subscription Token.

**Returns:**

* `any`: Subscription link based on the user agent.

### `get_user_subscription_info(token: str) -> dict`

Retrieves detailed information about the user's subscription.

**Parameters:**

* `token (str)`: Subscription Token.

**Returns:**

* `dict`: Detailed subscription information.

### `get_user_subscription_usage(token: str)`

Fetches usage statistics for the user within a specified date range.

**Parameters:**

* `token (str)`: Subscription Token.

**Returns:**

* `any`: Usage statistics.

### `get_user_subscription_with_client(token: str, client_type: str)`

Provides a subscription link formatted for a specific client type.

**Parameters:**

* `token (str)`: Subscription Token.
* `client_type (str)`: Must be one of `['sing-box', 'clash-meta', 'clash', 'outline', 'v2ray', 'v2ray-json']`.

**Raises:**

* `Exception`: If `client_type` is not in the allowed list.

**Returns:**

* `any`: Subscription data formatted for the client.

---

## System Class Documentation <a id="system-class"></a>

The `System` class provides a wrapper around the `Panel` API for managing system-related endpoints.
It supports fetching system statistics, retrieving inbound configurations, managing proxy hosts, and modifying hosts.

---

### Class Initialization

```python
from marzban_client import Panel, System

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
system_manager = System(panel=panel)
```

**Parameters:**

* `panel (Panel)`: An instance of the `Panel` API client.

---

## Methods

### `get_system_info() -> dict`

Fetch system stats including memory, CPU, and user metrics.

**Returns:**

* `dict`: System information including memory, CPU, and user statistics.

---

### `get_all_inbounds() -> dict`

Retrieve inbound configurations grouped by protocol.

**Returns:**

* `dict`: Inbounds configurations.

---

### `get_hosts() -> dict`

Get a list of proxy hosts grouped by inbound tag.

**Returns:**

* `dict`: Hosts information.

---

### `modify_hosts(hosts: ModifyHostsRequest)`

Modify proxy hosts configuration.

**Parameters:**

* `hosts (ModifyHostsRequest)`: Hosts modification request object containing updated host settings.

---

## User Class Documentation <a id="user-class"></a>

The `User` class provides a wrapper around the `Panel` API for managing user accounts and their subscriptions. It supports CRUD operations, usage tracking, subscription management, and administrative actions for users.

---

### Class Initialization

```python
from marzban_client import Panel, User

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
user_manager = User(panel=panel)
```

**Parameters:**

* `panel (Panel)`: An instance of the `Panel` API client.

---

## Methods

### `add_user(user: UserModel) -> dict`

Add a new user to the panel.

**Parameters:**

* `user (UserModel)`: User model containing user information.

**Returns:**

* `dict`: API response with user creation details.

---

### `get_user(username: str) -> dict`

Retrieve information about a specific user.

**Parameters:**

* `username (str)`: Username of the user.

**Returns:**

* `dict`: User information.

---

### `modify_user(username: str, user: UserModel) -> dict`

Update an existing user's information.

**Parameters:**

* `username (str)`: Username of the user to modify.
* `user (UserModel)`: Updated user model.

**Returns:**

* `dict`: Updated user information.

---

### `remove_user(username: str) -> dict`

Delete a user from the panel.

**Parameters:**

* `username (str)`: Username of the user to remove.

**Returns:**

* `dict`: API response confirming deletion.

---

### `reset_user_data_usage(username: str) -> str`

Reset data usage for a specific user.

**Parameters:**

* `username (str)`: Username of the user.

**Returns:**

* `str`: "success" if the reset was successful.

---

### `remoke_user_subscription(username: str) -> dict`

Revoke a user's subscription including subscription links and proxies.

**Parameters:**

* `username (str)`: Username of the user.

**Returns:**

* `dict`: Updated user information.

---

### `get_user_usage(username: str) -> dict`

Retrieve usage statistics for a specific user.

**Parameters:**

* `username (str)`: Username of the user.

**Returns:**

* `dict`: User usage information.

---

### `active_next_user_plan(username: str) -> dict`

Activate the next subscription plan for a user.

**Parameters:**

* `username (str)`: Username of the user.

**Returns:**

* `dict`: Updated user information.

---

### `get_users() -> dict`

Retrieve a list of all users.

**Returns:**

* `dict`: All users in the panel.

---

### `reset_users_data_usage() -> str`

Reset data usage for all users.

**Returns:**

* `str`: "success" if the reset was successful.

---

### `get_users_usage() -> dict`

Retrieve usage statistics for all users.

**Returns:**

* `dict`: Users' usage statistics.

---

### `set_owner_for_user(username: str, admin_username: str) -> dict`

Assign an admin as the owner of a specific user.

**Parameters:**

* `username (str)`: Username of the user.
* `admin_username (str)`: Admin username to assign as owner.

**Returns:**

* `dict`: API response.

---

### `get_expired_users() -> dict`

Retrieve a list of users whose accounts have expired.

**Returns:**

* `dict`: Expired users information.

---

### `delete_expired_users() -> dict`

Delete all users whose accounts have expired.

**Returns:**

* `dict`: API response confirming deletion.

---

# UserTemplate Documentation <a id="templates-class"></a>

The `UserTemplate` class provides an abstraction layer for managing **user templates** through the `Panel` API.
It includes methods for creating, retrieving, updating, and deleting templates.

---

## Initialization

```python
from marzban import Panel
from marzban.models.user_template_model import UserTemplateConfig
from marzban.user_template import UserTemplate

panel = Panel(panel_url="https://marzban.panel:8000/DASHBOARD_PATH")
user_templates = UserTemplate(panel)
```

**Parameters:**

* `panel (Panel)`: Instance of the Panel API client.

---

## Methods

### `add_user_template(template: UserTemplateConfig) -> dict`

Add a new user template.

**Parameters:**

* `template (UserTemplateConfig)`: The configuration of the template to create.

**Returns:**

* `dict`: Created template's data.

---

### `get_user_templates() -> dict`

Retrieve a list of user templates.

**Returns:**

* `dict`: A dictionary containing templates' data (may include pagination info).

---

### `get_user_template_endpoint(template_id: int) -> dict`

Retrieve information about a specific user template by its ID.

**Parameters:**

* `template_id (int)`: The ID of the user template.

**Returns:**

* `dict`: The template's details.

---

### `modify_user_template(template_id: int, template: UserTemplateConfig) -> dict`

Update an existing user template.

**Parameters:**

* `template_id (int)`: The ID of the user template to update.
* `template (UserTemplateConfig)`: The updated template configuration.

**Returns:**

* `dict`: The updated template's data.

---

### `remove_user_template(template_id: int) -> dict`

Delete a user template by ID.

**Parameters:**

* `template_id (int)`: The ID of the user template to remove.

**Returns:**

* `dict`: The API response after deletion.
