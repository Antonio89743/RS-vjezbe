def checked_number(broj) -> str:
    clean = ""
    for char in broj:
        if char.isdigit():
            clean += char
    return clean

def validiraj_broj_telefona(broj: str):
    broj = checked_number(broj)
    pozivni_broj = None
    broj_ostatak = None
    vrsta = None
    mjesto = None
    operater = None
    validan = True
    if broj.startswith('0'):
        if broj.startswith('01'):
            pozivni_broj = broj[:2]
            broj_ostatak = broj[2:]
            validan = check_length(broj_ostatak)
            vrsta = 'Fiksna mreža'
            mjesto = get_location(pozivni_broj)
        elif broj.startswith('02'):
            if broj[2] in '0123':
                pozivni_broj = broj[:3]
                broj_ostatak = broj[3:]
                validan = check_length(broj_ostatak)
                vrsta = 'Fiksna mreža'
                mjesto = get_location(pozivni_broj)
            else:
                validan = False
        elif broj.startswith('03'):
            if broj[2] in '12345':
                pozivni_broj = broj[:3]
                broj_ostatak = broj[3:]
                validan = check_length(broj_ostatak)
                vrsta = 'Fiksna mreža'
                mjesto = get_location(pozivni_broj)
            else:
                validan = False
        elif broj.startswith('04'):
            if broj[2] in '02345789':
                pozivni_broj = broj[:3]
                broj_ostatak = broj[3:]
                validan = check_length(broj_ostatak)
                vrsta = 'Fiksna mreža'
                mjesto = get_location(pozivni_broj)
            else:
                validan = False
        elif broj.startswith('05'):
            if broj[2] in '123':
                pozivni_broj = broj[:3]
                broj_ostatak = broj[3:]
                validan = check_length(broj_ostatak)
                vrsta = 'Fiksna mreža'
                mjesto = get_location(pozivni_broj)
            else:
                validan = False
        elif broj.startswith('06'):
            if broj[2] in '01459':
                pozivni_broj = broj[:3]
                broj_ostatak = broj[3:]
                validan = check_length(broj_ostatak, '6')
                vrsta = 'Posebne usluge'
            else:
                validan = False
        elif broj.startswith('072'):
            pozivni_broj = broj[:3]
            broj_ostatak = broj[3:]
            validan = check_length(broj_ostatak, '6')
            vrsta = 'Posebne usluge'

        elif broj.startswith('0800'):
            pozivni_broj = broj[:4]
            broj_ostatak = broj[4:]
            validan = check_length(broj_ostatak)
            vrsta = 'Posebne usluge'

        elif broj.startswith('09'):
            if broj[2] in '125789':
                pozivni_broj = broj[:3]
                broj_ostatak = broj[3:]
                validan = check_length(broj_ostatak)
                vrsta = 'Mobilna mreža'
                operater = get_operator(pozivni_broj)
            else:
                validan = False

        else:
            validan = False
    else:
        validan = False

    return {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": broj_ostatak,
        "vrsta": vrsta,
        "mjesto": mjesto,
        "operater": operater,
        "validan": validan,
    }

def check_length(broj: str, expected_length: str = '67') -> bool:
    return str(len(broj)) in expected_length

def get_operator(pozivni_broj: str) -> str:
    match pozivni_broj:
        case '091':
            return 'A1 Hrvatska'
        case '092':
            return 'Tomato'
        case '095':
            return 'Telemach'
        case '097':
            return 'bonbon'
        case '098' | '099':
            return 'Hrvatski Telekom'
        case _:
            return 'Nepoznato - Invalid'

def get_location(pozivni_broj: str) -> str:
    match pozivni_broj:
        case '01':
            return 'Grad Zagreb i Zagrebačka županija'
        case '020':
            return 'Dubrovačko-neretvanska županija'
        case '021':
            return 'Splitsko-dalmatinska županija'
        case '022':
            return 'Šibensko-kninska županija'
        case '023':
            return 'Zadarska županija'
        case '031':
            return 'Osječko-baranjska županija'
        case '032':
            return 'Vukovarsko-srijemska županija'
        case '033':
            return 'Virovitičko-podravska županija'
        case '034':
            return 'Požeško-slavonska županija'
        case '035':
            return 'Brodsko-posavska županija'
        case '040':
            return 'Međimurska županija'
        case '042':
            return 'Varaždinska županija'
        case '043':
            return 'Bjelovarsko-bilogorska županija'
        case '044':
            return 'Sisačko-moslavačka županija'
        case '047':
            return 'Karlovačka županija'
        case '048':
            return 'Koprivničko-križevačka županija'
        case '049':
            return 'Krapinsko-zagorska županija'
        case '051':
            return 'Primorsko-goranska županija'
        case '052':
            return 'Istarska županija'
        case '053':
            return 'Ličko-senjska županija'
        case _:
            return 'Nepoznato - Invalid'
