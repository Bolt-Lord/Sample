from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

encrypted_token = 'CE93C414E02A32023E883A728271A0BA467DBC51D9919D87B7BE7AB5BE3032603F354367751BC212D2FD1600F37F6DF5ABCE8188A5235B3F1A23EC670D2366C8'
secret_key = 'Vf22InD6h6cCjYxR'
encoded_secret = secret_key.encode('utf-8').hex()
secret_key = bytes.fromhex(encoded_secret)
iv = bytes.fromhex(encrypted_token[:32])
ciphertext_string = bytes.fromhex(encrypted_token[32:])
ciphertext = ciphertext_string
cipher = AES.new(secret_key, 2, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(plaintext.decode())
