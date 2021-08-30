import sys
import random
import json
import re
import base64
from AES_module import AES
from ECC_module import ECC
from Convert import converter
from PIL import Image


def main():
    # AES_tester()
    # ECC_tester()
    # Converter_tester()

    input_file = input(
        "Enter the name of file to encrypt present in ./test_files/ > ")
    file_type = input_file.split(".")[1]
    output_file = "test."+file_type

    # im = Image.open("test_files/"+input_file)
    # width, height = im.size
    ######################################################################################
    # 1. Multimedia data -> Base64 Encoding and plain text
    multimedia_data = converter.fileToBase64("test_files/" + input_file)

    # print(multimedia_data[0:100])

    # multimedia_data = (b"hey").decode('utf-8')
    # multimedia_data = input("Enter the data >")
    ######################################################################################

    aes_key = 57811460909138771071931939740208549692

    ######################################################################################
    # Encrypt  AES_key with ECC public key
    ecc_obj_AESkey = ECC.ECC()
    private_key = 59450895769729158456103083586342075745962357150281762902433455229297926354304
    public_key = ecc_obj_AESkey.gen_pubKey(private_key)
    (C1_aesKey, C2_aesKey) = ecc_obj_AESkey.encryption(public_key, str(aes_key))
    # decryptedAESkey = ecc_AESkey.decryption(C1_aesKey,C2_aesKey, private_key)
    ######################################################################################

    ######################################################################################
    # 2. Encrypt the multimedia_data with AES algorithm
    aes = AES.AES(aes_key)
    encrypted_multimedia = aes.encryptBigData(multimedia_data)
    data_for_ecc = converter.makeSingleString(encrypted_multimedia)

    # converter.base64ToFile(decrypted_multimedia.encode('utf-8'),"test_success.jpg")
    ######################################################################################

    ######################################################################################
    # 3. Encrypt the encrypted_multimedia with ECC
    ecc = ECC.ECC()
    (C1_multimedia, C2_multimedia) = ecc.encryption(public_key, data_for_ecc)
    ######################################################################################

    cipher = {
        "file_type": file_type,
        "C1_aesKey": C1_aesKey,
        "C2_aesKey": C2_aesKey,
        "C1_multimedia": C1_multimedia,
        "C2_multimedia": C2_multimedia,
        "private_key": private_key
    }
    with open('cipher.json', 'w') as fp:
        json.dump(cipher, fp)

    converter.encodeStringinImage(json.dumps(cipher), "success.jpg", "JPEG")


if __name__ == "__main__":
    main()
