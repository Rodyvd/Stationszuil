import psycopg2

def database():

    while True:
        with open('moderatie.csv', 'r') as file:
            firstline = file.readline()
            x = firstline
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

            station = [i.split(',')[11] for i in list]
            station = station[0]
            print(station)

            keuring = [i.split(',')[5] for i in list]
            keuring = keuring[0]

            naammod = [i.split(',')[6] for i in list]
            naammod = naammod[0]

            emailmod = [i.split(',')[7] for i in list]
            emailmod = emailmod[0]

            datummod = [i.split(',')[8] for i in list]
            datummod = datummod[0]

            tijdmod = [i.split(',')[9] for i in list]
            tijdmod = tijdmod[0]

            modnummer = [i.split(',')[10] for i in list]
            modnummer = modnummer[0]
        file.close()


        if 'Utrecht' in station:
            station = 'Utrecht'
        elif 'Amsterdam' in station:
            station = 'Amsterdam'
        else:
            station = 'Groningen'


        goedgekeurd = input('Kunnen de gegevens worden doorgestuurd naar de database? [Y/N]')
        if goedgekeurd == 'Y':
            connection_string = "host='localhost' dbname='Stationszuil' user='postgres' password='Willysch@t1'"
            conn = psycopg2.connect(connection_string)
            cursor = conn.cursor()

            query = """INSERT INTO moderator (nummer, naam, email)
                        VALUES (%s, %s, %s);"""
            moderator = (modnummer, naammod, emailmod)
            cursor.execute(query, moderator)

            query = """INSERT INTO bericht (nummer, naamreiziger, berichtzelf, datum, tijd, stationnaam)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            bericht = (berichtid, naamreiziger, feedback, datum, tijd, station)
            cursor.execute(query, bericht)

            query = """INSERT INTO moderation (datum, tijd, goedgekeurd, moderatornummer, berichtnummer)
                        VALUES (%s, %s, %s, %s, %s)"""
            moderation = (datummod, tijdmod, keuring, modnummer, berichtid)
            cursor.execute(query, moderation)

            conn.commit()
            conn.close()

            with open('moderatie.csv', 'r+') as fp:
                lines = fp.readlines()
                fp.seek(0)
                fp.truncate()
                fp.writelines(lines[1:])
            break

database()


