import hashlib



str = "hello"

encoded_str = str.encode()


hash_obj_sha3_224 = hashlib.sha3_224(encoded_str)
hash_obtenido = hash_obj_sha3_224.hexdigest()

print("\nSHA3-224 Hash:", hash_obtenido)

has_original = "b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81"

if has_original == hash_obtenido:
    print("verdadero")
else:
    print("falso")
