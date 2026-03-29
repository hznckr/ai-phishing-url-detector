import re
import pandas as pd
from urllib.parse import urlparse

def extract_features(url):
    try:
        if not isinstance(url, str):
            raise ValueError("URL is not a string")

        # Eğer URL http veya https ile başlamıyorsa başına http:// ekle
        url_to_parse = url if url.startswith('http') else 'http://' + url
        parsed = urlparse(url_to_parse)

        url_length = len(url)
        domain = parsed.netloc
        path = parsed.path

        # Özellikleri hesapla
        url_features = {
            'url_length': url_length,
            'domain_length': len(domain),
            'path_length': len(path),
            'has_https': int(url.startswith('https')),
            'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', domain))),  # sadece domain kısmında IP kontrolü
            'count_dot': url.count('.'),
            'count_hyphen': url.count('-'),
            'count_at': url.count('@'),
            'count_question': url.count('?'),
            'count_equals': url.count('='),
            'count_slash': url.count('/'),
            'count_digits': sum(c.isdigit() for c in url),
            'digit_ratio': sum(c.isdigit() for c in url) / (url_length if url_length > 0 else 1),
            'uppercase_ratio': sum(c.isupper() for c in url) / (url_length if url_length > 0 else 1),
            'suspicious_word': int(any(word in url.lower() for word in ['login', 'secure', 'account', 'update', 'verify']))
        }

        return pd.Series(url_features)

    except Exception:
        # Hatalı veya boş URL varsa sıfır değerler döndür
        zero_dict = {
            'url_length': 0,
            'domain_length': 0,
            'path_length': 0,
            'has_https': 0,
            'has_ip': 0,
            'count_dot': 0,
            'count_hyphen': 0,
            'count_at': 0,
            'count_question': 0,
            'count_equals': 0,
            'count_slash': 0,
            'count_digits': 0,
            'digit_ratio': 0,
            'uppercase_ratio': 0,
            'suspicious_word': 0
        }
        return pd.Series(zero_dict)