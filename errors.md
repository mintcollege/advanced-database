# Midterm Errors


```python
class Error(SQLModel, table=True):
    __tablename__ = 'errors'
    id: UUID = Field(factory=uuid4, primary_key=True)
    
    inmate_number: str
    
    inmate_number: int = None
    
    some_number: int = Field(sa_column=Column(String(199), default_factory=some_function))
    
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
```
