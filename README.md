# Exemplo de Comunicação RSA em Python sem bibliotecas externas

## Índice
- [Visão Geral](#visão-geral)
- [Arquivos Incluídos](#arquivos-incluídos)
- [Como Executar](#como-executar)
  - [Executando o Servidor](#executando-o-servidor)
  - [Executando o Cliente](#executando-o-cliente)
- [Como Funciona](#como-funciona)
- [Licença](#licença)

## Visão Geral
Este projeto implementa uma comunicação segura entre um servidor e um cliente usando criptografia RSA com chaves de 4096 bits. A comunicação é estabelecida através de sockets, e tanto o servidor quanto o cliente geram seus próprios pares de chaves RSA, trocam chaves públicas e utilizam essas chaves para criptografar e descriptografar a mensagem trocadas entre eles.

## Arquivos Incluídos

- **Simple_tcpServer.py**: Script que implementa o servidor TCP.
- **Simple_tcpClient.py**: Script que implementa o cliente TCP.

## Como Executar
**Importante:** Recomendado executar primeiro o `Simple_tcpServer.py` até que a mensagem TCP Server seja exibida

### Executando o Servidor
 1. Abra um terminal e navegue até o diretório onde o arquivo `Simple_tcpServer.py` está localizado.
 2. Execute o servidor com o comando:
     ```bash
     python Simple_tcpServer.py
     ```
 3. O servidor irá gerar suas chaves RSA e ficará aguardando uma conexão do cliente.

### Executando o Cliente
1. Abra um segundo terminal e navegue até o diretório onde o arquivo `Simple_tcpClient.py` está localizado.
2. Execute o cliente com o comando:
     ```bash
     python Simple_tcpClient.py
     ```
3. O cliente irá gerar suas chaves RSA, conectar-se ao servidor, trocar chaves públicas, e enviar uma mensagem criptografada.

## Como Funciona

1. **Geração de Chaves:**
   - Tanto o servidor quanto o cliente geram pares de chaves RSA de 4096 bits (pública e privada) usando a função `generate_keypair`, com números primos testados atráves do `miller_rabin_test`.

2. **Troca de Chaves Públicas:**
   - O servidor envia sua chave pública para o cliente, e o cliente envia sua chave pública de volta para o servidor.

3. **Criptografia e Descriptografia:**
   - O cliente criptografa a mensagem “The information security is of significant importance to ensure the privacy of communications” usando a chave pública do servidor e envia a mensagem criptografada para o servidor.
   - O servidor descriptografa a mensagem recebida usando sua chave privada.
   - O servidor envia uma resposta de confirmação criptografada com a chave pública do cliente. O cliente descriptografa a resposta usando sua chave privada.

4. **Segurança:**
   - A criptografia RSA garante que apenas o destinatário com a chave privada correspondente possa descriptografar as mensagens, assegurando a privacidade e a integridade da comunicação.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE). Você é livre para usar, modificar e distribuir este software, desde que mantenha a atribuição ao autor original.
