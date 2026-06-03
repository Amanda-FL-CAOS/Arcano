from flask import Flask, render_template, request

app = Flask(__name__)


arcanos = {
    0: "O Louco",
    1: "O Mago",
    2: "A Sacerdotisa",
    3: "A Imperatriz",
    4: "O Imperador",
    5: "O Hierofante",
    6: "Os Enamorados",
    7: "O Carro",
    8: "A Justiça",
    9: "O Eremita",
    10: "A Roda da Fortuna",
    11: "A Força",
    12: "O Enforcado",
    13: "A Morte",
    14: "A Temperança",
    15: "O Diabo",
    16: "A Torre",
    17: "A Estrela",
    18: "A Lua",
    19: "O Sol",
    20: "O Julgamento",
    21: "O Mundo"
}

@app.route("/", methods=["GET", "POST"])
def home():

    resultado = None


    if request.method == "POST":


        data = request.form["birthdate"]


        numeros = []

        for caractere in data:

            if caractere.isdigit():
                numeros.append(int(caractere))


        soma = sum(numeros)


        soma_reduzida = soma

        while soma_reduzida >= 10:

            soma_reduzida = sum(
                int(numero)
                for numero in str(soma_reduzida)
            )

        resultado = {
            "soma": soma,
            "arcano_principal": arcanos.get(soma, "Não encontrado"),
            "arcano_reduzido": arcanos.get(soma_reduzida, "Não encontrado"),
            "numero_reduzido": soma_reduzida
        }

    return render_template(
        "index.html",
        resultado=resultado
    )

app.run(debug=True)