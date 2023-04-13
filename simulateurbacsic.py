from tkinter import *

base = Tk()
base.title('Simulateur des résultats du bac : édition SIC')
base.geometry("1360x700")

def pagelancement():
    fenetre = Canvas(base, width=1360, height=700)
    fenetre.place(x=1, y=1)
    bienvenue= Label(base, text="Bienvenue sur le simulateur SIC ! ", font=('Arvo',35))
    bienvenue.place(x=350, y=200)
    bcontinuer = Button(base, text = 'Continuer', font=("Joystix Monospace",20),command = mettre_notes, background='#ffffff')
    bcontinuer.place(x=590,y=530)


def mettre_notes():
    fenetre = Canvas(base, width=1360, height=700)
    fenetre.place(x=1, y=1)
    #initialisation
    global alatin1
    alatin1 = False
    global coptions
    coptions = 0
    global amathsexop
    amathsexop = False
    global adgemc
    adgemc = False
    global alatin2
    alatin2 = False
    #notes1ere
    consigne = Label(base, text="Notes de l'année dernière", font=('Arvo',20))
    consigne.place(x=50, y=30)
    global h1
    h1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    h1.place(x=50, y=100)
    h1.insert(0,'moyenne histoire(3)')
    global lva1
    lva1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    lva1.place(x=50, y=160)
    lva1.insert(0,'moyenne lva(3)')
    global lvb1
    lvb1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    lvb1.place(x=50, y=220)
    lvb1.insert(0,'moyenne lvb(3)')
    global ens1
    ens1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    ens1.place(x=50, y=280)
    ens1.insert(0,'moyenne ens(3)')
    global emc1
    emc1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    emc1.place(x=50, y=340)
    emc1.insert(0,'moyenne emc(1)')
    global spea
    spea = Entry(base, width=22, bg="#dedede", borderwidth=5,font=('Arvo',20))
    spea.place(x=50, y=400)
    spea.insert(0,'moyenne spe abandonnée(8)')
    global fre
    fre = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    fre.place(x=50, y=460)
    fre.insert(0,'français écrit(5)')
    global fro
    fro = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    fro.place(x=50, y=520)
    fro.insert(0,'français oral(5)')
    #notes terminale
    consigne2 = Label(base, text="Notes de cette année", font=('Arvo',20))
    consigne2.place(x=600, y=30)
    global h2
    h2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    h2.place(x=600, y=100)
    h2.insert(0,'moyenne histoire(3)')
    global lva2
    lva2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    lva2.place(x=600, y=160)
    lva2.insert(0,'moyenne lva(3)')
    global lvb2
    lvb2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    lvb2.place(x=600, y=220)
    lvb2.insert(0,'moyenne lvb(3)')
    global eps
    eps = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    eps.place(x=600, y=280)
    eps.insert(0,'moyenne eps(6)')
    global ens2
    ens2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    ens2.place(x=600, y=340)
    ens2.insert(0,'moyenne ens(3)')
    global emc2
    emc2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    emc2.place(x=600, y=400)
    emc2.insert(0,'moyenne emc(1)')
    global spe1
    spe1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    spe1.place(x=600, y=460)
    spe1.insert(0,'première spe(16)')
    global spe2
    spe2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    spe2.place(x=600, y=520)
    spe2.insert(0,'deuxième spe(16)')
    global philo
    philo = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    philo.place(x=600, y=580)
    philo.insert(0,'philo(8)')
    global go
    go = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    go.place(x=600, y=640)
    go.insert(0,'grand oral(10)')
    global llco
    llco = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    llco.place(x=900, y=100)
    llco.insert(0,'llc oral(5)')
    global llce
    llce = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    llce.place(x=900, y=160)
    llce.insert(0,'llc ecrit(10)')
    global mc
    mc = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    mc.place(x=900, y=220)
    mc.insert(0,'maths chinois(10)')
    #checkbox
    vlatin1 = Checkbutton(base, text = "Latin ?", command = mlatin1, font=('Arvo',15) )
    vlatin1.pack()
    vlatin1.place(x=50,y=580)
    vmaths = Checkbutton(base, text = "Maths expertes, complémentaires ?", command =mathsexop, font=('Arvo',15))
    vmaths.pack()
    vmaths.place(x=900, y=280)
    vdroit = Checkbutton(base, text = "DGEMC ?", command = dgmc, font=('Arvo',15))
    vdroit.pack()
    vdroit.place(x=900, y=400)
    vlatin2 = Checkbutton(base, text = "Latin ?", command = mlatin2, font=('Arvo',15))
    vlatin2.pack()
    vlatin2.place(x=900, y=520)
    #bouton continuer
    bcontinuer2 = Button(base, text = 'Continuer', font=("Joystix Monospace",15),command = resultats, background='#ffffff')
    bcontinuer2.place(x=1100,y=30)

def mlatin1():
    global alatin1
    alatin1 = True
    global coptions 
    coptions += 2
    global latin1
    latin1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    latin1.place(x=50, y=640)
    latin1.insert(0,'latin(2)')

