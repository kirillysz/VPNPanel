from pydantic import BaseModel
from typing import List, Optional


class HostConfig(BaseModel):
    remark: str = "string"
    address: str = "string"
    port: int = 0
    sni: str = "string"
    host: str = "string"
    path: str = "string"
    security: str = "inbound_default"
    alpn: str = ""
    fingerprint: str = ""
    allowinsecure: bool = True
    is_disabled: bool = True
    mux_enable: bool = True
    fragment_setting: str = "string"
    noise_setting: str = "string"
    random_user_agent: bool = True
    use_sni_as_host: bool = True


class ModifyHostsRequest(BaseModel):
    additionalProp1: List[HostConfig]