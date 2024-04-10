import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
key_servidor=os.environ.get("KEY_SERVIDOR")
key_remetente=os.environ.get("KEY_REMETENTE")
key_email=os.environ.get("KEY_EMAIL")


@app.route("/apresentacao")
def apresentacao():
    return render_template("apresentacao.html")

#Raspar as matérias publicadas mais recentes
@app.route("/materias")
def materias():
    req_jota_melissa=requests.get("https://www.jota.info/autor/melissa-duartejota-info")
    conteudo_jota_melissa=req_jota_melissa.content
    html_jota_melissa=BeautifulSoup(conteudo_jota_melissa)
    noticias=html_jota_melissa.findAll('div',{'class':'jota-posts-list__body'})

    materias_melissa=[]
    for noticia in noticias:
        titulo=noticia.find('h3').text.strip()
        link=noticia.find('a').get('href')        
        materias_melissa.append({"titulo": titulo, "link": link})
    print(materias_melissa)    
    return render_template("materias.html" , materias=materias_melissa)

@app.route("/contato")
def contato():
    enviado = False
    return render_template("contato.html")

@app.route("/enviar_contato" , methods=["POST" , "GET"])
def enviar_contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]
        
    
        #Conectar no servidor SMTP:
        smtp_server = key_servidor
        port = 587
        email_remetente = key_remetente
        password = key_email
        
        #Receber a msg do formulário por e-mail + resposta automática
        try:
        
            msg = MIMEText(f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}")
            msg['Subject'] = "Contato do site"
            msg['From'] = email_remetente
            msg['To'] = "alvarojusten@gmail.com , nicole.lacerda05@gmail.com"
            
    
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(email_remetente, password)
            server.sendmail(email_remetente, msg['To'].split(" , "), msg.as_string())
            server.quit()
            enviado = True
        
            return "Obrigada por entrar em contato comigo!"
        except Exception as e:
            return f"Erro ao enviar mensagem: {e}"

if __name__ == '__main__':
    app.run(port=5000, debug=True) 