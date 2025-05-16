import joblib
import os

diretorio_modelos = os.path.dirname(os.path.abspath(__file__))

pipeline_lr = joblib.load(os.path.join(diretorio_modelos, 'assistente_logistic_regression_model.pkl'))
pipeline_svm = joblib.load(os.path.join(diretorio_modelos, 'assistente_svm_model.pkl'))
label_encoder = joblib.load(os.path.join(diretorio_modelos, 'label_encoder.pkl'))

def prever_intencao(frase, modelo='svm'):
    if modelo == 'svm':
        model = pipeline_svm
    elif modelo == 'lr':
        model = pipeline_lr
    else:
        print("Modelo não reconhecido")
        return None

    # Prever diretamente
    classe_idx = model.predict([frase])[0]
    intencao = label_encoder.inverse_transform([classe_idx])
    print(intencao)
    return intencao[0]

if __name__ == "__main__":
    while True:
        frase_teste = input("Digite a frase: ")
        intencao_prevista = prever_intencao(frase_teste, modelo='lr')  # ou 'svm'
        print(f"Intenção prevista: {intencao_prevista}")
