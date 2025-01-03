from fastapi import FastAPI

from models import Identity, MultipleResponseWrapper, Place, PlaceCreate, Placelist, PlacelistCreate, PlacelistUpdate, SingleResponseWrapper, User, UserUpdate

app = FastAPI(
    title='Placelists',
    version='1.0',
    servers=[{'url': 'http://localhost:8082/api/v1'}],
)


@app.get('/login', tags=['identity'])
def get_login(client_id: str, code: str) -> SingleResponseWrapper[Identity]:
    pass


@app.get('/refresh', tags=['identity'])
def get_login(client_id: str, refresh_token: str) -> SingleResponseWrapper[Identity]:
    pass


@app.get('/users/{username}', tags=['users'])
def get_users_username(username: str) -> SingleResponseWrapper[User]:
    pass


@app.put('/users/{username}', tags=['users'])
def put_users_username(username: str, user_update: UserUpdate) -> SingleResponseWrapper[User]:
    pass


@app.get('/placelists',tags=['placelists'])
def get_placelists(query: str) -> MultipleResponseWrapper[Placelist]:
    pass


@app.post('/placelists', tags=['placelists'])
def post_placelists(placelist_create: PlacelistCreate) -> SingleResponseWrapper[Placelist]:
    pass


@app.get('/placelists/{id}', tags=['placelists'])
def get_placelists_id(id: str) -> SingleResponseWrapper[Placelist]:
    pass


@app.put('/placelists/{id}', tags=['placelists'])
def put_placelists_id(id: str, placelist_update: PlacelistUpdate) -> SingleResponseWrapper[Placelist]:
    pass


@app.delete('/placelists/{id}', tags=['placelists'])
def delete_placelists_id(id: str) -> SingleResponseWrapper[Placelist]:
    pass


@app.get('/places', tags=['places'])
def get_places(query: str) -> MultipleResponseWrapper[Place]:
    pass


@app.post('/places', tags=['places'])
def post_places(place_create: PlaceCreate) -> SingleResponseWrapper[Place]:
    pass


@app.get('/places/{id}', tags=['places'])
def get_places_id(id: str) -> SingleResponseWrapper[Place]:
    pass


@app.put('/places/{id}/visit', tags=['places'])
def put_places_id(id: str) -> SingleResponseWrapper[Place]:
    pass
