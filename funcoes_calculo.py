def root_number(a):
    return a**0.5


def equa_2(a, b, c):

    delta = b**2-4*a*c
    if delta < 0:
        print("delta menor que zero raizes inexistentes, nesse caso por não utilizarmos números imaginários nesse exemplo")
        return 0
    if delta == 0:
        print("delta igual a zero raizes reais e iguais")
        return round((-b+(root_number(delta)))/(2*a), 2), round((-b-(root_number(delta)))/(2*a), 2)
    if delta > 0:
        print("delta maior que zero raizes reais e diferentes")
        return round((-b+(root_number(delta)))/(2*a), 2), round((-b-(root_number(delta)))/(2*a), 2)
