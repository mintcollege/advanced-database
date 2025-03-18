from sqlmodel import SQLModel, Field, Relationship


class SteamGame(SQLModel, table=True):
    __tablename__ = 'app_steamgame'
    id: int | None = Field(primary_key=True)
    name: str = Field(max_length=199)

    genres: list['Genre'] = Relationship(back_populates='game', sa_relationship_kwargs={
        'lazy': 'selectin'
    })

    def __str__(self):
        return f'<SteamGame {self.id}: {self.name}>'


class Genre(SQLModel, table=True):
    __tablename__ = 'app_genre'
    id: int | None = Field(primary_key=True)
    steamgame_id: int | None = Field(foreign_key='app_steamgame.id')
    name: str = Field(max_length=199)

    game: 'SteamGame' = Relationship(back_populates='genres')

    def __str__(self):
        return f'<SteamGame {self.id}: {self.name}>'