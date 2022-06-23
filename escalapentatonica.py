do = ['Cb', 'C', 'C#', 'Cm' ]
re = ['Db', 'D', 'D#' 'Dm']
mi = ['Eb', 'E', 'E#', 'Em']
fa = ['Fb', 'F', 'F#', 'Fm']
sol = ['Gb', 'G', 'G#','Gm']
la = ['Ab', 'A', 'A#', 'Am']
si = ['Bb', 'B', 'B#', 'Bm']
while True:
    print('''   QUAL TIPO DE ESCALA PENTATÔNICA DESEJA ?
                     [ 1 ] - Menor 7
                     [ 2 ] - Maior''')
    resp = int(input('Digite sua escolha: '))
    if resp > 2 or resp < 1:
        print('Opção incorreta. Tente novamente.')
    else:
        if resp == 1:
            print('''Qual a tonalidade da escala: [C D E F G A B]''')
            esc = str(input('Digite sua escolha: ')).strip().upper()
            if esc == 'C':
                print(f' {do[1]} {mi[0]} {fa[1]} {sol[1]} {si[0]}')
            if esc == 'D':
                print(f' {re[1]} {fa[1]} {sol[1]} {la[1]} {do[1]}')
            if esc == 'E':
                print(f' {mi[1]} {sol[1]} {la[1]} {si[1]} {re[1]}')
            if esc == 'F':
                print(f' {fa[1]} {la[0]} {si[0]} {do[1]} {mi[0]}')
            if esc == 'G':
                print(f' {sol[1]} {si[0]} {do[1]} {re[1]} {fa[1]}')
            if esc == 'A':
                print(f' {la[1]} {do[1]} {re[1]} {mi[1]} {sol[1]}')
            if esc == 'B':
                print(f' {si[1]} {re[1]} {mi[1]} {fa[2]} {la[1]}')
            else:
                print('Opção incorreta. Tente novamente.')
        elif resp == 2:
            print('''Qual a tonalidade da escala: [C D E F G A B]''')
            esc = str(input('Digite sua escolha: ')).strip().upper()
            if esc == 'C':
                print(f' {do[1]} {re[1]} {mi[1]} {fa[1]} {la[1]}')
            if esc == 'D':
                print(f' {re[1]} {mi[1]} {fa[2]} {sol[1]} {si[1]}')
            if esc == 'E':
                print(f' {mi[1]} {fa[2]} {sol[2]} {si[1]} {do[2]}')
            if esc == 'F':
                print(f' {fa[1]} {sol[1]} {la[1]} {do[1]} {re[1]}')
            if esc == 'G':
                print(f' {sol[1]} {la[1]} {si[1]} {re[1]} {mi[1]}')
            if esc == 'A':
                print(f' {la[1]} {si[1]} {do[2]} {mi[1]} {fa[1]}')
            if esc == 'B':
                print(f' {si[1]} {do[2]} {re[2]} {fa[2]} {sol[2]}')
            else:
                print('Opção incorreta. Tente novamente.')
        else:
            print('Opção incorreta. Tente novamente.')
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()
    if 'N' in op:
        print('Programa encerrado.')
        break