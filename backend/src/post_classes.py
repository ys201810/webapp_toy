# coding=utf-8
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
