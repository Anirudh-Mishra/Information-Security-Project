import base64
import hashlib
from PIL import Image
from random import randint
from src.AESCipher import AESCipher

class Decrypter:
    def __init__(self, cipher):
        self.cipher = cipher
        
    def decrypt_image(self,k):
        key = k
        cipher = self.cipher
        aes = AESCipher(key)
        base64_decoded = aes.decrypt(cipher)
        fh = open("decryptedImage.png", "wb")
        fh.write(base64.b64decode(base64_decoded))
        fh.close() 
        return (base64.b64decode(base64_decoded))
        



