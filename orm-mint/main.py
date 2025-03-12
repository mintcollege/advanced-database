from typing import Annotated
from fastapi import FastAPI, Depends, Body
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from models.Pokemon import Pokemon
from pydantic import BaseModel
from icecream import ic


# Setup the use of your database
DATABASE_URL = 'postgresql+asyncpg://postgres:pass123@localhost:5432/postgres'
async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)

async def get_session() -> AsyncSession:
    """
    Return the async session for use in endpoints.
    Refer to: https://chatgpt.com/c/675b9fb2-ec10-8000-a269-35fdbf5d20ef
    """
    async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


app = FastAPI()


@app.get('/')
async def index():
    return 'Hello to you!'


class CreatePokemon(BaseModel):
    name: str
    type: str
    health: int
    weakness: str


@app.post('/create')
async def create(data: CreatePokemon, session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Create a new Pokemon
    """
    ic(data)
    pokemon = Pokemon(name=data.name, type=data.type, health=data.health, weakness=data.weakness)
    ic(pokemon)
    session.add(pokemon)
    await session.commit()      # Saves pikachu to the database
    await session.refresh(pokemon) # Updates pikachu with the db id
    ic(pokemon)
    return pokemon


@app.post('/edit/{id_}')
async def edit_pokemon(id_: int, data: Annotated[dict, Body()],
                       session: Annotated[AsyncSession, Depends(get_session)]):
    pokemon = await session.get(Pokemon, id_)
    ic(type(pokemon))
    pokemon.name = data['name']
    session.add(pokemon)
    await session.commit()
    return True