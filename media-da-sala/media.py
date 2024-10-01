def input_nota(msg):
    while True:
        try:
            nota = float(input(msg))
            if 0 <= nota <= 10 and len(str(nota).split('.')[-1]) <= 2:
                return nota
            else:
                print("por favor, isira uma nota valida entre 0.0 e 10.0")
        except ValueError:
            print('valor invalido')

nota0 = input_nota('qual a primeira nota do carlos')
nota1 = input_nota('qual a segunda nota do carlos')
nota2 = input_nota('qual a terceira nota do carlos')

nota3 = input_nota('qual a primeira nota da maria')
nota4 = input_nota('qual a segunda nota da maria')
nota5 = input_nota('qual a terceira nota da maria')

nota6 = input_nota('qual a primeira nota do marcos')
nota7 = input_nota('qual a segunda noto marcos')
nota8 = input_nota('qual a terceira nota do marcos')

media1 = (nota0 + nota1 + nota2) /3
media2 = (nota3 + nota4 + nota5) /3
media3 = (nota6 + nota7 + nota8) /3
if media1 >= 7:
    print('carlos passou de ano!{:2}'.format(media1))
else:
    print('carlos não passou de ano!{:.1f}'.format(media1))

if media2 >= 7:
    print('maria passou de ana!{:.1f}'.format(media2))
else:
    print('maria não passou de ano!{:.1f}'.format(media2))

if media3 >= 7:
    print('marcos passou de ana!{:.1f}'.format(media3))
else:
    print('marcos não passou de ano!{:.1f}'.format(media3))