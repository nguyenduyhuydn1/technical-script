import base64

fr = open('./accept.py', 'rb')
piece = fr.read()

asd = base64.b64encode(piece)

def en(temp, needEncode):
    try:
        index = 0
        lengthPass = len(temp) - 1
        textEncoded = b''
        for i in needEncode:
            textEncoded += (ord(i) ^ ord(temp[index])).to_bytes(1, 'little')
            if index + 1 > lengthPass:
                index = 0
            else:
                index += 1
        return base64.b64encode(textEncoded)
    except:
        print('error')


print(
    en('''^).RRg~.\;f?Z'G`+!n"m?6E`%a'fN>yn;_|'^Nb]hpr]ut3fK^Y]bF9xQ~=)~JSUyx$iCZS*>@4:^)Si\+|z#P@vBYF$d{Cx$_>999''', asd.decode('ascii')))




#maybe de
# PS = '''^).RRg~.\;f?Z'G`+!n"m?6E`%a'fN>yn;_|'^Nb]hpr]ut3fK^Y]bF9xQ~=)~JSUyx$iCZS*>@4:^)Si\+|z#P@vBYF$d{Cx$_>'''
# def en(n):
#     try:
#         ix = 0
#         m_ix = len(PS) - 1
#         alo = ''
#         with open(n, 'rb') as f:
#             alo = f.read()
#         with open(n, 'w') as f:
#             f.write('')
#         for b in alo:
#             x = b ^ ord(PS[ix])
#             with open(n, 'ab') as f:
#                 f.write(x.to_bytes(1, 'little'))
#             if ix + 1 > m_ix:
#                 ix = 0
#             else:
#                 ix += 1
#     except:
#         print('error')


# en('b.uyu')
