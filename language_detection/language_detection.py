from langdetect import detect


portuguese_str = 'Ouvi, que não vereis com vãs façanhas, Fantásticas, fingidas, mentirosas, Louvar os vossos, como nas estranhas'

print(detect(portuguese_str))


english_str = 'Shakespeare produced most of his known works between 1589 and 1613. His early plays were \
    primarily comedies and histories and are regarded as some of the best works produced in these gender.'
 
print(detect(english_str))

ukranian_str = 'Ви полюбля́єте ходи́ти у похі́д? Я зо́всім ні та за́раз ви дізна́єтесь чому́. Одно́го ра́зу, коли́ \
    мені́ було́ 19 ро́ків, ми з дру́зями ви́рішили піти́ у похі́д.'

print(detect(ukranian_str))

german_str = 'In diesem Sommer macht sie einen Sprachkurs in Freiburg. Das ist eine Universitätsstadt im \
    Süden von Deutschland.'

print(detect(german_str))
