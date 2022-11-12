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



#1-OSDADOS //////////////////////////////////////////////////////////////////////////////

##OSDADOS__Definição
dados_originais = funcoes_game.criar_copo_original_dados()
faces_dado_vermelho = funcoes_game.criar_dado_vermelho()
faces_dado_amarelo = funcoes_game.criar_dado_amarelo()
faces_dado_verde = funcoes_game.criar_dado_verde()



#1-OJOGO //////////////////////////////////////////////////////////////////////////////////

##OJOGO__PLAY

play_game = funcoes_auxiliares.comecar_jogo()
if (play_game == "N"):
    exit()


###OJOGO__PLAY__TOTAL
pontos_totais_tiro, pontos_totais_passo, pontos_totais_cerebro = funcoes_game.criarEzerar_placar(ordem_players)



###OJOGO__PLAY__TURNO
ordinal_turno = 1
while (play_game == "S"):
    copo_dados = list(dados_originais)
    qtd__dados_copo = len(copo_dados)
    dados_sorteados = []

    funcoes_auxiliares.cabecalho()    
    funcoes_game.mostrar_dados_copo(copo_dados)
    

    pts_turno_tiro = funcoes_game.zerar_pts_turno()
    pts_turno_passo = funcoes_game.zerar_pts_turno()
    pts_turno_cerebro = funcoes_game.zerar_pts_turno() 

    print(f"\n \033[1;30;43m {ordinal_turno}º TURNO \033[m")
    funcoes_game.exibir_placar(ordem_players, pontos_totais_cerebro)

    ####OJOGO__PLAY__TURNO__CadaJogador
    for indice_player, player in enumerate(ordem_players): # Repetição do jogador no momento
        print(f"\033[33m\n\n Turno {ordinal_turno} | Jogando agora: Player{indice_player+1}: {player}\033[m")

        
        
        ###OJOGO__PLAY__RODADA
        play_rodada_jogador = 'S'
        num_rodadas = 0
        pt_rodada_pass = funcoes_game.zerar_pt_rodada()
        while (play_rodada_jogador == 'S'): # Loop para o mesmo jogador fazer infinitas jogadas                
            num_rodadas = num_rodadas + 1
            qtd_dados_ajogar = 3
            
            play_rodada_jogador = str(input(f"\n:> {player}, insira S para sortear {(qtd_dados_ajogar - pt_rodada_pass)} dados => "))

            ####OJOGO__PLAY__RODADA__SorteioDadosCores
            print('\033[1;30;40mDados Sorteados: \033[m')
            qtd__dados_copo, copo_dados, dados_sorteados = funcoes_game.sortear_dados(pt_rodada_pass, qtd__dados_copo, copo_dados, dados_sorteados)


            ####OJOGO__PLAY__RODADA__SorteioDadoFaces
            pt_rodada_tir = funcoes_game.zerar_pt_rodada()
            pt_rodada_pass = funcoes_game.zerar_pt_rodada()
            pt_rodada_cer = funcoes_game.zerar_pt_rodada()

            play_rodada = str(input('\n:> Insira S para jogar os dados => ')).upper()
            sleep(1)
            print("Resultado:") # Exibe Faces Sorteadas

            pt_rodada_tir, pt_rodada_pass, pt_rodada_cer, faces_sorteadas = funcoes_game.sortear_faces(0, dados_sorteados, pt_rodada_tir, pt_rodada_pass, pt_rodada_cer, faces_dado_vermelho, faces_dado_amarelo, faces_dado_verde)
            
            pts_turno_tiro += pt_rodada_tir
            pts_turno_passo += pt_rodada_pass
            pts_turno_cerebro += pt_rodada_cer

            pontos_totais_tiro[indice_player] += pts_turno_tiro
            pontos_totais_passo[indice_player] += pts_turno_passo
            pontos_totais_cerebro[indice_player] += pts_turno_cerebro


            funcoes_game.exibir_score_rodada(pt_rodada_tir, pt_rodada_pass, pt_rodada_cer)
            funcoes_game.exibir_score_turno(pts_turno_tiro, pts_turno_passo, pts_turno_cerebro)
            
            print(f"\033[1;43m========== Acumulado {indice_player+1}-{player}\033[m")
            print(f"Tiro: {pontos_totais_tiro[indice_player]}")
            print(f"Passo: {pontos_totais_passo[indice_player]}")
            print(f"Quantidade Cérebros: {pontos_totais_cerebro[indice_player]}\n\n")

            if (funcoes_game.checar_derrota(pontos_totais_tiro[indice_player])):
                print("PERDEEU O TURNO!")
                print(f"{pontos_totais_tiro[indice_player]} tiros te atingiram. E você perdeu os cérebros do turno.")
                pontos_totais_cerebro[indice_player] = pontos_totais_cerebro[indice_player] - pts_turno_cerebro
                pontos_totais_tiro[indice_player] = 0
                break
            else:
                if (funcoes_game.checar_vitoria(pontos_totais_cerebro[indice_player])):
                    funcoes_auxiliares.cabecalho()
                    funcoes_game.exibir_placar(ordem_players, pontos_totais_cerebro)
                    play_rodada_jogador = "N"
                    break
                else:
                    #####OJOGO__Iniciar__Turno__CadaJogador__CadaRodada__Continuar
                    funcoes_game.mostrar_dados_copo(copo_dados)
                    if(funcoes_game.checar_continuidade_rodada()):
                        play_rodada_jogador = "S"
                        #pt_rodada_pass = 0
                        #print(play_rodada_jogador) #Teste
                        readicionados = []
                        for i in range(0, 3):
                            if (faces_sorteadas[i] == 'Passo'):
                                readicionados.append(dados_sorteados[i])

                        print(readicionados)
                        dados_sorteados.clear()
                        dados_sorteados = readicionados
                        print(dados_sorteados)
                        num_rodadas = num_rodadas + 1
                    else:
                        copo_dados = list(dados_originais)
                        print(f"Dados no copo: {copo_dados}")
                        pontos_totais_tiro[indice_player] = 0



            if (qtd_dados_ajogar > qtd__dados_copo):
                copo_dados = list(dados_originais)

        sleep(3)
        
    ###OJOGO__Iniciar__Turno
    ordinal_turno += 1 # Adiciona mais 1 no turno
   

