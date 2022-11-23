# IMPORTS DE CONFIGURAÇÃO
import colorama
from time import sleep

# IMPORTS DE FUNÇÕES
import funcoes_auxiliares
import funcoes_game

# INICIALIZAÇÕES NECESSÁRIAS
colorama.init()



# 1-APRESENTAÇÃO////////////////////////////////////////////////////////////////////////
funcoes_auxiliares.cabecalho()

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
else:
    print('\033[0;35;40m Bem vindo ao Zombie Dice \033[m')
    sleep(2)



# 1-JOGADORES////////////////////////////////////////////////////////////////////////////

# 2JOGADORES__Quantidade
funcoes_auxiliares.cabecalho()
qtd_players = funcoes_auxiliares.definir_qtd_players("N")
# 2JOGADORES__Nomes
nomes_players = funcoes_auxiliares.nomear_players(qtd_players)
# 2--JOGADORES__Sorteio
ordem_players = funcoes_auxiliares.sortear_jogadores(nomes_players)


# 1-OSDADOS //////////////////////////////////////////////////////////////////////////////

# 2OSDADOS__Definição
faces_dado_vermelho = funcoes_game.criar_dado_vermelho()
faces_dado_amarelo = funcoes_game.criar_dado_amarelo()
faces_dado_verde = funcoes_game.criar_dado_verde()


# 1-OJOGO //////////////////////////////////////////////////////////////////////////////////

# 2--OJOGO__PLAY
play_game = funcoes_auxiliares.comecar_jogo()
if (play_game == "N"):
    exit()

# 3---OJOGO__PLAY__TOTAL
pontos_totais_tiro, pontos_totais_passo, pontos_totais_cerebro = funcoes_game.criarEzerar_placar(ordem_players)

# 3---OJOGO__PLAY__TURNO
ordinal_turno = 1
while (play_game == "S"):
    copo_dados = funcoes_game.reinicia_copo()
    funcoes_auxiliares.cabecalho()    
    funcoes_game.mostrar_dados_copo(copo_dados)
    pts_turno_tiro, pts_turno_passo, pts_turno_cerebro = funcoes_game.zerar_pts_turno()

    qtd__dados_copo = len(copo_dados)
    dados_sorteados = []

    print(f"\n \033[1;30;43m {ordinal_turno}º TURNO \033[m")
    funcoes_game.exibir_placar(ordem_players, pontos_totais_cerebro)

    # 4----OJOGO__PLAY__TURNO__CadaJogador
    for indice_player, player in enumerate(ordem_players): # Repetição do jogador no momento
        print(f"\033[33m\n\n Turno {ordinal_turno} | Jogando agora: Player{indice_player+1}: {player}\033[m")
        pts_turno_tiro, pts_turno_passo, pts_turno_cerebro = funcoes_game.zerar_pts_turno()


        # 3---OJOGO__PLAY__RODADA
        play_rodada_jogador = 'S'
        num_rodadas = 0
        pt_rodada_pass = funcoes_game.zerar_pt_rodada()
        while (play_rodada_jogador == 'S'): # Loop para o mesmo jogador fazer infinitas jogadas
            num_rodadas = num_rodadas + 1
            qtd_dados_ajogar = 3
            
            play_rodada_jogador = str(input(f"\n:> {player}, insira S para sortear {(qtd_dados_ajogar - pt_rodada_pass)} dados => "))

            # 4----OJOGO__PLAY__RODADA__SorteioDados
            print('\033[1;30;47mDados Sorteados: \033[m')
            qtd__dados_copo, copo_dados, dados_sorteados = funcoes_game.sortear_dados(pt_rodada_pass, qtd__dados_copo, copo_dados, dados_sorteados)


            # 4----OJOGO__PLAY__RODADA__SorteioFaces
            pt_rodada_tir = funcoes_game.zerar_pt_rodada()
            pt_rodada_pass = funcoes_game.zerar_pt_rodada()
            pt_rodada_cer = funcoes_game.zerar_pt_rodada()

            play_rodada = str(input('\n:> Insira S para jogar os dados => ')).upper()
            sleep(1)

            pt_rodada_tir, pt_rodada_pass, pt_rodada_cer, faces_sorteadas = funcoes_game.sortear_faces(dados_sorteados, pt_rodada_tir, pt_rodada_pass, pt_rodada_cer, faces_dado_vermelho, faces_dado_amarelo, faces_dado_verde)
            
            pts_turno_tiro += pt_rodada_tir
            pts_turno_passo += pt_rodada_pass
            pts_turno_cerebro += pt_rodada_cer

            pontos_totais_cerebro[indice_player] += pt_rodada_cer


            funcoes_game.exibir_score_rodada(pt_rodada_tir, pt_rodada_pass, pt_rodada_cer)
            funcoes_game.exibir_score_turno(pts_turno_tiro, pts_turno_passo, pts_turno_cerebro)
            funcoes_game.exibir_score_total_cerebros(indice_player, player, pontos_totais_cerebro[indice_player])
            

            if (funcoes_game.checar_derrota(pts_turno_tiro)):  # Checa Vitória
                print("PERDEEU O TURNO!")
                print(f"{pts_turno_tiro} tiros te atingiram. E voc? perdeu os {pts_turno_cerebro} cérebros conquistados neste turno.")
                pontos_totais_cerebro[indice_player] -= pts_turno_cerebro
                pontos_totais_tiro[indice_player] = 0
                pontos_totais_passo[indice_player] = 0
                copo_dados = funcoes_game.reinicia_copo()
                sleep(3)
                break
            else:
                if (funcoes_game.checar_vitoria(pontos_totais_cerebro[indice_player])):  # Checa derrota
                    funcoes_game.exibir_placar(ordem_players, pontos_totais_cerebro)
                    play_game = "N"
                    play_rodada_jogador = "N"
                    break
                else:
                    funcoes_game.mostrar_dados_copo(copo_dados)
                    if(funcoes_game.checar_continuidade_rodada(num_rodadas)):
                        play_rodada_jogador = "S"
                        dados_sorteados = funcoes_game.manter_dados_passo(faces_sorteadas, dados_sorteados)
                    else:
                        copo_dados = funcoes_game.reinicia_copo()
                        funcoes_game.mostrar_dados_copo(copo_dados)
                        dados_sorteados.clear()
                        pontos_totais_tiro[indice_player] = 0
                        break

            if (qtd_dados_ajogar > qtd__dados_copo):
                copo_dados = funcoes_game.reinicia_copo()

        sleep(3)
        
    # 4----OJOGO__PLAY__TURNO__AdicionaOrdinal
    ordinal_turno += 1  # Adiciona mais 1 no turno
   
print('\033[1;30;45m = Obrigado por jogar Zombie Dice. Espero que tenha se divertido. = \033[m')
exit()