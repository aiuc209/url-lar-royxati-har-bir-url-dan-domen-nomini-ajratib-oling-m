from urllib.parse import urlparse

url_list = ["https://example.com", "http://test.com", "https://www.google.com"]
domain_list = [urlparse(url).netloc for url in url_list]
print(domain_list)
