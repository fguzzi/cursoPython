def voto(a, b, c):
    from datetime import date
    from dateutil.relativedelta import relativedelta
    nascimento = date(a, b, c)
    hoje = date.today()
    idade = relativedelta(hoje, nascimento)
    id = idade.years
    if id > 70:
        print(f" Com {id} anos, o voto é opcional.")
    if 18 < id < 70:
        print(f' Com {id} anos, o voto é obrigatório.')
    if id < 18:
        print(f" Com {id} anos, você não pode votar.")



voto(a = 2008, b = 5, c = 8)





