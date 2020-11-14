# Um bot que simula o jogo One Night: Ultimate Werewolf

# Biblioteca para distribuir aleatoriamente as cartas
import random

# Dicionarios para a quantidade de jogadores!
# 1
d1 = {'werewolf': False, 'seer': False, 'villager': False, 'villager2': False}

# 3
d3 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False}

# 4
d4 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False}

# 5
d5 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False, 'villager3': False}

# 6
d6 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False, 'villager3': False, 'hunter': False}

# 7
d7 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False, 'villager3': False, 'hunter': False, 'drunk': False}

# 8
d8 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False, 'villager3': False, 'hunter': False, 'drunk': False, 'insomniac': False}

# 9
d9 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False, 'villager3': False, 'hunter': False, 'insomniac': False, 'drunk': False, 'tanner': False}

# 10
d10 = {'werewolf': False, 'werewolf2': False, 'seer': False, 'robber': False, 'troublemaker': False, 'villager': False, 'villager2': False, 'villager3': False, 'hunter': False, 'insomniac': False, 'drunk': False, 'tanner': False, 'minion': False}

# Uma lista que contem a lista de papeis
listaD = [0, d1, 2, d3, d4, d5, d6, d7, d8, d9, d10]

# Dicionario das fases do jogo
dPlay = {'minion': True, 'seer': True, 'robber': True, 'drunk': True, 'troublemaker': True, 'insomniac': True}

# Um dicionario que tem a descricao de cada papel

# Dicionario explicando cada papel
dPapel = {
            'villager': 'Você é um simples aldeão. Você faz parte do time da vila e não tem funcão durante a noite!',
            'werewolf': 'Voce é um lobisomem. Você faz parte do time dos lobisomens. Seu papel durante a noite e reconhecer o outro lobisomem (caso tenha)',
            'seer': 'Você é a vidente. Você faz parte do time da vila. Seu papel é acordar em um certo instante da noite e ou olhar duas cartas do centro ou olhar a carta de outro jogador',
            'robber': 'Voce é o ladrao. Você faz parte do time da vila. Seu papel é acordar em um certo instante da noite e olhar a carta de um jogador e trocá-la com a sua',
            'troublemaker': 'Você é a encrenqueira. Você faz parte do time da vila. Seu papel é trocar a carta de dois outros jogadores em um certo momento da noite.',
            'tanner': 'Voce é o lenhador. Voce nao esta em nenhum time. Seu papel é ter o maior número de votos e ser escolhido, assim ganhando!',
            'drunk': 'Voce é o bebado. Voce faz parte do time da vila. Seu papel e trocar sua carta com alguma do centro sem olha-la.',
            'hunter': 'Voce é o cacador. Voce faz parte do time da vila. Caso tenha o maior número de votos, voce escolhera outro pessoa para morrer junto com voce.',
            'insomniac': 'Voce é a sonâmbula. Você faz parte do time da vila. Ao final da noite, você acorda e checa a sua carta somente.',
            'minion': 'Você é o lacaio. Você faz parte do time dos lobisomens. Após o turno dos lobisomens, você acorda e vê quem são os lobisomens, porém eles não sabem que você é o lacaio.'
        }

# Variáveis globais para impedir que um jogador faça mais de uma coisa
umSeer = True
umRobber = True
umTrouble = True

# Lista para organizar quem esta participando
participando = []

# Classe para guardar o ID e a carta do jogador
class player:
    def __init__(self, ID):
        self.ID = ID
        self.carta = ''

# Funcao para resetar os dicionarios
def reset():
    for dic in listaD:
        for chave, valor in dic.items():
            dic[chave] = False

# Uma funcao que ira designar uma carta para cada jogador
def orgRoles():
    print('Entrou em orgRoles!')
    
    dic = listaD[qtd]
    print(dic)
    cont = 0
    # Enquanto houver mais de 3 cartas nao designadas (Quando houver 3, ele para [Serao as cartas do centro])
    while sum(map((False).__eq__, dic.values())) != 3:
        print('oi')
        key = random.choice(list(dic.keys()))
        print(key)
        if not dic[key]:
            dic[key] = True
            print(lista[cont])
            lista[cont].carta = key
            cont+=1

