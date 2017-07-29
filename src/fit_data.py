# For some reason, "build" can't be found by PyCharm Community for me, but the program still runs fine, if you have that
# problem. If you know the solution, please help!
import datetime
from apiclient.discovery import build

from src import auth
from src import in_out

if __name__ == "__main__":
    settings = in_out.load_json("settings.json")
    client_secrets_url = settings["client_secrets_url"]
    oauth_scope = settings["oauth_scope"]

    client_secrets = in_out.load_json(client_secrets_url)["installed"]
    client_id = client_secrets["client_id"]
    client_secret = client_secrets["client_secret"]
    redirect_uri = client_secrets["redirect_uris"][0]

    http, cred = auth.first_auth(client_id, client_secret, oauth_scope, redirect_uri)

    http = auth.refresh_auth(cred)

    fitness_service = build('fitness', 'v1', http=http)

    data_set = in_out.make_request(fitness_service, in_out.load_json("request.json"))

    steps_object = {}

    for bucket in data_set["bucket"]:
        start_time = datetime.datetime.fromtimestamp(int(bucket["startTimeMillis"]) / 1000.0)
        daily_steps = 0

        for dataset in bucket["dataset"]:
            if len(dataset["point"]) is not 0:
                daily_steps += dataset["point"][0]["value"][0]["intVal"]

            steps_object[str(start_time)] = daily_steps

    in_out.make_json(steps_object, "../../steps.json")
