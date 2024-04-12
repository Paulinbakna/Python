import urllib.request

def verifica_site_acessivel(url):
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.URLError:
        return False

if verifica_site_acessivel("https://www.pudim.com.br/"):
    print("O site Pudim está acessível!")
else:
    print("Não foi possível acessar o site Pudim.")

