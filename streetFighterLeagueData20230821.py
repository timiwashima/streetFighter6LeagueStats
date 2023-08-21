# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:55:11 2023

@author: tiwashima
"""

import matplotlib.pyplot as plot
import numpy

#Raw Data:
#https://www.streetfighter.com/6/buckler/ranking/league?character_filter=1&character_id=luke&platform=1&user_status=1&home_filter=1&home_category_id=0&home_id=1&league_rank=36&page=1
rookie1=53591
rookie2=20175
rookie3=21296
rookie4=18622
rookie5=18081
rookieTotal=rookie1+rookie2+rookie3+rookie4+rookie5

iron1=83916
iron2=46700
iron3=48236
iron4=43516
iron5=27351
ironTotal=iron1+iron2+iron3+iron4+iron5

bronze1=74049
bronze2=48635
bronze3=51700
bronze4=47523
bronze5=29895
bronzeTotal=bronze1+bronze2+bronze3+bronze4+bronze5

silver1=122760
silver2=72825
silver3=71421
silver4=60613
silver5=37495
silverTotal=silver1+silver2+silver3+silver4+silver5

gold1=101661
gold2=56876
gold3=53308
gold4=49039
gold5=55495
goldTotal=gold1+gold2+gold3+gold4+gold5

platinum1=194887
platinum2=80319
platinum3=62800
platinum4=47267
platinum5=41846
platinumTotal=platinum1+platinum2+platinum3+platinum4+platinum5

diamond1=71041
diamond2=19069
diamond3=12262
diamond4=8407
diamond5=3854
diamondTotal=diamond1+diamond2+diamond3+diamond4+diamond5

master=43516

#Pie Chart of all Leagues
pieChart=numpy.array([rookieTotal,ironTotal,bronzeTotal,silverTotal,goldTotal,platinumTotal,diamondTotal,master])
pieLabels=['Rookie','Iron','Bronze','Silver','Gold','Platinum','Diamond','Master']
pieColors=['green','slategrey','darkorange','silver','gold','skyblue','cyan','dodgerblue']
plot.pie(pieChart,labels=pieLabels,colors=pieColors,autopct='%1.1f%%')
plot.show()

#Bar Chart
leagueX=numpy.array(['Rookie 1','Rookie 2','Rookie 3','Rookie 4','Rookie 5',
                     'Iron 1','Iron 2','Iron 3','Iron 4', 'Iron 5',
                     'Bronze 1', 'Bronze 2', 'Bronze 3', 'Bronze 4','Bronze 5',
                     'Silver 1', 'Silver 2', 'Silver 3', 'Silver 4', 'Silver 5',
                     'Gold 1', 'Gold 2', 'Gold 3', 'Gold 4', 'Gold 5',
                     'Platinum 1', 'Platinum 2', 'Platinum 3', 'Platinum 4', 'Platinum 5',
                     'Diamond 1', 'Diamond 2', 'Diamond 3', 'Diamond 4', 'Diamond 5',
                     'Master'])
leagueY=[rookie1,rookie2,rookie3,rookie4,rookie5,
         iron1,iron2,iron3,iron4,iron5,
         bronze1,bronze2,bronze3,bronze4,bronze5,
         silver1,silver2,silver3,silver4,silver5,
         gold1,gold2,gold3,gold4,gold5,
         platinum1,platinum2,platinum3,platinum4,platinum5,
         diamond1,diamond2,diamond3,diamond4,diamond5,
         master]
barColors=['lime','springgreen','limegreen','forestgreen','green',
           'darkgrey','grey','dimgrey','lightslategrey','slategrey',
           'lightsalmon','sandybrown','coral','orange','darkorange',
           'gainsboro','lightgrey','silver','darkgrey','grey',
           'lemonchiffon','palegoldenrod','khaki','gold','yellow',
           'aquamarine','turquoise','mediumturquoise','lightseagreen','cadetblue',
           'lightskyblue','skyblue','lightsteelblue','cornflowerblue','royalblue',
           'blue']
plot.bar(leagueX,leagueY,color=barColors)
plot.xticks(rotation=90)
plot.show()