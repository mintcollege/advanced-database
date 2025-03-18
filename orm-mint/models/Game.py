from sqlmodel import SQLModel, Field, Relationship


class GameTags(SQLModel, table=True):
    game_id: int = Field(foreign_key='app_game.id', primary_key=True, ondelete='CASCADE')
    tag_id: int = Field(foreign_key='app_tag.id', primary_key=True, ondelete='CASCADE')
    foo: str = Field(max_length=199, default='nothing here')


class Game(SQLModel, table=True):
    __tablename__ = 'app_game'
    id: int | None = Field(primary_key=True)
    name: str = Field(max_length=199)

    genres: list['Genre'] = Relationship(back_populates='game',
                                         sa_relationship_kwargs={'lazy': 'selectin'})
    tags: list['Tag'] = Relationship(back_populates='games', link_model=GameTags,
                                     sa_relationship_kwargs={'lazy': 'selectin'})


    def __str__(self):
        return f'<SteamGame {self.id}: {self.name}>'


class Tag(SQLModel, table=True):
    __tablename__ = 'app_tag'
    id: int | None = Field(primary_key=True)
    tag: str = Field(max_length=100)

    games: list['Game'] = Relationship(back_populates='tags', link_model=GameTags,
                                       sa_relationship_kwargs={'lazy': 'selectin'})


class Genre(SQLModel, table=True):
    __tablename__ = 'app_genre'
    id: int | None = Field(primary_key=True)
    steamgame_id: int | None = Field(foreign_key='app_game.id', ondelete='CASCADE')
    name: str = Field(max_length=199)

    game: 'Game' = Relationship(back_populates='genres', sa_relationship_kwargs={'lazy': 'selectin'})


    def __str__(self):
        return f'<SteamGame {self.id}: {self.name}>'
