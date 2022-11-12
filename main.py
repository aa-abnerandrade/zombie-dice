# IMPORTS DE CONFIGURAÇÃO
import colorama
import random
from time import sleep
import os

#IMPORTS DE FUNÇÕES
import funcoes_auxiliares
import funcoes_game

# INICIALIZAÇÕES NECESSÁRIAS
colorama.init()



funcoes_auxiliares.cabecalho()


#1-APRESENTAÇÃO////////////////////////////////////////////////////////////////////////

ler_orientacoes = str(input('\033[0;35;40m :> Deseja ler as orientações do jogo? [S/N]:\033[m ')).upper()

if (ler_orientacoes == "S"):
    r_go_to_game = funcoes_auxiliares.exibir_orientacoes()
    if (r_go_to_game == "N"):
        print("\033[1;30;45m========= ENCERRANDO... =========\033[m")
        sleep(2)
        exit()
    else:
        print('\033[0;35;40m Bem vindo ao Zombie Dice \033[m')
        sleep(2)
        funcoes_auxiliares.cabecalho()
else:
    print('\033[0;35;40m Bem vindo ao Zombie Dice \033[m')
    sleep(2)
    funcoes_auxiliares.cabecalho()



#1-JOGADORES////////////////////////////////////////////////////////////////////////////

##JOGADORES__Quantidade
funcoes_auxiliares.cabecalho()
qtd_players = funcoes_auxiliares.definir_qtd_players(0, confirma__qtd_players = "N")


##JOGADORES__Nomes
nomes_players = funcoes_auxiliares.nomear_players(qtd_players)


##JOGADORES__Sorteio
ordem_players = funcoes_auxiliares.sortear_jogadores(nomes_players)


##JOGADORES__Placar
pontos_totais_tiro, pontos_totais_passo, pontos_totais_cerebro = funcoes_game.criarEzerar_placar(ordem_players)



#1-OSDADOS //////////////////////////////////////////////////////////////////////////////


##OSDADOS__Definição
''' 
qtd_total_dados = 13
qtd_dados_vermelhos = 3
qtd_dados_amarelos = 4
qtd_dados_verdes = 6
'''
dados_originais = funcoes_game.criar_copo_original_dados()
faces_dado_vermelho = funcoes_game.criar_dado_vermelho()
faces_dado_amarelo = funcoes_game.criar_dado_amarelo()
faces_dado_verde = funcoes_game.criar_dado_verde()



#1-OJOGO //////////////////////////////////////////////////////////////////////////////////

##OJOGO__Iniciar
print("\033[0;33m :> Qualquer caractere para começar o jogo. Ou X para sair.\033[m")
start_game = str(input(":> \033[1;30;42mInsira aqui:\033[m ")).upper()
if (start_game == "X"):
    play_turno = "N"
    funcoes_auxiliares.cabecalho()
    print("Jogo Encerrado.") #Sair do jogo
    exit()
else:
    play_turno = "S"
    funcoes_auxiliares.cabecalho()
    print("Ir para jogo") #Ir para jogo
    print("\033[1;32mPLAY")
    sleep(1)
    print("Que vença o melhor")
    sleep(1)



###OJOGO__Iniciar__Turno
ordinal_turno = 1

