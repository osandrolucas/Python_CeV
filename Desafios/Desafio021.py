#from pygame import *
from playsound import playsound
print('Desafio: Faça um programa que abra e reproduza o audio de um arquivo mp3.')

#Primeira opção
#mixer.init()
#mixer.music.load('brainer.mp3')
#mixer.music.play()
#mixer.event.wait() #Espera a musica terminar (não funcionou)
#input() #Tive que colocar isso para funcionar a pygame

#Segunda opção
playsound('brainer.mp3')

#Terceira forma
#mixer.init()
#mixer.music.load('brainer.mp3')
#mixer.music.play()
#while mixer.music.get_busy():
#    time.Clock().tick(10)
