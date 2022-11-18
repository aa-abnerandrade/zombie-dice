import colorama
import random

import funcoes_auxiliares

colorama.init()


# ESTRUTURANDO PLACAR TOTAL ZERADO
def criarEzerar_placar(ordem_players):
      """
      Estrutura listas que controlam a pontuação de cada item, de cada gamer.

      :param ordem_players: Lista com nicks dos jogadores, já na sequência sorteada para jogar.
      :return: 3 Listas com posições correspondentes a quantidade jogadores. Posições com valores zerados.
      """
      listTotTiro = []  # Zerando Pontos
      listTotPasso = []
      listTotCerebro = []
      print("\033[1;mOrdem de jogadores:")  # Exibindo ordem de jogadores
      for cont in range(0, len(ordem_players)):
            print(f"{(cont + 1):>4}º {ordem_players[cont]:>15}".upper())
            listTotTiro.append(int(0))
            listTotPasso.append(int(0))
            listTotCerebro.append(int(0))

      return listTotTiro, listTotPasso, listTotCerebro


# REINICIA O COPO DE DADOS COM OS 13 DADOS
def reinicia_copo():
    """
    Conserva a forma inicial do copo de dados. Objetiva reiniciar o copo com todos os dados, na correta sequência.

    :return: Retorna lista com todos os dados
    """
    return ["Vermelho",
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
            "Verde"]


# EXIBIR PLACAR
def exibir_placar(ordem_players, pontos_totais_cerebro):

      """
      Exibe placar atualizado de cérebros de cada jogador

      :param ordem_players: Lista com jogadores
      :param pontos_totais_cerebro: Lista de pontuação de cérebros de cada jogador
      """
      print("\n:> SCORE CÉREBROS")
      for i in range(0, len(ordem_players)):
            print(f"Cérebros capturados de {ordem_players[i]} --> {pontos_totais_cerebro[i]} ")


# # EXIBE DADOS NO COPO DO JOGO
def mostrar_dados_copo(copo_dados):
      """
      Exibe os dados no copo no momento da execução.

      :param copo_dados: Lista com os dados presentes no copo.
      """
      print(f"\033[1;30;40mCopo de Dados: {copo_dados}\033[m\n")


# ZERA OS PONTOS DO TURNO 
def zerar_pts_turno():
      """
      Zera a pontuação do turno.

      :returns: 3 inteiros zero.
      """
      return 0, 0, 0


# ZERA PONTOS DA RODADA
def zerar_pt_rodada():
      """
      Zera a pontuação em um item na variável de rodada.

      :return: 1 inteiro zero.
      """
      return 0


# SORTEAR DADOS
def sortear_dados(ponto_rodada_passo, qtd__dados_copo, copo_dados, dados_sorteados):
      for i in range(1, ((3 + 1) - ponto_rodada_passo)):
            indice_de_sorteio = random.randint(0, (qtd__dados_copo - 1))  # Sorteia o índice
            # print(f"Índice Sorteado {indice_de_sorteio}")
            cor_dado_sorteado = copo_dados[indice_de_sorteio]  # Pega a cor de acordo com o índice
            dados_sorteados.append(cor_dado_sorteado)  # Coloca a cor em Dados Sorteados
            qtd__dados_copo -= 1  # Diminui 1 na quantidade do copo
            copo_dados.pop(indice_de_sorteio)  # Retira a cor do copo
            print(f"{cor_dado_sorteado:>15}")
      return qtd__dados_copo, copo_dados, dados_sorteados


# CRIA DADO VERMELHO
def criar_dado_vermelho():
      return ("Tiro", "Passo", "Tiro", "Cérebro", "Passo", "Tiro")


# CRIA DADO AMARELO 
def criar_dado_amarelo():
      return ("Tiro", "Passo", "Cérebro", "Tiro", "Passo", "Cérebro")


# CRIA DADO VERDE 
def criar_dado_verde():
      return ("Cérebro", "Passo", "Cérebro", "Tiro", "Passo", "Cérebro")


