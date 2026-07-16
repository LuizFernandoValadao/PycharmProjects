frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.upper().count('O'))
print(frase.lower())
print(len(frase))
print(len(frase.strip())) #strip remove os espaços!
print(frase.replace('Python', 'Android'))
#frase = frase.replace('Python', 'Android')
print('Curso' in frase)
print(frase.find('Video')) #-1 = nao tem na frase
print(frase.lower().find('video'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])


#print("""Você quer enviar uma mensagem com fontes que
#mostrem sua singularidade de forma sutil? Use o gerador de
#textos pequenos para gerar textos pequenos a serem usados com suas fontes de tamanho normal.
#O texto gerado pelo gerador de texto pequeno ou pelo gerador de fonte extremamente pequena
#pode aparecer um pouco acima ou abaixo dos caracteres típicos, semelhante ao símbolo ™.""")