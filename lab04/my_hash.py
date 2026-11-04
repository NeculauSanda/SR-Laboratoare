import hashlib

# Solicita adresa de e-mail-ul institutionala
email_institutional = input("Introduceti e-mail-ul propriu institutional: ").strip().lower()

if email_institutional:
    # Generare hash SHA-256
    hashed_id = hashlib.sha256(email_institutional.encode("utf-8")).hexdigest()

    print(f"E-mail procesat: {email_institutional}")
    print(f"ID HASH: {hashed_id}")
    print("\n")
    print("Copiati codul HASH de mai sus în WebProtege ca valoare pentru proprietatea hasUserHash.")
else:
    print("\nNu ati introdus nicio adresa de e-mail!")
