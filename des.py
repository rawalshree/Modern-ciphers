'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


from Crypto.Cipher import DES
from Crypto import Random


global plain
global cipher
global Success
global obj
Success = False
plain = ""
cipher = ""


class SimpleDES:

    def setKey(self, key):
        global Success, obj
        try:
            self.key = key
            if len(self.key) == 8:
                Success = True
                obj = DES.new(self.key, DES.MODE_ECB)
        except:
            pass


    def encryption(self, plainText):
        global cipher, Success, obj
        self.plainText = plainText

        while len(self.plainText) % 8 != 0:
            self.plainText += '*'
        
        if Success:
            cipher = obj.encrypt(self.plainText)
            return cipher
        else:
            print("Invalid Key")
            return self.plainText
        
        
    def decryption(self, cipherText):
        global plain, Success, obj
        self.cipherText = cipherText
        if Success:
            plain = obj.decrypt(self.cipherText)
            return plain
        else:
            print("Invalid Key")
            return self.cipherText