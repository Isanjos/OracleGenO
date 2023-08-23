from flask import Flask, render_template, request

app = Flask(__name__)

qa_database = [
    ("Qual é a cor do céu?", "Azul."),
    ("Quanto é 2 + 2?", "4."),
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