import secrets
secret_key = secrets.token_hex(16)  # Genera una clave secreta de 16 bytes
print(secret_key)