from flask import Flask, render_template, request

app = Flask(__name__)

qa_database = [
    ("1", "Pode parecer um pouco estranho, mas não se preocupe, estou aqui para te ajudar no processo! 😊<br><br> Para conseguir acesso ao seu email e às plataformas, é simples: <br><br> ➡ Ligue para o número <b>+55 11 5189-7346</b> <br> ➡ Durante a chamada, basta confirmar sua solicitação (sugerimos dizer <b>'I need to reset my email/SSO password'</b> e soletrar o seu e-mail ao atendente) e, se você não se sentir à vontade em falar em inglês, não tem problema - você pode pedir ajuda à Geize. Ela está aqui para te apoiar! 🤝<br> ➡ Quando questionado, informe seu nome, email e o nome do <b>Hiring Manager - Alexandre Maioral</b>.<br> ➡ Por fim, você receberá um email com a senha temporária que, por questões de segurança, você deve alterar. <br><br>  <b>Observação: </b>Se a ligação estiver demorando muito, considere tentar durante a noite, pois o fluxo de ligações costuma ser menor. 🌙"),
    ("2", "Para garantir o seu laptop corporativo, você receberá um e-mail do <b>Persio Junior</b>, do <b>IT Support</b>, informando que o equipamento está pronto para entrega. Se você estiver trabalhando na sede em São Paulo, poderá retirá-lo facilmente no 1º andar do escritório. Caso esteja em outro estado, o laptop será enviado diretamente para o seu endereço. 😊👨‍💻📦"),
    ("3", "💻 Para conectar a VPN pelo <b>computador</b>, siga os seguintes passos:<br><br> ➡ Acesse o link a seguir <a href='https://vsupport.oracle.com/application-vsupport-context-root/?root=downloads'>Cisco VPN</a> <br> ➡ Faça download do Cisco AnyConnect Secure Mobility Client (VPN) de acordo com seu sistema de operação <br> ➡ Execute o arquivo para instalar <br><br>📱 Para acessar a VPN pelo <b>celular</b>, acesse os links abaixo:<br> <a href='https://myhelp.oracle.com/app/answers/answer_view/a_id/1009267'>Android</a> <br> <a href='https://myhelp.oracle.com/app/answers/answer_view/a_id/1003689'>Iphone/Ipad</a>"),
    ("4", "Sim e não! Não é um pré-requisito começar o programa já falando espanhol. No entanto, como trabalhamos com colegas e projetos em toda a América Latina, é provável que você tenha algum contato com o idioma em reuniões, dinâmicas e rotações. A dica aqui é começar a se familiarizar com o idioma, se arriscar na prática e, claro, dedicar um tempinho para estudar! Lembre-se, a fluência não acontece da noite para o dia. O aprendizado leva tempo, paciência e dedicação. 🌎📚"),
    ("5", "Sim e não! Também não é pré-requisito iniciar o programa sabendo falar inglês, mas é comum ouvir expressões estrangeiras e passar por situações na rotina de trabalho que podem exigir a compreensão do idioma. E, não se preocupe, pois a Oracle oferece cursos de inglês para seus colaboradores que, com certeza, vão te ajudar na sua jornada! Aqui, a gente te prepara pra tudo! 💬👨‍🏫"),
    ("6", "Para solicitar o seu crachá, siga os seguintes passos: <br><br> ➡ Acesse <a href='https://badge.oraclecorp.com/'>https://badge.oraclecorp.com/</a> (é necessário VPN) <br> ➡ Clique em <b>Request Card</b> <br> ➡ Preencha as informações solicitadas (Não coloque data de desativação) <br> ➡ Em Envio do cartão, deixe o local de retirada do cartão em <b>São Paulo</b> e clique em Terminar.<br> ➡ Para validar o crachá, siga o tutorial no <a href='https://otube.oracle.com/media/EmployeeA+Activate+your+new+Oracle+badge/1_97xbxsvp/273870812'>Otube</a> <br><br> Em alguns casos, é preciso também solicitar acesso. Para isso, siga os seguintes passos:<br> ➡ Acesse <a href='https://badge.oraclecorp.com/'>https://badge.oraclecorp.com/</a> (é necessário VPN) <br> ➡ Clique em Solicitar acesso <br> ➡ Preencha as informações solicitadas (Em Área, selecione <b>SAO PAULO BRA [CAMPUS] - GENERAL ACCESS 24HR</b>) <br> ➡ Clique em Salvar <br> ➡ Por fim, você receberá um email aprovando seu pedido"),
    ("7", "Tudo bem, meu caro GenO! Eu preparei um <a href='https://oradocs.oracle.com/documents/link/LD141817F98E3A41D8A5D76BA5A96B76E72BEE306DB7/fileview/D1C7A1C72972C06A746B16067FCD05A5C449AE8A85AD/_Glossário_Oracle_(1).pdf'>Glossário</a> com as principais expressões que utilizamos para te ajudar. Espero que isso possa te guiar durante a sua jornada! 😊📖🚀"),
    ("8", "Tá querendo estudar, né? Gostei de você! Para conquistar as certificações de que precisa, acesse o link do <a href='https://mylearn.oracle.com/ou/home'>Oracle My Learn</a>. Espero ter ajudado na sua jornada de conhecimento! 😉📚🚀"),
    ("9", "Que bacana, o cordão de diversidade é realmente incrível! Eu consegui o meu com a ajuda do Lucas do RH, que fica no 5º andar. Não tenho certeza se ainda está disponível, mas vale a pena tentar. 😊🌈"),
    ("10", "Eu também estava ansioso para este cartão! 😃 Depois dele, minha pausa para o café nunca mais foi a mesma! O time de <b>Facilities</b> enviará um e-mail para você retirar o seu cartão. Aqui estão algumas informações úteis sobre o cartão:<br><br> - O cartão é recarregado automaticamente com 900 créditos mensais (não cumulativos) todo dia 1º do mês;<br> - Você pode retirar até 5 itens por dia;<br> - Se por acaso o produto que você escolher ficar preso na máquina, o valor do crédito será automaticamente estornado para o seu cartão (você não perderá os créditos).<br><br>Aproveite ao máximo sua pausa e desfrute das suas opções! 😊🍪🥤")
]

@app.route("/")
def index():
    welcome_message = "Bem-vindo ao ChatBot! Faça suas perguntas."
    return render_template('chat.html', welcome_message=welcome_message)

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_Chat_response(msg)
    return response

def get_Chat_response(text):
    for question, answer in qa_database:
        if question.lower() == text.lower():
            return answer
    return "Desculpe, não tenho uma resposta para essa pergunta."

if __name__ == '__main__':
    app.run()