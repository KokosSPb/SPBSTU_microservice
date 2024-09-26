from typing import Optional

from pydantic import BaseModel, ConfigDict


class SStudentAdd(BaseModel):
    fname: str
    lname: str
    mname: Optional[str] = None
    group: Optional[int] = None
    elder: bool

class SStudent(SStudentAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class SGroupAdd(BaseModel):
    name: str
    num: str

class SGroup(SGroupAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)