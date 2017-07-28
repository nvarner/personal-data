import json
import urllib.request

def load_file(url):
    """Loads a file from URL. It can retrieve files locally and over HTTP."""
    request_type = url.split(":")[0]

    if request_type == "http":
        response = urllib.request.urlopen(url)
        return response.read().decode()
    else:
        with open(url) as file:
            return file.read()


def load_json(url):
    """Loads JSON from a URL. See load_file for more info."""
    return json.loads(load_file(url))


def make_request(fitness_service, request, user_id="me"):
    """Makes a request to the REST API with JSON"""
    return fitness_service.users().dataset().aggregate(userId=user_id, body=request).execute()