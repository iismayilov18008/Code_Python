import requests

# URL of the website
url = "https://code.edu.az/"

# Dictionary of common security headers to check
security_headers = {
    "Content-Security-Policy": "",
    "X-Frame-Options": "",
    "X-Content-Type-Options": "",
    "Strict-Transport-Security": "",
    "Referrer-Policy": "",
    "Permissions-Policy": "",
    "Feature-Policy": "",
    "Expect-CT": "",
    "X-XSS-Protection": "",
    "Cache-Control": "",
    "Pragma": "",
    "Access-Control-Allow-Origin": "",
    "Strict-Transport-Security": "",  
    "Cross-Origin-Opener-Policy": "",
    "Cross-Origin-Embedder-Policy": "",
    "Content-Type": "",
    "Authorization": "",
    "X-Permitted-Cross-Domain-Policies": ""
}

try:
    response = requests.get(url)

    for header in security_headers:
        if header in response.headers:
            security_headers[header] = response.headers[header]
            print(f"{header} exists, Value: {response.headers[header]}")
        else:
            print(f" {header} does not exist ")

except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
