import os
import urllib.request
import ssl

#LISTA DE PROXYS
file = open("proxies.txt", "r").read()
proxys = file.split("\n")

def test_proxy(proxy):
    url = 'https://google.com'  # URL de teste, você pode alterar para um site de sua escolha

    proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl.create_default_context()))
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    try:
        response = opener.open(url, timeout=3)
        if response.getcode() == 200:
            print(f"Proxy {proxy} está funcionando corretamente")
            #os.system(f"echo {proxy} >> proxys_funcionando.txt")
        else:
            print(f"Proxy {proxy} retornou uma resposta inválida")
    except urllib.error.URLError as e:
        print(f"Erro ao conectar-se ao proxy {proxy}: {e.reason}")

# Lista de proxies para testar
for proxy in proxys:
    try:
        test_proxy(proxy)
    except:
        print("Erro ao conectar-se ao proxy {proxy}: Proxy inativo")
