def metade(n,format=True):
    if format:
        return(f'R${n/2:.2f}')
    return n/2


def dobro(n,format=True):
    if format:
        return(f'R${n*2:.2f}')
    return n*2


def aumentar(n,p,format=True):
    if format:
        return(f'R${n+(n*p/100):.2f}')
    return n+(n*p/100)


def diminuir(n,p,format=True):
    if format:
        return(f'R${n-(n*p/100):.2f}')
    return n-(n*p/100)


def moeda(n):
    return (f'R${n:.2f}')
