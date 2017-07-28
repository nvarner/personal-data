# For some reason, "build" can't be found by PyCharm Community for me, but the program still runs fine, if you have that
# problem. If you know the solution, please help!
from apiclient.discovery import build

from src import auth
from src import io

if __name__ == "__main__":
    settings = io.load_json("settings.json")
    client_secrets_url = settings["client_secrets_url"]
    oauth_scope = settings["oauth_scope"]

    client_secrets = io.load_json(client_secrets_url)["installed"]
    client_id = client_secrets["client_id"]
    client_secret = client_secrets["client_secret"]
    redirect_uri = client_secrets["redirect_uris"][0]

    http, cred = auth.first_auth(client_id, client_secret, oauth_scope, redirect_uri)

    http = auth.refresh_auth(cred)

    fitness_service = build('fitness', 'v1', http=http)

    data_set = auth.make_request(fitness_service, io.load_json("request.json"))

    steps_this_week = 0

    with open("../../steps.txt", "w") as f:
        for bucket in data_set["bucket"]:
            for point in bucket["dataset"]:
                if len(point["point"]) is not 0:
                    f.write(str(point["point"][0]["value"][0]["intVal"]) + "\n")
                    steps_this_week += point["point"][0]["value"][0]["intVal"]

    print(steps_this_week)
