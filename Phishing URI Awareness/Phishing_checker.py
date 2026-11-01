import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """URL text me se 6 warning signs check karta hai."""
    url = raw_url.strip()
    findings = []
    
    if not url:
        return ["No URL entered."]
        
    candidate = url if "://" in url else "http://" + url
    
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]
        
    host = (parsed.hostname or "").lower()
    if not host:
        return ["Could not identify a hostname."]
        
    # Check 1: @ Symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")
        
    # Check 2: Length over 100
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")
        
    # Check 3: IP Address Hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")
        
    # Check 4: Many Subdomains (5 or more)
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")
        
    # Check 5: Punycode (xn--)
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")
        
    # Check 6: HTTP Scheme
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")
        
    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")
        
    return findings

def main():
    print("=== EWB Phishing URL Awareness Checker ===")
    print("Text checks only - this program does not open URLs.\n")
    
    while True:
        raw_url = input("Enter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break
            
        print("\nResult:")
        for item in inspect_url(raw_url):
            print("- " + item)
        print()

if __name__ == "__main__":
    main()