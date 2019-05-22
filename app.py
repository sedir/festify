from os import environ

from flask import Flask, render_template, session, redirect, request
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy
import lineupify
import base64

app = Flask(__name__)

app.secret_key = b'abF0bhedwig03#45cv'
scope = 'user-top-read'


@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/login")
def login():
    # Obtém as credenciais da aplicação cliente (cadastrada no dashboard do Spotify Developers)
    cred = SpotifyClientCredentials()

    # Obtém o objeto de autenticação OAuth2
    url = SpotifyOAuth(cred.client_id,
                       cred.client_secret,
                       environ['SPOTIPY_REDIRECT_URI'],
                       scope=scope)

    # Obtém a URL de autorização do Spotify e redireciona o usuário para esta
    return redirect(url.get_authorize_url())


@app.route("/logout")
def logout():
    # Limpa a sessão do usuário
    session.clear()
    return redirect('/')


@app.route("/callback/")
def callback():
    # Grava o código acesso retornado pelo Spotify na sessão do usuário
    session['spotify_code'] = request.args['code']
    # Redirectiona o usuário para a página principal
    return redirect('/')


@app.route("/festify")
def festify():
    # Obtém as credenciais da aplicação cliente (cadastrada no dashboard do Spotify Developers)
    cred = SpotifyClientCredentials()

    # Obtém o objeto de autenticação OAuth2
    oauth = SpotifyOAuth(cred.client_id,
                         cred.client_secret,
                         environ['SPOTIPY_REDIRECT_URI'],
                         scope=scope)

    # Obtém o token de acesso
    token_info = oauth.get_access_token(session['spotify_code'])

    # Obtém os artistas do usuário
    spotify = spotipy.Spotify(auth=token_info['access_token'])

    # Obtém os artistas do usuário
    artistas = spotify.current_user_top_artists(time_range='long_term')

    # Extrai os nomes das bandas/artistas
    nomes_bandas = []
    for artista in artistas['items']:
        nomes_bandas.append(artista['name'])

    print(nomes_bandas)

    # Cria o poster, resultando numa imagem PNG em bytes
    img_bytes = lineupify.make_lineup("Sedir Open Air",
                                      "A festa para entrar na sua vibe.",
                                      bands=nomes_bandas).read()

    # Codifica os bytes em base64
    img_url = base64.b64encode(img_bytes).decode('utf-8')

    # Envia os bytes para a variavel imagem no template
    return render_template("festify.html", imagem=img_url)
