import re
from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd


class BatePapo(BotPlugin):
    """
    Conversas no chat com o Julinho Marvi.E.
    """
 
    @botcmd
    def duvidei(self, msg, args):
        """
        Resposta do Julinho à sua descrença.
        """
        yield("Duvidando? De mim? Que audácia!")

    @botcmd
    def like(self, msg, args):
        """
        Pede ao Julinho um like.
        """
        yield(":thumbsup_all:")

  @re_botcmd(pattern=r"posso ganhar (uma|um) (bolacha|biscoito), por favor?")
    def biscoito(self, msg, match):
        """
        Pede por um biscoito/bolacha para o Julinho.
        """
        yield("Tome aqui, {}!").format(msg.frm)
        yield(":cookie:")
    
    @re_botcmd(pattern=r"[cad(e|ê)|e] a (j|J)ulinha?")
    def julinha(self, msg, match):
        """
        Pergunta ao Julinho sobre sua irmã.
        """
        yield("Está fazendo uiuu uiuu por aí...:robot_face:")
        yield("Mas você já procurou na biblioteca?")

    @re_botcmd(pattern=r"e nessa loucura?")
    def evidencias(self, msg, args):
        """
        As evidências de uma paixão.
        """
        yield("_De dizer que não te quero!_:microphone::notes:")
        yield("_Vou negando as aparências!_:microphone::notes:")
        yield("_Disfarçando as evidências!_:microphone::notes:")
        yield("_Mas pra que viver fingindo_:microphone::notes:")
        yield("_Se eu não posso enganar meu coração..._:microphone::notes:")
        yield("_Eu sei que te amo!_:microphone::notes:")
        yield("Agora é com você, {}!").format(msg.frm)
        
        
