from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Subject, Grade, Teacher, Group

engine = create_engine('postgresql://username:password@localhost/dbname')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    top_students = session.query(Student, func.avg(Grade.score).label('average_score')).\
        join(Grade).group_by(Student.id).order_by(func.avg(Grade.score).desc()).limit(5).all()
    return top_students

# Подібно select_2, select_3, і так далі для всіх ваших запитів

if __name__ == "__main__":
    result = select_1()
    print(result)
