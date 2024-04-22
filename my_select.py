from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher, Group, Session

# Сесія
session = Session()

# Знайти 5 студентів з найбільшим середнім балом з усіх предметів
def select_1():
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Grade) \
                  .group_by(Student.id) \
                  .order_by(desc('avg_grade')) \
                  .limit(5) \
                  .all()

# Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Grade) \
                  .join(Subject) \
                  .filter(Subject.name == subject_name) \
                  .group_by(Student.id) \
                  .order_by(desc('avg_grade')) \
                  .first()

# Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Student) \
                  .join(Grade) \
                  .join(Subject) \
                  .filter(Subject.name == subject_name) \
                  .group_by(Group.id) \
                  .all()

# Знайти середній бал на потоці
def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()

# Знайти які курси читає певний викладач
def select_5(teacher_name):
    return session.query(Subject.name) \
                  .join(Teacher) \
                  .filter(Teacher.name == teacher_name) \
                  .all()

# Знайти список студентів у певній групі
def select_6(group_name):
    return session.query(Student.fullname) \
                  .join(Group) \
                  .filter(Group.name == group_name) \
                  .all()

# Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    return session.query(Student.fullname, Grade.grade) \
                  .join(Group) \
                  .join(Subject) \
                  .filter(Group.name == group_name) \
                  .filter(Subject.name == subject_name) \
                  .all()

# Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Subject) \
                  .join(Teacher) \
                  .filter(Teacher.name == teacher_name) \
                  .scalar()

# Знайти список курсів, які відвідує певний студент
def select_9(student_name):
    return session.query(Subject.name) \
                  .join(Grade) \
                  .join(Student) \
                  .filter(Student.fullname == student_name) \
                  .all()

# Список курсів, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    return session.query(Subject.name) \
                  .join(Grade) \
                  .join(Student) \
                  .join(Teacher) \
                  .filter(Student.fullname == student_name) \
                  .filter(Teacher.name == teacher_name) \
                  .all()
