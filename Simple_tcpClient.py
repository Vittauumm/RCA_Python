from socket import *
import random

def generate_prime(bits): #Gera um numero primo com a quantidade de bits fornecida
    while True:
        number = random.getrandbits(bits)
        if miller_rabin_test(number):
            return number
        
def miller_rabin_test(n, k=40): #Verifica se o numero é primo através do teste de miller rabin
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def mod(a, m): #Calcula o modulo
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def gcd(a, b): #Calcula o maximo divisor comum
    while b:
        a, b = b, a % b
    return a

def generate_e(phi): #Gera um número e aleatório
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    return e

def generate_keys(bits): #Calcula as chaves a partir de P e Q gerados
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_e(phi)
    d = mod(e, phi)
    return ((n, e), (n, d))

def encrypt(public_key, text): #Criptografa
    n, e = public_key
    text = int.from_bytes(text.encode('utf-8'), byteorder='big')
    encrypted_text = pow(text, e, n)
    return encrypted_text

def decrypt(private_key, encrypted_text): #Decriptografa
    n, d = private_key
    text = pow(encrypted_text, d, n)
    text = text.to_bytes((text.bit_length() + 7) // 8, byteorder='big')
    return text.decode('utf-8')

message = "The information security is of significant importance to ensure the privacy of communications"

client_public_key, client_private_key = generate_keys(4096) 

serverPort = 1300
serverName = "192.168.1.20"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

server_response = clientSocket.recv(4096).decode()
server_n, server_e = map(int, server_response.split(','))
server_public_key = (server_n, server_e)

clientSocket.send(f"{client_public_key[0]},{client_public_key[1]}".encode()) #Envia a chave publica para o server

encrypted_text = encrypt(server_public_key, message)
clientSocket.send(str(encrypted_text).encode())
print("Enviado ao Servidor Criptogrado: ", encrypted_text)

serverResponse = clientSocket.recv(4096)
encrypted_response = int(serverResponse.decode())
print("Recebida do Servidor Criptogrado: ", encrypted_response)
response = decrypt(client_private_key, encrypted_response)
print("Recebida do Servidor Descriptografado: ", response)

clientSocket.close()