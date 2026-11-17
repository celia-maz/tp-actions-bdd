def add_student(conn, name, grade):
    """Ajoute un etudiant et retourne son id."""
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s) RETURNING id",
            (name, grade),
        )
        new_id = cur.fetchone()[0]
    conn.commit()
    return new_id


def get_student(conn, student_id):
    """Retourne (name, grade) ou None si l'etudiant n'existe pas."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT name, grade FROM students WHERE id = %s", (student_id,)
        )
        return cur.fetchone()


def average_grade(conn):
    """Retourne la moyenne des notes. A ECRIRE (exercice 2)."""
    raise NotImplementedError
