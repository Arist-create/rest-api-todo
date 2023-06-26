from pydantic import BaseModel


class UserRequestSchema(BaseModel):
    username: str = 'ivan2002'
    password: str = '12345'
    is_superuser: bool = True
