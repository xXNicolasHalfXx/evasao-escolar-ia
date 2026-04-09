#  Predição de Evasão Escolar com Inteligência Artificial

##  Objetivo

Este projeto tem como objetivo desenvolver uma aplicação web capaz de prever a evasão de alunos utilizando técnicas de Machine Learning. A aplicação recebe dados de um aluno e retorna a probabilidade de evasão, auxiliando na identificação de possíveis riscos acadêmicos.

---

##  Dataset

Foi utilizado o dataset **dataset_alunos_evasao.csv**, contendo informações acadêmicas e socioeconômicas dos alunos, como:

* Idade
* Gênero
* Estado civil
* Tipo de escola do ensino médio
* Nota do ENEM
* Renda familiar
* Situação de trabalho
* Horas de estudo semanal
* Distância até o campus
* Entre outros

A variável alvo é:

* **status_curso**

  * `0` → Concluiu
  * `1` → Evadiu

---

## Modelo de Machine Learning

Foi utilizado o algoritmo:

* **Random Forest Classifier**

### Justificativa:

O Random Forest foi escolhido por:

* Boa performance em problemas de classificação
* Capacidade de lidar com dados categóricos
* Baixa necessidade de ajuste fino
* Robustez contra overfitting

---

## Pré-processamento

* Conversão do target (evasão) para valores numéricos
* Transformação de variáveis categóricas com **LabelEncoder**
* Separação entre variáveis independentes (X) e dependente (y)
* Divisão dos dados em treino e teste (80/20)

---

## Avaliação do Modelo

O modelo foi avaliado utilizando:

* Classification Report (Precisão, Recall, F1-score)
* Acurácia

---

## Explainable AI (SHAP)

Para interpretação do modelo, foi utilizada a biblioteca **SHAP**, permitindo:

* Identificar quais variáveis mais influenciam na evasão
* Visualizar a importância das features
* Explicar previsões individuais

---

## Aplicação Web

Foi desenvolvida uma aplicação web utilizando **Flask**, que permite:

* Inserir dados do aluno via formulário
* Processar os dados com o modelo treinado
* Retornar a previsão de evasão
* Exibir a probabilidade associada

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/xXNicolasHalfXx/evasao-escolar-ia.git
```

### 2. Acesse a pasta do projeto

```bash
cd evasao-escolar-ia
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
cd app
python app.py
```

### 5. Acesse no navegador

```
http://127.0.0.1:5000
```

---

## Como utilizar

1. Preencha os dados do aluno no formulário
2. Clique em **Prever**
3. O sistema exibirá:

   * Classificação (evasão ou não)
   * Probabilidade de evasão

---

## Estrutura do Projeto

```
evasao-escolar-ia/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── data/
│   └── dataset_alunos_evasao.csv
│
├── model/
│   ├── modelo.pkl
│   ├── encoders.pkl
│   └── columns.pkl
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Autor

Desenvolvido por **Nicolas Isaac**
Curso: Ciência da Computação

---

## Observações

* O modelo foi treinado com base no dataset fornecido na disciplina
* A aplicação tem fins acadêmicos
* O desempenho pode variar dependendo dos dados inseridos

---
