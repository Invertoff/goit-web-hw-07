from sqlalchemy import func, cast, Numeric, desc
from models_db import Student, Group, Teacher, Subject, Grade
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def select_1(session):
    return session.query(
        Student.fullname,
        func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
    ).select_from(Group).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session, subject_id):
    return session.query(
        Student.fullname, 
        func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
    ).select_from(Student).join(Grade, isouter=True).filter(Grade.subject_id == subject_id)\
    .group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(session, subject_id):
    return session.query(
        Group.name, 
        func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
    ).join(Student).select_from(Student).join(Grade).filter(Grade.subject_id == subject_id)\
    .group_by(Group.id).all()

def select_4(session):
    return session.query(
        func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
    ).all()

def select_5(session, teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(session, group_id):
    return session.query(Student.fullname).filter(Student.group_id == group_id).all()

def select_7(session, group_id, subject_id):
    return session.query(Student.fullname, Grade.grade).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(session, teacher_id):
    return session.query(
        func.round(cast(func.avg(Grade.grade), Numeric), 2).label('avg_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).all()

def select_9(session, student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, isouter=True).group_by(Subject.id).all()

def select_10(session, student_id, teacher_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()

db_url = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()