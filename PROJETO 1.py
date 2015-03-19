# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:44:59 2015

@author: PedroSambi
"""
#importando random e craindo as variaveis
from random import choice
jogador=0
computador=0 
#parametros para mudanca
#tesoura =1 
#spock=2
#papel=3
#lagarto=4
#pedra
lagarto = "lagarto"
tesoura = "tesoura"
spock = "spock"
papel = "papel"
pedra = "pedra"

opcoes = ["lagarto","tesoura","spock","papel","pedra"]
print("E ai nerdão, gosta do Sheldon né? Então vamo jogar um lizard spock paper rock scissors? as regras sao claras!:  Tesoura corta papel, papel cobre pedra, pedra esmaga lagarto, lagarto envenena spock, spock esmaga tesoura, tesoura decapita lagarto, lagarto come papel, papel refuta spock, spock vaporiza pedra , e como sempre, pedra quebra tesoura! quem fizer 3 pontos primeiro leva a mlehor!")
 
#escolhendo opcao do computador em x e do jogador em y
while jogador<3 and computador <3:
	x=choice(opcoes)
	y=str(input("E ai nerdão , qaul vai ser: lagarto, spock, papel, pedra ou tesoura??"))
		


	if x == y:
		print("voces empataram")

#computador sendo tesoura
	elif x==tesoura and y==spock:
		print("o computador jogou tesoura,voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==tesoura and y==papel:
		print("o computador jogou tesoura,Voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==tesoura and y==lagarto:
		print("o computador jogou tesoura, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==tesoura and y==pedra:
		print("o computador jogou tesoura, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))

#computador sendo spock
	elif x==spock and y==tesoura:
		print("o computador jogou spock, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==spock and y==papel:
		print("o computador jogou spock, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==spock and y==lagarto:
		print("o computador jogou spock, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==spock and y==pedra:
		print("o computador jogou spock, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))

#computador sendo papel
	elif x==papel and y==tesoura:
		print("o computador jogou papel, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==papel and y==spock:
		print("o computador jogou papel, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==papel and y==lagarto:
		print("o computador jogou papel, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==papel and y==pedra:
		print("o computador jogou papel, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
#computador sendo lagarto
	elif x==lagarto and y==tesoura:
		print("o computador jogou lagarto, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==lagarto and y==spock:
		print("o computador jogou lagarto, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==lagarto and y==papel:
		print("o computador jogou lagarto, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==lagarto and y==pedra:
		print("o computador jogou lagarto, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
		
#computador sendo pedra
	elif x==pedra and y==tesoura:
		print("o computador escolheu pedra, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==pedra and y==spock:
		print("o computador escolheu pedra, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==pedra and y==papel:
		print("o computador escolheu pedra, voce venceu")
		jogador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))
	elif x==pedra and y==lagarto:
		print("o computador escolheu pedra, voce perdeu")
		computador+=1
		print("Placar : computador %d X %f jogador"%(computador,jogador))


if jogador==3:
  print("parabeens nerdão, levou a melhor em cima do Sheldon, ta preparado pra cursar engenharia no Insper!")
if computador == 3:
  print("xiii nerdão voce perdeu, volta a assistir o seu anime predileto!")

		
		