# SORTEAR FACES DOS DADOS JÁ SORTEADOS
def sortear_faces(cont, dados_sorteados, pt_rd_tiro, pt_rd_passo, pt_rd_cerebro, d_vermelho, d_amarelo, d_verde):
      faces_sorteadas = []
      face_sorteada = ''
      print("Resultado:")  # Exibe Faces Sorteadas
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
            if (face_sorteada == 'Tiro'):
                  pt_rd_tiro += 1
            elif (face_sorteada == 'Passo'):
                  pt_rd_passo += 1
            elif (face_sorteada == 'Cérebro'):
                  pt_rd_cerebro += 1
            print(f"Dado {dados_sorteados[cont]}: --> {faces_sorteadas[cont]}")

      return pt_rd_tiro, pt_rd_passo, pt_rd_cerebro, faces_sorteadas


# EXIBE SCORE DA RODADA
def exibir_score_rodada(ponto_rodada_tiro, ponto_rodada_passo, ponto_rodada_cerebro):
      print("\n")
      print(f"\033[1;43m==================== Pontos da Rodada:\033[m")
      print(f"Tiro: {ponto_rodada_tiro}")
      print(f"Passo: {ponto_rodada_passo}")
      print(f"Cérebro: {ponto_rodada_cerebro}")


# EXIBE SCORE DO TURNO
def exibir_score_turno(ponto_turno_tiro, ponto_turno_passo, ponto_turno_cerebro):
      print(f"\033[1;43m==================== Pontos do Turno:\033[m")
      print(f"Tiro: {ponto_turno_tiro}")
      print(f"Passo: {ponto_turno_passo}")
      print(f"Cérebro: {ponto_turno_cerebro}")


# EXIBE SCORE ACUMULADO TOTAL
def exibir_score_total_cerebros(i_player, player, totalCerebros):
      print(f"\033[1;43m========== Acumulado {i_player + 1}-{player}\033[m")
      print(f"Quantidade Cérebros: {totalCerebros}\n\n")


# CHECA DERROTA
def checar_derrota(ptTiro):
      if (ptTiro >= 3):
            return True
      else:
            return False


# CHECA VITÓRIA
def checar_vitoria(ptCerebro):
      """
      Verifica se o jogador da vez venceu o jogo.

      :param ptCerebro: Variável de controle com numeração da rodada.
      :return: Booleano com vitória ou não vitória.
      """
      if (ptCerebro >= 13):
            funcoes_auxiliares.cabecalho()
            print("YOU WIN")
            print(f"Você capturou {ptCerebro} cérebros!")
            return True
      else:
            return False


# CHECA SE JOGADOR DESEJA CONTINUAR COM MAIS 1 RODADA:
def checar_continuidade_rodada(rodada):
      """
      Verifica se o gamer deseja seguir com mais 1 rodada no mesmo turno.

      :param rodada: Variável de controle com numeração da rodada.
      :return: Booleano correspondente à informação do gamer.
      """
      continuar = str(input(f"\n\033[1;30;42m :> Continuar para {rodada + 1}ª Rodada?\033[m [S/N]")).upper()
      if (continuar == 'S'):
            return True
      else:
            return False


# CONSERVA OS DADOS QUE DERAM PASSO NA RODADA ANTERIOR
def manter_dados_passo(faces, dados_sorteados):
      """
      Verifica quais dados resultaram em PASSO a fim de mantê-los na próxima rodada do mesmo jogador.

      :param faces: Lista com faces resultadas na última rodada.
      :param dados_sorteados: Lista com dados sorteados na última rodada.
      :return: Lista de dados sorteados contendo apenas os dados que resultaram em PASSO na rodada anterior.
      """
      listaDadosPasso = []
      for i in range(0, 3):
            if (faces[i] == 'Passo'):
                  listaDadosPasso.append(dados_sorteados[i])
      dados_sorteados.clear()
      dados_sorteados = listaDadosPasso
      print("Dados herdados da última rodada:")
      if (len(dados_sorteados) > 0):
            for dado in dados_sorteados:
                  print(f"{dado:>10}")
      else:
            print("Nenhum dado herdado.")
      return dados_sorteados

