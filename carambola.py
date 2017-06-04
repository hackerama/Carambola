#/usr/bin/env python3
import subprocess
import time
import requests
import socket
import sys
import threading
import time


print('\033[1m'+'\033[33m'+"""
                           _hackerama_  '||            '||`         
                                         ||             ||          
.|'',  '''|.  '||''|  '''|.  '||),,(|,   ||''|, .|''|,  ||   '''|.  
||    .|''||   ||    .|''||   || || ||   ||  || ||  ||  ||  .|''||  
`|..' `|..||. .||.   `|..||. .||    ||. .||..|' `|..|' .||. `|..||. 
"""+'\033[36m'+'bpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpdbqpd'+'\33[1m')
print(' '*31+'v1.0')
print('\033[31m'+(' '*21)+'Fast Fingerprint Scanner'+'\033[0;0m')

def convert(x):
    if x.startswith('www.'):
        return ('http://') + x
    elif x.startswith('https://'):
        return ('http://') + x[len('https://'):]
    elif x.startswith('http://'):
        return x
    elif not x.startswith('www'):
        return ('http://www.') + x

def scan(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, porta))
    if result == 0:
        print ("Porta {}: 	 Aberta".format(porta))
    s.close()

print()
a = input('Entre com a URL: ')
a = a.lower()
print()
print(("+")+(("-")*65)+("+"))
print("|"+'\033[36m'+"dbqpdbqpdbqpdbqpdbqpdb"+ '\033[0;0m'+"[  ALGUÉM VIVO AÍ!? ]"+'\033[36m'+"qpdbqpdbqpdbqpdbqpdbqp" + '\033[0;0m'+"|")
print(("+")+(("-")*65)+("+"))
print()
try:

    r = requests.get(convert(a))
    headers = r.headers #debug
    srv = (r.headers['Server'])
    print('\033[33m'+"+| SERVER: "+'\033[0;0m', srv)
except socket.gaierror:
    print ("Que porra é essa que você digitou? Não consegui conectar")
except KeyError:
    print('\033[33m'+"+| SERVER: Não foi possível identificar o servidor."+'\033[0;0m')
except requests.exceptions.MissingSchema:
    print("Errado")
except requests.exceptions.ConnectionError:
    print ("Que porra é essa que voce digitou?")
    sys.exit(1)

try:
    r = requests.get(convert(a))
    pwr = (r.headers['X-Powered-By'])
    print('\033[33m'+'+| POWERED BY:'+'\033[0;0m', pwr)
    if pwr == ("ASP.NET"):
        aspversion =  (r.headers['X-AspNet-Version'])
        print ('\033[33m'+"+| ASP.NET VERSION:"+'\033[0;0m', aspversion)

except KeyError:
    pass



stslst = [404, '[Não Encontrado]', 200, '[0k]', 401, '[Não Autorizado]', 403, '[Proibido]']

if r.status_code in stslst:
    idx = (stslst.index(r.status_code))
    print ('\033[33m'+"+| STATUS HTTP: " + '\033[0;0m', (r.status_code),(stslst[idx+1]))
else:
    print('\033[33m'+'+| STATUS HTTP: INDEFINIDO'+'\033[0;0m')

a = convert(a)[len('http://'):]

#print("resultado de a", a)

try:
    ip = (socket.gethostbyname(a.lower()))
    print('\033[33m'+"+| IP:"+'\033[0;0m', ip)

except socket.gaierror:
    print('\033[33m'+"+| IP: não foi possível obter o IP"+'\033[0;0m')
    sys.exit(0)

try:
    dns = (socket.gethostbyaddr(a))
    print('\033[33m'+"+| DNS:"+'\033[0;0m', dns[0])
except socket.herror:
    print ('\033[33m'+"+| DNS: Não foi possível resolver o DNS"+'\033[0;0m')

print()
print(("+")+(("-")*65)+("+"))
print("|"+'\033[36m'+"dbqpdbqpdbqpdbqpdbqpb"+ '\033[0;0m'+"[  RESULTADO DO WHOIS ]"+'\033[36m'+"pdbqpdbqpdbqpdbqpdbqp" + '\033[0;0m' + "|")
print(("+")+(("-")*65)+("+"))
print()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.registro.br", 43))
s.send((a).encode())
response = b""

while True:
    data = s.recv(4096)
    response += data
    if not data:
        break
s.close()

#convert bytes to string
try:
    out = (response.decode())
    str0 = (out.find('domain', 0))
    str = (out.find('%', 339))
    print()
    sai = (out[(str0):(str)])
    if not sai:
        print("Parece que o Whois não retornou resultados...")
    else:
        print(sai)
except UnicodeDecodeError:
    print ("\nHouve um erro de unicode/decode")
#print (str)


# Limpa a tela.
subprocess.call('cls', shell=True)

print()
print(("+")+(("-")*65)+("+"))
print("|"+'\033[36m'+"dbqpdbqpd"+ '\033[0;0m'+"[ RODANDO SCANNER DE PORTAS, AGUARDE UM POUCO ]"+'\033[36m'+"qdbqpdbdb"+'\033[0;0m'+"|")
print(("+")+(("-")*65)+("+"))
print()

t1 = time.time()
try:
    for porta in range(1,1025):
        if threading.active_count() > 600:
            time.sleep(0.5)
        t = threading.Thread(target=scan, args=(porta,))
        t.setDaemon(True)
        t.start()

except KeyboardInterrupt:
    print ()
    print ("Você pressionou Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Não foi possével resolver o hostname')
    sys.exit()

except socket.error:
    print ("Nao foi possível conectar com o servidor")
    sys.exit()

t2 = time.time()
total = t2 - t1
print ('\nEscaneamento completo em %.2f segundos' % total)
