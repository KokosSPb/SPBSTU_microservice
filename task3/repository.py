from sqlalchemy import select, null

from database import new_session, StudentsOrm, GroupsOrm
from schemas import SStudentAdd, SStudent, SGroupAdd, SGroup


class StudentsRepository:
    @classmethod
    async def add_one(cls, data: SStudentAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            student = StudentsOrm(**task_dict)
            session.add(student)
            await session.flush()
            await session.commit()
            return student.id

    @classmethod
    async def find_all(cls) -> list[SStudent]:
        async with (new_session() as session):
            query = select(StudentsOrm)
            result = await session.execute(query)
            students_models = result.scalars().all()
            student_schemas = [SStudent.model_validate(student_models) for student_models in students_models]
            return student_schemas

    @classmethod
    async def find_one(self, id) -> SStudent:
        async with new_session() as session:
            query = select(StudentsOrm).where(StudentsOrm.id == id)
            result = await session.execute(query)
            student_models = result.scalar()
            student_schemas = SStudent.model_validate(student_models)
            return student_schemas

    @classmethod
    async def del_student(self, id):
        async with new_session() as session:
            query = select(StudentsOrm).filter(StudentsOrm.id == id)
            result = await session.execute(query)
            student_models = result.scalar()
            await session.delete(student_models)
            await session.flush()
            await session.commit()
            return id

class GroupsRepository:
    @classmethod
    async def add_one(cls, data: SGroupAdd) -> int:
        async with new_session() as session:
            group_dict = data.model_dump()

            group = GroupsOrm(**group_dict)
            session.add(group)
            await session.flush()
            await session.commit()
            return group.id

    @classmethod
    async def find_all(cls) -> list[SGroup]:
        async with new_session() as session:
            query = select(GroupsOrm)
            result = await session.execute(query)
            group_models = result.scalars().all()
            group_schemas = [SGroup.model_validate(group_model) for group_model in group_models]
            return group_schemas

    @classmethod
    async def find_one(self, id) -> SGroup:
        async with new_session() as session:
            query = select(GroupsOrm).where(GroupsOrm.id == id)
            result = await session.execute(query)
            group_models = result.scalar()
            group_schemas = SGroup.model_validate(group_models)
            return group_schemas

    @classmethod
    async def del_group(self, id):
        async with new_session() as session:
            query = select(GroupsOrm).filter(GroupsOrm.id == id)
            result = await session.execute(query)
            group_models = result.scalar()
            await session.delete(group_models)
            await session.flush()
            await session.commit()
            return id

    @classmethod
    async def students_list(self, id):
        async with new_session() as session:
            query = select(StudentsOrm).where(StudentsOrm.group == id)
            result = await session.execute(query)
            students_models = result.scalars().all()
            student_schemas = [SStudent.model_validate(student_models) for student_models in students_models]
            return student_schemas

    @classmethod
    async def update_group(self, group_id, student_id) -> SStudent:
        async with new_session() as session:
            query = select(StudentsOrm).filter(StudentsOrm.id == student_id)
            result = await session.execute(query)
            student_model = result.scalar()
            student_model.group = group_id
            await session.flush()
            await session.commit()
            await session.refresh(student_model)
            student_schemas = SStudent.model_validate(student_model)
            return student_schemas

    @classmethod
    async def del_student(self, student_id) -> SStudent:
        async with new_session() as session:
            query = select(StudentsOrm).filter(StudentsOrm.id == student_id)
            result = await session.execute(query)
            student_model = result.scalar()
            student_model.group = null()
            await session.flush()
            await session.commit()
            await session.refresh(student_model)
            student_schemas = SStudent.model_validate(student_model)
            return student_schemas