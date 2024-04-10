# Projeto: Portfólio para Jornalista
Trabalho feito para a disciplina Algoritmos de Automação do Master em Jornalismo de Dados, Automação e Data Storytelling, do Insper. Professor: Álvaro Justen 

# Objetivo
O projeto pretende reunir em um único site informações importantes sobre uma jornalista para facilitar o networking. O site possui uma página de apresentação com nome, idade, foto e um breve resumo profissional. Em outra página, é possível encontrar as matérias mais recentes que a jornalista publicou. Ao carregar a página, sempre vão aparecer as matérias mais recentes publicadas pela jornalista. Na página de contato, além dos dados, tem uma caixa de mensagem onde o usuário pode enviar uma mensagem diretamente para a jornalista. O texto escrito na caixa vai direto para o endereço da jornalista, junto com o nome e e-mail do usuário que está enviando. 

Todas as páginas possuem um menu que liga os endereços: Apresentação | Portfólio | Contato


## app.py

#### Bibliotecas

requests > para fazer a requisição

bs4 > extrair os dados html

flask > desenvolver o site

smtplib > envio de e-mails com SMTP

email.mime.multipart + email.mime.text > contruir o e-mail

os + dotenv > acessar as variáveis de ambiente 


#### Variável de ambiente 
Utilizei o arquivo .env e a aba de variável de ambiente do Render para armazenar as senhas e dados sensíveis do código: 

key_servidor 

key_remetente

key_email




### Página - apresentacao.html
Esta função retorna o template inicial do site da jornalista, com nome, idade, foto e um resumo profissional. Usei o CSS para centralizar o conteúdo do site, ajustar a foto e fonte das letras, mudar as cores das letras. 

### Página - materias.html
Neste função, eu apliquei o código que raspa as últimas matérias publicadas pela jornalista no site que ela trabalha (https://www.jota.info/autor/melissa-duartejota-info). A função extrai o link e o título das matérias e adiciona em uma lista. Essa lista é o resultado mostrado ao carregar a página do site. Ao clicar em cada item, o usuário é direcionado para a publicação original. 

### Página - contato.html
Para esta página, eu criei duas funções: a primeira é para a página estática, quando o usuário acessa (/contato). 
A segunda função (/enviar_contato) tem o objetivo de receber por e-mail a mensagem enviada pelo usuário na caixa de contato e enviar para o usuário uma resposta automática como confirmação de que a mensagem foi enviada para a jornalista. 
Usei o provedor BREVO nesta etapa.

No fim do código, utilizei o recurso - except Exception as e: - para capturar possíveis mensagens de erro e facilitar a identificação do problema. 
