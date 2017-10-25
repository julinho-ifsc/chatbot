import re, json, os
from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd, ONLINE, AWAY
from client import RouteClients

route_clients = RouteClients(
    base_url='http://nuvem.sj.ifsc.edu.br:18080',
    client_id=2
)

class Comandos(BotPlugin):
    """
    Comandos da Julinha Marvi·e.
    """

    @botcmd
    def teste(self, msg, args):
        yield(route_clients.get_routes())

    
    @botcmd
    def rumo(self, _, args):
        destino = [
            'banheiro fem subsolo',
            'banheiro masc subsolo',
            'banheiro fem 1',
            'banheiro masc 1',
            'banheiro fem biblioteca',
            'banheiro masc biblioteca',
            'banheiro fem armário',
            'banheiro masc armário',
            'sala 01',
            'sala 02',
            'sala 03',
            'sala 04',
            'sala 05',
            'sala 07',
            'sala 08',
            'sala 09',
            'sala 10',
            'sala 11',
            'sala 12',
            'sala 13',
            'sala 14',
            'sala 15', 
            'sala de cultura',
            'orientação de turno',
            'lab de alunos',
            'lab interativo',
            'miniauditório',
            'almoxarifado geral',
            'sala dos professores',
            'coordenadoria pedagógica',
            'sala multimeios de rac',
            'sala multimeios de cultura geral',
            'sala dos professores de tele 3',
            'reprografia', 'cozinha e refeitório',
            'coordenadoria de extensão',
            'representação estudantil',
            'atendimento paralelo',
            'monitoria',
            'auditório',
            'armários',
            'lab de testes em refrigeração',
            'lab de eficiência energética',
            'almoxarifado de rac',
            'lab de ciências térmicas',
            'lab de ar condicionado',
            'lab de refrigeração',
            'lab de solda',
            'biblioteca',
            'sala dos professores de tele 1',
            'sala dos professores de tele 2',
            'lab de informática 1',
            'lab de cad 1',
            'gerac',
            'lab de cad 3',
            'lab de educação a distância',
            'lab de biologia',
            'lab química',
            'lab de física',
            'lab meios de transmissão',
            'almoxarifado de tele',
            'lab de programação',
            'lab de comunicação e expressão',
            'lab de redes de computadores 2',
            'lab de redes de computadores 1',
            'lab de sistemas de voz e imagem',
            'lab de apoio ao ensino de tele',
            'lab de eletrônica aplicada',
            'lab de manutenção de computadores',
            'centro de convivência',
            'academia',
            'secretaria',
            'coordenadoria de registros',
            'coordenadoria de estágio',
            'coordenadoria de tele',
            'coordenadoria de rac',
            'coordenadoria de cultura geral',
            'direção',
            'ambulatório',
            'departamento de administração',
            'coordenadoria de finanças',
            'coordenadoria de gestão de pessoas',
            'laboratório de iniciação científica'
            ]

        """
        Envia a Julinha para a rota inserida. Utilize como "Julinha rumo ___________".
        """
        mensagem = {}
        mensagem['rota'] = args
        print(json.dumps(mensagem))
        if(args in destino):
            yield("Siga-me até " + args + ". Obrigada.:relaxed:")
        else:
            yield("Desculpe, esta rota não está disponível ou não existe.:white_frowning_face:")


    
#funções


    @botcmd
    def buzinar(self, msg, args):
        """
        Aciona a buzina do Arduino.
        """
        yield("Bip bip!:mega:")

    @botcmd
    def desligar(self, msg, args):
        """
        Desliga a Julinha.
        """
        yield("Foi um prazer trabalhar hoje! Beijo, me liga!:kissing_heart:")
        self.change_presence(AWAY)

    @botcmd
    def direita(self, msg, args):
        """
        Manda a Julinha virar à direita.
        """
        yield("Virando à direita!")

    @botcmd
    def esquerda(self, msg, args):
        """
        Manda a Julinha virar à esquerda.
        """
        yield("Virando à esquerda!")
    
    @botcmd
    def frente(self, msg, args):
        """
        Manda a Julinha ir à frente.
        """
        yield("Para frente e avante!")

    @botcmd
    def ligar(self, msg, args):
        """
        Liga a Julinha.
        """
        yield("Julinha às suas ordens, capitão!")
        self.change_presence(ONLINE)
      
    @botcmd
    def sirene(self, msg, args):
        """
        Aciona a sirene do Arduino.
        """
        yield("Uiuuu uiuuu!:rotating_light:")

    @botcmd
    def tras(self, msg, args):
        """
        Manda a Julinha para trás.
        """
        yield("Dando ré!")


    @re_botcmd(pattern=r"andar [0-9]+")
    def andar(self, msg, match):
        """
        Manda a Julinha andar x.
        """
        mensagem = {}
        mensagem['comando'] = "andar"
        quantidade = match.group().split(' ')[1]
        if quantidade:
            mensagem['valor'] = quantidade
            yield(mensagem)

#ROTA

   