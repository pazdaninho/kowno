def cidr_to_bin(bits):
    end = 32 - bits
    mesut = str(bits * '1')+str(end * '0')
    l=[]
    for num, bit in enumerate(mesut):
        l.append(bit)
        if (num+1) %8 == 0:
            l.append('.')
    return ''.join(l).strip('.')

def add_to_bin(add):
    add = add.split('.');l=[]
    add = [f"{bin(int(ad))[2:]}" for ad in add]
    for ad in add:
        rest = 8; rest -= len(ad)
        true_address = rest * '0' + ad
        l.append(true_address)
            
    return '.'.join(l)

# adres sieci
def funcand_bojl(ab, mb):
    l = []
    for s1, s2 in zip(ab,mb):
        try:
            if int(s1)+ int(s2) == 2:
                l.append('1')
            else: l.append('0')
        except ValueError:
            l.append('.')
    return ''.join(l)

# code from https://www.simplifiedpython.net/python-binary-to-decimal/
def binToDec(binNum):
    decNum = 0
    power = 0
    while binNum>0:
        decNum += 2 **power* (binNum%10)
        binNum //=10
        power += 1
    return decNum

def get_broadcast(ab, mb):
    ones = 32 - int(mb); l = []
    address_mask = f'{mb*"0"}{ones*"1"}'
    address_ip = ''.join(ab.split('.'))
    lim = address_mask.count('0')
    raw_address = address_ip[:lim]+address_mask[lim:]
    dotted_address = []
    for i, let in enumerate(raw_address):
        dotted_address.append(let)
        if (i+1) % 8 == 0:
            dotted_address.append('.')
    
    dotted_address = ''.join(dotted_address).strip('.')
    return dotted_address
def fill_zeros(val):
    value = bin(int(val))[2:]
    lenglet = 8 - len(value)
    return str('0'*lenglet)+str(value)

#andres ip; maska
def display(aip, cidr):
    # andress bit notation
    ab = add_bits = add_to_bin(aip)
    print(f'{"adres ip":20} : {aip:20} | {ab}')
    # mask bit notation
    mb = cidr_to_bin(cidr)
    print(f'{"maska podsieci":20} : {"/"+str(cidr):20} | {mb}')
    # andress network binarly
    nab = funcand_bojl(ab, mb)
    # andress network decimaly
    nad = '.'.join([str(binToDec(int(bin))) for bin in nab.split('.')])
    print(f'{"adres sieci":20} : {nad:20} | {nab}')
    # broadcast andress binarly
    bab = get_broadcast(ab, cidr)
    # broadcast andress decimaly
    bad = '.'.join([str(binToDec(int(bit))) for bit in bab.split('.')])
    print(f'adres rozgłoszeniowy : {bad:20} | {bab}')
    print(f'ilość hostów w sieci : {(2 ** ( 32 - cidr ))}')
    fh = nad[:-1]+str(int(nad[-1])+1)
    first_host_bin = '.'.join([fill_zeros(val) for val in fh.split('.')])
    print(f'pierwszy host w sieci: {fh:20} | {first_host_bin}')
    lh = bad[:-1]+str(int(bad[-1])-1)
    last_host_bin = '.'.join([fill_zeros(val) for val in lh.split('.')])
    print(f'ostatni host w sieci : {lh:20} | {last_host_bin}')

display('192.168.0.105', 21)