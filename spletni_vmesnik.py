import bottle
import model
import racunalnik
import random
import math


SKRIVNOST = 'abrakadabra'
PISKOTEK = 'idigre'

igre = model.Shramba()

@bottle.get('/')
def zacetna():
    return bottle.template('zacetna.html')

@bottle.get('/zacetna')
def vrnitev():
    return bottle.template('zacetna.html')

@bottle.post('/nova_igra_1/')
def nova_igra_1():
    id_igre = igre.nova_igra()
    bottle.response.set_cookie(PISKOTEK, str(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra_1/')

@bottle.post('/nova_igra_2/')
def nova_igra_2():
    id_igre = igre.nova_igra()
    bottle.response.set_cookie(PISKOTEK, str(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra_2/')

@bottle.get('/igra_1/')
def pokazi_igro_1():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, _ = igre.igre[id_igre]
    return bottle.template('igra_1.html', igra=igra)

@bottle.get('/igra_2/')
def pokazi_igro_2():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, _ = igre.igre[id_igre]
    return bottle.template('igra_2.html', igra=igra)

@bottle.post('/igra_kos1/')
def poteza_kos1():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    stolpec = int(bottle.request.forms.getunicode('stolpec_kos1'))
    igra, _ = igre.igre[id_igre]
    igra.celotna_poteza(stolpec, 1)
    bottle.redirect('/igra_2/')

@bottle.post('/igra_kos2/')
def poteza_kos2():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    stolpec = int(bottle.request.forms.getunicode('stolpec_kos2'))
    igra, _ = igre.igre[id_igre]
    igra.celotna_poteza(stolpec, 2)
    bottle.redirect('/igra_2/')

@bottle.post('/poteza_igralec/')
def poteza_igralec():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    stolpec = int(bottle.request.forms.getunicode('stolpec_igralec'))
    igra, _ = igre.igre[id_igre]
    igra.celotna_poteza(stolpec, 1)
    bottle.redirect('/igra_1/')

@bottle.post('/poteza_racunalnik/')
def poteza_racunalnik():
    id_igre = int(bottle.request.get_cookie(PISKOTEK, secret=SKRIVNOST))
    igra, _ = igre.igre[id_igre]
    stolpec = racunalnik.najboljsa_poteza(igra.polje, 2)
    igra.celotna_poteza(stolpec, 2)
    bottle.redirect('/igra_1/')











    











bottle.run(reloader=True, debug=True)
