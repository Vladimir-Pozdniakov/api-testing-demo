from pydantic import BaseModel


class PoemResponse(BaseModel):
    title: str
    author: str
    lines: list[str]
    linecount: str


class AuthorsResponse(BaseModel):
    authors: list[str]


class TitlesResponse(BaseModel):
    titles: list[str]
