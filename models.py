from pydantic import BaseModel


class Meta(BaseModel):
    success: bool


class Error(BaseModel):
    message: str


class SingleResponseWrapper[T](BaseModel):
    data: T | None = None
    meta: Meta
    errors: list[Error] = []


class MultipleResponseWrapper[T](BaseModel):
    data: list[T] = []
    meta: Meta
    errors: list[Error] = []


class Identity(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int


class User(BaseModel):
    id: str
    username: str


class UserUpdate(BaseModel):
    username: str


class Placelist(BaseModel):
    id: str
    name: str
    author: User


class PlacelistCreate(BaseModel):
    name: str


class PlacelistUpdate(BaseModel):
    name: str


class Place(BaseModel):
    id: str
    name: str
    address: str
    visited: bool


class PlaceCreate(BaseModel):
    name: str
    address: str
