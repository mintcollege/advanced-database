from sqlmodel import SQLModel, Field, Relationship, text, DateTime, func
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from sqlalchemy.orm import declared_attr


class UpdatedAtMixin:
    @declared_attr
    def updated_at(cls):  # noqa
        return Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=True)


class CreatedAtMixin:
    @declared_attr
    def created_at(cls):  # noqa
        return Column(DateTime(timezone=True), server_default=func.now(), nullable=True)


class CommonMixin(UpdatedAtMixin, CreatedAtMixin):
    id: int | None = Field(primary_key=True)


class BookAuthors(SQLModel, table=True):
    __tablename__ = 'book_authors'
    book_id: int = Field(primary_key=True, foreign_key='book.id', ondelete='CASCADE')
    author_id: int = Field(primary_key=True, foreign_key='author.id', ondelete='CASCADE')
    # abc_id: int = Field(primary_key=True, foreign_key='abc.id', ondelete='CASCADE')


# class BookGenre(SQLModel, table=True):
#     __tablename__ = 'book_genres'
#     book_id: int = Field(primary_key=True, foreign_key='book.id', ondelete='CASCADE')
#     genre_id: int = Field(primary_key=True, foreign_key='genre.id', ondelete='CASCADE')
#
#
# class Genre(CommonMixin, SQLModel, table=True):
#     name: str = Field(max_length=255)
#     books: list['Book'] = Relationship(back_populates='genres')
#
#
#     def __str__(self) -> str:
#         return f'<Genre {self.id}: {self.name}>'  # noqa


class Book(CommonMixin, SQLModel, table=True):
    title: str = Field(max_length=199)
    year: int = Field(gt=0)
    isbn: int = Field(max_length=20)
    pages: int = Field(gt=0)
    rating: str = Field(max_length=100)

    authors: list['Author'] = Relationship(back_populates='book_authors', link_model=BookAuthors)
    # genres: list['Author'] = Relationship(back_populates='book_genres', link_model=BookAuthors)


    def __str__(self) -> str:
        """Magic method"""
        return f'<Book {self.id}: {self.title}>'  # noqa


class Author(CommonMixin, SQLModel, table=True):
    first_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    gender: str = Field(max_length=255)
    published: int = Field(ge=0)
    nationality: str = Field(max_length=255)
    meta: dict = Field(sa_column=Column(JSONB, server_default=text("'{}'::jsonb")))

    book_authors: list['Book'] = Relationship(back_populates='authors', link_model=BookAuthors)


    def __str__(self) -> str:
        return f'<Author {self.id}: {self.first_name} {self.last_name}>'  # noqa
