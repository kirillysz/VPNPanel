from pydantic import BaseModel, Field
from typing import Dict, List, Optional

class UserTemplateConfig(BaseModel):
    name: str = Field(..., max_length=64, description="User template name, up to 64 characters")
    data_limit: int = Field(..., ge=0, description="Data limit in bytes, must be >= 0")
    expire_duration: int = Field(..., ge=0, description="Expiration duration in seconds, must be >= 0")
    inbounds: Optional[Dict[str, List[str]]] = Field(default_factory=dict, description="Dictionary of protocol:inbound_tags, empty means all inbounds")


class CreateUserTemplateRequest(BaseModel):
    additionalProp1: List[UserTemplateConfig]
