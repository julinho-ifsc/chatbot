import re
from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd

class Vernissage(BotPlugin):
    """
    Conversa com a Julinha Marvi-E.
    """

#Streaming

    def callback_stream(self, stream):
        self.send(stream.identifier, "Arquivo para :" + str(stream.identifier))
        stream.accept()
        self.send(stream.identifier, "Conteúdo:" + str(stream.fsource.read()))


#Julinha
    @botcmd
    def sentido(self, msg, args):
        """
        Chama a Julinha.
        """
        yield("Julinha às suas ordens, capitão!")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/sentido.png', 'rb'),
                                          name='sentido.png',
                                          stream_type = 'photo')

    @re_botcmd(pattern=r"(o que vamos fazer a noite?)")
    def online(self, msg, args):
        """
        Acorda a Julinha.
        """
        yield("A mesma coisa que fazemos todas as noites, Pinky!")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/cérebro.jpg', 'rb'),
                                          name='cérebro.jpg',
                                          stream_type = 'photo')

    @re_botcmd(pattern=r"(cadê o Julinho?|cadê o julinho?)")
    def online(self, msg, args):
        """
        Pergunta do seu irmão.
        """
        yield("Deve estar fazendo bip bip por aí... 🙄")
        yield("Mas você já procurou na portaria?")

    @re_botcmd(pattern=r"me leve ao auditório")
    def auditorio(self, msg, args):
        """
        Pede à Julinha uma música.
        """
        yield("Desculpe, este código não está disponível para o momento de convivência. Mas se quiser ouvir a trilha de futuras caminhadas...")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Trilha.mp3', 'rb'),
                                          name='Trilha.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"cante uma música")
    def evidencias(self, msg, args):
        """
        Música em texto.
        """
        yield("E nessa loucura 🎤🎶\nDe dizer que não te quero! 🎤🎶\nVou negando as aparências!🎤🎶\nDisfarçando as evidências! 🎤🎶\nMas pra que viver fingindo? 🎤🎶\nSe eu não posso enganar meu coração...🎤🎶\nEu sei que te amo!🎤🎶")
        yield("Agora é com você!")

    @re_botcmd(pattern=r"toque uma música")
    def musica(self, msg, args):
        """
        Pede à Julinha uma música.
        """
        yield("Aí vai uma do meu extenso repertório. Espero que goste...  Se divirta para descobrir mais!!")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música5.mp3', 'rb'),
                                          name='Música5.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"aqueça meu coração")
    def coracao(self, msg, args):
        """
        Pede à Julinha uma música para aquecer seu coração em dias sofridos.
        """
        yield("Só uma palhinha, espero que goste...")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música2.mp3', 'rb'),
                                          name='Música2.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"pode me dar dinheiro?")
    def money(self, msg, args):
        """
        Pede à Julinha dinheiro.
        """
        yield("Desculpe, não tenho... Mas isso me lembra uma tristeza")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música3.mp3', 'rb'),
                                          name='Música3.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"você sabe falar inglês?")
    def ingles(self, msg, args):
        """
        Pergunta à Julinha sobre seu inglês.
        """
        yield("Sei...")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música4.mp3', 'rb'),
                                          name='Música4.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"e nessa loucura?")
    def evidencias(self, msg, args):
        """
        Pergunta à Julinha sobre a loucura.
        """
        yield("Olha....")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música7.mp3', 'rb'),
                                          name='Música7.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"você é fogo")
    def fogo(self, msg, args):
        """
        JUlinha não é uma menina fácil...
        """
        yield("Bom, se sou fogo...")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música8.mp3', 'rb'),
                                          name='Música8.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"você sabe esperar?")
    def lgbt(self, msg, args):
        """
        Pergunta à Julinha sobre espera.
        """
        yield("Prefiro cantarolar...")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música1.mp3', 'rb'),
                                          name='Música1.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"(eu te traí|eu te trai)")
    def infiel(self, msg, args):
        """
        Nada a declarar.
        """
        yield("Tudo bem...")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música9.mp3', 'rb'),
                                          name='Música9.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"você já chegou?")
    def anitta(self, msg, args):
        """
        Nada a declarar 2.0
        """
        yield("ÓBVIOOO")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Música6.mp3', 'rb'),
                                          name='Música6.mp3',
                                          stream_type = 'audio')


    @re_botcmd(pattern=r"você gosta de artes?")
    def artes(self, msg, args):
        """
        Pergunta à Julinha sobre artes.
        """
        yield("Gosto muito!! Meu folclorista predileto é Franklin Cascaes!")

    @re_botcmd(pattern=r"(me mostre Cascaes|me mostre cascaes)")
    def cascaes(self, msg, args):
        """
        Pergunta à Julinha sobre Frankilin Cascaes.
        """
        yield("Além de gravurista, Frankilin Cascaes também era escritor.")
        yield("“Este boitatá está passeando sobre a Ilha de Santa Catarina. É meia-noite. Ele está apreciando, de riba, as 60 praias que ela possui, brancas quiném jasmim”")
        yield("O Boitatá/1960. Nanquim sobre papel")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/boitatá.jpg', 'rb'),
                                          name='boitatá.jpg',
                                          stream_type = 'photo')
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Boitatá.mp3', 'rb'),
                                          name='Boitatá.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"(me mostre côsas de floripa|me mostre côsas de Floripa)")
    def floripa(self, msg, args):
        """
        Pergunta à Julinha sobre côsas de Floripa.
        """
        yield("“A procissão do Senhor dos Passos, o terno de reis, a velha rendeira, a pesca da tainha, o surfe e as favelas de Florianópolis ganharam os traços de Souza. As brincadeiras de roda, as pandorgas e as bruxas da Ilha também estão presentes na exposição “Côsas de Floripa”. O artista Hamilton José de Souza tem 63 anos, é natural de São José e morador de Florianópolis.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/cosa1.jpg', 'rb'),
                                          name='cosa1.jpg',
                                          stream_type = 'photo')
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/cosa2.jpg', 'rb'),
                                          name='cosa2.jpg',
                                          stream_type = 'photo')
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/Cosas.mp3', 'rb'),
                                          name='Cosas.mp3',
                                          stream_type = 'audio')

    @re_botcmd(pattern=r"me mostre Willy Zumblick")
    def willy(self, msg, args):
        """
        Pergunta à Julinha sobre Willy Zumblick.
        """
        yield("“Willy Alfredo Zumblick nasceu em Tubarão em 26 de setembro de 1913 e faleceu em 2008.. Autodidata, suas obras abordaram, em sua maioria, os aspectos históricos e sociais da gente de sua região.“")
        yield("“Curiosidade: existe o Museu Willy Zumblick,foi inaugurado em setembro de 2001, mesmo ano em que o artista deixou os pincéis e espátulas, por recomendações médicas, aos 87 anos, devido à toxicidade das tintas que lhe afetava a saúde. A pujança proporcionou 75 anos de dedicação à arte e um verdadeiro legado histórico para os brasileiros.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/willy.jpg', 'rb'),
                                          name='willy.jpg',
                                          stream_type = 'photo')
        yield("Desculpe, esta obra não possui arquivos de áudio. Em todos esses anos nessa indústria vital, é a primeira vez que isso me acontece..")

    @re_botcmd(pattern=r"me fale um pouco sobre Valda Costa")
    def valda(self, msg, args):
        """
        Pergunta à Julinha sobre Valda Costa.
        """
        yield("“Vivalda Terezinha da Costa, nascida em 20 de maio de 1951, em Florianópolis, onde viveu inicialmente no bairro Estreito, e posteriormente Morro do Mocotó. Trabalhou como atendente de enfermagem no Hospital de Caridade antes de ser aprendiz de Martinho de Haro em seu ingresso ao mundo das artes.“")
        yield("“Negra e moradora de uma comunidade de baixa renda, Valda Costa conseguiu inserir-se nos ambientes culturais locais da época e chegou fazer exposições em Chapecó, Joinville, Curitiba e Porto Alegre. Foi até comparada com Di Cavalcanti, importante pintor modernista brasileiro. Seus quadros retratavam geralmente imagens e pessoas ligadas ao cotidiano da autora e da Ilha de Santa Catarina, com forte presença de figuras humanas.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/valda.jpeg', 'rb'),
                                          name='valda.jpeg',
                                          stream_type = 'photo')
        yield("Desculpe, esta obra não possui arquivos de áudio. Em todos esses anos nessa indústria vital, é a primeira vez que isso me acontece..")

    @re_botcmd(pattern=r"pintora Sônia Furtado")
    def sonia(self, msg, args):
        """
        Pergunta à Julinha sobre Sônia Furtado.
        """
        yield("“Sônia Furtado (Tubarão, 1950), formou-se em educação física e exerceu o magistério por dez anos. Mudando-se em 1979 para Curitiba, ali pintou seu primeiro quadro. Em 1980 transferiu-se para Brasília, onde passou a se dedicar profissionalmente à arte.“")
        yield("“Desde 1981 participa de salões e mostras, tendo conquistado diversas premiações. Sua obra enfoca principalmente o campo, os trabalhadores rurais e as festas populares.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/sonia.jpg', 'rb'),
                                          name='sonia.jpg',
                                          stream_type = 'photo')
        yield("Desculpe, esta obra não possui arquivos de áudio. Em todos esses anos nessa indústria vital, é a primeira vez que isso me acontece..")

    @re_botcmd(pattern=r"me fale sobre Tercília dos Santos")
    def tercilia(self, msg, args):
        """
        Pergunta à Julinha sobre Tercília dos Santos.
        """
        yield("“Tercília dos Santos começou a pintar somente em 1990, logo expondo seus trabalhos. Sua pintura remete à infância, com grande riqueza de cores. Em 1996 conquistou o Prêmio Aquisição na Bienal Brasileira de Arte Naïf de Piracicaba.“")
        yield("“Artista plástica apontada pela crítica como a grande revelação da pintura Naif de Santa Catarina. Seus quadros através de figuras totalmente coloridas, em acrílico sobre tela, registram o colorido rural do Estado.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/tercila.jpg', 'rb'),
                                          name='tercila.jpg',
                                          stream_type = 'photo')
        yield("Desculpe, esta obra não possui arquivos de áudio. Em todos esses anos nessa indústria vital, é a primeira vez que isso me acontece..")

    @re_botcmd(pattern=r"me fale sobre o artista catarinense Juarez Machado")
    def juarez(self, msg, args):
        """
        Pergunta à Julinha sobre Juarez Machado.
        """
        yield("“Juarez Machado (Joinville, 16 de março de 1941). Além de dedicar-se à pintura, é também escultor, desenhista, caricaturista, mímico, designer, cenógrafo, escritor, fotógrafo e ator. Em 1964 realizou sua 1ª mostra individual na Galeria Cocaco, de Curitiba, iniciando uma carreira de grande sucesso. Foi chargista dos principais jornais brasileiros e mímico no programa Fantástico, da TV Globo.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/juarez.jpg', 'rb'),
                                          name='juarez.jpg',
                                          stream_type = 'photo')
        yield("Desculpe, esta obra não possui arquivos de áudio. Em todos esses anos nessa indústria vital, é a primeira vez que isso me acontece..")

    @re_botcmd(pattern=r"quem é Victor Meirelles?")
    def victor(self, msg, args):
        """
        Pergunta à Julinha sobre Victor Meirelles.
        """
        yield("“Victor Meirelles nascido em 1832, em Florianópolis, Meirelles estudou as obras dos artistas da Escola Veneziana, Ticiano (1488-1576) e Veronese (1528-1588). Consagrado como pintor histórico, seu quadro mais reproduzido nos livros escolares é A Primeira Missa no Brasil, feito durante sua estadia na França e exposto no Salão de Paris de 1861.“")
        yield("“Retrata a primeira missa da maneira como foi descrita na carta de Pero Vaz de Caminha, e muitos intelectuais do século 19 o consideraram como a primeira grande obra de arte brasileira.“")
        stream = self.send_stream_request(msg.frm, open('/errbot/data/plugins/boidacarapreta/marvie-bot/meirelles.jpg', 'rb'),
                                          name='meirelles.jpg',
                                          stream_type = 'photo')
        yield("Desculpe, esta obra não possui arquivos de áudio. Em todos esses anos nessa indústria vital, é a primeira vez que isso me acontece..")

        
    @re_botcmd(pattern=r"receita minicupcake de chocolate")
    def victor(self, msg, args):
        """
        Pergunta à Julinha sobre minicupcake de chocolate.
        """
        yield("4 ovos\n1 xícara de leite\n¼ de xícara de óleo\n½ xícara de chocolate em pó\n1 xícara de nescau\n2 xícaras de açúcar\n3 xícaras de trigo\n1 colher de fermento de bolo\nColocar no liquidificador os ingrediente molhados (leite, ovo, óleo)\nAcrescentar os achocolatados e o açúcar, bater bem, parar, colocar uma\nxícara de trigo, bater só pra misturar, repetir até terminar o trigo, parar de\nbater, acrescentar o fermento, colocar em uma forma untada e levar ao\nforno por em média 40min. Em forno 180°.")
        
    @re_botcmd(pattern=r"receita de minicupcake de cenoura")
    def victor(self, msg, args):
        """
        Pergunta à Julinha sobre minicupcake de cenoura.
        """
        yield("1 cenoura em média picada\n4 ovos\n¾ de xícara de óleo\n3 xícaras de açúcar\n3 xícaras de trigo\n1 colher de fermento\nColocar no liqüidificador a cenoura, o açúcar, os ovos e o óleo, bater bem\naté a cenoura ficar invisível, misturar uma a uma as xícaras de trigo, parar\nde bater, misturar o fermento, colocar em uma forma untada, levar ao\nforno preaquecido em média 40min\nPra fazer bolo de laranja é só substituir a cenoura por uma laranja sem\ncaroço, sem o miolo e sem a metade da casca.\nPara fazer de milho é só substituir a cenoura por uma lata de milho verde\nsem água.\nCobertura\n1 lata de leite condensado\n1 caixinha de creme de leite\n3 colheres de leite")
