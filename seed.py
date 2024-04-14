from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import random

fake = Faker()

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="grades")
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship("Subject", back_populates="grades")
    score = Column(Float)

Group.students = relationship("Student", back_populates="group")
Teacher.subjects = relationship("Subject", back_populates="teacher")
Student.grades = relationship("Grade", back_populates="student")
Subject.grades = relationship("Grade", back_populates="subject")

engine = create_engine('postgresql://username:password@localhost/dbname')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add groups
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

# Add teachers
teachers = [Teacher(name=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# Add students
students = []
for _ in range(30):
    student = Student(name=fake.name(), group=random.choice(groups))
    students.append(student)
session.add_all(students)
session.commit()

# Add subjects
subjects = []
for _ in range(5):
    subject = Subject(name=fake.word(), teacher=random.choice(teachers))
    subjects.append(subject)
session.add_all(subjects)
session.commit()

# Add grades
for student in students:
    for subject in subjects:
        score = round(random.uniform(60, 100), 2)
        grade = Grade(student=student, subject=subject, score=score)
        session.add(grade)
session.commit()
