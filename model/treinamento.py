import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
import joblib
import os

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "dataset.csv")
df = pd.read_csv(csv_path)

# Preparação dos dados
X = df['frase']
y = df['intencao']

# Codificar as intenções em valores numéricos
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Criar o pipeline com vetorização e modelo de classificação (Logistic Regression e SVM)
pipeline_lr = make_pipeline(CountVectorizer(), LogisticRegression())
pipeline_svm = make_pipeline(CountVectorizer(), SVC(kernel='linear'))

# Treinar os modelos
pipeline_lr.fit(X_train, y_train)
pipeline_svm.fit(X_train, y_train)

# Salvar os modelos treinados
joblib.dump(pipeline_lr, 'assistente_logistic_regression_model.pkl')
joblib.dump(pipeline_svm, 'assistente_svm_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')  # Salvar o LabelEncoder também

print("Modelos e encoder salvos com sucesso!")