from typing import Annotated
from fastapi import FastAPI, Depends, Body
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from pydantic import BaseModel
from models.Pokemon import Pokemon
from icecream import ic
from models.Game import Game, Genre, Tag, GameTags


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
    await session.commit()  # Saves pikachu to the database
    await session.refresh(pokemon)  # Updates pikachu with the db id
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


@app.post('/populate')
async def foo(session: Annotated[AsyncSession, Depends(get_session)]):
    # Tags
    tag1 = Tag(tag='apple')
    tag2 = Tag(tag='orange')
    tag3 = Tag(tag='banana')
    game = Game(name='mygame', tags=[tag1, tag2])
    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.add(game)
    await session.commit()
    await session.refresh(tag1)
    await session.refresh(tag2)
    await session.refresh(tag3)
    await session.refresh(game)

    genre1 = Genre(name='rpg', game=game)
    genre2 = Genre(name='isometric', game=game)
    session.add(genre1)
    session.add(genre2)
    await session.commit()
    await session.refresh(genre1)
    await session.refresh(genre2)

    return True


@app.get('/foo')
async def foo(session: Annotated[AsyncSession, Depends(get_session)]):
    # Game
    stmt = select(Game).where(Game.name == 'mygame')  # noqa
    exec_ = await session.exec(stmt)  # noqa
    if game := exec_.one_or_none():
        # ic(game, game.genres, game.tags)

        # Genre
        stmt = select(Genre).where(Genre.id == 1)  # noqa
        exec_ = await session.exec(stmt)  # noqa
        genre = exec_.one_or_none()
        # ic(genre, genre.game)

        # Tags
        tag = await session.get(Tag, 1)
        await session.refresh(tag, attribute_names=['games'])
        # ic(tag, tag.games)

        # # Add/Remove tag to/from Game
        # tag3 = await session.get(Tag, 3)
        # game.tags.append(tag3)
        # game.tags = list(filter(lambda x: x.id != 2, game.tags))
        # session.add(game)
        # await session.commit()
        #
        # # View Game again
        # game = await session.get(Game, 1)
        # ic(game, game.tags)

        # # Delete tag
        # ic(game.tags)
        # await session.delete(tag)
        # await session.commit()
        # await session.refresh(game)
        # ic(game.tags)

        stmt = select(GameTags).where(GameTags.game_id == 1)    # noqa
        exec_ = await session.exec(stmt)    # noqa
        gt = exec_.all()
        ic(gt)


    return True
