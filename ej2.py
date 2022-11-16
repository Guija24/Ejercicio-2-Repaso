NotaHI=float(input('Dime tu nota del Hito Individual: '))
NotaHG=float(input('Dime tu nota del Hito Grupal: '))
NotaE=float(input('Dime tu nota del Examen: '))
nota1=NotaHI*0.3
nota2=NotaHG*0.2
nota3=NotaE*0.5
NotaT=nota1+nota2+nota3
print(f'Tu nota del Trimestre es {round(NotaT)}')
