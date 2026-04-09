from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# carregar modelo e arquivos
model = joblib.load("../model/modelo.pkl")
encoders = joblib.load("../model/encoders.pkl")
columns = joblib.load("../model/columns.pkl")


# rota inicial
@app.route("/")
def home():
    return render_template("index.html")


#  rota predict
@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()

    df = pd.DataFrame([data])

    # converter valores numéricos
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    # aplicar encoders
    for col in df.columns:
        if col in encoders:
            try:
                df[col] = encoders[col].transform(df[col])
            except:
                return render_template(
                    "index.html",
                    resultado=f"Valor inválido para {col}"
                )

    # garantir todas as colunas
    for col in columns:
        if col not in df:
            df[col] = 0

    # garantir ordem correta
    df = df[columns]

    # previsão
    try:
        prediction = model.predict(df)[0]
        prob = model.predict_proba(df)[0]
    except Exception as e:
        return render_template("index.html", resultado=f"Erro: {e}")

    if prediction == 1:
        resultado = "Aluno com risco de evasão"
    else:
        resultado = "Aluno sem risco de evasão"

    resultado += f" (Probabilidade: {prob[1]:.2f})"

    return render_template("index.html", resultado=resultado)


# rodar servidor
if __name__ == "__main__":
    app.run(debug=True)