import joblib
import os

# Caminho absoluto para os modelos (ajuste para seu diretório correto)
diretorio_modelos = os.path.dirname(os.path.abspath(__file__))  # Pega o diretório atual

# Carregar os modelos treinados e o label encoder
pipeline_lr = joblib.load(os.path.join(diretorio_modelos, 'assistente_logistic_regression_model.pkl'))
pipeline_svm = joblib.load(os.path.join(diretorio_modelos, 'assistente_svm_model.pkl'))
label_encoder = joblib.load(os.path.join(diretorio_modelos, 'label_encoder.pkl'))

# Função para prever a intenção do comando
def prever_intencao(frase, modelo='svm'):
    if modelo == 'svm':
        model = pipeline_svm
    elif modelo == 'lr':
        model = pipeline_lr
    else:
        print("Modelo não reconhecido")
        return None

    # Prever a intenção
    pred = model.predict([frase])
    intencao = label_encoder.inverse_transform(pred)
    return intencao[0]

# Testar a previsão

while True:
    frase_teste = input("Digite a frase: ")
    intencao_prevista = prever_intencao(frase_teste, modelo='lr')
    print(f"Intenção prevista: {intencao_prevista}")
