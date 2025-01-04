from fastapi import FastAPI
from fastapi.responses import JSONResponse

from values import PLACELIST, USER, USER_PLACELIST

import string
import random

from models import Error, Identity, Meta, MultipleResponseWrapper, Place, PlaceCreate, Placelist, PlacelistCreate, PlacelistUpdate, PlacelistWithPlaces, SingleResponseWrapper, User, User

app = FastAPI(
    title='Placelists',
    version='1.0',
    servers=[{'url': 'http://localhost:8082'}],
)


def get_id():
    return ''.join(random.choices(string.ascii_letters, k=9))


@app.get('/api/v1/login', tags=['identity'])
def get_login(client_id: str, code: str) -> SingleResponseWrapper[Identity]:
    pass


@app.get('/api/v1/refresh', tags=['identity'])
def get_login(client_id: str, refresh_token: str) -> SingleResponseWrapper[Identity]:
    pass


@app.get('/api/v1/users/{username}', tags=['users'])
def get_users_username(username: str) -> SingleResponseWrapper[User]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=User(
        username=get_id()
    ), meta=Meta(success=True)).model_dump())


@app.put('/api/v1/users/{username}', tags=['users'])
def put_users_username(username: str, user_update: User) -> SingleResponseWrapper[User]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=User(
        username=get_id()
    ), meta=Meta(success=True)).model_dump())


@app.get('/api/v1/placelists',tags=['placelists'])
def get_placelists(query: str) -> MultipleResponseWrapper[Placelist]:
    return JSONResponse(status_code=200, content=MultipleResponseWrapper(data=[Placelist(
        id=get_id(),
        name=get_id(),
        author_username=get_id() if i % 4 != 0 else None
    ) for i in range(20)], meta=Meta(success=True)).model_dump())


@app.post('/api/v1/placelists', tags=['placelists'])
def post_placelists(placelist_create: PlacelistCreate) -> SingleResponseWrapper[Placelist]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Placelist(
        id=get_id(),
        name=get_id(),
        author_username=get_id()
    ), meta=Meta(success=True)).model_dump())


@app.get('/api/v1/placelists/{id}', tags=['placelists'])
def get_placelists_id(id: str) -> SingleResponseWrapper[PlacelistWithPlaces]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Placelist(
        id=get_id(),
        name=get_id(),
        author_username=get_id()
    ), meta=Meta(success=True)).model_dump())


@app.put('/api/v1/placelists/{id}', tags=['placelists'])
def put_placelists_id(id: str, placelist_update: PlacelistUpdate) -> SingleResponseWrapper[PlacelistWithPlaces]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Placelist(
        id=get_id(),
        name=get_id(),
        author_username=get_id()
    ), meta=Meta(success=True)).model_dump())


@app.delete('/api/v1/placelists/{id}', tags=['placelists'])
def delete_placelists_id(id: str) -> SingleResponseWrapper[PlacelistWithPlaces]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Placelist(
        id=get_id(),
        name=get_id(),
        author_username=get_id()
    ), meta=Meta(success=True)).model_dump())


@app.get('/api/v1/places', tags=['places'])
def get_places(query: str) -> MultipleResponseWrapper[Place]:
    return JSONResponse(status_code=200, content=MultipleResponseWrapper(data=[Place(
        id=get_id(),
        name=get_id(),
        address=get_id(),
        visited=i % 3 == 0
    ) for i in range(20)], meta=Meta(success=True)).model_dump())


@app.post('/api/v1/places', tags=['places'])
def post_places(place_create: PlaceCreate) -> SingleResponseWrapper[Place]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Place(
        id=get_id(),
        name=get_id(),
        address=get_id(),
        visited=False
    ), meta=Meta(success=True)).model_dump())


@app.get('/api/v1/places/{id}', tags=['places'])
def get_places_id(id: str) -> SingleResponseWrapper[Place]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Place(
        id=get_id(),
        name=get_id(),
        address=get_id(),
        visited=False
    ), meta=Meta(success=True)).model_dump())


@app.put('/api/v1/places/{id}/visit', tags=['places'])
def put_places_id(id: str) -> SingleResponseWrapper[Place]:
    return JSONResponse(status_code=200, content=SingleResponseWrapper(data=Place(
        id=get_id(),
        name=get_id(),
        address=get_id(),
        visited=False
    ), meta=Meta(success=True)).model_dump())
