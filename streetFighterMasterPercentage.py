# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:15:19 2023

@author: tiwashima
"""

import matplotlib.pyplot as plot

lukeRookie=4359+1557+1632+1355+1307
lukeIron=6221+3339+3454+3076+1957
lukeBronze=5212+3339+3515+3258+2029
lukeSilver=8458+4791+4826+3944+2456
lukeGold=6731+3699+3388+3189+3495
lukePlatinum=12775+5004+3881+2920+2766
lukeDiamond=4898+1269+809+516+255
lukeNonMaster=lukeRookie+lukeIron+lukeBronze+lukeSilver+lukeGold+lukePlatinum+lukeDiamond
lukeMaster=2959

jamieRookie=3989+1399+1420+1201+112
jamieIron=5196+2700+2523+2139+1277
jamieBronze=3589+2213+2306+1972+1235
jamieSilver=5563+3119+2876+2442+1529
jamieGold=4219+2299+2201+2011+2381
jamiePlatinum=8176+3286+2624+2051+1633
jamieDiamond=2935+868+595+409+188
jamieNonMaster=jamieRookie+jamieIron+jamieBronze+jamieSilver+jamieGold+jamiePlatinum+jamieDiamond
jamieMaster=1840

manonRookie=2629+1033+1118+997+911
manonIron=4256+2545+2836+2667+1705
manonBronze=4788+3120+3526+3322+2192
manonSilver=8641+5185+5126+4215+2509
manonGold=6989+3662+3307+3132+3311
manonPlatinum=12397+4905+3664+2900+2470
manonDiamond=4058+1081+709+443+183
manonNonMaster=manonRookie+manonIron+manonBronze+manonSilver+manonGold+manonPlatinum+manonDiamond
manonMaster=2358

kimberlyRookie=2950+1062+976+812+759
kimberlyIron=3339+1824+1889+1582+967
kimberlyBronze=2613+1669+1786+1526+1045
kimberlySilver=4157+2358+2316+1935+1176
kimberlyGold=3314+1760+1645+1492+1738
kimberlyPlatinum=6553+2629+2115+1688+1427
kimberlyDiamond=2655+670+469+321+141
kimberlyNonMaster=kimberlyRookie+kimberlyIron+kimberlyBronze+kimberlySilver+kimberlyGold+kimberlyPlatinum+kimberlyDiamond
kimberlyMaster=1934

marisaRookie=2340+911+1076+983+979
marisaIron=4315+2717+2929+2944+1885
marisaBronze=4942+3463+3733+3452+2276
marisaSilver=9179+5611+5695+4765+3092
marisaGold=8183+4547+4287+3800+4295
marisaPlatinum=16231+6628+5141+3825+3332
marisaDiamond=5374+1469+901+627+263
marisaNonMaster=marisaRookie+marisaIron+marisaBronze+marisaSilver+marisaGold+marisaPlatinum+marisaDiamond
marisaMaster=3150

lilyRookie=1200+485+510+472+496
lilyIron=2106+1242+1245+1229+774
lilyBronze=2111+1437+1509+1433+881
lilySilver=3548+2106+2064+1739+1074
lilyGold=3252+1719+1528+1405+1503
lilyPlatinum=5631+2234+1724+1311+1185
lilyDiamond=2025+470+296+219+103
lilyNonMaster=lilyRookie+lilyIron+lilyBronze+lilySilver+lilyGold+lilyPlatinum+lilyDiamond
lilyMaster=1003

jpRookie=1850+688+676+617+644
jpIron=2372+1339+1430+1270+833
jpBronze=2212+1409+1582+1415+924
jpSilver=3675+2292+2303+2089+1350
jpGold=3602+2072+2042+1873+2207
jpPlatinum=8914+3881+3163+2440+2243
jpDiamond=4031+1094+728+516+261
jpNonMaster=jpRookie+jpIron+jpBronze+jpSilver+jpGold+jpPlatinum+jpDiamond
jpMaster=3376

juriRookie=7090+2608+2569+2200+2084
juriIron=10401+5089+4942+4118+2268
juriBronze=6543+3945+3873+3331+1934
juriSilver=8665+4789+4563+3732+2205
juriGold=6322+3323+3096+2766+3113
juriPlatinum=12086+4995+3756+2773+2361
juriDiamond=4245+1228+815+558+277
juriNonMaster=juriRookie+juriIron+juriBronze+juriSilver+juriGold+juriPlatinum+juriDiamond
juriMaster=2768

deejayRookie=1792+670+702+661+620
deejayIron=2686+1604+1697+1549+1000
deejayBronze=2667+1836+2021+1916+1163
deejaySilver=4674+2951+2947+2513+1615
deejayGold=4276+2502+2394+2222+2477
deejayPlatinum=9338+4188+3309+2414+2274
deejayDiamond=3918+1178+723+581+249
deejayNonMaster=deejayRookie+deejayIron+deejayBronze+deejaySilver+deejayGold+deejayPlatinum+deejayDiamond
deejayMaster=3023

cammyRookie=7074+2695+2872+2481+2371
cammyIron=11892+6033+5719+4712+2764
cammyBronze=7675+4659+4594+3908+2304
cammySilver=10137+5578+5197+4156+2589
cammyGold=7026+3793+3447+3059+3696
cammyPlatinum=13794+5232+3980+3074+2539
cammyDiamond=4461+1349+829+595+284
cammyNonMaster=cammyRookie+cammyIron+cammyBronze+cammySilver+cammyGold+cammyPlatinum+cammyDiamond
cammyMaster=3340

ryuRookie=3893+1514+1648+1375+1416
ryuIron=6106+3672+3706+3421+2157
ryuBronze=5863+4073+4291+3978+2486
ryuSilver=10121+6156+5985+5239+3256
ryuGold=8900+5149+4873+4599+5514
ryuPlatinum=17474+7327+5686+4226+3659
ryuDiamond=6010+1446+991+593+289
ryuNonMaster=ryuRookie+ryuIron+ryuBronze+ryuSilver+ryuGold+ryuPlatinum+ryuDiamond
ryuMaster=2673

hondaRookie=1057+381+479+438+383
hondaIron=1753+1065+1149+1153+774
hondaBronze=2047+1388+1560+1594+1079
hondaSilver=3801+2511+2607+2357+1564
hondaGold=4053+2449+2364+2199+2227
hondaPlatinum=8195+3448+2832+2322+2172
hondaDiamond=4033+807+541+350+193
hondaNonMaster=hondaRookie+hondaIron+hondaBronze+hondaSilver+hondaGold+hondaPlatinum+hondaDiamond
hondaMaster=2175

blankaRookie=706+258+296+268+238
blankaIron=1119+616+735+738+507
blankaBronze=1162+844+878+857+604
blankaSilver=2307+1417+1551+1322+862
blankaGold=2397+1386+1327+1213+1421
blankaPlatinum=5062+2446+2026+1589+1448
blankaDiamond=2555+582+404+242+123
blankaNonMaster=blankaRookie+blankaIron+blankaBronze+blankaSilver+blankaGold+blankaPlatinum+blankaDiamond
blankaMaster=1401

guileRookie=1059+393+413+397+402
guileIron=1661+1015+1155+1111+769
guileBronze=1958+1322+1516+1536+1084
guileSilver=3980+2551+2619+2362+1555
guileGold=4071+2477+2401+2276+2612
guilePlatinum=8400+3603+2873+2152+2011
guileDiamond=3299+822+537+332+170
guileNonMaster=guileRookie+guileIron+guileBronze+guileSilver+guileGold+guilePlatinum+guileDiamond
guileMaster=1583

kenRookie=5152+2202+2393+2205+2198
kenIron=10807+6425+6832+6175+4057
kenBronze=10709+7177+7577+6834+4042
kenSilver=17206+10072+9547+7814+4505
kenGold=12068+6672+6314+5631+6692
kenPlatinum=21098+8537+6646+4877+4094
kenDiamond=6849+2169+1415+997+439
kenNonMaster=kenRookie+kenIron+kenBronze+kenSilver+kenGold+kenPlatinum+kenDiamond
kenMaster=4974

chunliRookie=3791+1297+1330+1086+1016
chunliIron=4780+2165+2212+1797+1146
chunliBronze=3017+1848+1940+1786+1078
chunliSilver=4543+2653+2556+2214+1370
chunliGold=3739+2030+1927+1861+2032
chunliPlatinum=6973+2862+2206+1757+1545
chunliDiamond=2621+793+513+340+172
chunliNonMaster=chunliRookie+chunliIron+chunliBronze+chunliSilver+chunliGold+chunliPlatinum+chunliDiamond
chunliMaster=1968

zangiefRookie=983+394+552+506+576
zangiefIron=2543+1846+2239+2456+1752
zangiefBronze=4464+3158+3777+3735+2356
zangiefSilver=9219+5879+5883+5275+3197
zangiefGold=8264+4937+4627+4152+4612
zangiefPlatinum=14169+5606+4252+2930+2628
zangiefDiamond=3569+940+575+372+151
zangiefNonMaster=zangiefRookie+zangiefIron+zangiefBronze+zangiefSilver+zangiefGold+zangiefPlatinum+zangiefDiamond
zangiefMaster=1592

dhalsimRookie=971+384+351+313+304
dhalsimIron=1290+729+754+691+396
dhalsimBronze=1160+792+772+738+483
dhalsimSilver=2042+1118+1095+989+613
dhalsimGold=1777+839+808+671+805
dhalsimPlatinum=3113+1287+990+758+646
dhalsimDiamond=1124+311+231+186+89
dhalsimNonMaster=dhalsimRookie+dhalsimIron+dhalsimBronze+dhalsimSilver+dhalsimGold+dhalsimPlatinum+dhalsimDiamond
dhalsimMaster=1114

rashidRookie=475+204+229+217+205
rashidIron=1008+683+792+654+458
rashidBronze=1303+962+1048+1018+719
rashidSilver=2952+1819+1771+1648+1100
rashidGold=2775+1630+1671+1634+1785
rashidPlatinum=5705+2825+2364+1807+1903
rashidDiamond=3301+822+507+355+148
rashidNonMaster=rashidRookie+rashidIron+rashidBronze+rashidSilver+rashidGold+rashidPlatinum+rashidDiamond
rashidMaster=1758

randomRookie=421+117+135+123+89
randomIron=415+213+210+180+96
randomBronze=307+207+171+196+129
randomSilver=494+312+286+275+183
randomGold=466+235+217+193+211
randomPlatinum=616+238+228+145+127
randomDiamond=312+18+11+10+6
randomNonMaster=randomRookie+randomIron+randomBronze+randomSilver+randomGold+randomPlatinum+randomDiamond
randomMaster=28

characters = ['Luke','Jamie','Manon','Kimberly','Marisa','Lily','JP','Juri',
              'Dee-Jay','Cammy','Ryu','E.Honda','Blanka','Guile','Ken','Chun-Li',
              'Zangief','Dhalsim','Rashid','Random']
masters = [lukeMaster,jamieMaster,manonMaster,kimberlyMaster,marisaMaster,lilyMaster,
           jpMaster,juriMaster,deejayMaster,cammyMaster,ryuMaster,hondaMaster,
           blankaMaster,guileMaster,kenMaster,chunliMaster,zangiefMaster,dhalsimMaster,
           rashidMaster,randomMaster]
nonMasters = [lukeNonMaster,jamieNonMaster,manonNonMaster,kimberlyNonMaster,marisaNonMaster,lilyNonMaster,
              jpNonMaster,juriNonMaster,deejayNonMaster,cammyNonMaster,ryuNonMaster,hondaNonMaster,
              blankaNonMaster,guileNonMaster,kenNonMaster,chunliNonMaster,zangiefNonMaster,dhalsimNonMaster,
              rashidNonMaster,randomNonMaster]

chartSize=plot.figure()
chartSize.set_figwidth(20)
chartSize.set_figheight(10)

xPosition=-1
#Add values to the chart
for value in range(len(characters)):
#    Check all Masters Values    
#    print(masters[value])
#    Check all Non-Masters' Values
#    print(nonMasters[value])
    xPosition+=1
    printableMaster=f'{masters[value]:,d}'
    plot.text(xPosition,int(masters[value]),printableMaster,ha='center')
    characterTotal=masters[value]+nonMasters[value]
    printableCharacterTotal=f'{characterTotal:,d}'
    printableNonMaster=f'{nonMasters[value]:,d}'
    plot.text(xPosition,characterTotal,printableCharacterTotal,ha='center')
    percentage=(masters[value]/characterTotal)*100
    roundPercentage=round(percentage,2)
    printablePercentage=str(roundPercentage) + '%'
    plot.text(xPosition,(characterTotal/2),printablePercentage,ha='center')

plot.bar(characters, masters, color='dodgerblue')
plot.bar(characters, nonMasters, bottom=masters, color='silver')
plot.xticks(rotation=90)
plot.show()