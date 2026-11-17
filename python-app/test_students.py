import psycopg2
import pytest

from students import add_student, get_student, average_grade


@pytest.fixture
def conn():
    """Connexion a la base tp, table videe avant chaque test."""
    connection = psycopg2.connect(
        host="localhost", dbname="tp", user="postgres", password="postgres"
    )
    with connection.cursor() as cur:
        cur.execute("TRUNCATE students RESTART IDENTITY")
    connection.commit()
    yield connection
    connection.close()


def test_ajout_et_lecture(conn):
    student_id = add_student(conn, "Amel", 15)
    name, grade = get_student(conn, student_id)
    assert name == "Amel"
    assert float(grade) == 15.0


def test_lecture_inexistant(conn):
    assert get_student(conn, 9999) is None


def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)
    assert average_grade(conn) == 12.0