def mathsexop():
    global amathsexop
    amathsexop = True
    global coptions 
    coptions += 2
    global mathsop
    mathsop = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    mathsop.place(x=900, y=340)
    mathsop.insert(0,'maths ex/comp(2)')

def dgmc():
    global adgemc
    adgemc = True
    global coptions 
    coptions += 2
    global dgmc1
    dgmc1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    dgmc1.place(x=900, y=460)
    dgmc1.insert(0,'dgemc(2)')

def mlatin2():
    global coptions 
    coptions += 2
    global latin2
    latin2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
    latin2.place(x=900, y=580)
    latin2.insert(0,'latin(2)')

def retour():
        #pareil que resultat mais on change juste les insert avec ce qu'on avait récupéré lors de la première saisie
        fenetre = Canvas(base, width=1360, height=700)
        fenetre.place(x=1, y=1)
        #initialisation
        global alatin1
        alatin1 = False
        global coptions
        coptions = 0
        global amathsexop
        amathsexop = False
        global adgemc
        adgemc = False
        global alatin2
        alatin2 = False
        #notes1ere
        consigne = Label(base, text="Notes de l'année dernière", font=('Arvo',20))
        consigne.place(x=50, y=30)
        global h1
        h1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        h1.place(x=50, y=100)
        h1.insert(0,nh1)
        global lva1
        lva1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        lva1.place(x=50, y=160)
        lva1.insert(0,nlva1)
        global lvb1
        lvb1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        lvb1.place(x=50, y=220)
        lvb1.insert(0,nlvb1)
        global ens1
        ens1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        ens1.place(x=50, y=280)
        ens1.insert(0,nens1)
        global emc1
        emc1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        emc1.place(x=50, y=340)
        emc1.insert(0,nemc1)
        global spea
        spea = Entry(base, width=22, bg="#dedede", borderwidth=5,font=('Arvo',20))
        spea.place(x=50, y=400)
        spea.insert(0,nspea)
        global fre
        fre = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        fre.place(x=50, y=460)
        fre.insert(0,nfre)
        global fro
        fro = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        fro.place(x=50, y=520)
        fro.insert(0,nfro)
        #notes terminale
        consigne2 = Label(base, text="Notes de cette année", font=('Arvo',20))
        consigne2.place(x=600, y=30)
        global h2
        h2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        h2.place(x=600, y=100)
        h2.insert(0,nh2)
        global lva2
        lva2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        lva2.place(x=600, y=160)
        lva2.insert(0,nlva2)
        global lvb2
        lvb2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        lvb2.place(x=600, y=220)
        lvb2.insert(0,nlvb2)
        global eps
        eps = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        eps.place(x=600, y=280)
        eps.insert(0,neps)
        global ens2
        ens2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        ens2.place(x=600, y=340)
        ens2.insert(0,nens2)
        global emc2
        emc2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        emc2.place(x=600, y=400)
        emc2.insert(0,nemc2)
        global spe1
        spe1 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        spe1.place(x=600, y=460)
        spe1.insert(0,nspe1)
        global spe2
        spe2 = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        spe2.place(x=600, y=520)
        spe2.insert(0,nspe2)
        global philo
        philo = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        philo.place(x=600, y=580)
        philo.insert(0,nphilo)
        global go
        go = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        go.place(x=600, y=640)
        go.insert(0,ngo)
        global llco
        llco = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        llco.place(x=900, y=100)
        llco.insert(0,nllco)
        global llce
        llce = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        llce.place(x=900, y=160)
        llce.insert(0,nllce)
        global mc
        mc = Entry(base, width=15, bg="#dedede", borderwidth=5,font=('Arvo',20))
        mc.place(x=900, y=220)
        mc.insert(0,nmc)
        #checkbox
        vlatin1 = Checkbutton(base, text = "Latin ?", command = mlatin1, font=('Arvo',15) )
        vlatin1.pack()
        vlatin1.place(x=50,y=580)
        vmaths = Checkbutton(base, text = "Maths expertes, complémentaires ?", command =mathsexop, font=('Arvo',15))
        vmaths.pack()
        vmaths.place(x=900, y=280)
        vdroit = Checkbutton(base, text = "DGEMC ?", command = dgmc, font=('Arvo',15))
        vdroit.pack()
        vdroit.place(x=900, y=400)
        vlatin2 = Checkbutton(base, text = "Latin ?", command = mlatin2, font=('Arvo',15))
        vlatin2.pack()
        vlatin2.place(x=900, y=520)
        #bouton continuer
        bcontinuer2 = Button(base, text = 'Continuer', font=("Joystix Monospace",15),command = resultats, background='#ffffff')
        bcontinuer2.place(x=1100,y=30)
 
