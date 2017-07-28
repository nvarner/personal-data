import httplib2

from oauth2client.client import OAuth2WebServerFlow


def first_auth(client_id, client_secret, oauth_scope, redirect_uri):
    """Authorises the app for the first time. Requires a Google sign-in."""
    flow = OAuth2WebServerFlow(client_id, client_secret, oauth_scope, redirect_uri=redirect_uri)
    authorize_url = flow.step1_get_authorize_url()
    print('Go to the following link in your browser:')
    print(authorize_url)
    code = input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)

    http = httplib2.Http()
    return credentials.authorize(http), credentials


def refresh_auth(credentials):
    """Re-authorises the app after the first time using the refresh token. Does not require Google sign-in."""
    return credentials.authorize(httplib2.Http())