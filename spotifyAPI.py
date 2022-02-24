import requests
import datetime
import os

# client_id = os.environ("d04be567989d427e8ca8b0b27faa9bdc")
# client_secret = os.environ("07721eeec6e1493f80a52f79335f1a12")

class spotifyAPI(object):
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'
    access_token_expires = datetime.datetime.now()
    access_token_did_expires = True
    

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        
    
    def get_client_credentials(self):
        import base64
        client_id = self.client_id
        client_secret = self.client_secret

        client_creds = f"{client_id}:{client_secret}"
        client_creds_64 = base64.b64encode(client_creds.encode())
        return client_creds_64.decode()


    def get_token_data(self):
        return {
                'grant_type' : 'client_credentials'
            }
    def get_token_headers(self):
        client_credentials = self.get_client_credentials()
        return {
                'Authorization' : f"Basic {client_credentials}"
            }
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data = token_data, headers = token_headers)

        valid_request = r.status_code in range(200, 299)
        if r.status_code not in range(200, 299):
            raise Exception(f"Could not authenticate client. Status code {r.status_code}")
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds = expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expires = expires < now

        return True, access_token


client = spotifyAPI(os.environ["client_id"], os.environ.get["client_secret"])
client.perform_auth()
