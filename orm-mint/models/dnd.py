from sqlmodel import SQLModel, Field, Relationship


class CommonFields(SQLModel):
    id: int | None = Field(primary_key=True)


class Weapon(CommonFields, SQLModel, table=True):
    name: str = Field(max_length=199)
    type: str = Field(max_length=199)
    rarity: int = Field(ge=1, le=5, default=1)
    is_equiped: bool = Field(default=False)
    character_id: int = Field(foreign_key='character.id', ondelete='CASCADE')

    character: 'Character' = Relationship(back_populates='weapons')




class Character(CommonFields, SQLModel, table=True):
    name: str = Field(max_length=199)
    race: str = Field(max_length=199)
    health: int = Field(ge=0, le=1000, default=100)

    weapons: 'Weapon' = Relationship(back_populates='character',
                                     sa_relationship_kwargs={'lazy': 'selectin'})
