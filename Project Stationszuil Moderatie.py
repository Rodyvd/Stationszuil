import os
import datetime
import random

x = datetime.datetime.now()
datum = (x.strftime('%d/%m/%Y'))
tijd = (x.strftime('%H:%M'))


def moderatie():

    # modnummer = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    # print(modnummer)

    while True:
        naam = input('Voer hier uw naam in: ')
        if len(naam) == 0:
            print('U heeft geen naam ingevoerd, probeer het overnieuw!')
        else:
            break

    while True:
        email = input('Voer hier uw email-adres in: ')
        if len(email) == 0:
            print('U heeft geen email ingevoerd, probeer het overnieuw!')
        else:
            break



    while True:
        modnummer = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        print(modnummer)
        file_path = 'Bericht.txt'
        if os.stat(file_path).st_size == 0:
            print('Er zijn geen berichten om te beoordelen!')
            break
        else:
            with open('Bericht.txt', 'r') as file:
                firstlines = file.readline()
                x = firstlines
                list = [x]
                feedback = [i.split(',')[0] for i in list]
                feedback = feedback[0]

                berichtid = [i.split(',')[1] for i in list]
                berichtid = berichtid[0]

                naamreiziger = [i.split(',')[2] for i in list]
                naamreiziger = naamreiziger[0]

                datum = [i.split(',')[3] for i in list]
                datum = datum[0]

                tijd = [i.split(',')[4] for i in list]
                tijd = tijd[0]

                station = [i.split(',')[5] for i in list]
                station = station[0]
                print(feedback)
                file.close()
                test = input('Is dit bericht voldoende? [Y/N]: ')
                if test == 'Y':
                    with open('Bericht.txt', 'r+') as fp:
                        lines = fp.readlines()
                        file = open('moderatie.csv', 'a')
                        file.write(feedback + ',' + berichtid + ',' + naamreiziger + ',' + datum + ',' + tijd + ',' + 'True' + ',' + str(naam) + ',' + str(email) + ',' + datum + ',' + tijd + ',' + modnummer + ',' + station)
                        file.write('\n')
                        fp.seek(0)
                        fp.truncate()
                        fp.writelines(lines[1:])
                        file_path = 'Bericht.txt'
                elif test == 'N':
                    with open('Bericht.txt', 'r+') as fp:
                        lines = fp.readlines()
                        fp.seek(0)
                        fp.truncate()
                        fp.writelines(lines[1:])

                else:
                    print('U kunt alleen Y (yes) of N (no) invullen!')


moderatie()
