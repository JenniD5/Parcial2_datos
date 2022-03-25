
import hashlib


str = "hello"

encoded_str = str.encode()


hash_obj_sha256 = hashlib.sha256(encoded_str)
hash_obtenido = hash_obj_sha256.hexdigest()

print("\nSHA256 Hash:", hash_obtenido)
hash_original = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

if hash_original == hash_obtenido:
    print("verdadero")
else:
    print("falso")
