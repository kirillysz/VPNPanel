from typing import Dict, Optional
from pydantic import BaseModel, Field, constr, conint
from datetime import datetime

class UserModel(BaseModel):
    username: constr(min_length=3, max_length=32, regex=r'^[a-z0-9_]+$')
    status: str = Field(default="active", description="User's status, defaults to active. Special rules if on_hold.")
    expire: int = Field(default=0, description="UTC timestamp for account expiration. Use 0 for unlimited.")
    data_limit: int = Field(default=0, description="Max data usage in bytes. 0 means unlimited.")
    data_limit_reset_strategy: str = Field(default="no_reset", description="Defines how/if data limit resets.")
    proxies: Dict[str, Dict] = Field(default_factory=dict, description="Dictionary of protocol settings (vmess, vless, etc.)")
    inbounds: Dict[str, str] = Field(default_factory=dict, description="Dictionary of protocol tags for inbound connections")
    note: Optional[str] = Field(default=None, description="Optional additional notes")
    on_hold_timeout: Optional[int] = Field(default=None, description="UTC timestamp when on_hold status should start or end")
    on_hold_expire_duration: Optional[int] = Field(default=None, description="Duration in seconds for on_hold status")
    next_plan: Optional[str] = Field(default=None, description="Next user plan (resets after use)")

