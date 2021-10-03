import os
import sys
import base64
from PIL import Image as Img
from Crypto.Cipher import AES
from PIL import ImageTk as ImgTk
from src.Encrypter import Encrypter
from src.Decrypter import Decrypter

def enc():
    with open("./src/image.jpg", "rb") as imageFile:
        value = base64.b64encode(imageFile.read())
        
    myKey = "1234"
    x = Encrypter(value, myKey)
    cipher = x.encrypt_image()
    fh = open("./src/cipher.txt", "wb")
    fh.write(cipher)
    fh.close()