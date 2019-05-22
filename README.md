# Festify

Esse é o código da aplicação Festify criado na aula de Python para a escolinha de programação do LAIS.

## Instalação de dependências

Execute no terminal, no ambiente virtual Python:

```
pip install -r requirements.txt
```

## Variáveis de ambiente

Defina as seguintes variáveis de ambiente criando o arquivo `.env` na raíz do projeto, trocando os valores de `SPOTIPY_CLIENT_ID` e `SPOTIPY_CLIENT_SECRET`:

```
FLASK_APP=app.py
FLASK_DEBUG=True
SPOTIPY_CLIENT_ID=SEU_SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET=SEU_SPOTIPY_CLIENT_ID
SPOTIPY_REDIRECT_URI='http://localhost:5000/callback/'
```

## Executando a aplicação

Ainda no terminal, execute o comando:

```
flask run
```
