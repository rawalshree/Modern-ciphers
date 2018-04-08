

#### TO EXECUTE THE CIPHERS ####
> Run the cipher.py file followed by the arguments

**The arguments are**
> root@name:~# python cipher.py  <cipher_name>  <cipher_key>  <ENC/DEC>  <input_file>  <output_file>

```
<cipher_name> : AES - AES
                DES - DES
              
<cipher_key> : The key to be used

<ENC/DEC> : ENC - Encryption
            DEC - Decryption

<input_file> : The file to be ENC/DEC

<output_file> : The output of the cipher function

```

**An example would be**

> root@name:~# python cipher.py DES "01234567" ENC small.txt smallout.txt

---------

**Note**

> Length of key for AES is 16 (i.e. 128 bits) and for DES is 8 (i.e. 64 bits)

