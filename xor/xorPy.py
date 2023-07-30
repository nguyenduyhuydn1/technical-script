def xor(data, encryption_key):
    encryption_key = str(encryption_key)
    output = ""
    for i in range(len(data)):
        current_key = encryption_key[i % len(encryption_key)]
        output += chr(ord(data[i]) ^ ord(current_key))
    return output


def deXor(data, encryption_key):
    encryption_key = str(encryption_key)
    output = ""
    for i in range(len(data)):
        current_key = encryption_key[i % len(encryption_key)]
        output += chr(ord(data[i]) ^ ord(current_key))
    return output


print(deXor("kU\td\u0000.$/w,*i0E\\\tU\u0000=724", "0xTDFGHJWEYI^*()"))
