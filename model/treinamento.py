import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Carregar dados
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "dataset.csv")
df = pd.read_csv(csv_path)

# Exemplo de verificação para garantir que as colunas estão corretas
if 'frase' not in df.columns or 'intencao' not in df.columns:
    raise ValueError("O dataset deve conter as colunas 'frase' e 'intencao'.")

# Preparação dos dados
X = df['frase']
y = df['intencao']

# Codificar as intenções em valores numéricos
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Criar o pipeline com vetorização TF-IDF e modelo de classificação (Logistic Regression e SVM)
pipeline_lr = make_pipeline(TfidfVectorizer(ngram_range=(1, 2), stop_words='english'), LogisticRegression())
pipeline_svm = make_pipeline(TfidfVectorizer(ngram_range=(1, 2), stop_words='english'), SVC(kernel='linear', probability=True))  # Ativar probabilidades para SVM

# Treinar os modelos
pipeline_lr.fit(X_train, y_train)
pipeline_svm.fit(X_train, y_train)

# Testar a acurácia dos modelos
acuracia_lr = pipeline_lr.score(X_test, y_test)
acuracia_svm = pipeline_svm.score(X_test, y_test)

print(f"Acurácia - Logistic Regression: {acuracia_lr:.2f}")
print(f"Acurácia - SVM: {acuracia_svm:.2f}")

# Função para predizer com threshold de confiança
def predizer_com_threshold(frase, modelo, threshold=0.5):
    # Predizer com probabilidades
    probabilidade = modelo.predict_proba([frase])
    classe_predita = probabilidade.argmax()  # A classe com a maior probabilidade
    probabilidade_maxima = probabilidade[0][classe_predita]  # Probabilidade máxima da classe predita
    
    if probabilidade_maxima < threshold:
        return "desconhecido"  # Ou qualquer resposta de erro personalizada
    else:
        return label_encoder.inverse_transform([classe_predita])[0]

if __name__ == "__main__": # Teste de exemplo para verificar a funcionalidade do threshold
    frase_test = "Qualquer frase desconhecida"
    resultado = predizer_com_threshold(frase_test, pipeline_lr, threshold=0.7)
    print(f"Resultado: {resultado}")

# Salvar os modelos e o encoder
joblib.dump(pipeline_lr, 'assistente_logistic_regression_model.pkl')
joblib.dump(pipeline_svm, 'assistente_svm_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("Modelos e encoder salvos com sucesso!")
