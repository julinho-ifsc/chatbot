import re
from errbot import BotPlugin, botcmd, re_botcmd, ONLINE, AWAY


class ChatBot(BotPlugin):
    """
    Uma conversa franca com Julinho, o robô do Integrado.
    """

    @botcmd
    def descansar(self, msg, args):
        """
        Manda o Julinho descansar.
        """
        yield("Adeus, mundo cruel!")
        self.change_presence(AWAY, "Eu não estou aqui!")

    @botcmd
    def acordar(self, msg, args):
        """
        Manda o Julinho acordar.
        """
        yield("Sim, senhor SENHOR!")
        self.change_presence(ONLINE, "Às suas ordens!")

    @botcmd
    def buzinar(self, msg, args):
        """
        Aciona a buzina do Arduino.
        """
        yield("Bip bip!")

    @re_botcmd(pattern=r"(^| )andar [0-9]+( |$)")
    def andar(self, msg, match):
        """
        Aciona a buzina do Arduino.
        """
        mensagem = {}
        mensagem['comando'] = "andar"
        quantidade = match.group().split(' ')[1]
        if quantidade:
            mensagem['valor'] = quantidade
            yield(mensagem)
        else:
            yield("{}")
