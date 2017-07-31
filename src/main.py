from datetime import date, timedelta
import time

import in_out
from db import DB
from db_user import DBUser
from fit_data import FitData

if __name__ == "__main__":
    settings = in_out.load_json("settings.json")
    login = in_out.load_json(settings["login_url"])
    base_request = in_out.load_json(settings["base_request_url"])

    personal_info = DB("localhost", "personal_data", DBUser(login["username"], login["password"]))
    fit_data = FitData(settings)

    yesterday = date.today() - timedelta(days=1)

    start_request = int(time.mktime(time.strptime(yesterday.strftime("%Y-%m-%d") + " 00:00:00", '%Y-%m-%d %H:%M:%S'))) \
        * 1000
    end_request = int(time.mktime(time.strptime(yesterday.strftime("%Y-%m-%d") + " 23:59:59", '%Y-%m-%d %H:%M:%S'))) \
        * 1000

    request = base_request
    request["startTimeMillis"] = start_request
    request["endTimeMillis"] = end_request

    yesterday_steps = fit_data.get_data(request=request)[yesterday.strftime("%Y-%m-%d") + " 00:00:00"]
    print(yesterday_steps)
    personal_info.update(
        "INSERT INTO health values ('" + yesterday.strftime("%y/%m/%d") + "', " + str(yesterday_steps) + ");")

    # result = personal_info.query("SELECT * FROM `health` ORDER BY `steps` DESC")
