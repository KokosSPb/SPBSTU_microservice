from typing import Annotated

from fastapi import APIRouter, Depends

from repository import StudentsRepository, GroupsRepository
from schemas import SStudentAdd, SStudent, SGroupAdd, SGroup

routerStudents = APIRouter(prefix="/students", tags=["Студенты"])
routerGroups = APIRouter(prefix="/groups", tags=["Группы"])


@routerStudents.post("")
async def add_student(student: Annotated[SStudentAdd, Depends()]):
    student_id = await StudentsRepository.add_one(student)
    return {"add": True, "student_id": student_id}


@routerStudents.get("")
async def get_students() -> list[SStudent]:
    students = await StudentsRepository.find_all()
    return students

@routerStudents.get("/{student_id}")
async def get_student(student_id: int) -> SStudent:
    student = await StudentsRepository.find_one(student_id)
    return student

@routerStudents.delete("/{student_id}")
async def del_student(student_id: int):
    student = await StudentsRepository.del_student(student_id)
    return {"delete": True, "student_id": student}

@routerGroups.post("")
async def add_groups(group: Annotated[SGroupAdd, Depends()]):
    group_id = await GroupsRepository.add_one(group)
    return {"ok": True, "group_id": group_id}


@routerGroups.get("")
async def get_groups() -> list[SGroup]:
    groups = await GroupsRepository.find_all()
    return groups

@routerGroups.get("/{group_id}")
async def get_groups(group_id: int) -> SGroup:
    groups = await GroupsRepository.find_one(group_id)
    return groups

@routerGroups.delete("/{group_id}")
async def del_group(group_id: int):
    group = await GroupsRepository.del_group(group_id)
    return {"delete": True, "group_id": group}

@routerGroups.get("/list/{group_id}")
async def get_students_list(group_id: int) -> list[SStudent]:
    students = await GroupsRepository.students_list(group_id)
    return students

@routerGroups.put("/{group_id}/{student_id}")
async def update_group(group_id: int, student_id:int) -> SStudent:
    student = await GroupsRepository.update_group(group_id, student_id)
    return student

@routerGroups.put("/{student_id}")
async def del_student(student_id: int) -> SStudent:
    student = await GroupsRepository.del_student(student_id)
    return student
