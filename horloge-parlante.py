from espeakng import ESpeakNG
import time
 
### Liste des mois
mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
 
### Liste des jours de la semaine
jour = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
 
##
## Prononce la date et l'heure
## @param t le moment (time)
##
def direHeure(t):
    esng = ESpeakNG(voice='fr')
 
    s = 'Nous sommes le ' + jour[t.tm_wday]
 
    if t.tm_mday == 1:
        s = s + ' premier'
    else:
        s = s + ' ' + str(t.tm_mday)
         
    s = s + ' ' + mois[t.tm_mon - 1] + '. ' + str(t.tm_year)
 
    if t.tm_hour == 12:
        s = s + 'Il est midi.'
    else:
        s = s + 'Il est : ' + str(t.tm_hour) + ' heure.'
    esng.say(s, sync=True)
 
##
## Prononce l'heure et les minutes
## @param t le moment (time)
##
def direHeureMin(t):
    esng = ESpeakNG(voice='fr')
    if t.tm_hour == 12:
        s = 'midi'
    else:
        s = str(t.tm_hour) + ' heure'
    esng.say(u'Il est : ' + s + ' ' + str(t.tm_min), sync=True)
   
##
## Prononce la date complète et l'heure
##  
def direTout():
    esng = ESpeakNG(voice='fr')
 
    esng.say('Bonjour.', sync=True)
 
    t = time.localtime()
    s = 'Nous sommes le '
    s = s + jour[t.tm_wday]
 
    if t.tm_mday == 1:
        s = s + ' premier'
    else:
        s = s + ' ' + str(t.tm_mday)
         
    s = s + ' ' + mois[t.tm_mon - 1]
    s = s + ' ' + str(t.tm_year)
 
    esng.say(s + '.', sync=True)
 
    s = 'Il est : '
    s = s + str(t.tm_hour) + ' heure'
    s = s + ' ' + str(t.tm_min) + ' et'
    s = s + ' ' + str(t.tm_sec) + ' seconde'
 
    esng.say(s + '.', sync=True)
 
 
##
## Début du programme
##
     
esng = ESpeakNG()
print(esng.voices)
     
direTout();
 
while True:
    t = time.localtime()
    if t.tm_sec == 0:        ## Minute entière
        if t.tm_min == 0:    ## Heure entière
            direHeure(t)                    
        else:
            direHeureMin(t)
    else:
        time.sleep(1);
