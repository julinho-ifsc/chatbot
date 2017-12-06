import re, json, os, datetime, requests, jwt
from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd, ONLINE, AWAY

class RouteClients():
    def __init__(self, base_url, client_id):
        self.base_url = base_url
        self.params = self.get_params(client_id)
        self.key = self.get_key()

    def get_routes(self):
        response = requests.get(
            self.base_url + '/routes',
            headers=self.get_headers(),
            params=self.params
        )
        return response.json()

    def status(self, message):
        response = requests.post(
            self.base_url + '/status',
            json=message,
            headers=self.get_headers(),
            params=self.params
        )
        return response.json()

    def walk(self, message):
        response = requests.post(
            self.base_url + '/walk',
            json=message,
            headers=self.get_headers(),
            params=self.params
        )
        return response.json()

    def get_params(self, client_id):
        return {'client_id': client_id}

    def get_headers(self):
        token = self.get_token()
        return {'Authorization': 'Bearer ' + token.decode('utf-8')}

    def get_token(self):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)
        body = {'exp': expiration}
        return jwt.encode(body, self.key, algorithm='RS256')

    def get_key(self):
        path = os.getenv('KEY_PATH', '/errbot/private.key')
        key_file = open(path, 'r')
        return key_file.read()

route_clients = RouteClients(
    base_url='http://nuvem.sj.ifsc.edu.br:18080',
    client_id=2
)

class Comandos(BotPlugin):
    """
    Comandos do Julinho Marvi.E.
    """

    @botcmd
    def teste(self, msg, args):
        yield(route_clients.get_routes())

    @botcmd
    def rumo(self, _, args):
        """
        Envia o Julinho para a rota inserida. Utilize como "Julinho, rumo ___________".
        """
        if args:
            mensagem = {}
            mensagem['route'] = args
            rota = route_clients.walk(mensagem)
            if rota['message'] == 'Route sent with success!':
                yield("Siga-me até " + args + ". Valeu!")
            else:
                yield("Desculpe, esta rota não está disponível ou não existe.")
        else:
            yield("Sem rumo? Quer ir a lugar nenhum? Gaiman, vem cá me ajudar!")

    @botcmd
    def buzinar(self, msg, args):
        """
        Aciona a buzina do Arduino.
        """
        yield("Bip bip!")

    @botcmd
    def desligar(self, msg, args):
        """
        Desliga o Julinho.
        """
        yield("Adeus, mundo cruel!")
        self.change_presence(AWAY)

    @botcmd
    def direita(self, msg, args):
        """
        Manda o Julinho virar a direita.
        """
        yield("Virando a estibordo!")

    @botcmd
    def esquerda(self, msg, args):
        """
        Manda o Julinho virar a esquerda.
        """
        yield("Virando a bombordo!")

    @botcmd
    def frente(self, msg, args):
        """
        Manda o Julinho ir a frente.
        """
        yield("Para frente e avante!")

    @botcmd
    def acordar(self, msg, args):
        """
        Acorda o Julinho.
        """
        yield("Sim, senhor SENHOR!")
        self.change_presence(ONLINE)

    @botcmd
    def sirene(self, msg, args):
        """
        Aciona a sirene do Arduino.
        """
        yield("Uiuuu uiuuu!")

    @botcmd
    def tras(self, msg, args):
        """
        Manda o Julinho ir para trás.
        """
        yield("Dando ré!")
