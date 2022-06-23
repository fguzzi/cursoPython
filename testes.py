from datetime import date
from dateutil.relativedelta import relativedelta

nascimento = date(1997, 6, 1)
hoje = date.today()
idade = relativedelta(hoje, nascimento)




















