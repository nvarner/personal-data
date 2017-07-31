# For some reason, "build" can't be found by PyCharm Community for me, but the program still runs fine, if you have that
# problem. If you know the solution, please help!
import datetime
from apiclient.discovery import build

from src import auth
from src import in_out


class FitData:
    def __init__(self, settings):
        # Define settings (normally settings.json)
        self.settings = settings

        # Variables for quick access to settings
        client_secrets_url = self.settings["client_secrets_url"]
        oauth_scope = self.settings["oauth_scope"]

        # Authentication variables
        client_secrets = in_out.load_json(client_secrets_url)["installed"]
        self.client_id = client_secrets["client_id"]
        self.client_secret = client_secrets["client_secret"]
        self.redirect_uri = client_secrets["redirect_uris"][0]

        self.http, self.cred = auth.first_auth(self.client_id, self.client_secret, oauth_scope, self.redirect_uri)

    def get_data(self, request=in_out.load_json("request.json"), write_file=False, out_url="../../steps.json"):
        self.http = auth.refresh_auth(self.cred)

        fitness_service = build('fitness', 'v1', http=self.http)
        data_set = in_out.make_request(fitness_service, request)
        steps_object = {}

        for bucket in data_set["bucket"]:
            start_time = datetime.datetime.fromtimestamp(int(bucket["startTimeMillis"]) / 1000.0)
            daily_steps = 0

            for dataset in bucket["dataset"]:
                if len(dataset["point"]) is not 0:
                    daily_steps += dataset["point"][0]["value"][0]["intVal"]

                steps_object[str(start_time)] = daily_steps

        if write_file:
            in_out.make_json(steps_object, out_url)
        return steps_object
