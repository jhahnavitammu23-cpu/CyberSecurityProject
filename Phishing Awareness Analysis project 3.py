# Phishing Awareness Analysis

message = input("Enter the email/message:\n")

keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click",
    "login",
    "account",
    "prize",
    "winner",
    "http",
    "https"
]

red_flags = []

for word in keywords:
    if word.lower() in message.lower():
        red_flags.append(word)

print("\n----- Analysis Result -----")

if red_flags:
    print("⚠ Possible Phishing Message")
    print("\nRed Flags Found:")
    for flag in red_flags:
        print("-", flag)
    print("\nReason:")
    print("This message contains suspicious words or links that are commonly used in phishing attacks.")
else:
    print("✓ No common phishing indicators found.")