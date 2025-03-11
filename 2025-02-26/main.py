from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    age: int = Field(le=100)
    name: str = Field(max_length=10)
    password: str = Field(min_length=8,)
    number: str


class Account(BaseModel):
    pass



def abc(data: UserInfo):
    # Save to account table
    print(data)


# userinfo = UserInfo(age=100, name='abc1234567', password='pass1234', number='1234-567')
# abc(userinfo)



class CharacterSchema(BaseModel):
    id: int  = Field(gt=0)
    name: str = Field(max_length=100)
    age: int = Field(gt=0)
    gender: str = Field(min_length=1, max_length=1, pattern='^[M|F|m|f]$')
    email: str = Field(pattern='[a-zA-Z.]+@mintcollege.com$')

class Character:
    id: int
    alignment: str = 'hero'
    name: str
    gender: str
    age: int
    status: str = 'alive'
    nationality: str = 'Filipino'
    max_health: int = 100
    skin: str = ''


    def __init__(self, data: CharacterSchema):
        self.id = data.id
        self.name = data.name
        self.age = data.age
        self.gender = data.gender


    def __str__(self):
        return f'<Character {self.id}: {self.name}>'


    def attack(self):
        print('USER IS ATTACKING!')


sally = Character(CharacterSchema(id=1, name='sally', age=123, gender='m', email='aaa@mintcollege.com'))
print(sally)