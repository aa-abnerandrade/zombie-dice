def solution(k, a):
      qtd_par = 0
      for X in range(0, len(a)):
            print("X aqui", X)
            for Y in range(0, len(a)):
                  print("Y aqui", Y)
                  print("A na posição X", a[X])
                  print("A na posição Y", a[Y])
                  if (a[X] + a[Y] == k):
                        if qtd_par == 0:
                              par1 = a[X]
                              par2 = a[Y]
                              qtd_par += 1
                              print("par + 1 1ª vez")
                        else:
                              if (a[X] == par1 and a[Y] == par2) or (a[X] == par2 and a[Y] == par1):
                                    par1 = a[X]
                                    par2 = a[Y]
                              else:
                                    qtd_par += 1
                                    print("par + 1")

      print( qtd_par)

solution(11, [10, 9, 4, 0, 8, 1, 7, 6, 10, 5])
