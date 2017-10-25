import re
from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd


class BatePapo(BotPlugin):
    """
    Conversas no chat com a Julinha Marvi-e.
    """
 
    @botcmd
    def duvidei(self, msg, args):
        """
        Resposta Julinha à sua descrença.
        """
        yield("Duvidando? De mim? Que audácia!:rage:")

    @botcmd
    def like(self, msg, args):
        """
        Pede a Julinha um like.
        """
        yield(":thumbsup_all:")


    @re_botcmd(pattern=r"quero (uma|um) (bolacha|biscoito)?")
    def biscoito(self, msg, match):
        """
        Pede por um biscoito/bolacha para a Julinha.
        """
        yield("Seja educado, {}!").format(msg.frm)
    
    @re_botcmd(pattern=r"[cad(e|ê)|e] o (j|J)ulinho?")
    def julinho(self, msg, match):
        """
        Pergunta à Julinha sobre seu irmão.
        """
        yield("Está fazendo bip bip por aí...:robot_face:")
        yield("Mas você já procurou na portaria?")

    @re_botcmd(pattern=r"e nessa loucura?")
    def evidencia(self, msg, args):
        """
        As evidências de uma paixão.
        """
        yield("_De dizer que não te quero!_:microphone::notes:")
        yield("_Vou negando as aparências!_:microphone::notes:")
        yield("_Disfarçando as evidências!_:microphone::notes:")
        yield("_Mas pra que viver fingindo_:microphone::notes:")
        yield("_Se eu não posso enganar meu coração..._:microphone::notes:")
        yield("_Eu sei que te amo!_:microphone::notes:")
        yield("Agora é com você!")
        