from flask import Flask, render_template, request

app = Flask(__name__)

qa_database = [
    ("1", "Parece estranho, mas confia no processo! <br><br> Para conseguir acesso ao seu email e às plataformas da Oracle, é necessário: Ligar para o número +55 11 5189-7346 <br> Durante a chamada, confirme sua solicitação (minha sugestão é falar I need to reset my email/SSO password) <br> Quando perguntado, informar, em inglês, seu nome, email Oracle e o nome do Hiring Manager - Alexandre Maioral. <br> Por fim, você receberá um email com a senha temporária que, por segurança, você deve alterar."),
    ("2", "4."),
    ("2", "4."),
    ("2", "4."),
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
        if question.lower() in text.lower():
            return answer
    return "Desculpe, não tenho uma resposta para essa pergunta."

if __name__ == '__main__':
    app.run()