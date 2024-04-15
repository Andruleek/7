from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random

fake = Faker()

engine = create_engine('postgresql://username:password@localhost/dbname')  # Замініть на ваші дані
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Заповнення таблиці груп
groups = ['Group A', 'Group B', 'Group C']
for name in groups:
    group = Group(name=name)
    session.add(group)

# Заповнення таблиці викладачів
for _ in range(3):
    teacher = Teacher(fullname=fake.name())
    session.add(teacher)

# Заповнення таблиці студентів
for _ in range(30):
    student = Student(fullname=fake.name())
    session.add(student)

# Заповнення таблиць предметів та оцінок
for _ in range(5):
    subject_name = fake.word()
    teacher_id = random.randint(1, 3)
    subject = Subject(name=subject_name, teacher_id=teacher_id)
    session.add(subject)
    for student in session.query(Student).all():
        grade = Grade(student_id=student.id, subject_id=subject.id, value=random.uniform(4, 10))
        session.add(grade)

session.commit()
