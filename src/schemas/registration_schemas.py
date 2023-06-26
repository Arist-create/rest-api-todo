from pydantic import BaseModel


class RegistrationRequestSchema(BaseModel):
    username: str = 'ivan2002'
    password: str = '12345'


class RegistrationResponseSchema(BaseModel):
    message: str = "User created successfully"
