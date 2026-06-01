import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Veri setini yükle
data = pd.read_csv("train.csv")
print("İlk 5 satır:")
print(data.head())

# 2. Eksik verileri doldur
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data = data.drop('Cabin', axis=1)

# 3. Kategorik verileri dönüştür
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 4. Özellikleri ve hedefi ayır
X = data.drop(['Survived', 'Name', 'Ticket', 'PassengerId'], axis=1)
y = data['Survived']

print("\nÖzellikler (X):")
print(X.head())
print("\nHedef (y):")
print(y.head())

# 5. Veri analizi (EDA)
print("\nEksik veri kontrolü:")
print(data.isnull().sum())

sns.countplot(x='Survived', data=data)
plt.title("Hayatta Kalma Dağılımı")
plt.show()

sns.histplot(data['Age'])
plt.title("Yaş Dağılımı")
plt.show()

# 6. Model kurma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 7. Tahmin ve değerlendirme
y_pred = model.predict(X_test)

print("\nModel Değerlendirme:")
print("Doğruluk (Accuracy):", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
