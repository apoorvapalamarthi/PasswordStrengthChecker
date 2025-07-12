import requests
import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'\W', password):
        score += 1

    if score >= 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

def check_breach(password):
    import hashlib
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return "⚠️ Breach check failed"

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f"❌ This password appeared in {count} breaches!"
    return "✅ No known breaches found."

def main():
    print("🔐 Password Strength & Breach Checker 🔍")
    password = input("Enter your password: ")

    strength = check_password_strength(password)
    print(f"\n🧠 Password Strength: {strength}")

    breach_result = check_breach(password)
    print(f"{breach_result}")

if __name__ == "__main__":
    main()

