import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import RandomOverSampler
import joblib
from feature_extraction import extract_features
from collections import Counter

# Veri dosyasını oku
df = pd.read_csv("phishing_urls.csv")

# -1 gibi hatalı etiketleri temizle
df = df[df['type'].notnull()]  # NaN varsa
df = df[df['type'] != -1]      # Hatalı sınıf varsa

# Etiket kategorilerini al ve kodları oluştur
labels = df['type'].astype('category')
label_names = labels.cat.categories  # Etiket isimleri
y = labels.cat.codes                 # Sayısal etiketler

# Özellik çıkarımı
features_df = df['url'].apply(extract_features)

# Özelliklere label ekle
features_df['label'] = y.values

# Giriş ve çıkış verileri
X = features_df.drop('label', axis=1)
y = features_df['label']

# ▶️ 1. Aşama: Oversampling (azınlık sınıfları çoğalt)
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)

print("Oversampling sonrası sınıf dağılımı:", Counter(y_resampled))

# ▶️ 2. Aşama: Eğitim/test bölmesi
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# ▶️ 3. Aşama: Model eğitimi
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# ▶️ 4. Aşama: Tahmin ve değerlendirme
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=label_names))

# Label map: sayısal kod -> isim
label_map = {code: name for code, name in enumerate(label_names)}

# Örnek tahminleri isim olarak yazdır
print("\nÖrnek tahminler:")
for pred_num in y_pred[:10]:
    print("Tahmin:", label_map[pred_num])
print(df['type'].value_counts())

# ▶️ 5. Aşama: Modeli kaydet
joblib.dump(model, "model_balanced.pkl")