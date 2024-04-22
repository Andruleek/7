from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random

# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Створюємо базовий клас моделі
Base = declarative_base()

# Клас моделі для студентів
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")

# Клас моделі для груп
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")

# Клас моделі для предметів
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Клас моделі для викладачів
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Клас моделі для оцінок
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)

# З'єднуємося з базою даних SQLite
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()

# Додаємо групи
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)

# Додаємо предмети
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
for subject_name in subjects:
    subject = Subject(name=subject_name)
    session.add(subject)

# Додаємо викладачів
for _ in range(5):
    teacher = Teacher(name=fake.name())
    session.add(teacher)

# Додаємо студентів
for _ in range(30):
    name = fake.name()
    group_id = random.randint(1, len(groups))
    student = Student(name=name, group_id=group_id)
    session.add(student)

# Додаємо оцінки
students = session.query(Student).all()
subjects = session.query(Subject).all()

for student in students:
    for subject in subjects:
        grade = random.randint(60, 100)
        grade_entry = Grade(student_id=student.id, subject_id=subject.id, grade=grade)
        session.add(grade_entry)

# Зберігаємо зміни у базі даних
session.commit()

# Закриваємо сесію
session.close()
