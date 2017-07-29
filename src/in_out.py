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


def write_file(url, contents):
    """Writes to a file at a URL. It can only write to files locally."""
    request_type = url.split(":")[0]

    if request_type == "http":
        raise ValueError("io.write_file can only write to local files, not files over http.")
    else:
        with open(url, 'w') as file:
            file.writelines(contents)


def make_json(obj, url, write_to_file=True):
    """Writes JSON to a file. See write_file for more info. Can also return JSON string."""
    json_string = json.dumps(obj)

    if write_to_file:
        write_file(url, json_string)
    else:
        return json_string


def make_request(fitness_service, request, user_id="me"):
    """Makes a request to the REST API with JSON"""
    return fitness_service.users().dataset().aggregate(userId=user_id, body=request).execute()