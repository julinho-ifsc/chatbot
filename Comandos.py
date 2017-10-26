import re, json, os
from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd, ONLINE, AWAY
from client import RouteClients

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
        destino = [
            'ao banheiro fem subsolo',
            'ao banheiro masc subsolo',
            'ao banheiro fem 1',
            'ao banheiro masc 1',
            'ao banheiro fem biblioteca',
            'ao banheiro masc biblioteca',
            'ao banheiro fem armário', 'ao banheiro fem armario',
            'ao banheiro masc armário', 'ao banheiro masc armario',
            'à sala 01', 'a sala 01',
            'à sala 02', 'a sala 02',
            'à sala 03', 'a sala 03',
            'à sala 04', 'a sala 04',
            'à sala 05', 'a sala 05',
            'à sala 07', 'a sala 07',
            'à sala 08', 'a sala 08',
            'à sala 09', 'a sala 09',
            'à sala 10', 'a sala 10',
            'à sala 11', 'a sala 11',
            'à sala 12', 'a sala 12',
            'à sala 13', 'a sala 13',
            'à sala 14', 'a sala 14',
            'à sala 15', 'a sala 15',
            'à sala de cultura','a sala de cultura',
            'à orientação de turno', 'a orientaçao de turno',
            'ao lab de alunos',
            'ao lab interativo',
            'ao miniauditório', 'ao miniauditorio',
            'ao almoxarifado geral',
            'à sala dos professores', 'a sala de professores ',
            'à coordenadoria pedagógica', 'a coordenadoria pedagogica',
            'à multimeios de rac', 'a multimeios de rac',
            'à multimeios de cultura geral', 'a multimeios de cultura geral',
            'à sala dos professores de tele 3', 'a sala dos professores de tele 3',
            'à reprografia', 'a reprografia',
            'à cozinha e refeitório', 'a cozinha e refeitorio',
            'à coordenadoria de extensão', 'a coordenadoria de extensao',
            'à representação estudantil', 'a representaçao estudantil,
            'ao atendimento paralelo',
            'à monitoria', 'a monitoria',
            'ao auditório', 'ao auditorio',
            'aos armários', 'aos armarios,
            'ao lab de testes em refrigeração', 'ao lab de testes em refrigeraçao',
            'ao lab de eficiência energética', 'ao lab de eficiencia energetica',
            'ao almoxarifado de rac',
            'ao lab de ciências térmicas', 'ao lab de ciencias termicas',
            'ao lab de ar condicionado',
            'ao lab de refrigeração', 'ao lab de refrigeraçao', 'ao lab de refrigeracao',
            'ao lab de solda',
            'à biblioteca', 'a biblioteca',
            'à sala dos professores de tele 1', 'a sala dos professores de tele 1',
            'à sala dos professores de tele 2', 'a sala dos professores de tele 2',
            'ao lab de informática 1', 'ao lab de informatica 1',
            'à lab de cad 1', 'a lab de cad 1',
            'à gerac', 'a gerac',
            'ao lab de cad 3',
            'ao lab de educação à distância', 'ao lab de educaçao a distancia',
            'ao lab de biologia',
            'ao lab química', 'ao lab quimica',
            'ao lab de física', 'ao lab de fisica',
            'ao lab meios de transmissão', 'ao lab meios de transmissao',
            'ao almoxarifado de tele',
            'ao lab de programação', 'ao lab de programaçao',
            'ao lab de comunicação e expressão', 'ao lab de comunicaçao e expressao',
            'ao lab de redes de computadores 2',
            'ao lab de redes de computadores 1',
            'ao lab de sistemas de voz e imagem',
            'ao lab de apoio ao ensino de tele',
            'ao lab de eletrônica aplicada', 'ao lab de eletronica aplicada',
            'ao lab de manutenção de computadores', 'ao lab de manutençao de computadores',
            'ao centro de convivência', 'ao centro de convivencia',
            'à academia', 'a academia',
            'à secretaria', 'a secretaria',
            'à coordenadoria de registros', 'a coordenadoria de registros',
            'à coordenadoria de estágio', 'a coordenadoria de estagio',
            'à coordenadoria de tele', 'a coordenadoria de tele',
            'à coordenadoria de rac', 'a coordenadoria de rac',
            'à coordenadoria de cultura geral', 'a coordenadoria de cultura geral',
            'à direção', 'a direçao',
            'ao ambulatório', 'ao ambulatorio',
            'ao departamento de administração', 'ao departamento de administraçao',
            'à coordenadoria de finanças', 'a coordenadoria de finanças',
            'à coordenadoria de gestão de pessoas', 'a coordenadoria de gestao de pessoas',
            'ao lab de iniciação científica', 'ao lab de iniciaçao cientifica',
            ]

        """
        Envia o Julinho para a rota inserida. Utilize como "Julinho, rumo ___________".
        """
        mensagem = {}
        mensagem['rota'] = args
        print(json.dumps(mensagem))
        if(args in destino):
            yield("Siga-me " + args + ". Obrigado!:sunglasses:")
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
        Desliga o Julinho.
        """
        yield("Adeus, mundo cruel!:skull:")
        self.change_presence(AWAY)

    @botcmd
    def direita(self, msg, args):
        """
        Manda o Julinho virar à direita.
        """
        yield("Virando à estibordo!:arrow_right:")

    @botcmd
    def esquerda(self, msg, args):
        """
        Manda o Julinho virar à esquerda.
        """
        yield("Virando à bombordo!:arrow_left:")
    
    @botcmd
    def frente(self, msg, args):
        """
        Manda o Julinho ir à frente.
        """
        yield("Para frente e avante!:arrow_up:")

    @botcmd
    def ligar(self, msg, args):
        """
        Liga o Julinho.
        """
        yield("Sim, senhor SENHOR!")
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
        Manda o Julinho ir para trás.
        """
        yield("Dando ré!:arrow_down:")


    @re_botcmd(pattern=r"andar [0-9]+")
    def andar(self, msg, match):
        """
        Manda o Julinho andar X.
        """
        mensagem = {}
        mensagem['comando'] = "andar"
        quantidade = match.group().split(' ')[1]
        if quantidade:
            mensagem['valor'] = quantidade
            yield(mensagem)
   
