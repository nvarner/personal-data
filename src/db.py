import pymysql


class DB:
    def __init__(self, host, db_name, user):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.code_word = self.user.get_code_word()

        self.connection = pymysql.connect(host=self.host,
                                          user=self.user.get_username(self.code_word),
                                          password=self.user.get_password(self.code_word),
                                          db=self.db_name,
                                          charset="utf8mb4",
                                          cursorclass=pymysql.cursors.DictCursor)

    def update(self, sql_statement):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_statement)

        self.connection.commit()

    def query(self, sql_statement):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
        return result
