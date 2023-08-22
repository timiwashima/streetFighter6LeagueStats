# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:37:47 2023

@author: tiwashima
"""

import matplotlib.pyplot
import numpy

lukes=2381
jamies=1398
manons=1737
kimberlys=1465
marisas=2462
lilys=737
jps=2651
juris=2154
deejays=2337
cammys=2593
ryus=2093
hondas=1589
blankas=1065
guiles=1294
kens=4054
chunlis=1553
zangiefs=1310
dhalsims=903
rashids=1490
randoms=23

characterNames=numpy.array(['Luke','Jamie','Manon','Kimberly','Marisa','Lily',
                            'JP','Juri','Dee-Jay','Cammy','Ryu','E. Honda',
                            'Blanka','Guile','Ken','Chun-Li','Zangief','Dhalsim',
                            'Rashid','Random'])
masterCount=[lukes,jamies,manons,kimberlys,marisas,lilys,jps,juris,deejays,
             cammys,ryus,hondas,blankas,guiles,kens,chunlis,zangiefs,dhalsims,
             rashids,randoms]
barColors=['blue','yellow','pink','red','maroon','teal','sienna','magenta',
           'brown','green','red','blue','green','navy','red','dodgerblue',
           'crimson','sienna','grey','midnightblue']
matplotlib.pyplot.bar(characterNames,masterCount,color=barColors)
matplotlib.pyplot.xticks(rotation=90)
matplotlib.pyplot.show()