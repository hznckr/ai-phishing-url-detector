import joblib
import pandas as pd
from feature_extraction import extract_features

# Modeli yükle
model = joblib.load("model_balanced.pkl")

# Etiketleri tersine çeviren sözlük
label_map = {
    0: 'benign',
    1: 'malware',
    2: 'phishing',
    3: 'defacement'
}

# Kullanıcıdan URL al
url = input("Tahmin etmek istediğiniz URL'yi girin: ")

# Özellik çıkarımı
features = extract_features(url)
features_df = pd.DataFrame([features])  # DataFrame'e çevir

try:
    # Tahmin al
    prediction = model.predict(features_df)[0]
    label = label_map.get(prediction, "Unknown")
    
    # Olasılıkları al
    probs = model.predict_proba(features_df)[0]
    
    print("Tahmin:", label)
    print("Olasılıklar:")
    for idx, prob in enumerate(probs):
        print(f"  {label_map.get(idx, idx)}: {prob:.4f}")

except Exception as e:
    print("Bir hata oluştu:", e)
print("Model sınıfları (model.classes_):", model.classes_)
print("Label map:", label_map)

print("Modelin eğitimde kullandığı özellikler:", model.feature_names_in_)
print("Tahmin için çıkarılan özellikler:", features_df.columns.tolist())

print(features_df)