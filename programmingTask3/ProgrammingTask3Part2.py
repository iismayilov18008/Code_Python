import re

def is_valid_url(url, url_index):
    try:       
        if not (url.startswith("http://") or url.startswith("https://")):
            print("there should be 'http://' or 'https://'")
            return False
            
        if "." not in url:
            print(f"URL {url_index}: Invalid URL. Missing dot in domain: {url}")
            return False    
        
        invalid_chars = " <>^~{[#%}|]`\\ "
        for char in invalid_chars:
            if char in url:
                print(" Invalid URL. It contains special characters")
                return False
            
        domain_parts = url.split(".")
        domain_name = domain_parts[1].split(":")[0]
        if len(domain_name) < 2:
            print(" Invalid domain in URL")
            return False
        
        for part in domain_parts:
            if not part:
                print(" Domain part is empty:")
                return False
    except Exception as error:
        print(f"Error occurred: {error}")
            
    return True

def parse_url(url):
    protocol, rest_of_url = url.split("://", 1)
    domain_with_port = rest_of_url  
    
    parts = domain_with_port.split(":", 1)
    domain = parts[0]
    port = parts[1] if len(parts) > 1 else ""
    
    if not port:
        port = "80" if protocol == "http" else "443" if protocol == "https" else None    
    if port and "/" in port:
        port = port.split("/", 1)[0]
    
    return protocol, domain, port

def compare_url_origins(url1, url2):
    if not is_valid_url(url1, 1) or not is_valid_url(url2, 2):
        return "One or both URLs are invalid."

    protocol1, domain1, port1 = parse_url(url1)
    
    protocol2, domain2, port2 = parse_url(url2)
    
    if domain1 == domain2 and protocol1 == protocol2  and port1 == port2:
        return "Same origin"    
    differences = []
    if protocol1 != protocol2:
        differences.append("different protocols")
    if domain1 != domain2:
        differences.append("different domains")
    if port1 != port2:
        differences.append("different ports")
    return "Different origin: " + ", ".join(differences)





url1 = input("Enter the first URL: ")
url2 = input("Enter the second URL: ")
print(compare_url_origins(url1, url2))