def resultats():
    #calcul total des coefficients
    cototaux = 60 + 40 + 25 + coptions
    #sauvegarde de ce qui est marqué
    global nh1
    nh1 = h1.get()
    global nh2
    nh2 = h2.get()
    global nlva1
    nlva1 = lva1.get()
    global nlva2
    nlva2 = lva2.get()
    global nlvb1
    nlvb1 = lvb1.get()
    global nlvb2
    nlvb2 = lvb2.get()
    global neps
    neps = eps.get()
    global nens1
    nens1 = ens1.get()
    global nens2
    nens2 = ens2.get()
    global nemc1
    nemc1 = emc1.get()
    global nemc2
    nemc2 = emc2.get()
    global nspea
    nspea = spea.get()
    global nfre
    nfre = fre.get()
    global nfro
    nfro = fro.get()
    global nspe1
    nspe1 = spe1.get()
    global nspe2
    nspe2 = spe2.get()
    global nphilo
    nphilo = philo.get()
    global ngo
    ngo = go.get()
    global nllco
    nllco = llco.get()
    global nllce
    nllce = llce.get()
    global nmc
    nmc = mc.get()
    #création canvas
    fenetre = Canvas(base, width=1360, height=700)
    fenetre.place(x=1, y=1)
    #bouton retour 
    bretour = Button(base, text = 'Retour', font=("Joystix Monospace",15),command =retour, background='#ffffff')
    bretour.place(x=100,y=30)
    #contenu du tableau
    ticalcul = Label(base, text="Calcul des résulats", font=('Arvo',30))
    ticalcul.place(x=600, y=30)
    tiep = Label(base, text="Epreuves terminales                            60", font=('Arvo',20))
    tiep.place(x=100, y=250)
    ticc = Label(base, text="Contrôle continu                                   40", font=('Arvo',20))
    ticc.place(x=100, y=300)
    tisic = Label(base, text="SIC                                                                 25", font=('Arvo',20))
    tisic.place(x=100, y=350)
    tiop = Label(base, text="Options                                                         " + str(coptions), font=('Arvo',20))
    tiop.place(x=100, y=400)
    tito = Label(base, text="Totaux                                                         "+ str(cototaux), font=('Arvo',20))
    tito.place(x=100, y=450)
    tico = Label(base, text="Coefficients", font=('Arvo',20))
    tico.place(x=500, y=150)
    tipo = Label(base, text="Points", font=('Arvo',20))
    tipo.place(x=800, y=150)
    timo = Label(base, text="Moyenne finale", font=('Arvo',25))
    timo.place(x=100, y=525)
    #lignes et colonnes du tableau 
    horizontal = Label(base, text="_______________________________________________________________", font=('Arvo',20))
    horizontal.place(x=75, y=185)
    vertical = Label(base, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", font=('Arvo',20))
    vertical.place(x=400, y=130)
    vertical2 = Label(base, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", font=('Arvo',20))
    vertical2.place(x=720, y=130)
    #calcul des moyennes pondérées
    #on calcule la somme des notes multipliées par leur coefficient
    ep =  int(fre.get())*5 + int(fro.get())*5 +int(spe1.get())*16 + int(spe2.get())*16 + int(philo.get())*8 + int(go.get())*10 
    cc = float(h1.get())*3 + float(lva1.get())*3 + float(lvb1.get())*3 + float(ens1.get())*3 + float(emc1.get())*1 + int(spea.get())*8 + float(h2.get())*3 + float(lva2.get())*3 + float(lvb2.get())*3 + float(eps.get())*6 + float(ens2.get())*3 + float(emc2.get())*1
    sic = int(llco.get())*5 + int(llce.get())*10 + int(mc.get())*10
    op = 0
    if alatin1 == True :
        op += int(latin1.get())*2
    if amathsexop == True :
        op += int(mathsop.get())*2
    if adgemc == True :
        op += int(dgmc1.get())*2
    if alatin2 == True :
        op += int(latin2.get())*2
    #calcul total des points
    totalpoints = ep + cc + sic + op
    #affichage de tout
    rep = Label(base, text= ep, font=('Arvo',20))
    rep.place(x=800, y=250)
    rcc = Label(base, text= cc, font=('Arvo',20))
    rcc.place(x=800, y=300)
    rsic = Label(base, text= sic, font=('Arvo',20))
    rsic.place(x=800, y=350)
    rop = Label(base, text= op, font=('Arvo',20))
    rop.place(x=800, y=400)
    rtp = Label(base, text= totalpoints, font=('Arvo',20))
    rtp.place(x=800, y=450)
    #calcul de la moyenne
    moyenne = totalpoints/cototaux
    rmo = Label(base, text= moyenne, font=('Arvo',30))
    rmo.place(x=800, y=525)
    #calcul de la mention obtenue grace à la moyenne
    if moyenne < 12 :
        mention = "pas de mention"
    elif moyenne < 14 and moyenne >= 12 :
        mention = "assez bien !"
    elif moyenne < 16 and moyenne >= 14 :
        mention = "bien !"
    elif moyenne >= 16 :
        mention = 'très bien !'
    affmention = Label(base, text= "Tu obtiens la mention " + mention, font=('Arvo',25))
    affmention.place(x=300,y=600)

pagelancement()
base.mainloop()