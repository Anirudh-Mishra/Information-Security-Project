from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Encrypter import Encrypter
from Decrypter import Decrypter
from PIL import Image as Img
from PIL import ImageTk as ImgTk
import base64
from Crypto.Cipher import AES
import os
import sys
import io
Qt = QtCore.Qt

def dec():
    myKey = "1234"
    file  = "D:\\Project\\ISAA Project\\Information-Security-Project\\src\\encrypted.txt"
    text=open(file).read()
    cipher= text.encode('utf-8')
    x = Decrypter(cipher)
    image=x.decrypt_image(myKey)
    print(type(image))
    imag = Img.open(io.BytesIO(image))
    imag.save('D:\\Project\\ISAA Project\\Information-Security-Project\\src\\decryptedimage.png')

    # ba = QtCore.QByteArray(image)
    # print(ba)