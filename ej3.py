preg=int(input('Cuantas preguntas has respondido bien? '))
preg2=int(input('Cuantas preguntas has respondido mal? '))
nota1=preg*0.5
nota2=preg2*0.25
notaF=nota1-nota2
print(f'Tu nota del examen es {notaF}')