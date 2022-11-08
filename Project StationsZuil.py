def bericht():
    import datetime
    import random
    import uuid

    berichtid = uuid.uuid4()
    berichtidstr = str(berichtid)
    x = datetime.datetime.now()
    datum = (x.strftime('%d/%m/%Y'))
    tijd = (x.strftime('%H:%M'))

    random_line = random.choice(open('Stations.txt').readlines())
    while True:
        feedback = input('Beste reiziger, wij proberen uw reis ervaring zo prettig mogelijk te maken \n'
                         'en daarom vragen we of u de tijd zou willen nemen om uw feedback te geven! \nHet bericht mag maximaal uit'
                         ' 140 karakters bestaan: ')
        if len(feedback) > 140:
            print('U heeft teveel karakters gebruikt, probeer het opnieuw!')
        elif len(feedback) == 0:
            print('U heeft geen karakters gebruikt, probeer het opnieuw!')
        else:
            break

    naam = input('Voer hier uw naam in (optioneel): ')
    if len(naam) == 0:
        naam = 'Anoniem'
    file = open('Bericht.txt', 'a')
    file.write(str(feedback) + ',' + berichtidstr + ',' + str(naam) + ',' + datum + ',' + tijd + ',' + random_line)
    file.close()


bericht()


