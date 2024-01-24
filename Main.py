from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

student_id = '30000424'
counsellor_id = '400000039'

stg_hash = '51C658C91FB8B11B2F1556CF195BEE90BED46635CD8875B9808A12597A67451CAD1EF984076911C0ACBCFABE1BD5A918166378637396E2DAC455BFAB420F8CDC'
uat_hash = 'B0642DB0256327E4B14B1AFE76FDF1C009E2629FA90504FDA7001FE54FFCABD3AAF87438F37FC975A485DCF9AE677D34'


encrypted_token = uat_hash
secret_key = 'Vf22InD6h6cCjYxR'
encoded_secret = secret_key.encode('utf-8').hex()
secret_key = bytes.fromhex(encoded_secret)
iv = bytes.fromhex(encrypted_token[:32])
ciphertext_string = bytes.fromhex(encrypted_token[32:])
ciphertext = ciphertext_string
cipher = AES.new(secret_key, 2, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(plaintext.decode())