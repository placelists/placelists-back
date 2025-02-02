import random
import string

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from models import Meta
from models import MultipleResponseWrapper
from models import Place
from models import PlaceCreate
from models import Placelist
from models import PlacelistCreate
from models import PlacelistUpdate
from models import PlaceUpdate
from models import SingleResponseWrapper
from models import User
from models import UserUpdate


app = FastAPI(
    title="Placelists",
    version="1.0",
    servers=[{"url": "http://localhost:8082"}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_id():
    return "".join(random.choices(string.ascii_letters, k=9))


@app.get("/api/v1/users/my", tags=["users"])
def get_user_my() -> SingleResponseWrapper[User]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=User(username=get_id()), meta=Meta(success=True)
        ).model_dump(),
    )


@app.get("/api/v1/users/{username}", tags=["users"])
def get_user_by_username(username: str) -> SingleResponseWrapper[User]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=User(username=get_id()), meta=Meta(success=True)
        ).model_dump(),
    )


@app.put("/api/v1/users/{username}", tags=["users"])
def put_user_by_username(
    username: str, user_update: UserUpdate
) -> SingleResponseWrapper[User]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=User(username=get_id()), meta=Meta(success=True)
        ).model_dump(),
    )


@app.get("/api/v1/placelists", tags=["placelists"])
def get_placelists_by_query(query: str) -> MultipleResponseWrapper[Placelist]:
    return JSONResponse(
        status_code=200,
        content=MultipleResponseWrapper(
            data=[
                Placelist(
                    id=get_id(),
                    name=get_id(),
                    author_username=get_id() if i % 4 != 0 else None,
                )
                for i in range(20)
            ],
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.get("/api/v1/placelists/{id}", tags=["placelists"])
def get_placelist_by_id(id: str) -> SingleResponseWrapper[Placelist]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Placelist(id=get_id(), name=get_id(), author_username=get_id()),
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.post("/api/v1/placelists", tags=["placelists"])
def post_placelist(
    placelist_create: PlacelistCreate,
) -> SingleResponseWrapper[Placelist]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Placelist(id=get_id(), name=get_id(), author_username=get_id()),
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.get("/api/v1/placelists/my", tags=["placelists"])
def get_placelists_my(id: str) -> MultipleResponseWrapper[Placelist]:
    return JSONResponse(
        status_code=200,
        content=MultipleResponseWrapper(
            data=[
                Placelist(
                    id=get_id(),
                    name=get_id(),
                    author_username=get_id() if i % 4 != 0 else None,
                )
                for i in range(20)
            ],
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.get("/api/v1/placelists/{id}/places", tags=["placelists"])
def get_placelist_places_by_id(id: str) -> MultipleResponseWrapper[Place]:
    return JSONResponse(
        status_code=200,
        content=MultipleResponseWrapper(
            data=[
                Place(
                    id=get_id(),
                    name=get_id(),
                    address=get_id(),
                    visited=bool(random.getrandbits(1)),
                )
                for _ in range(20)
            ],
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.put("/api/v1/placelists/{id}", tags=["placelists"])
def put_placelists_id(
    id: str, placelist_update: PlacelistUpdate
) -> SingleResponseWrapper[Placelist]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Placelist(
                id=get_id(),
                name=get_id(),
                author_username=get_id(),
            ),
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.put("/api/v1/placelists/{id}/places", tags=["placelists"])
def put_placelist_places_by_id(
    id: str, places: list[Place]
) -> MultipleResponseWrapper[Place]:
    return JSONResponse(
        status_code=200,
        content=MultipleResponseWrapper(
            data=[
                Place(
                    id=get_id(),
                    name=get_id(),
                    address=get_id(),
                    visited=bool(random.getrandbits(1)),
                )
                for _ in range(20)
            ],
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.delete("/api/v1/placelists/{id}", tags=["placelists"])
def delete_placelists_by_id(id: str) -> SingleResponseWrapper[Placelist]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Placelist(
                id=get_id(),
                name=get_id(),
                author_username=get_id(),
            ),
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.get("/api/v1/places", tags=["places"])
def get_places_by_query(query: str) -> MultipleResponseWrapper[Place]:
    return JSONResponse(
        status_code=200,
        content=MultipleResponseWrapper(
            data=[
                Place(
                    id=get_id(),
                    name=get_id(),
                    address=get_id(),
                    visited=bool(random.getrandbits(1)),
                )
                for _ in range(20)
            ],
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.post("/api/v1/places", tags=["places"])
def post_place(place_create: PlaceCreate) -> SingleResponseWrapper[Place]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Place(
                id=get_id(),
                name=get_id(),
                address=get_id(),
                visited=bool(random.getrandbits(1)),
            ),
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.get("/api/v1/places/{id}", tags=["places"])
def get_place_by_id(id: str) -> SingleResponseWrapper[Place]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Place(
                id=get_id(),
                name=get_id(),
                address=get_id(),
                visited=bool(random.getrandbits(1)),
            ),
            meta=Meta(success=True),
        ).model_dump(),
    )


@app.put("/api/v1/places/{id}", tags=["places"])
def put_place_by_id(id: str, place_update: PlaceUpdate) -> SingleResponseWrapper[Place]:
    return JSONResponse(
        status_code=200,
        content=SingleResponseWrapper(
            data=Place(
                id=get_id(),
                name=get_id(),
                address=get_id(),
                visited=bool(random.getrandbits(1)),
            ),
            meta=Meta(success=True),
        ).model_dump(),
    )
