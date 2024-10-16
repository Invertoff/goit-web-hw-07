from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models_db import Student, Group, Teacher, Subject, Grade, Base
from datetime import datetime
import random

faker = Faker()

# Connect to PostgreSQL database
db_url = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

# Generate random groups
groups = []
for _ in range(3):
    group = Group(name=faker.word())
    session.add(group)
    groups.append(group)

# Generate random teachers
teachers = []
for _ in range(3):
    teacher = Teacher(fullname=faker.name())
    session.add(teacher)
    teachers.append(teacher)

# Generate random subjects
subjects = []
for _ in range(5):
    subject = Subject(name=faker.word(), teacher=random.choice(teachers))
    session.add(subject)
    subjects.append(subject)

# Generate random students and their grades
for _ in range(30):
    student = Student(fullname=faker.name(), group=random.choice(groups))
    session.add(student)

    for subject in subjects:
        for _ in range(10):  # Multiple grades for each subject
            grade = Grade(student=student, subject=subject, grade=random.uniform(60, 100), date_received=datetime.now())
            session.add(grade)

session.commit()
session.close()
