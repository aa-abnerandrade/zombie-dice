import colorama
import os
from time import sleep
import random

colorama.init()


#ESTRUTURANDO PLACAR ZERADO
def criarEzerar_placar(ordem_players):
    cont = 0
    pontos_totais_tiro = []  # Zerando Pontos
    pontos_totais_passo = []
    pontos_totais_cerebro = []
    print("\033[1;mOrdem de jogadores:") #Exibindo ordem de jogadores
    for cont in range(0, len(ordem_players)):
        print(f"{(cont+1):>4}º {ordem_players[cont]:>15}".upper())
        pontos_totais_tiro.append(int(0))
        pontos_totais_passo.append(int(0))
        pontos_totais_cerebro.append(int(0))

    return pontos_totais_tiro, pontos_totais_passo, pontos_totais_cerebro


# CRIA COPO ORIGINAL COM 13 DADOS
def criar_copo_original_dados():
    dados_originais = ("Vermelho",
         "Vermelho",
         "Vermelho",
         "Amarelo",
         "Amarelo",
         "Amarelo",
         "Amarelo",
         "Verde",
         "Verde",
         "Verde",
         "Verde",
         "Verde",
         "Verde" )
    return dados_originais

# EXIBIR PLACAR
def exibir_placar(ordem_players, pontos_totais_cerebro):
    print("\n:> SCORE CÉREBROS")
    for i in range(0, len(ordem_players)):
        print(f"Cérebros capturados de {ordem_players[i]} --> {pontos_totais_cerebro[i]} ")

# EXIBE DADOS NO COPO DO JOGO
def mostrar_dados_copo(copo_dados):
    print(f"Copo de Dados: {copo_dados}\n\n")

#SORTEAR DADOS
def sortear_dados(ponto_rodada_passo, qtd__dados_copo, copo_dados, dados_sorteados):
    for i in range(1, ((3+1)-ponto_rodada_passo)):
        indice_de_sorteio = random.randint(0, (qtd__dados_copo-1)) #Sorteia o índice
        # print(f"Índice Sorteado {indice_de_sorteio}")
        cor_dado_sorteado = copo_dados[indice_de_sorteio] # Pega a cor de acordo com o índice
        dados_sorteados.append(cor_dado_sorteado) # Coloca a cor em Dados Sorteados
        # print(dados_sorteados)
        qtd__dados_copo = qtd__dados_copo - 1 # Diminui 1 na quantidade do copo
        copo_dados.pop(indice_de_sorteio) # Retira a cor do copo
        print(f"{cor_dado_sorteado:>15}")
    return ponto_rodada_passo, qtd__dados_copo, copo_dados, dados_sorteados

# CRIA DADO VERMELHO
def criar_dado_vermelho(): 
    return ("Tiro", "Passo", "Tiro", "Cérebro", "Passo", "Tiro")

# CRIA DADO AMARELO 
def criar_dado_amarelo():
    return ("Tiro", "Passo", "Cérebro", "Tiro", "Passo", "Cérebro")

# CRIA DADO VERDE 
def criar_dado_verde():
    return ("Cérebro", "Passo", "Cérebro", "Tiro", "Passo", "Cérebro")


#SORTEAR FACES DOS DADOS JÁ SORTEADOS
def sortear_faces(cont, dados_sorteados, pt_rd_tiro, pt_rd_cerebro, d_vermelho, d_amarelo, d_verde):
    pt_rd_passo = 0
    faces_sorteadas = []
    face_sorteada = ''

    for cont in range(0, 3):
        if (dados_sorteados[cont] == "Vermelho"):
            face_sorteada = random.choice(d_vermelho)
        elif (dados_sorteados[cont] == "Amarelo"):
            face_sorteada = random.choice(d_amarelo)
        elif (dados_sorteados[cont] == "Verde"):
            face_sorteada = random.choice(d_verde)
        print(f"+ {face_sorteada:>10}")
        faces_sorteadas.append(face_sorteada)

        ######OJOGO__Iniciar__Turno__CadaJogador__CadaRodada__Contabilizar
        if (face_sorteada == 'Tiro'): # Alterar esse bloco: pulverizar dentro da condicional
            pt_rd_tiro = pt_rd_tiro + 1
        elif (face_sorteada == 'Passo'):
            pt_rd_passo = pt_rd_passo + 1
        elif (face_sorteada == 'Cérebro'):
            pt_rd_cerebro = pt_rd_cerebro + 1
        print(f"Dado {dados_sorteados[cont]}: --> {faces_sorteadas[cont]}")

    return pt_rd_tiro, pt_rd_passo, pt_rd_cerebro, faces_sorteadas


# EXIBE SCORE DO TURNO
def exibir_score_turno(ponto_rodada_tiro, ponto_rodada_passo, ponto_rodada_cerebro):
    print("\n")    
    print(f"\033[1;43m==================== Score do Turno:\033[m")
    print(f"Tiro: {ponto_rodada_tiro}")
    print(f"Passo: {ponto_rodada_passo}")
    print(f"Cérebro: {ponto_rodada_cerebro}")

# CHECA DERROTA
def checar_derrota(ptTiro):
    if (ptTiro >= 3):
        return True
    else:
        return False

# CHECA VITÓRIA
def checar_vitoria(ptCerebro):
    if(ptCerebro >= 13):
        print("YOU WIN")
        print(f"Você capturou {ptCerebro} cérebros!")
        return True
    else:
        return False

# CHECA SE JOGADOR DESEJA CONTINUAR COM MAIS 1 RODADA:
def checar_continuidade_rodada():
    continuar = str(input("\n\033[1;30;42m :> Continuar com + 1 Rodada?\033[m [S/N]")).upper()
    return True
    
    


