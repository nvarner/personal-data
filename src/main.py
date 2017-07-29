import in_out
from db import DB
from db_user import DBUser

if __name__ == "__main__":
    login = in_out.load_json("../../login_data.json")

    personal_info = DB("localhost", "personal_data", DBUser(login["username"], login["password"]))
    personal_info.update("INSERT INTO health values ('2017/7/28', 4165);")

    # result = personal_info.query("SELECT * FROM `health` ORDER BY `steps` DESC")
