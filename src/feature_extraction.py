import re
from urllib.parse import urlparse
from urllib.parse import urlparse

from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    features = []

    features.append(len(url))                     # length_url
    features.append(len(domain))                  # length_hostname
    features.append(url.count('.'))               # nb_dots
    features.append(url.count('-'))               # nb_hyphens
    features.append(url.count('@'))               # nb_at
    features.append(url.count('?'))               # nb_qm
    features.append(1 if "www" in domain else 0)  # nb_www
    features.append(1 if parsed.scheme == "https" else 0)  # https_token

    digits = sum(c.isdigit() for c in url)
    features.append(digits / len(url) if len(url) > 0 else 0)  # ratio_digits_url

    features.append(domain.count('.'))           # nb_subdomains
    features.append(1 if '-' in domain else 0)   # prefix_suffix
    features.append(1 if "bit.ly" in url or "tinyurl" in url else 0)  # shortening

    return features
