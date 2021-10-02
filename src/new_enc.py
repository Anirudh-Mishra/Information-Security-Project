from PyQt5 import QtCore
from PyQt5.QtCore import *
from Encrypter import Encrypter
from Decrypter import Decrypter
from PIL import Image as Img
from PIL import ImageTk as ImgTk
import base64
from Crypto.Cipher import AES
import os
import sys
Qt = QtCore.Qt

def enc():
    with open("./src/image.jpg", "rb") as imageFile:
        value = base64.b64encode(imageFile.read())
        #print(str)
    myKey = "1234"
    # ba = QtCore.QByteArray()
    # buff = QtCore.QBuffer(ba)
    # buff.open(QtCore.QIODevice.WriteOnly) 
    # #ok = pixmap.save(buff, "PNG")
    # #assert ok
    # pixmap_bytes = ba.data()
    # value = base64.b64encode(pixmap_bytes)
    x = Encrypter(value, myKey)
    cipher = x.encrypt_image()
    fh = open("./src/cipher.txt", "wb")
    fh.write(cipher)
    fh.close()