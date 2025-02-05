from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    foo: int
    bar: int


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict()

    id: int
