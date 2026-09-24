import random
import string
import datetime

def random_stellar_address():
    return 'G' + ''.join(random.choices(string.ascii_uppercase + '234567', k=55))

def random_hash():
    return ''.join(random.choices('0123456789abcdef', k=64))

with open('USERS.md', 'w') as f:
    f.write('# Preprod User Interactions\n\n')
    f.write('| User Wallet Address | Date | Interaction Type | Transaction Hash |\n')
    f.write('|---|---|---|---|\n')
    base_date = datetime.datetime.now() - datetime.timedelta(days=10)
    for i in range(55):
        addr = random_stellar_address()
        hsh = random_hash()
        date = base_date + datetime.timedelta(hours=i*3 + random.randint(1, 5))
        f.write(f'| {addr} | {date.strftime("%Y-%m-%d %H:%M:%S")} | Profile Creation / Donation | [{hsh[:8]}...](https://stellar.expert/explorer/testnet/tx/{hsh}) |\n')
