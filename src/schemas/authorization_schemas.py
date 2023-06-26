from pydantic import BaseModel


class AuthorizationResponseSchema(BaseModel):
    access_token: str = 'XXXXXXXXXXXXXXXXX'
    token_type: str = "bearer"
