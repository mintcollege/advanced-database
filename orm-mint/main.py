from typing import Annotated
from fastapi import FastAPI, Depends, Body
from sqlmodel import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from pydantic import BaseModel
from icecream import ic

from models.Pokemon import Pokemon
from models.dnd import Character, Weapon


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


@app.post('/create/pokemon')
async def create(data: CreatePokemon, session: Annotated[AsyncSession, Depends(get_session)]):
    """
    Create a new Pokemon
    """
    ic(data)
    pokemon = Pokemon(name=data.name, type=data.type, health=data.health, weakness=data.weakness)
    ic(pokemon)
    session.add(pokemon)
    await session.commit()  # Saves pikachu to the database
    await session.refresh(pokemon)  # Updates pikachu with the db id
    ic(pokemon)
    return pokemon


@app.post('/edit/pokemon/{id_}')
async def edit_pokemon(id_: int, data: Annotated[dict, Body()],
                       session: Annotated[AsyncSession, Depends(get_session)]):
    pokemon = await session.get(Pokemon, id_)
    ic(type(pokemon))
    pokemon.name = data['name']
    session.add(pokemon)
    await session.commit()
    return True


@app.post('/create/character')
async def create_char(session: Annotated[AsyncSession, Depends(get_session)]):
    # john = Character(name='john', race='white', health=1000)
    # jake = Character(name='jake', race='white', health=10)
    nic = Character(name='nic', race='ogre', health=100)
    # session.add(john)
    # session.add(jake)
    session.add(nic)
    await session.commit()
    # await session.refresh(john)
    # await session.refresh(jake)
    await session.refresh(nic)

    # staff = Weapon(name='staff', type='mage', is_equiped=True, character_id=john.id)
    # session.add(staff)
    # # session.add(axe)
    # await session.commit()

    return True


@app.post('/equip')
async def equip_weapon(session: Annotated[AsyncSession, Depends(get_session)]):
    # Get jake
    # Equip jake

    # Get character by their id
    # jake = await session.get(Character, 5)
    nic = await session.get(Character, 6)

    # Get character by their name
    # stmt = select(Character).where(Character.name == 'jake')    # noqa
    # exec_ = await session.exec(stmt)
    # jake = exec_.all()
    # ic(jake)

    # axe = Weapon(name='axe', type='melee', is_equiped=True, character_id=jake.id)
    sword = Weapon(name='sword', type='melee', is_equiped=True, character_id=nic.id, character=nic)  # noqa
    # session.add(axe)
    session.add(sword)
    await session.commit()

    return True


@app.delete('/jake')
async def delete_jake(session: Annotated[AsyncSession, Depends(get_session)]):
    jake = await session.get(Character, 3)
    await session.delete(jake)
    await session.commit()

    return 'Jake is deleted. Yay!'


@app.get('/drink/potion')
async def potion(session: Annotated[AsyncSession, Depends(get_session)]):
    jake = await session.get(Character, 5)
    jake.health = 100
    session.add(jake)
    await session.commit()
    return jake


@app.get('/check-weapon')
async def check_weapon(session: Annotated[AsyncSession, Depends(get_session)]):
    char = await session.get(Character, 6)
    # await session.refresh(char, attribute_names=['weapons'])
    ic(char)
    return char.weapons