# Organizarr as cartas do centro
def orgCentro():
    print('Entrou em orgCentro!')
    
    global cartasãoCentro
    cartasãoCentro = []
    
    dic = listaD[qtd]
    for chave, valor in dic.items():
        if not dic[chave]:
            dic[chave] = True
            cartasãoCentro.append(chave)
            
    print(cartasãoCentro)
         
# Guardar o objeto de um jogador no dicionario dPlay para facil acesso
def organizarD():
    print('Entrou em organizarD!')
    
    for player in lista:
        try:
            if dPlay[player.carta]:
                dPlay[player.carta] = player
        except KeyError:
            pass
    
# Pegar os jogadores que sao lobisomens
def getWerewolf():
    listaW = []
    
    for player in lista:
        if player.carta == 'werewolf' or player.carta == 'werewolf2':
            listaW.append(player)
            
    return listaW

# Pegar a posicao do objeto de um jogador na lista
def getPos(ID):
    pos = 0
    
    for player in lista:
        if player.ID == ID:
            return pos
        pos+=1

# Importando as bibliotecas do discord.py
import discord
from discord.ext import commands

# Criando o client
client = commands.Bot(command_prefix='!')

# Quando estiver pronto
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(sum(map((False).__eq__, d1.values())))
    
# Quando alguem enviar uma mensagem
@client.event
async def on_message(message):
    # Se for mensagem de algum bot, ele retorna
    if message.author.bot: return
    
    # Olhar se a mensagem nao e um comando
    await client.process_commands(message)
    
    # Adicionando ao bloco as variaveis
    global umSeer
    global umRobber
    global umTrouble
    
    # Checar se a mensagem recebida foi da DM da pessoa com a carta 'seer'
    try:
        if message.channel.id == dmseer.id:
            # Variavel utilizada para receber somente uma mensagem desse tipo (para nao fazer a funcao da carta mais de uma vez)
            if umSeer == True:
                # Recebendo o tipo de mensagem
                # @0 para carta do centro
                if message.content == '@0':
                    # Escolhendo a carta do centro (entre as 3)
                    await dmseer.send('Agora digite #0, #1 ou #2 para escolher alguma carta do centro!')
                                      
                # @1 para carta de jogador
                elif message.content == '@1':
                    # Imprimindo os jogadores
                    for pos in range(len(lista)):
                        await dmseer.send('Pessoa: {}  -  Número: {} '.format(client.get_user(lista[pos].ID).name, pos))
                    # Para escolher os jogadores
                    await dmseer.send('Agora escolha um Número de 0 a {}, EXCETO {}! USE $ ANTES DO Número! Exemplo: $1'.format(qtd-1, getPos(message.author.id)))
                
                # Revelando a carta do centro
                elif message.content.startswith('#'):
                    cartaEscolhida = cartasAoCentro[int(message.content[1])]
                    await dmseer.send('A carta escolhida foi {}!'.format(cartaEscolhida))
                    umSeer = False
                    
                # Revelando o jogador
                elif message.content.startswith('$'):
                    pos = int(message.content[1])
                    username = client.get_user(lista[pos].ID).name
                    await dmseer.send('A carta escolhida foi {}, do jogador {}'.format(lista[pos].carta, username))
                    umSeer = False
    except NameError:
        pass
    
    # Checar se a mensagem recebida foi da DM da pessoa com a carta 'robber'
    try:
        if message.channel.id == dmrobber.id:
            # Variavel utilizada para receber somente uma mensagem desse tipo (para nao fazer a funcao da carta mais de uma vez)
            if umRobber == True:
                # Checa se e um comando
                if message.content.startswith('@'):
                    # Procura o jogador escolhido e entao e feita a troca
                    robber = lista[getPos(message.author.id)]
                    pessoa = lista[int(message.content[1])]
                    aux = robber.carta
                    robber.carta = pessoa.carta
                    pessoa.carta = aux
                    await dmrobber.send('A carta que você viu era {}! Portanto agora você se tornou o que viu!'.format(robber.carta))
                    umRobber = False
    except NameError:
        pass                
    
    # Checar se a mensagem recebida foi da DM da pessoa com a carta 'troublemaker'
    try:      
        if message.channel.id == dmtrouble.id:
            # Checar se a mensagem e referente ao comando enviado na DM
            if message.content.startswith('@'):
                # Variavel utilizada para receber somente uma mensagem desse tipo (para nao fazer a funcao da carta mais de uma vez)
                if umTrouble == True:
                    # Apos a escolha dos jogadores, sera feita a troca das cartas entre eles
                    primeiraPessoa = lista[int(message.content[1])]
                    segundaPessoa = lista[int(message.content[3])]
                    umTrouble = False
                    aux = primeiraPessoa.carta
                    primeiraPessoa.carta = segundaPessoa.carta
                    segundaPessoa.carta = aux
    except NameError:
        pass

