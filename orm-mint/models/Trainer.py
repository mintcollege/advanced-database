from sqlmodel import SQLModel, Field



class Trainer(SQLModel, table=True):
    __tablename__ = "trainerxyz123"
    id: int | None = Field(primary_key=True)
    name: str = Field(max_length=199)
    email: str = Field(max_length=256)
    region: str = Field(max_length=199)
    type: str = Field(max_length=20)
    gender: str = Field(min_length=1, max_length=1)