from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///edu.db", echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class StudentsOrm(Model): # name, fname, lname, group
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fname: Mapped[str]
    lname: Mapped[str]
    mname: Mapped[Optional[str]]
    group: Mapped[int] = mapped_column(ForeignKey('groups.id'), nullable=True)
#    group: Mapped["Groups"] = relationship(back_populates="groups", uselist=False) #many-to-one связь
    elder: Mapped[bool]

class GroupsOrm(Model):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    num: Mapped[str]
#    students: Mapped[list["Students"]] = relationship(back_populates="students", uselist=True) #one-to-many связь


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)