# Comando para instancia um jogo novo. O argumento passado e a quantidade de jogadores
@client.command()
async def jogar(ctx, arg):
    if ctx.author.id == 200414640570761216:
        global lista
        lista = []
        global qtd
        qtd = int(arg)
        
        global cartasDoCentro
        cartasDoCentro = []
        
# Comando que pode ser feito por qualquer um que queira jogar o jogo
@client.command()
async def p(ctx):
    if ctx.author.id not in participando:
        participando.append(ctx.author.id)
        newPlayer = player(ctx.author.id)
        lista.append(newPlayer)
    
# Comando para iniciar o jogo
@client.command()
async def iniciar(ctx):
    if not qtd == len(lista):
        return
    
    orgRoles()
    orgCentro()
    
    # Enviando a carta para cada jogador em sua DM!
    for player in lista:
        user = client.get_user(player.ID)
        dm = await user.create_dm()
        await dm.send('Sua carta é {}!'.format(player.carta))
        await dm.send(file=discord.File('{}.jpg'.format(player.carta)))
        
    print('Pronto!')
        
    organizarD()

# Comando auxiliar para printar as variaveis
@client.command()
async def printar(ctx):
    if ctx.author.id == 200414640570761216:
        print(lista)
        print(len(lista))
        print(qtd)
        print(cartasãoCentro)
        print(dPlay)
  
# Comando para chamar a funcao reset
@client.command()
async def resetd(ctx):
    if ctx.author.id == 200414640570761216:
        reset()
  
# Comando para finalizar o jogo e mostrar a todos, as cartas      
@client.command()
async def fim(ctx):
    if ctx.author.id == 200414640570761216:
        
        for player in lista:
            user = client.get_user(player.ID)
            await ctx.message.channel.send('--------------------------------------------------------------------------------------------------------------------')
            await ctx.message.channel.send(user.name)
            await ctx.message.channel.send(player.carta)
            
        await ctx.message.channel.send('======================================================================')
            
        for carta in cartasãoCentro:
            await ctx.message.channel.send(carta)
            await ctx.message.channel.send('--------------------------------------------------------------------------------------------------------------------')
            
        
# Comando para caso haja somente werewolf
@client.command()
async def werewolf(ctx):
    if ctx.author.id == 200414640570761216:
        lw = getWerewolf()
        
        if len(lw) == 0:
            return
        
        if len(lw) == 1:
            user = client.get_user(lw[0].ID)
            dm = await user.create_dm()
            await dm.send('Você é um lobisomem solitario!')
            return
        
        user1 = client.get_user(lw[0].ID)
        user2 = client.get_user(lw[1].ID)
        
        dm1 = await user1.create_dm()
        dm2 = await user2.create_dm()
        
        await dm1.send('Seu outro parceiro lobisomem é {}!'.format(user2.name))
        await dm2.send('Seu outro parceiro lobisomem é {}!'.format(user1.name))
        
