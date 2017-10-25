import os, datetime, requests, jwt

class RouteClients():
    def __init__(self, base_url, client_id):
        self.base_url = base_url
        self.params = self.get_params(client_id)
        self.headers = self.get_headers()

    def get_routes(self):
        response = requests.get(
            self.base_url + '/routes',
            headers=self.headers,
            params=self.params
        )
        return response.json()

    def status(self, message):
        response = requests.post(
            self.base_url + '/status',
            json=message,
            headers=self.headers,
            params=self.params
        )
        return response.json()

    def walk(self, message):
        response = requests.post(
            self.base_url + '/walk',
            json=message,
            headers=self.headers,
            params=self.params
        )
        return response.json()

    def get_params(self, client_id):
        return {'client_id': client_id}

    def get_headers(self):
        token = self.get_token()
        return {'Authorization': 'Bearer ' + token.decode('utf-8')}

    def get_token(self):
        key = self.get_key()
        expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)
        body = {'exp': expiration}
        return jwt.encode(body, key, algorithm='RS256')
        
    def get_key(self):
        path = os.getenv('KEY_PATH', '/home/ubuntu/workspace/julinha/private.key')
        key_file = open(path, 'r')
        return key_file.read()
        