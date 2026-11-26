from urllib.parse import urlparse
import tldextract

extractor = tldextract.TLDExtract(suffix_list_urls=())

NUM_COLS = [
    "url_lenght", "domain_length", "subdomain_length", "path_length",
    "query_length", "has_query", "num_dots", "num_hyphens", "num_digits",
    "num_subdomains", "has_at", "has_ip",
]

def clean_url(url):
    url = str(url).strip()
    if "://" not in url:
        url = "http://" + url
    return url

def extraction_features(url):
    """"""
    url = clean_url(url)
    parsed = urlparse(url)
    ext = extractor(url)

    return {
            "url_lenght": len(url),
            "domain_length":len(ext.domain),
            "subdomain_length":len(ext.subdomain),
            "path_length":len(parsed.path),
            "query_length":len(parsed.query),
            "has_query":int(len(parsed.query) > 0),
            "num_dots": url.count("."),
            "num_hyphens": url.count("-"),
            "num_digits": sum(c.isdigit() for c in url),
            "num_subdomains":len(ext.subdomain.split(".")) if ext.subdomain else 0,
            "has_at": int("@" in url),
            "has_ip":int(ext.domain.replace(".", "").isdigit()),
    }
