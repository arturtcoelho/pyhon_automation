import datetime
import traceback

from scraping import get_pratos
from send_email import send_email_with_attach
from sheets import update_data_to_sheets

if __name__ == '__main__':
    try:
        pratos = get_pratos()
        update_data_to_sheets(data={'values': pratos}, cust_space='!A:C')

        p_fmt = '\n'.join([': '.join(p) for p in pratos])
        with open(f'cardapio_{datetime.date.today()}.txt', 'w') as f:
            f.write(p_fmt)

        send_email_with_attach('artur.temporal@hotmail.com', f'Cardapio do RU de hoje {datetime.date.today()}', p_fmt)
    except:
        traceback.print_exc()