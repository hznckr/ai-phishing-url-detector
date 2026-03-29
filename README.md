# 🛡️ Multi-Class Phishing & Malicious URL Detector

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![CyberSecurity](https://img.shields.io/badge/Focus-Cyber_Security-red?style=for-the-badge)

An intelligent URL analysis system that classifies web addresses into four categories: **Benign, Malware, Phishing, and Defacement**. Using advanced feature extraction and a Random Forest Classifier, this tool identifies malicious patterns in URL structures to prevent cyber attacks.

## 🕵️‍♂️ Key Capabilities
- **Heuristic Feature Extraction:** Extracts 15+ lexical features including URL length, digit-to-letter ratio, suspicious keywords, and domain analysis.
- **Multi-Class Classification:** Unlike standard detectors, this model distinguishes between specific attack types (Phishing vs. Malware vs. Defacement).
- **Data Balancing:** Implements `RandomOverSampler` to ensure high accuracy even for rare attack types.
- **Real-time Prediction:** Includes an inference script for manual URL checking with probability scores.

## 🛠 Features Analyzed
The model inspects URLs for:
- 📏 **Structural Metrics:** URL, Domain, and Path lengths.
- 🔐 **Security Indicators:** HTTPS presence and IP-based domains.
- 🔠 **Lexical Analysis:** Count of special characters (`.`, `-`, `@`, `?`, `=`, `/`).
- 🚩 **Suspicious Keywords:** Detection of words like `login`, `secure`, `verify`, `account`.
- 📊 **Complexity:** Digit and Uppercase ratios.

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-phishing-url-detector.git](https://github.com/YOUR_USERNAME/ai-phishing-url-detector.git)
cd ai-phishing-url-detector
