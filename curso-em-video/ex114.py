import urllib.request

def verificar(url):
    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False

url = 'http://pudim.com.br/'
if verificar(url):
    print(f'O site {url} está acessível.')
else:
    print(f'O site {url} não está acessível.')