while (play_turno == "S"):
    funcoes_auxiliares.cabecalho()    
    
    copo_dados = list(dados_originais)
    funcoes_game.mostrar_dados_copo(copo_dados)

    qtd__dados_copo = len(copo_dados)
    dados_sorteados = []

    print(f"\n \033[1;30;43m {ordinal_turno}º TURNO \033[m")
    funcoes_game.exibir_placar(ordem_players, pontos_totais_cerebro)

    ####OJOGO__Iniciar__Turno__CadaJogador
    for indice_player, player in enumerate(ordem_players):
        print(f"\033[33m\n\n Turno {ordinal_turno} | Jogando agora: Player{indice_player+1}: {player}\033[m")

        #####OJOGO__Iniciar__Turno__CadaJogador__CadaRodada
        play_jogador = 'S'
        ordinal_rodada = 0
        ponto_rodada_passo = 0 # Zerando Rodada PASSO

        while (play_jogador == 'S'):
            ordinal_rodada = ordinal_rodada + 1
            qtd_dados_ajogar = 3
            play_jogador = str(input(f"\n:> {player}, insira S para sortear {(qtd_dados_ajogar - ponto_rodada_passo)} dados => "))

            ######OJOGO__Iniciar__Turno__CadaJogador__CadaRodada__SorteioDadosCores
            print('\033[1;30;40mDados Sorteados: \033[m')
            ponto_rodada_passo, qtd__dados_copo, copo_dados, dados_sorteados = funcoes_game.sortear_dados(ponto_rodada_passo, qtd__dados_copo, copo_dados, dados_sorteados)

            ######OJOGO__Iniciar__Turno__CadaJogador__CadaRodada__SorteioDadoFaces
            
            play_rodada = 'S'
            ponto_rodada_tiro = 0 # Zerando Tiro
            ponto_rodada_cerebro = 0 # Zerando Cérebro

            play_rodada = str(input('\n:> Insira S para jogar os dados => ')).upper()
            sleep(1)
            print("Resultado:") # Exibe Faces Sorteadas

            ponto_rodada_tiro, ponto_rodada_passo, ponto_rodada_cerebro, faces_sorteadas = funcoes_game.sortear_faces(0, dados_sorteados, ponto_rodada_tiro, ponto_rodada_cerebro, faces_dado_vermelho, faces_dado_amarelo, faces_dado_verde)
            pontos_totais_tiro[indice_player] += ponto_rodada_tiro
            pontos_totais_passo[indice_player] += ponto_rodada_passo
            pontos_totais_cerebro[indice_player] += ponto_rodada_cerebro


            funcoes_game.exibir_score_turno(ponto_rodada_tiro, ponto_rodada_passo, ponto_rodada_cerebro)

            
            
            print(f"\033[1;43m======= Acumulado {indice_player+1}-{player}\033[m")
            #print(f"Tiro: {pontos_totais_tiro[indice_player]}")
            #print(f"Passo: {pontos_totais_passo[indice_player]}")
            print(f"Quantidade Cérebros: {pontos_totais_cerebro[indice_player]}\n\n")

            if (funcoes_game.checar_derrota(pontos_totais_tiro[indice_player])):
                print("PERDEEU O TURNO!")
                print(f"{pontos_totais_tiro[indice_player]} tiros te atingiram. E você perdeu todos os cérebros.")
                pontos_totais_cerebro[indice_player] = pontos_totais_cerebro[indice_player] - ponto_rodada_cerebro
                pontos_totais_tiro[indice_player] = 0
                break
            else:
                if (funcoes_game.checar_vitoria(pontos_totais_cerebro[indice_player])):
                    funcoes_auxiliares.cabecalho()
                    funcoes_game.exibir_placar(ordem_players, pontos_totais_cerebro)
                    play_jogador = "N"
                    break
                else:
                    #####OJOGO__Iniciar__Turno__CadaJogador__CadaRodada__Continuar
                    funcoes_game.mostrar_dados_copo(copo_dados)
                    if(funcoes_game.checar_continuidade_rodada()):
                        play_jogador == "S"
                        #ponto_rodada_passo = 0
                        #print(play_jogador) #Teste
                        readicionados = []
                        for i in range(0, 3):
                            if (faces_sorteadas[i] == 'Passo'):
                                readicionados.append(dados_sorteados[i])

                        print(readicionados)
                        dados_sorteados.clear()
                        dados_sorteados = readicionados
                        print(dados_sorteados)
                        ordinal_rodada = ordinal_rodada + 1
                    else:
                        copo_dados = list(dados_originais)
                        print(f"Dados no copo: {copo_dados}")
                        pontos_totais_tiro[indice_player] = 0



            if (qtd_dados_ajogar > qtd__dados_copo):
                copo_dados = list(dados_originais)

        sleep(3)
        
    ###OJOGO__Iniciar__Turno
    ordinal_turno = ordinal_turno + 1 # Adiciona mais 1 no turno
   

