from sqlmodel import SQLModel, Field


class Pokemon(SQLModel, table=True):
    __tablename__ = "pokemon"
    id: int | None = Field(primary_key=True)
    name: str = Field(max_length=199)
    type: str = Field(max_length=40)
    health: int = Field(ge=0)
    weakness: str = Field(max_length=50)
    evolution: int = Field(ge=1, le=3, default=1)
    notes: str = Field(max_length=256, default="",)