# Comando para caso haja werewolf e minion
@client.command()
async def wereminion(ctx):
    if ctx.author.id == 200414640570761216:
        lw = getWerewolf()
        minion = dPlay['minion']
        
        if len(lw) == 0:
            user = client.get_user(minion.ID)
            dm = await user.create_dm()
            await dm.send('Não há nenhum lobisomem, você está sozinho...')
            return
            
        if len(lw) == 1:
            user = client.get_user(lw[0].ID)
            dm = await user.create_dm()
            await dm.send('Você é um lobisomem solitário!')
            
            userm = client.get_user(minion.ID)
            dmm = await user.create_dm()
            await dm.send('Há um lobisomem e ele é {}'.format(user.name))
            return
        
        user1 = client.get_user(lw[0].ID)
        user2 = client.get_user(lw[1].ID)
        
        dm1 = await user1.create_dm()
        dm2 = await user2.create_dm()
        
        await dm1.send('Seu outro parceiro lobisomem é {}!'.format(user2.name))
        await dm2.send('Seu outro parceiro lobisomem é {}!'.format(user1.name))
        
        userm = client.get_user(minion.ID)
        dmm = await userm.create_dm()
        await dmm.send('Há dois lobisomens e eles são {} e {}!'.format(user1.name, user2.name))
            
# Comando para seer
@client.command()
async def seer(ctx):
    if ctx.author.id == 200414640570761216:
        if dPlay['seer'] == True:
            return
        seer = dPlay['seer']
        user = client.get_user(seer.ID)
        
        global dmseer
        dmseer = await user.create_dm()
        
        await dmseer.send('Você pode olhar uma carta do centro OU de outro jogador. '
                          'Digite @0 para pegar do centro ou @1 para pegar de um jogador')
     
# Comando para robber
@client.command()
async def robber(ctx):
    if ctx.author.id == 200414640570761216:
        if dPlay['robber'] == True:
            return
        
        robber = dPlay['robber']
        user = client.get_user(robber.ID)
        
        global dmrobber
        dmrobber = await user.create_dm()
        
        await dmrobber.send('Você pode olhar a carta de um outro jogador e então trocá-la com ele. ')
        
        for pos in range(len(lista)):
            await dmrobber.send('Pessoa: {}  -  Número: {} '.format(client.get_user(lista[pos].ID).name, pos))
            
        await dmrobber.send('Escolha o primeiro número - de 0 a {}. EXCETO {} USE @ ANTES DO Número! Exemplo: @1'.format(qtd-1, getPos(robber.ID)))
  
# Comando a ser implementado      
#@client.command()
#async def drunk(ctx):
#    if ctx.author.id == 200414640570761216:
#
       
# Comando para troublemaker
@client.command()
async def troublemaker(ctx):
    if ctx.author.id == 200414640570761216:
        if dPlay['troublemaker'] == True:
            return
        
        trouble = dPlay['troublemaker']
        user = client.get_user(trouble.ID)
        
        global dmtrouble
        dmtrouble = await user.create_dm()
        
        await dmtrouble.send('Você pode trocar a carta de dois outros jogadores! NAO INCLUI VC! ')
        
        for pos in range(len(lista)):
            await dmtrouble.send('Pessoa: {}  -  Número: {} '.format(client.get_user(lista[pos].ID).name, pos))
        
        await dmtrouble.send('Agora escolha dois Números de 0 a {}, EXCETO {}! USE @ ANTES DO PRIMEIRO Número E DE UM ESPACO DO PRIMEIRO PARA O SEGUNDO Número! Exemplo: @1 3'.format(qtd-1, getPos(trouble.ID)))

# Comando para insomniac        
@client.command()
async def insomniac(ctx):
    if ctx.author.id == 200414640570761216:
        if dPlay['insomniac'] == True:
            return
        
        inso = dPlay['insomniac']
        user = client.get_user(inso.ID)
        
        dmtrouble = await user.create_dm()
        
        carta = lista[getPos(inso.ID)].carta
        
        dmtrouble.send('Sua carta atual é {}!'.format(carta))   
    
# Rodar o client (bot)
client.run('Nzc1MTAyMjg5NzU2Njg0MzA4.X6hcQg.wtA6u_13pB_6RVchpxpIuMxaQuo')