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


class User(BaseModel):
    username: str


class UserUpdate(BaseModel):
    username: str


class Place(BaseModel):
    id: str
    name: str
    address: str
    visited: bool


class PlaceCreate(BaseModel):
    name: str
    address: str


class PlaceUpdate(BaseModel):
    name: str
    address: str
    visited: bool


class Placelist(BaseModel):
    id: str
    name: str
    author_username: str | None


class PlacelistCreate(BaseModel):
    name: str


class PlacelistUpdate(BaseModel):
    name: str
