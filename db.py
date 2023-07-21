import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS academic(
            id Integer Primary Key,
            name text,
            age text,
            dob text,
            email text,
            gender text,
            contact text,
            grade text,
            percentage text,
            branch text,
            course text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, grade, percentage, branch
, course):
        self.cur.execute("insert into academic values (NULL,?,?,?,?,?,?,?,?,?,?)",
                         (name, age, dob, email, gender, contact, grade, percentage, branch
, course))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from academic")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from academic where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, grade, percentage, branch
, course):
        self.cur.execute(
            "update academic set name=?, age=?, dob=?, email=?, gender=?, contact=?, grade=?, percentage=?, branch=?, course=? where id=?",
            (name, age, dob, email, gender, contact, grade, percentage, branch
, course, id))
        self.con.commit()
