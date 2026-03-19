from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    senha: str