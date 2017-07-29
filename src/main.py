from db import DB
from db_user import DBUser

if __name__ == "__main__":
    personal_info = DB("localhost", "personal_data", DBUser("sqluser", "sqluserpw"))
    personal_info.update("INSERT INTO health values ('2017/7/28', 4165);")
    result = personal_info.query("SELECT * FROM `health` ORDER BY `steps` DESC")

    print(result)
