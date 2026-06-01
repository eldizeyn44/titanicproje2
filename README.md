# 🚢 Titanic Hayatta Kalma Tahmini

Bu proje, Titanic yolcularının hayatta kalıp kalmadığını tahmin etmek için **Makine Öğrenmesi** yöntemlerini kullanır.  
Amaç, veri temizleme, veri analizi (EDA) ve sınıflandırma modeli kurarak yolcuların hayatta kalma durumunu tahmin etmektir.

---

## 📌 İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Sonuçlar](#sonuçlar)
- [Geliştirme Önerileri](#geliştirme-önerileri)

---

## 📖 Proje Hakkında
Bu proje, Kaggle üzerinde bulunan **Titanic Dataset** kullanılarak geliştirilmiştir.  
Veri setinde şu özellikler bulunmaktadır:
- `PassengerId` → Yolcu ID
- `Survived` → Hayatta kalma durumu (0 = Hayır, 1 = Evet)
- `Pclass` → Yolcu sınıfı
- `Name`, `Sex`, `Age` → Yolcu bilgileri
- `SibSp`, `Parch` → Aile bireyleri
- `Ticket`, `Fare`, `Cabin`, `Embarked` → Bilet ve gemi bilgileri

Model, **Logistic Regression** ile kurulmuş ve doğruluk oranı ile değerlendirilmiştir.

---

## 🛠 Kullanılan Teknolojiler
- Python 3
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (Logistic Regression, Train-Test Split, Metrics)

---

## ⚙️ Kurulum
1. Bu repoyu klonla:
   ```bash
   git clone https://github.com/eldizeyn44/titanicproje2.git
