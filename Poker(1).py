from random import*
import time
y=input('Bienvenido a nuestra mesa de poker, si quieres jugar escribe J, sino oprime 0')
#Cartas:
#A
Ap='Ap'
At='At'
Ad='Ad'
Ac='Ac'
#2
dp='2p'
dt='2t'
dd='2d'
dc='2c'
#3
tp='3p'
tt='3t'
td='3d'
tc='3c'
#4
cp='4p'
ct='4t'
cd='4d'
cc='4c'
#5
Cp='5p'
Ct='5t'
Cd='5d'
Cc='5c'
#6
sp='6p'
st='6t'
sd='6d'
sc='6c'
#7
Sp='7p'
St='7t'
Sd='7d'
Sc='7c'
#8
op='8p'
ot='8t'
od='8d'
oc='8c'
#9
np='9p'
nt='9t'
nd='9d'
nc='9c'
#10
Dp='10p'
Dt='10t'
Dd='10d'
Dc='10c'
#J
jp='Jp'
jt='Jt'
jd='Jd'
jc='Jc'
#Q
qp='Qp'
qt='Qt'
qd='Qd'
qc='Qc'
#K
kp='Kp'
kt='Kt'
kd='Kd'
kc='Kc'
DineroJ=1000
DineroM=1000
if(y=='J'):
    print ('Tienes',DineroJ,'dolares, la apuesta minima de cada juego son 10 dolares')
    print ('Jugadas: Carta alta < par < doble par < terna < escalera < color\n\
< full house < poker < escalera de color < flor imperial')
    print('Las cartas estan escritas de esta manera: Ad, esto significa As de Diamantes,At seria As de Trebol, etc,')
else:
    exit('Gracias por Jugar')
ApuestaP=0
ApuestaF=0
ApuestaT=0
ApuestaR=0
while(DineroJ>0)and(DineroM>0):
    ApuestaP=0
    ApuestaF=0
    ApuestaT=0
    ApuestaR=0
    ApuestaTotal=0
    CartasSobreLaMesa=[]
    L=[Ap,At,Ad,Ac,dp,dt,dd,dc,tp,tt,td,tc,cp,ct,cd,cc,Cp,Ct,Cd,Cc,sp,st,sd,sc,Sp,St,Sd,Sc,op,ot,od,oc,np,nt,nd,nc,Dp,Dt,Dd,Dc,jp,jt,jd,jc,qp,qt,qd,qc,kp,kt,kd,kc]
    L.sort()
    CartasJ1=choice(L)
    L.remove(CartasJ1)
    CartasM1=choice(L)
    L.remove(CartasM1)
    CartasJ2=choice(L)
    L.remove(CartasJ2)
    CartasM2=choice(L)
    L.remove(CartasM2)
    print ('Estas son tus cartas:',CartasJ1,CartasJ2,'apuestas:')
    ApuestaP=int(input('Cuanto apuestas?'))
    ApuestaTotal=ApuestaP
    while(0<ApuestaP<10):
        print('La apuesta minima son 10 dolares')
        ApuestaP=0
        ApuestaTotal=0
        ApuestaP=int(input('Cuanto apuestas?'))
        ApuestaTotal=ApuestaP
    DineroJ=DineroJ-ApuestaP
    print('Tu dinero:',DineroJ)
    A=[1,2]
    q=choice(A)
    if(q==1):
        print('Tu oponente iguala la apuesta')
        DineroM=DineroM-ApuestaP
        ApuestaTotal=ApuestaP+ApuestaP
    else:
        print('Tu oponente sube la apuesta')
        B=[10,20,50,100]
        e=choice(B)
        if(e==10):
            print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
            DineroM=DineroM-ApuestaP-e
            ApuestaTotal=ApuestaP+ApuestaP+e
            r=int(input('Oprime 10 para igualar o 0 para retirarte'))
            if(r==10):
                DineroJ=DineroJ-e
                ApuestaTotal=ApuestaTotal+r
                print('Tu dinero:', DineroJ)
            else:
                exit('Gracias por Jugar')
        elif(e==20):
            print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
            DineroM=DineroM-ApuestaP-e
            ApuestaTotal=ApuestaP+ApuestaP+e
            r=int(input('Oprime 20 para igualar o 0 para retirarte'))
            if(r==20):
                DineroJ=DineroJ-e
                ApuestaTotal=ApuestaTotal+r
                print('Tu dinero:',DineroJ)
            else:
                exit('Gracias por Jugar')
        elif(e==50):
            print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
            DineroM=DineroM-ApuestaP-e
            ApuestaTotal=ApuestaP+ApuestaP+e
            r=int(input('Oprime 50 para igualar o 0 para retirarte'))
            if(r==50):
                DineroJ=DineroJ-e
                ApuestaTotal=ApuestaTotal+r
                print('Tu dinero:',DineroJ)
            else:
                exit('Gracias por Jugar')
        else:
            print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
            DineroM=DineroM-ApuestaP-e
            ApuestaTotal=ApuestaP+ApuestaP+e
            r=int(input('Oprime 100 para igualar o 0 para retirarte'))
            if(r==100):
                DineroJ=DineroJ-e
                ApuestaTotal=ApuestaTotal+r
                print('Tu dinero:',DineroJ)
            else:
                exit('Gracias por Jugar')
#Flop
    Quema1=choice(L)
    L.remove(Quema1)
    Flop1=choice(L)
    CartasSobreLaMesa.append(Flop1)
    L.remove(Flop1)
    Flop2=choice(L)
    CartasSobreLaMesa.append(Flop2)
    L.remove(Flop2)
    Flop3=choice(L)
    CartasSobreLaMesa.append(Flop3)
    L.remove(Flop3)
    print ('Las primeras 3 cartas son:',Flop1,Flop2,Flop3)
    print('Tus cartas:',CartasJ1,CartasJ2)
    p=input('Apuestas o check?\n\
(para apostar escribe A, para chequear escribe Check)')
    if(p=='A'):
        ApuestaF=int(input('Cuanto apuestas?'))
        if(ApuestaF>=10):
            ApuestaTotal=ApuestaTotal+ApuestaF
        while(0<ApuestaF<10):
            print('La apuesta minima son 10 dolares')
            ApuestaF=0
            ApuestaF=int(input('Cuanto apuestas?'))
            if(ApuestaF>=10):
                ApuestaTotal=ApuestaTotal+ApuestaF
        DineroJ=DineroJ-ApuestaF
        print('Tu dinero:',DineroJ)
        q=choice(A)
        if(q==1):
            print('Tu oponente iguala la apuesta')
            DineroM=DineroM-ApuestaF
            ApuestaTotal=ApuestaTotal+ApuestaF
            print('Tu dinero:',DineroJ)
        else:
            print('Tu oponente sube la apuesta')
            B=[10,20,50,100]
            e=choice(B)
            if(e==10):
                print('Tu oponente añade',e,'dolar a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaF
                ApuestaTotal=ApuestaF+ApuestaF+e
                r=int(input('Oprime 10 para igualar o 0 para retirarte'))
                if(r==10):
                    DineroJ=DineroJ-e
                    print('Tu dinero:', DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==20):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaF
                ApuestaTotal=ApuestaTotal+ApuestaF+e
                r=int(input('Oprime 20 para igualar o 0 para retirarte'))
                if(r==20):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==50):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaF
                ApuestaTotal=ApuestaTotal+ApuestaF+e
                r=int(input('Oprime 50 para igualar o 0 para retirarte'))
                if(r==50):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            else:
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaF
                ApuestaTotal=ApuestaTotal+ApuestaF+e
                r=int(input('Oprime 100 para igualar o 0 para retirarte'))
                if(r==100):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
    else:
        q=choice(A)
        if(q==1):
            print('Tu oponente chequea')
            ApuestaTotal=ApuestaTotal
            print('Tu dinero:',DineroJ)
        else:
            print('Tu oponente sube la apuesta')
            B=[10,20,50,100]
            e=choice(B)
            if(e==10):
                print('Tu oponente añade',e,'dolar a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:', DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==20):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escrbe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==50):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            else:
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
#Turn
    Quema2=choice(L)
    L.remove(Quema2)
    Turn=choice(L)
    CartasSobreLaMesa.append(Turn)
    L.remove(Turn)
    print('Las cartas hasta el Turn son:',Flop1,Flop2,Flop3,Turn)
    print('Tus cartas:',CartasJ1,CartasJ2)
    p=input('Apuestas o check?\n\
(para apostar escribe A, para chequear escribe Check)')
    if(p=='A'):
        ApuestaT=int(input('Cuanto apuestas?'))
        if(ApuestaT>=10):
            ApuestaTotal=ApuestaTotal+ApuestaT
        while(0<ApuestaT<10):
            print('La apuesta minima son 10 dolares')
            ApuestaT=0
            ApuestaT=int(input('Cuanto apuestas?'))
            if(ApuestaT>=10):
                ApuestaTotal=ApuestaTotal+ApuestaT
        DineroJ=DineroJ-ApuestaT
        print('Tu dinero:',DineroJ)
        q=choice(A)
        if(q==1):
            print('Tu oponente iguala la apuesta')
            DineroM=DineroM-ApuestaT
            ApuestaTotal=ApuestaTotal+ApuestaT
            print('Tu dinero:',DineroJ)
        else:
            print('Tu oponente sube la apuesta')
            B=[10,20,50,100]
            e=choice(B)
            if(e==10):
                print('Tu oponente añade',e,'dolar a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaT
                ApuestaTotal=ApuestaTotal+ApuestaT+e
                r=int(input('Oprime 10 para igualar o 0 para retirarte'))
                if(r==10):
                    DineroJ=DineroJ-e
                    print('Tu dinero:', DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==20):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaT
                ApuestaTotal=ApuestaTotal+ApuestaT+e
                r=int(input('Oprime 20 para igualar o 0 para retirarte'))
                if(r==20):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==50):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaT
                ApuestaTotal=ApuestaTotal+ApuestaT+e
                r=int(input('Oprime 50 para igualar o 0 para retirarte'))
                if(r==50):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            else:
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaT
                ApuestaTotal=ApuestaTotal+ApuestaT+e
                r=int(input('Oprime 100 para igualar o 0 para retirarte'))
                if(r==100):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
    else:
        q=choice(A)
        if(q==1):
            print('Tu oponente chequea')
            ApuestaTotal=ApuestaTotal
            print('Tu dinero:',DineroJ)
        else:
            print('Tu oponente sube la apuesta')
            B=[10,20,50,100]
            e=choice(B)
            if(e==10):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-ApuestaT-e
                    print('Tu dinero:', DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==20):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-ApuestaT-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==50):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-ApuestaT-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            else:
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                ApuestaTotal=ApuestaTotal+e
                DineroM=DineroM-ApuestaT
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-ApuestaT-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
#River
    Quema3=choice(L)
    L.remove(Quema3)
    River=choice(L)
    CartasSobreLaMesa.append(River)
    L.remove(River)
    print('Todas las cartas hasta el River son:',Flop1,Flop2,Flop3,Turn,River,)
    print('Tus cartas:',CartasJ1,CartasJ2)
    p=input('Apuestas o check?\n\
(para apostar escribe A, para chequear escribe Check)')
    if(p=='A'):
        ApuestaR=int(input('Cuanto apuestas?'))
        if(ApuestaR>=10):
            ApuestaTotal=ApuestaTotal+ApuestaR
        while(0<ApuestaR<10):
            print('La apuesta minima son 10 dolares')
            ApuestaR=0
            ApuestaR=int(input('Cuanto apuestas?'))
            if(ApuestaR>=10):
                ApuestaTotal=ApuestaTotal+ApuestaR
        DineroJ=DineroJ-ApuestaR
        print('Tu dinero:',DineroJ)
        q=choice(A)
        if(q==1):
            print('Tu oponente iguala la apuesta')
            DineroM=DineroM-ApuestaR
            ApuestaTotal=ApuestaTotal+ApuestaR
            print('Tu dinero:',DineroJ)
        else:
            print('Tu oponente sube la apuesta')
            B=[10,20,50,100]
            e=choice(B)
            if(e==10):
                print('Tu oponente añade',e,'dolar a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaR
                ApuestaTotal=ApuestaTotal+ApuestaR+e
                r=int(input('Oprime 10 para igualar o 0 para retirarte'))
                if(r==10):
                    DineroJ=DineroJ-e
                    print('Tu dinero:', DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==20):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaR
                ApuestaTotal=ApuestaTotal+ApuestaR+e
                r=int(input('Oprime 20 para igualar o 0 para retirarte'))
                if(r==20):
                    DineroJ=DineroJ-r
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==50):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaR
                ApuestaTotal=ApuestaTotal+ApuestaR+e
                r=int(input('Oprime 50 para igualar o 0 para retirarte'))
                if(r==50):
                    DineroJ=DineroJ-r
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            else:
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e-ApuestaR
                ApuestaTotal=ApuestaTotal+ApuestaR+e
                r=int(input('Oprime 100 para igualar o 0 para retirarte'))
                if(r==100):
                    DineroJ=DineroJ-r
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
    else:
        q=choice(A)
        if(q==1):
            print('Tu oponente chequea')
            ApuestaTotal=ApuestaTotal
            print('Tu dinero:',DineroJ)
        else:
            print('Tu oponente sube la apuesta')
            B=[10,20,50,100]
            e=choice(B)
            if(e==10):
                print('Tu oponente añade',e,'dolar a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:', DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==20):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            elif(e==50):
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
            else:
                print('Tu oponente añade',e,'dolares a la apuesta\n\
Igualas o te retiras?')
                DineroM=DineroM-e
                ApuestaTotal=ApuestaTotal+e
                r=int(input('Escribe 1 para igualar o 0 para retirarte'))
                if(r==1):
                    DineroJ=DineroJ-e
                    print('Tu dinero:',DineroJ)
                    ApuestaTotal=ApuestaTotal+e
                else:
                    exit('Gracias por Jugar')
    print('Tus cartas:',CartasJ1,CartasJ2,'Cartas de tu oponente:',CartasM1,CartasM2,'Las cartas sobre la mesa son:\n\
',CartasSobreLaMesa)
    print('Calculando la jugada ganadora.')
    time.sleep(1)
    print('Calculando la jugada ganadora..')
    time.sleep(1)
    print('Calculando la jugada ganadora...')
    time.sleep(1.5)
#Jugadas
    JugadaJ=0
    JugadaM=0
#Flor imperial
#Picas
    FlorImperialPicasJ=[dp,jp,qp,kp,Ap]
    FlorImperialPicasM=[dp,jp,qp,kp,Ap]
    if(Dp in CartasSobreLaMesa):
        FlorImperialPicasJ.append(Dp)
        FlorImperialPicasM.append(Dp)
        if(CartasJ1==jp)or(CartasJ1==qp)or(CartasJ1==kp)or(CartasJ1==Ap):
            FlorImperialPicasJ.append(CartasJ1)
        elif(CartasM1==jp)or(CartasM1==qp)or(CartasM1==kp)or(CartasM1==Ap):
            FlorImperialPicasM.append(CartasM1)
        elif(CartasJ2==jp)or(CartasJ2==qp)or(CartasJ2==kp)or(CartasJ2==Ap):
            FlorImperialPicasJ.append(CartasJ2)
        elif(CartasM2==jp)or(CartasM2==qp)or(CartasM2==kp)or(CartasM2==Ap):
            FlorImperialPicasM.append(CartasM2)
    elif(jp in CartasSobreLaMesa):
        FlorImperialPicasJ.append(jp)
        FlorImperialPicasM.append(jp)
        if(CartasJ1==Dp)or(CartasJ1==qp)or(CartasJ1==kp)or(CartasJ1==Ap):
           FlorImperialPicasJ.append(CartasJ1)
        elif(CartasM1==Dp)or(CartasM1==qp)or(CartasM1==kp)or(CartasM1==Ap):
            FlorImperialPicasM.append(CartasM1)
        elif(CartasJ2==Dp)or(CartasJ2==qp)or(CartasJ2==kp)or(CartasJ2==Ap):
            FlorImperialPicasJ.append(CartasJ2)
        elif(CartasM2==Dp)or(CartasM2==qp)or(CartasM2==kp)or(CartasM2==Ap):
            FlorImperialPicasM.append(CartasM2)
    elif(qp in CartasSobreLaMesa):
        FlorImperialPicasJ.append(qp)
        FlorImperialPicasM.append(qp)
        if(CartasJ1==Dp)or(CartasJ1==jp)or(CartasJ1==kp)or(CartasJ1==Ap):
            FlorImperialPicasJ.append(CartasJ1)
        elif(CartasM1==Dp)or(CartasM1==jp)or(CartasM1==kp)or(CartasM1==Ap):
            FlorImperialPicasM.append(CartasM1)
        elif(CartasJ2==Dp)or(CartasJ2==jp)or(CartasJ2==kp)or(CartasJ2==Ap):
            FlorImperialPicasJ.append(CartasJ2)
        elif(CartasM2==Dp)or(CartasM2==jp)or(CartasM2==kp)or(CartasM2==Ap):
            FlorImperialPicasM.append(CartasM2)
    elif(kp in CartasSobreLaMesa):
        FlorImperialPicasJ.append(kp)
        FlorImperialPicasM.append(kp)
        if(CartasJ1==Dp)or(CartasJ1==jp)or(CartasJ1==qp)or(CartasJ1==Ap):
            FlorImperialPicasJ.append(CartasJ1)
        elif(CartasM1==Dp)or(CartasM1==jp)or(CartasM1==qp)or(CartasM1==Ap):
            FlorImperialPicasM.append(CartasM1)
        elif(CartasJ2==Dp)or(CartasJ2==jp)or(CartasJ2==qp)or(CartasJ2==Ap):
            FlorImperialPicasJ.append(CartasJ2)
        elif(CartasM2==Dp)or(CartasM2==jp)or(CartasM2==qp)or(CartasM2==Ap):
            FlorImperialPicasM.append(CartasM2)
    elif(Ap in CartasSobreLaMesa):
        FlorImperialPicasJ.append(Ap)
        FlorImperialPicasM.append(Ap)
        if(CartasJ1==Dp)or(CartasJ1==jp)or(CartasJ1==qp)or(CartasJ1==kp):
            FlorImperialPicasJ.append(CartasJ1)
        elif(CartasM1==Dp)or(CartasM1==jp)or(CartasM1==qp)or(CartasM1==kp):
            FlorImperialPicasM.append(CartasM1)
        elif(CartasJ2==Dp)or(CartasJ2==jp)or(CartasJ2==qp)or(CartasJ2==kp):
            FlorImperialPicasJ.append(CartasJ2)
        elif(CartasM2==Dp)or(CartasM2==jp)or(CartasM2==qp)or(CartasM2==kp):
            FlorImperialPicasM.append(CartasM2)
        FlorImperialPicasJ[0]=Dp;
        FlorImperialPicasJ[1]=jp;
        FlorImperialPicasJ[2]=qp;
        FlorImperialPicasJ[3]=kp;
        FlorImperialPicasJ[4]=Ap;
        FlorImperialPicasM[0]=Dp;
        FlorImperialPicasM[1]=jp;
        FlorImperialPicasM[2]=qp;
        FlorImperialPicasM[3]=kp;
        FlorImperialPicasM[4]=Ap;
    if(FlorImperialPicasJ==[Dp,jp,qp,kp,Ap]):
        print('Felicitaciones, obtuviste una flor imperial, la jugada mas alta de todas, ganas automaticamente')
        DineroJ=ApuestaTotal+DineroJ
        JugadaJ=10
    elif(FlorImperialPicasM==[Dp,jp,qp,kp,Ap]):
        print('Desgraciadamente tu oponente obtuvo una flor imperial, la jugada mas alta del juego, pierdes automaticamet')
        DineroM=ApuestaTotal+DineroM
        JugadaM=10
#Trebol
    FlorImperialTrebolJ=[dt,jt,qt,kt,At]
    FlorImperialTrebolM=[dt,jt,qt,kt,At]
    if(Dt in CartasSobreLaMesa):
        FlorImperialTrebolJ.append(Dt)
        FlorImperialTrebolM.append(Dt)
        if(CartasJ1==jt)or(CartasJ1==qt)or(CartasJ1==kt)or(CartasJ1==At):
            FlorImperialTrebolJ.append(CartasJ1)
        elif(CartasM1==jt)or(CartasM1==qt)or(CartasM1==kt)or(CartasM1==At):
            FlorImperialTrebolM.append(CartasM1)
        elif(CartasJ2==jt)or(CartasJ2==qt)or(CartasJ2==kt)or(CartasJ2==At):
            FlorImperialTrebolJ.append(CartasJ2)
        elif(CartasM2==jt)or(CartasM2==qt)or(CartasM2==kt)or(CartasM2==At):
            FlorImperialTrebolM.append(CartasM2)
    elif(jt in CartasSobreLaMesa):
        FlorImperialTrebolJ.append(jt)
        FlorImperialTrebolM.append(jt)
        if(CartasJ1==Dt)or(CartasJ1==qt)or(CartasJ1==kt)or(CartasJ1==At):
            FlorImperialTrebolJ.append(CartasJ1)
        elif(CartasM1==Dt)or(CartasM1==qt)or(CartasM1==kt)or(CartasM1==At):
            FlorImperialTrebolM.append(CartasM1)
        elif(CartasJ2==Dt)or(CartasJ2==qt)or(CartasJ2==kt)or(CartasJ2==At):
            FlorImperialTrebolJ.append(CartasJ2)
        elif(CartasM2==Dt)or(CartasM2==qt)or(CartasM2==kt)or(CartasM2==At):
            FlorImperialTrebolM.append(CartasM2)
    elif(qt in CartasSobreLaMesa):
        FlorImperialTrebolJ.append(qt)
        FlorImperialTrebolM.append(qt)
        if(CartasJ1==Dt)or(CartasJ1==jt)or(CartasJ1==kt)or(CartasJ1==At):
            FlorImperialTrebolJ.append(CartasJ1)
        elif(CartasM1==Dt)or(CartasM1==jt)or(CartasM1==kt)or(CartasM1==At):
            FlorImperialTrebolM.append(CartasM1)
        elif(CartasJ2==Dt)or(CartasJ2==jt)or(CartasJ2==kt)or(CartasJ2==At):
            FlorImperialTrebolJ.append(CartasJ2)
        elif(CartasM2==Dt)or(CartasM2==jt)or(CartasM2==kt)or(CartasM2==At):
            FlorImperialTrebolM.append(CartasM2)
    elif(kt in CartasSobreLaMesa):
        FlorImperialTrebolJ.append(kt)
        FlorImperialTrebolM.append(kt)
        if(CartasJ1==Dt)or(CartasJ1==jt)or(CartasJ1==qt)or(CartasJ1==At):
            FlorImperialTrebolJ.append(CartasJ1)
        elif(CartasM1==Dt)or(CartasM1==jt)or(CartasM1==qt)or(CartasM1==At):
            FlorImperialTrebolM.append(CartasM1)
        elif(CartasJ2==Dt)or(CartasJ2==jt)or(CartasJ2==qt)or(CartasJ2==At):
            FlorImperialTrebolJ.append(CartasJ2)
        elif(CartasM2==Dt)or(CartasM2==jt)or(CartasM2==qt)or(CartasM2==At):
            FlorImperialTrebolM.append(CartasM2)
    elif(At in CartasSobreLaMesa):
        FlorImperialTrebolJ.append(At)
        FlorImperialTrebolM.append(At)
        if(CartasJ1==Dt)or(CartasJ1==jt)or(CartasJ1==qt)or(CartasJ1==kt):
            FlorImperialTrebolJ.append(CartasJ1)
        elif(CartasM1==Dt)or(CartasM1==jt)or(CartasM1==qt)or(CartasM1==kt):
            FlorImperialTrebolM.append(CartasM1)
        elif(CartasJ2==Dt)or(CartasJ2==jt)or(CartasJ2==qt)or(CartasJ2==kt):
            FlorImperialTrebolJ.append(CartasJ2)
        elif(CartasM2==Dt)or(CartasM2==jt)or(CartasM2==qt)or(CartasM2==kt):
            FlorImperialTrebolM.append(CartasM2)
        FlorImperialTrebolJ[0]=Dt;
        FlorImperialTrebolJ[1]=jt;
        FlorImperialTrebolJ[2]=qt;
        FlorImperialTrebolJ[3]=kt;
        FlorImperialTrebolJ[4]=At;
        FlorImperialTrebolM[0]=Dt;
        FlorImperialTrebolM[1]=jt;
        FlorImperialTrebolM[2]=qt;
        FlorImperialTrebolM[3]=kt;
        FlorImperialTrebolM[4]=At;
    if(FlorImperialTrebolJ==[Dt,jt,qt,kt,At]):
        print('Felicitaciones, obtuviste una flor imperial, la jugada mas alta de todas, ganas automaticamente')
        DineroJ=ApuestaTotal+DineroJ
        JugadaJ=10
    elif(FlorImperialTrebolM==[Dt,jt,qt,kt,At]):
        print('Desgraciadamente tu oponente obtuvo una flor imperial, la jugada mas alta del juego, pierdes automaticamet')
        DineroM=ApuestaTotal+DineroM
        JugadaM=10
#Diamante
    FlorImperialDiamanteJ=[dd,jd,qd,kd,Ad]
    FlorImperialDiamanteM=[dd,jd,qd,kd,Ad]
    if(Dd in CartasSobreLaMesa):
        FlorImperialDiamanteJ.append(Dd)
        FlorImperialDiamanteM.append(Dd)
        if(CartasJ1==jd)or(CartasJ1==qd)or(CartasJ1==kd)or(CartasJ1==Ad):
            FlorImperialDiamanteJ.append(CartasJ1)
        elif(CartasM1==jd)or(CartasM1==qd)or(CartasM1==kd)or(CartasM1==Ad):
            FlorImperialDiamanteM.append(CartasM1)
        elif(CartasJ2==jd)or(CartasJ2==qd)or(CartasJ2==kd)or(CartasJ2==Ad):
            FlorImperialDiamanteJ.append(CartasJ2)
        elif(CartasM2==jd)or(CartasM2==qd)or(CartasM2==kd)or(CartasM2==Ad):
            FlorImperialDiamanteM.append(CartasM2)
    elif(jd in CartasSobreLaMesa):
        FlorImperialDiamanteJ.append(jd)
        FlorImperialDiamanteM.append(jd)
        if(CartasJ1==Dd)or(CartasJ1==qd)or(CartasJ1==kd)or(CartasJ1==Ad):
            FlorImperialDiamanteJ.append(CartasJ1)
        elif(CartasM1==Dd)or(CartasM1==qd)or(CartasM1==kd)or(CartasM1==Ad):
            FlorImperialDiamanteM.append(CartasM1)
        elif(CartasJ2==Dd)or(CartasJ2==qd)or(CartasJ2==kd)or(CartasJ2==Ad):
            FlorImperialDiamanteJ.append(CartasJ2)
        elif(CartasM2==Dd)or(CartasM2==qd)or(CartasM2==kd)or(CartasM2==Ad):
            FlorImperialDiamanteM.append(CartasM2)
    elif(qd in CartasSobreLaMesa):
        FlorImperialDiamanteJ.append(qd)
        FlorImperialDiamanteM.append(qd)
        if(CartasJ1==Dd)or(CartasJ1==jd)or(CartasJ1==kd)or(CartasJ1==Ad):
            FlorImperialDiamanteJ.append(CartasJ1)
        elif(CartasM1==Dd)or(CartasM1==jd)or(CartasM1==kd)or(CartasM1==Ad):
            FlorImperialDiamanteM.append(CartasM1)
        elif(CartasJ2==Dd)or(CartasJ2==jd)or(CartasJ2==kd)or(CartasJ2==Ad):
            FlorImperialDiamanteJ.append(CartasJ2)
        elif(CartasM2==Dd)or(CartasM2==jd)or(CartasM2==kd)or(CartasM2==Ad):
            FlorImperialDiamanteM.append(CartasM2)
    elif(kd in CartasSobreLaMesa):
        FlorImperialDiamanteJ.append(kd)
        FlorImperialDiamanteM.append(kd)
        if(CartasJ1==Dd)or(CartasJ1==jd)or(CartasJ1==qd)or(CartasJ1==Ad):
            FlorImperialDiamanteJ.append(CartasJ1)
        elif(CartasM1==Dd)or(CartasM1==jd)or(CartasM1==qd)or(CartasM1==Ad):
            FlorImperialDiamanteM.append(CartasM1)
        elif(CartasJ2==Dd)or(CartasJ2==jd)or(CartasJ2==qd)or(CartasJ2==Ad):
            FlorImperialDiamanteJ.append(CartasJ2)
        elif(CartasM2==Dd)or(CartasM2==jd)or(CartasM2==qd)or(CartasM2==Ad):
            FlorImperialDiamanteM.append(CartasM2)
    elif(Ad in CartasSobreLaMesa):
        FlorImperialDiamanteJ.append(Ad)
        FlorImperialDiamanteM.append(Ad)
        if(CartasJ1==Dd)or(CartasJ1==jd)or(CartasJ1==qd)or(CartasJ1==kd):
            FlorImperialDiamanteJ.append(CartasJ1)
        elif(CartasM1==Dd)or(CartasM1==jd)or(CartasM1==qd)or(CartasM1==kd):
            FlorImperialDiamanteM.append(CartasM1)
        elif(CartasJ2==Dd)or(CartasJ2==jd)or(CartasJ2==qd)or(CartasJ2==kd):
            FlorImperialDiamanteJ.append(CartasJ2)
        elif(CartasM2==Dd)or(CartasM2==jd)or(CartasM2==qd)or(CartasM2==kd):
            FlorImperialDiamanteM.append(CartasM2)
        FlorImperialDiamanteJ[0]=Dd;
        FlorImperialDiamanteJ[1]=jd;
        FlorImperialDiamanteJ[2]=qd;
        FlorImperialDiamanteJ[3]=kd;
        FlorImperialDiamanteJ[4]=Ad;
        FlorImperialDiamanteM[0]=Dd;
        FlorImperialDiamanteM[1]=jd;
        FlorImperialDiamanteM[2]=qd;
        FlorImperialDiamanteM[3]=kd;
        FlorImperialDiamanteM[4]=Ad;
    if(FlorImperialDiamanteJ==[Dd,jd,qd,kd,Ad]):
        print('Felicitaciones, obtuviste una flor imperial, la jugada mas alta de todas, ganas automaticamente')
        DineroJ=ApuestaTotal+DineroJ
        JugadaJ=10
    elif(FlorImperialDiamanteM==[Dd,jd,qd,kd,Ad]):
        print('Desgraciadamente tu oponente obtuvo una flor imperial, la jugada mas alta del juego, pierdes automaticamet')
        DineroM=ApuestaTotal+DineroM
        JugadaM=10
#Corazon
    FlorImperialCorazonJ=[dc,jc,qc,kc,Ac]
    FlorImperialCorazonM=[dc,jc,qc,kc,Ac]
    if(Dc in CartasSobreLaMesa):
        FlorImperialCorazonJ.append(Dc)
        FlorImperialCorazonM.append(Dc)
        if(CartasJ1==jc)or(CartasJ1==qc)or(CartasJ1==kc)or(CartasJ1==Ac):
            FlorImperialCorazonJ.append(CartasJ1)
        elif(CartasM1==jc)or(CartasM1==qc)or(CartasM1==kc)or(CartasM1==Ac):
            FlorImperialCorazonM.append(CartasM1)
        elif(CartasJ2==jc)or(CartasJ2==qc)or(CartasJ2==kc)or(CartasJ2==Ac):
            FlorImperialCorazonJ.append(CartasJ2)
        elif(CartasM2==jc)or(CartasM2==qc)or(CartasM2==kc)or(CartasM2==Ac):
            FlorImperialCorazonM.append(CartasM2)
    elif(jc in CartasSobreLaMesa):
        FlorImperialCorazonJ.append(jc)
        FlorImperialCorazonM.append(jc)
        if(CartasJ1==Dc)or(CartasJ1==qc)or(CartasJ1==kc)or(CartasJ1==Ac):
            FlorImperialCorazonJ.append(CartasJ1)
        elif(CartasM1==Dc)or(CartasM1==qc)or(CartasM1==kc)or(CartasM1==Ac):
            FlorImperialCorazonM.append(CartasM1)
        elif(CartasJ2==Dc)or(CartasJ2==qc)or(CartasJ2==kc)or(CartasJ2==Ac):
            FlorImperialCorazonJ.append(CartasJ2)
        elif(CartasM2==Dc)or(CartasM2==qc)or(CartasM2==kc)or(CartasM2==Ac):
            FlorImperialCorazonM.append(CartasM2)
    elif(qc in CartasSobreLaMesa):
        FlorImperialCorazonJ.append(qc)
        FlorImperialCorazonM.append(qc)
        if(CartasJ1==Dc)or(CartasJ1==jc)or(CartasJ1==kc)or(CartasJ1==Ac):
            FlorImperialCorazonJ.append(CartasJ1)
        elif(CartasM1==Dc)or(CartasM1==jc)or(CartasM1==kc)or(CartasM1==Ac):
            FlorImperialCorazonM.append(CartasM1)
        elif(CartasJ2==Dc)or(CartasJ2==jc)or(CartasJ2==kc)or(CartasJ2==Ac):
            FlorImperialCorazonJ.append(CartasJ2)
        elif(CartasM2==Dc)or(CartasM2==jc)or(CartasM2==kc)or(CartasM2==Ac):
            FlorImperialCorazonM.append(CartasM2)
    elif(kc in CartasSobreLaMesa):
        FlorImperialCorazonJ.append(kc)
        FlorImperialCorazonM.append(kc)
        if(CartasJ1==Dc)or(CartasJ1==jc)or(CartasJ1==qc)or(CartasJ1==Ac):
            FlorImperialCorazonJ.append(CartasJ1)
        elif(CartasM1==Dc)or(CartasM1==jc)or(CartasM1==qc)or(CartasM1==Ac):
            FlorImperialCorazonM.append(CartasM1)
        elif(CartasJ2==Dc)or(CartasJ2==jc)or(CartasJ2==qc)or(CartasJ2==Ac):
            FlorImperialCorazonJ.append(CartasJ2)
        elif(CartasM2==Dc)or(CartasM2==jc)or(CartasM2==qc)or(CartasM2==Ac):
            FlorImperialCorazonM.append(CartasM2)
    elif(Ac in CartasSobreLaMesa):
        FlorImperialCorazonJ.append(Ac)
        FlorImperialCorazonM.append(Ac)
        if(CartasJ1==Dc)or(CartasJ1==jc)or(CartasJ1==qc)or(CartasJ1==kc):
            FlorImperialCorazonJ.append(CartasJ1)
        elif(CartasM1==Dc)or(CartasM1==jc)or(CartasM1==qc)or(CartasM1==kc):
            FlorImperialCorazonM.append(CartasM1)
        elif(CartasJ2==Dc)or(CartasJ2==jc)or(CartasJ2==qc)or(CartasJ2==kc):
            FlorImperialCorazonJ.append(CartasJ2)
        elif(CartasM2==Dc)or(CartasM2==jc)or(CartasM2==qc)or(CartasM2==kc):
            FlorImperialCorazonM.append(CartasM2)
        FlorImperialCorazonJ[0]=Dc;
        FlorImperialCorazonJ[1]=jc;
        FlorImperialCorazonJ[2]=qc;
        FlorImperialCorazonJ[3]=kc;
        FlorImperialCorazonJ[4]=Ac;
        FlorImperialCorazonM[0]=Dc;
        FlorImperialCorazonM[1]=jc;
        FlorImperialCorazonM[2]=qc;
        FlorImperialCorazonM[3]=kc;
        FlorImperialCorazonM[4]=Ac;
    if(FlorImperialCorazonJ==[Dc,jc,qc,kc,Ac]):
        print('Felicitaciones, obtuviste una flor imperial, la jugada mas alta de todas, ganas automaticamente')
        DineroJ=ApuestaTotal+DineroJ
        JugadaJ=10
    elif(FlorImperialCorazonM==[Dc,jc,qc,kc,Ac]):
        print('Desgraciadamente tu oponente obtuvo una flor imperial, la jugada mas alta del juego, pierdes automaticamente')
        DineroM=ApuestaTotal+DineroM
        JugadaM=10
#Escalera de color
#Picas
    EscaleraDeColorPicasJ=0
    EscaleraDeColorPicasM=0
    if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
        if(dp in CartasSobreLaMesa)or(dp==CartasJ1)or(dp==CartasJ2):
            if(tp in CartasSobreLaMesa)or(tp==CartasJ1)or(tp==CartasJ2):
                if(cp in CartasSobreLaMesa)or(cp==CartasJ1)or(cp==CartasJ2):
                    if(Cp in CartasSobreLaMesa)or(Cp==CartasJ1)or(Cp==CartasJ2):
                        Ap=1;dp=2;tp=3;cp=4;Cp=5
                        EscaleraDeColorPicasJ=Ap+dp+tp+cp+Cp
    elif(dp in CartasSobreLaMesa)or(dp==CartasJ1)or(dp==CartasJ2):
        if(tp in CartasSobreLaMesa)or(tp==CartasJ1)or(tp==CartasJ2):
            if(cp in CartasSobreLaMesa)or(cp==CartasJ1)or(cp==CartasJ2):
                if(Cp in CartasSobreLaMesa)or(Cp==CartasJ1)or(Cp==CartasJ2):
                    if(sp in CartasSobreLaMesa)or(sp==CartasJ1)or(sp==CartasJ2):
                        dp=2;tp=3;cp=4;Cp=5;sp=6
                        EscaleraDeColorPicasJ=dp+tp+cp+Cp+sp
    elif(tp in CartasSobreLaMesa)or(tp==CartasJ1)or(tp==CartasJ2):
        if(cp in CartasSobreLaMesa)or(cp==CartasJ1)or(cp==CartasJ2):
            if(Cp in CartasSobreLaMesa)or(Cp==CartasJ1)or(Cp==CartasJ2):
                if(sp in CartasSobreLaMesa)or(sp==CartasJ1)or(sp==CartasJ2):
                    if(Sp in CartasSobreLaMesa)or(Sp==CartasJ1)or(Sp==CartasJ2):
                        tp=3;cp=4;Cp=5;sp=6;Sp=7
                        EscaleraDeColorPicasJ=tp+cp+Cp+sp+Sp
    elif(cp in CartasSobreLaMesa)or(cp==CartasJ1)or(cp==CartasJ2):
        if(Cp in CartasSobreLaMesa)or(Cp==CartasJ1)or(Cp==CartasJ2):
            if(sp in CartasSobreLaMesa)or(sp==CartasJ1)or(sp==CartasJ2):
                if(Sp in CartasSobreLaMesa)or(Sp==CartasJ1)or(Sp==CartasJ2):
                    if(op in CartasSobreLaMesa)or(op==CartasJ1)or(op==CartasJ2):
                        cp=4;Cp=5;sp=6;Sp=7;op=8
                        EscaleraDeColorPicasJ=cp+Cp+sp+Sp+op
    elif(Cp in CartasSobreLaMesa)or(Cp==CartasJ1)or(Cp==CartasJ2):
        if(sp in CartasSobreLaMesa)or(sp==CartasJ1)or(sp==CartasJ2):
            if(Sp in CartasSobreLaMesa)or(Sp==CartasJ1)or(Sp==CartasJ2):
                if(op in CartasSobreLaMesa)or(op==CartasJ1)or(op==CartasJ2):
                    if(np in CartasSobreLaMesa)or(np==CartasJ1)or(np==CartasJ2):
                        Cp=5;sp=6;Sp=7;op=8;np=9
                        EscaleraDeColorPicasJ=Cp+sp+Sp+op+np
    elif(sp in CartasSobreLaMesa)or(sp==CartasJ1)or(sp==CartasJ2):
        if(Sp in CartasSobreLaMesa)or(Sp==CartasJ1)or(Sp==CartasJ2):
            if(op in CartasSobreLaMesa)or(op==CartasJ1)or(op==CartasJ2):
                if(np in CartasSobreLaMesa)or(np==CartasJ1)or(np==CartasJ2):
                    if(Dp in CartasSobreLaMesa)or(Dp==CartasJ1)or(Dp==CartasJ2):
                        sp=6;Sp=7;op=8;np=9;Dp=10
                        EscaleraDeColorPicasJ=sp+Sp+op+np+Dp
    elif(Sp in CartasSobreLaMesa)or(Sp==CartasJ1)or(Sp==CartasJ2):
        if(op in CartasSobreLaMesa)or(op==CartasJ1)or(op==CartasJ2):
            if(np in CartasSobreLaMesa)or(np==CartasJ1)or(np==CartasJ2):
                if(Dp in CartasSobreLaMesa)or(Dp==CartasJ1)or(Dp==CartasJ2):
                    if(jp in CartasSobreLaMesa)or(jp==CartasJ1)or(jp==CartasJ2):
                        Sp=7;op=8;np=9;Dp=10;jp=11
                        EscaleraDeColorPicasJ=Sp+op+np+Dp+jp
    elif(op in CartasSobreLaMesa)or(op==CartasJ1)or(op==CartasJ2):
        if(np in CartasSobreLaMesa)or(np==CartasJ1)or(np==CartasJ2):
            if(Dp in CartasSobreLaMesa)or(Dp==CartasJ1)or(Dp==CartasJ2):
                if(jp in CartasSobreLaMesa)or(jp==CartasJ1)or(jp==CartasJ2):
                    if(qp in CartasSobreLaMesa)or(qp==CartasJ1)or(qp==CartasJ2):
                        op=8;np=9;Dp=10;jp=11;qp=12
                        EscaleraDeColorPicasJ=op+np+Dp+jp+qp
    elif(np in CartasSobreLaMesa)or(np==CartasJ1)or(np==CartasJ2):
        if(Dp in CartasSobreLaMesa)or(Dp==CartasJ1)or(Dp==CartasJ2):
            if(jp in CartasSobreLaMesa)or(jp==CartasJ1)or(jp==CartasJ2):
                if(qp in CartasSobreLaMesa)or(qp==CartasJ1)or(qp==CartasJ2):
                    if(kp in CartasSobreLaMesa)or(kp==CartasJ1)or(kp==CartasJ2):
                        np=9;Dp=10;jp=11;qp=12;kp=13
                        EscaleraDeColorPicasJ=np+Dp+jp+qp+kp
    elif(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
        if(dp in CartasSobreLaMesa)or(dp==CartasM1)or(dp==CartasM2):
            if(tp in CartasSobreLaMesa)or(tp==CartasM1)or(tp==CartasM2):
                if(cp in CartasSobreLaMesa)or(cp==CartasM1)or(cp==CartasM2):
                    if(Cp in CartasSobreLaMesa)or(Cp==CartasM1)or(Cp==CartasM2):
                        Ap=1;dp=2;tp=3;cp=4;Cp=5
                        EscaleraDeColorPicasM=Ap+dp+tp+cp+Cp
    elif(dp in CartasSobreLaMesa)or(dp==CartasM1)or(dp==CartasM2):
        if(tp in CartasSobreLaMesa)or(tp==CartasM1)or(tp==CartasM2):
            if(cp in CartasSobreLaMesa)or(cp==CartasM1)or(cp==CartasM2):
                if(Cp in CartasSobreLaMesa)or(Cp==CartasM1)or(Cp==CartasM2):
                    if(sp in CartasSobreLaMesa)or(sp==CartasM1)or(sp==CartasM2):
                        dp=2;tp=3;cp=4;Cp=5;sp=6
                        EscaleraDeColorPicasM=dp+tp+cp+Cp+sp
    elif(tp in CartasSobreLaMesa)or(tp==CartasM1)or(tp==CartasM2):
        if(cp in CartasSobreLaMesa)or(cp==CartasM1)or(cp==CartasM2):
            if(Cp in CartasSobreLaMesa)or(Cp==CartasM1)or(Cp==CartasM2):
                if(sp in CartasSobreLaMesa)or(sp==CartasM1)or(sp==CartasM2):
                    if(Sp in CartasSobreLaMesa)or(Sp==CartasM1)or(Sp==CartasM2):
                        tp=3;cp=4;Cp=5;sp=6;Sp=7
                        EscaleraDeColorPicasM=tp+cp+Cp+sp+Sp
    elif(cp in CartasSobreLaMesa)or(cp==CartasM1)or(cp==CartasM2):
        if(Cp in CartasSobreLaMesa)or(Cp==CartasM1)or(Cp==CartasM2):
            if(sp in CartasSobreLaMesa)or(sp==CartasM1)or(sp==CartasM2):
                if(Sp in CartasSobreLaMesa)or(Sp==CartasM1)or(Sp==CartasM2):
                    if(op in CartasSobreLaMesa)or(op==CartasM1)or(op==CartasM2):
                        cp=4;Cp=5;sp=6;Sp=7;op=8
                        EscaleraDeColorPicasM=cp+Cp+sp+Sp+op
    elif(Cp in CartasSobreLaMesa)or(Cp==CartasM1)or(Cp==CartasM2):
        if(sp in CartasSobreLaMesa)or(sp==CartasM1)or(sp==CartasM2):
            if(Sp in CartasSobreLaMesa)or(Sp==CartasM1)or(Sp==CartasM2):
                if(op in CartasSobreLaMesa)or(op==CartasM1)or(op==CartasM2):
                    if(np in CartasSobreLaMesa)or(np==CartasM1)or(np==CartasM2):
                        Cp=5;sp=6;Sp=7;op=8;np=9
                        EscaleraDeColorPicasM=Cp+sp+Sp+op+np
    elif(sp in CartasSobreLaMesa)or(sp==CartasM1)or(sp==CartasM2):
        if(Sp in CartasSobreLaMesa)or(Sp==CartasM1)or(Sp==CartasM2):
            if(op in CartasSobreLaMesa)or(op==CartasM1)or(op==CartasM2):
                if(np in CartasSobreLaMesa)or(np==CartasM1)or(np==CartasM2):
                    if(Dp in CartasSobreLaMesa)or(Dp==CartasM1)or(Dp==CartasM2):
                        sp=6;Sp=7;op=8;np=9;Dp=10
                        EscaleraDeColorPicasM=sp+Sp+op+np+Dp
    elif(Sp in CartasSobreLaMesa)or(Sp==CartasM1)or(Sp==CartasM2):
        if(op in CartasSobreLaMesa)or(op==CartasM1)or(op==CartasM2):
            if(np in CartasSobreLaMesa)or(np==CartasM1)or(np==CartasM2):
                if(Dp in CartasSobreLaMesa)or(Dp==CartasM1)or(Dp==CartasM2):
                    if(jp in CartasSobreLaMesa)or(jp==CartasM1)or(jp==CartasM2):
                        Sp=7;op=8;np=9;Dp=10;jp=11
                        EscaleraDeColorPicasM=Sp+op+np+Dp+jp
    elif(op in CartasSobreLaMesa)or(op==CartasM1)or(op==CartasM2):
        if(np in CartasSobreLaMesa)or(np==CartasM1)or(np==CartasM2):
            if(Dp in CartasSobreLaMesa)or(Dp==CartasM1)or(Dp==CartasM2):
                if(jp in CartasSobreLaMesa)or(jp==CartasM1)or(jp==CartasM2):
                    if(qp in CartasSobreLaMesa)or(qp==CartasM1)or(qp==CartasM2):
                        op=8;np=9;Dp=10;jp=11;qp=12
                        EscaleraDeColorPicasM=op+np+Dp+jp+qp
    elif(np in CartasSobreLaMesa)or(np==CartasM1)or(np==CartasM2):
        if(Dp in CartasSobreLaMesa)or(Dp==CartasM1)or(Dp==CartasM2):
            if(jp in CartasSobreLaMesa)or(jp==CartasM1)or(jp==CartasM2):
                if(qp in CartasSobreLaMesa)or(qp==CartasM1)or(qp==CartasM2):
                    if(kp in CartasSobreLaMesa)or(kp==CartasM1)or(kp==CartasM2):
                        np=9;Dp=10;jp=11;qp=12;kp=13
                        EscaleraDeColorPicasM=np+Dp+jp+qp+kp
    elif(EscaleraDeColorPicasJ>EscaleraDeColorPicasM):
        if(JugadaJ<10):
            JugadaJ=9
    elif(EscaleraDeColorPicasJ<EscaleraDeColorPicasM):
        if(JugadaM<10):
            JugadaM=9
#Trebol
    EscaleraDeColorTrebolJ=0
    EscaleraDeColorTrebolM=0
    if(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
        if(dt in CartasSobreLaMesa)or(dt==CartasJ1)or(dt==CartasJ2):
            if(tt in CartasSobreLaMesa)or(tt==CartasJ1)or(tt==CartasJ2):
                if(ct in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2):
                    if(Ct in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2):
                        At=1;dt=2;tt=3;ct=4;Ct=5
                        EscaleraDeColorTrebolJ=At+dt+tt+ct+Ct
    elif(dt in CartasSobreLaMesa)or(dt==CartasJ1)or(dt==CartasJ2):
        if(tt in CartasSobreLaMesa)or(tt==CartasJ1)or(tt==CartasJ2):
            if(ct in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2):
                if(Ct in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2):
                    if(st in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2):
                        dt=2;tt=3;ct=4;Ct=5;st=6
                        EscaleraDeColorTrebolJ=dt+tt+ct+Ct+st
    elif(tt in CartasSobreLaMesa)or(tt==CartasJ1)or(tt==CartasJ2):
        if(ct in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2):
            if(Ct in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2):
                if(st in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2):
                    if(St in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2):
                        tt=3;ct=4;Ct=5;st=6;St=7
                        EscaleraDeColorTrebolJ=tt+ct+Ct+st+St
    elif(ct in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2):
        if(Ct in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2):
            if(st in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2):
                if(St in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2):
                    if(ot in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2):
                        ct=4;Ct=5;st=6;St=7;ot=8
                        EscaleraDeColorTrebolJ=ct+Ct+st+St+ot
    elif(Ct in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2):
        if(st in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2):
            if(St in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2):
                if(ot in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2):
                    if(nt in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2):
                        Ct=5;st=6;St=7;ot=8;nt=9
                        EscaleraDeColorTrebolJ=Ct+st+St+ot+nt
    elif(st in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2):
        if(St in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2):
            if(ot in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2):
                if(nt in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2):
                    if(Dt in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2):
                        st=6;St=7;ot=8;nt=9;Dt=10
                        EscaleraDeColorTrebolJ=st+St+ot+nt+Dt
    elif(St in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2):
        if(ot in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2):
            if(nt in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2):
                if(Dt in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2):
                    if(jt in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2):
                        St=7;ot=8;nt=9;Dt=10;jt=11
                        EscaleraDeColorTrebolJ=St+ot+nt+Dt+jt
    elif(ot in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2):
        if(nt in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2):
            if(Dt in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2):
                if(jt in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2):
                    if(qt in CartasSobreLaMesa)or(qt==CartasJ1)or(qt==CartasJ2):
                        ot=8;nt=9;Dt=10;jt=11;qt=12
                        EscaleraDeColorTrebolJ=ot+nt+Dt+jt+qt
    elif(nt in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2):
        if(Dt in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2):
            if(jt in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2):
                if(qt in CartasSobreLaMesa)or(qt==CartasJ1)or(qt==CartasJ2):
                    if(kt in CartasSobreLaMesa)or(kt==CartasJ1)or(kt==CartasJ2):
                        nt=9;Dt=10;jt=11;qt=12;kt=13
                        EscaleraDeColorTrebolJ=nt+Dt+jt+qt+kt
    elif(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
        if(dt in CartasSobreLaMesa)or(dt==CartasM1)or(dt==CartasM2):
            if(tt in CartasSobreLaMesa)or(tt==CartasM1)or(tt==CartasM2):
                if(ct in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2):
                    if(Ct in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2):
                        At=1;dt=2;tt=3;ct=4;Ct=5
                        EscaleraDeColorTrebolM=At+dt+tt+ct+Ct
    elif(dt in CartasSobreLaMesa)or(dt==CartasM1)or(dt==CartasM2):
        if(tt in CartasSobreLaMesa)or(tt==CartasM1)or(tt==CartasM2):
            if(ct in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2):
                if(Ct in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2):
                    if(st in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2):
                        dt=2;tt=3;ct=4;Ct=5;st=6
                        EscaleraDeColorTrebolM=dt+tt+ct+Ct+st
    elif(tt in CartasSobreLaMesa)or(tt==CartasM1)or(tt==CartasM2):
        if(ct in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2):
            if(Ct in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2):
                if(st in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2):
                    if(St in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2):
                        tt=3;ct=4;Ct=5;st=6;St=7
                        EscaleraDeColorTrebolM=tt+ct+Ct+st+St
    elif(ct in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2):
        if(Ct in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2):
            if(st in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2):
                if(St in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2):
                    if(ot in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2):
                        ct=4;Ct=5;st=6;St=7;ot=8
                        EscaleraDeColorTrebolM=ct+Ct+st+St+ot
    elif(Ct in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2):
        if(st in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2):
            if(St in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2):
                if(ot in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2):
                    if(nt in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2):
                        Ct=5;st=6;St=7;ot=8;nt=9
                        EscaleraDeColorTrebolM=Ct+st+St+ot+nt
    elif(st in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2):
        if(St in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2):
            if(ot in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2):
                if(nt in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2):
                    if(Dt in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2):
                        st=6;St=7;ot=8;nt=9;Dt=10
                        EscaleraDeColorTrebolM=st+St+ot+nt+Dt
    elif(St in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2):
        if(ot in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2):
            if(nt in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2):
                if(Dt in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2):
                    if(jt in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2):
                        St=7;ot=8;nt=9;Dt=10;jt=11
                        EscaleraDeColorTrebolM=St+ot+nt+Dt+jt
    elif(ot in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2):
        if(nt in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2):
            if(Dt in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2):
                if(jt in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2):
                    if(qt in CartasSobreLaMesa)or(qt==CartasM1)or(qt==CartasM2):
                        ot=8;nt=9;Dt=10;jt=11;qt=12
                        EscaleraDeColorTrebolM=ot+nt+Dt+jt+qt
    elif(nt in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2):
        if(Dt in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2):
            if(jt in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2):
                if(qt in CartasSobreLaMesa)or(qt==CartasM1)or(qt==CartasM2):
                    if(kt in CartasSobreLaMesa)or(kt==CartasM1)or(kt==CartasM2):
                        nt=9;Dt=10;jt=11;qt=12;kt=13
                        EscaleraDeColorTrebolM=nt+Dt+jt+qt+kt
    elif(EscaleraDeColorTrebolJ>EscaleraDeColorTrebolM):
        if(JugadaJ<10):
            JugadaJ=9
    elif(EscaleraDeColorTrebolJ<EscaleraDeColorTrebolM):
        if(JugadaM<10):
            JugadaM=9
#Diamante
    EscaleraDeColorDiamanteJ=0
    EscaleraDeColorDiamanteM=0
    if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
        if(dd in CartasSobreLaMesa)or(dd==CartasJ1)or(dd==CartasJ2):
            if(td in CartasSobreLaMesa)or(td==CartasJ1)or(td==CartasJ2):
                if(cd in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2):
                    if(Cd in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2):
                        Ad=1;dd=2;td=3;cd=4;Cd=5
                        EscaleraDeColorDiamanteJ=Ad+dd+td+cd+Cd
    elif(dd in CartasSobreLaMesa)or(dd==CartasJ1)or(dd==CartasJ2):
        if(td in CartasSobreLaMesa)or(td==CartasJ1)or(td==CartasJ2):
            if(cd in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2):
                if(Cd in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2):
                    if(sd in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2):
                        dd=2;td=3;cd=4;Cd=5;sd=6
                        EscaleraDeColorDiamanteJ=dd+td+cd+Cd+sd
    elif(td in CartasSobreLaMesa)or(td==CartasJ1)or(td==CartasJ2):
        if(cd in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2):
            if(Cd in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2):
                if(sd in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2):
                    if(Sd in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2):
                        td=3;cd=4;Cd=5;sd=6;Sd=7
                        EscaleraDeColorDiamanteJ=td+cd+Cd+sd+Sd
    elif(cd in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2):
        if(Cd in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2):
            if(sd in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2):
                if(Sd in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2):
                    if(od in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2):
                        cd=4;Cd=5;sd=6;Sd=7;od=8
                        EscaleraDeColorDiamanteJ=cd+Cd+sd+Sd+od
    elif(Cd in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2):
        if(sd in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2):
            if(Sd in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2):
                if(od in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2):
                    if(nd in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2):
                        Cd=5;sd=6;Sd=7;od=8;nd=9
                        EscaleraDeColorDiamanteJ=Cd+sd+Sd+od+nd
    elif(sd in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2):
        if(Sd in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2):
            if(od in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2):
                if(nd in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2):
                    if(Dd in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2):
                        sd=6;Sd=7;od=8;nd=9;Dd=10
                        EscaleraDeColorDiamanteJ=sd+Sd+od+nd+Dd
    elif(Sd in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2):
        if(od in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2):
            if(nd in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2):
                if(Dd in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2):
                    if(jd in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2):
                        Sd=7;od=8;nd=9;Dd=10;jd=11
                        EscaleraDeColorDiamanteJ=Sd+od+nd+Dd+jd
    elif(od in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2):
        if(nd in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2):
            if(Dd in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2):
                if(jd in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2):
                    if(qd in CartasSobreLaMesa)or(qd==CartasJ1)or(qd==CartasJ2):
                        od=8;nd=9;Dd=10;jd=11;qd=12
                        EscaleraDeColorDiamanteJ=od+nd+Dd+jd+qd
    elif(nd in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2):
        if(Dd in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dd==CartasJ2):
            if(jd in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2):
                if(qd in CartasSobreLaMesa)or(qd==CartasJ1)or(qd==CartasJ2):
                    if(kd in CartasSobreLaMesa)or(kd==CartasJ1)or(kd==CartasJ2):
                        nd=9;Dd=10;jd=11;qd=12;kd=13
                        EscaleraDeColorDiamanteJ=nd+Dd+jd+qd+kd
    elif(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
        if(dd in CartasSobreLaMesa)or(dd==CartasM1)or(dd==CartasM2):
            if(td in CartasSobreLaMesa)or(td==CartasM1)or(td==CartasM2):
                if(cd in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2):
                    if(Cd in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2):
                        Ad=1;dd=2;td=3;cd=4;Cd=5
                        EscaleraDeColorDiamanteM=Ad+dd+td+cd+Cd
    elif(dd in CartasSobreLaMesa)or(dd==CartasM1)or(dd==CartasM2):
        if(td in CartasSobreLaMesa)or(td==CartasM1)or(td==CartasM2):
            if(cd in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2):
                if(Cd in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2):
                    if(sd in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2):
                        dd=2;td=3;cd=4;Cd=5;sd=6
                        EscaleraDeColorDiamante=dd+td+cd+Cd+sd
    elif(td in CartasSobreLaMesa)or(td==CartasM1)or(td==CartasM2):
        if(cd in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2):
            if(Cd in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2):
                if(sd in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2):
                    if(Sd in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2):
                        td=3;cd=4;Cd=5;sd=6;Sd=7
                        EscaleraDeColorDiamanteM=td+cd+Cd+sd+Sd
    elif(cd in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2):
        if(Cd in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2):
            if(sd in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2):
                if(Sd in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2):
                    if(od in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2):
                        cd=4;Cd=5;sd=6;Sd=7;od=8
                        EscaleraDeColorDiamanteM=cd+Cd+sd+Sd+od
    elif(Cd in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2):
        if(sd in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2):
            if(Sd in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2):
                if(od in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2):
                    if(nd in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2):
                        Cd=5;sd=6;Sd=7;od=8;nd=9
                        EscaleraDeColorDiamanteM=Cd+sd+Sd+od+nd
    elif(sd in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2):
        if(Sd in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2):
            if(od in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2):
                if(nd in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2):
                    if(Dd in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2):
                        sd=6;Sd=7;od=8;nd=9;Dd=10
                        EscaleraDeColorDiamanteM=sd+Sd+od+nd+Dd
    elif(Sd in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2):
        if(od in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2):
            if(nd in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2):
                if(Dd in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2):
                    if(jd in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2):
                        Sd=7;od=8;nd=9;Dd=10;jd=11
                        EscaleraDeColorDiamanteM=Sd+od+nd+Dd+jd
    elif(od in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2):
        if(nd in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2):
            if(Dd in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2):
                if(jd in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2):
                    if(qd in CartasSobreLaMesa)or(qd==CartasM1)or(qd==CartasM2):
                        od=8;nd=9;Dd=10;jd=11;qd=12
                        EscaleraDeColorDiamanteM=ot+nt+Dt+jt+qt
    elif(nd in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2):
        if(Dd in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2):
            if(jd in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2):
                if(qd in CartasSobreLaMesa)or(qd==CartasM1)or(qd==CartasM2):
                    if(kd in CartasSobreLaMesa)or(kd==CartasM1)or(kd==CartasM2):
                        nd=9;Dd=10;jd=11;qd=12;kd=13
                        EscaleraDeColorDiamanteM=nd+Dd+jd+qd+kd
    elif(EscaleraDeColorDiamanteJ>EscaleraDeColorDiamanteM):
        if(JugadaJ<10):
            JugadaJ=9
    elif(EscaleraDeColorDiamanteJ<EscaleraDeColorDiamanteM):
        if(JugadaM<10):
            JugadaM=9
#Corazon
    EscaleraDeColorCorazonJ=0
    EscaleraDeColorCorazonM=0
    if(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
        if(dc in CartasSobreLaMesa)or(dc==CartasJ1)or(dc==CartasJ2):
            if(tc in CartasSobreLaMesa)or(tc==CartasJ1)or(tc==CartasJ2):
                if(cc in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2):
                    if(Cc in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2):
                        Ac=1;dc=2;tc=3;cc=4;Cc=5
                        EscaleraDeColorCorazonJ=Ac+dc+tc+cc+Cc
    elif(dc in CartasSobreLaMesa)or(dc==CartasJ1)or(dc==CartasJ2):
        if(tc in CartasSobreLaMesa)or(tc==CartasJ1)or(tc==CartasJ2):
            if(cc in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2):
                if(Cc in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2):
                    if(sc in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2):
                        dc=2;tc=3;cc=4;Cc=5;sc=6
                        EscaleraDeColorCorazonJ=dc+tc+cc+Cc+sc
    elif(tc in CartasSobreLaMesa)or(tc==CartasJ1)or(tc==CartasJ2):
        if(cc in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2):
            if(Cc in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2):
                if(sc in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2):
                    if(Sc in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2):
                        tc=3;cc=4;Cc=5;sc=6;Sc=7
                        EscaleraDeColorCorazonJ=tc+cc+Cc+sc+Sc
    elif(cc in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2):
        if(Cc in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2):
            if(sc in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2):
                if(Sc in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2):
                    if(oc in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2):
                        cc=4;Cc=5;sc=6;Sc=7;oc=8
                        EscaleraDeColorCorazonJ=cc+Cc+sc+Sc+oc
    elif(Cc in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2):
        if(sc in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2):
            if(Sc in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2):
                if(oc in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2):
                    if(nc in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2):
                        Cc=5;sc=6;Sc=7;oc=8;nc=9
                        EscaleraDeColorCorazonJ=Cc+sc+Sc+oc+nc
    elif(sc in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2):
        if(Sc in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2):
            if(oc in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2):
                if(nc in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2):
                    if(Dc in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2):
                        sc=6;Sc=7;oc=8;nc=9;Dc=10
                        EscaleraDeColorCorazonJ=sc+Sc+oc+nc+Dc
    elif(Sc in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2):
        if(oc in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2):
            if(nc in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2):
                if(Dc in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2):
                    if(jc in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2):
                        Sc=7;oc=8;nc=9;Dc=10;jc=11
                        EscaleraDeColorCorazonJ=Sc+oc+nc+Dc+jc
    elif(oc in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2):
        if(nc in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2):
            if(Dc in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2):
                if(jc in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2):
                    if(qc in CartasSobreLaMesa)or(qc==CartasJ1)or(qc==CartasJ2):
                        oc=8;nc=9;Dc=10;jc=11;qc=12
                        EscaleraDeColorCorazonJ=oc+nc+Dc+jc+qc
    elif(nc in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2):
        if(Dc in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2):
            if(jc in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2):
                if(qc in CartasSobreLaMesa)or(qc==CartasJ1)or(qc==CartasJ2):
                    if(kc in CartasSobreLaMesa)or(kc==CartasJ1)or(kc==CartasJ2):
                        nc=9;Dc=10;jc=11;qc=12;kc=13
                        EscaleraDeColorCorazonJ=nc+Dc+jc+qc+kc
    elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
        if(dc in CartasSobreLaMesa)or(dc==CartasM1)or(dc==CartasM2):
            if(tc in CartasSobreLaMesa)or(tc==CartasM1)or(tc==CartasM2):
                if(cc in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2):
                    if(Cc in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2):
                        Ac=1;dc=2;tc=3;cc=4;Cc=5
                        EscaleraDeColorCorazonM=Ac+dc+tc+cc+Cc
    elif(dc in CartasSobreLaMesa)or(dc==CartasM1)or(dc==CartasM2):
        if(tc in CartasSobreLaMesa)or(tc==CartasM1)or(tc==CartasM2):
            if(cc in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2):
                if(Cc in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2):
                    if(sc in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2):
                        dc=2;tc=3;cc=4;Cc=5;sc=6
                        EscaleraDeColorCorazonM=dc+tc+cc+Cc+sc
    elif(tc in CartasSobreLaMesa)or(tc==CartasM1)or(tc==CartasM2):
        if(cc in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2):
            if(Cc in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2):
                if(sc in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2):
                    if(Sc in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2):
                        tc=3;cc=4;Cc=5;sc=6;Sc=7
                        EscaleraDeColorCorazonM=tc+cc+Cc+sc+Sc
    elif(cc in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2):
        if(Cc in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2):
            if(sc in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2):
                if(Sc in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2):
                    if(oc in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2):
                        cc=4;Cc=5;sc=6;Sc=7;oc=8
                        EscaleraDeColorCorazonM=cc+Cc+sc+Sc+oc
    elif(Cc in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2):
        if(sc in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2):
            if(Sc in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2):
                if(oc in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2):
                    if(nc in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2):
                        Cc=5;sc=6;Sc=7;oc=8;nc=9
                        EscaleraDeColorCorazonM=Cc+sc+Sc+oc+nc
    elif(sc in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2):
        if(Sc in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2):
            if(oc in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2):
                if(nc in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2):
                    if(Dc in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2):
                        sc=6;Sc=7;oc=8;nc=9;Dc=10
                        EscaleraDeColorCorazonM=sd+Sd+od+nd+Dd
    elif(Sc in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2):
        if(oc in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2):
            if(nc in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2):
                if(Dc in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2):
                    if(jc in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2):
                        Sc=7;oc=8;nc=9;Dc=10;jc=11
                        EscaleraDeColorCorazonM=Sc+oc+nc+Dc+jc
    elif(oc in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2):
        if(nc in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2):
            if(Dc in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2):
                if(jc in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2):
                    if(qc in CartasSobreLaMesa)or(qc==CartasM1)or(qc==CartasM2):
                        oc=8;nc=9;Dc=10;jc=11;qc=12
                        EscaleraDeColorCorazonM=oc+nc+Dc+jc+qc
    elif(nc in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2):
        if(Dc in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2):
            if(jc in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2):
                if(qc in CartasSobreLaMesa)or(qc==CartasM1)or(qc==CartasM2):
                    if(kc in CartasSobreLaMesa)or(kc==CartasM1)or(kc==CartasM2):
                        nc=9;Dc=10;jc=11;qc=12;kc=13
                        EscaleraDeColorCorazonM=nc+Dc+jc+qc+kc
    elif(EscaleraDeColorCorazonJ>EscaleraDeColorCorazonM):
        if(JugadaJ<10):
            JugadaJ=9
    elif(EscaleraDeColorCorazonJ<EscaleraDeColorCorazonM):
        if(JugadaM<10):
            JugadaM=9
#Poker
    PokerJ=0
    PokerM=0
    if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
        if(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                if(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                    PokerJ=14
    elif(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
        if(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                if(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                    PokerJ=2
    elif(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
        if(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
            if(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                if(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                    PokerJ=3
    elif(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
        if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
            if(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                if(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                    PokerJ=4
    elif(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
        if(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
            if(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                if(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                    PokerJ=5               
    elif(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
        if(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                if(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                    PokerJ=6
    elif(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
        if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
            if(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                if(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                    PokerJ=7
    elif(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
        if(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                if(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                    PokerJ=8
    elif(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
        if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
            if(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                if(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                    PokerJ=9
    elif(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
        if(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
            if(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                    PokerJ=10
    elif(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
        if(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
            if(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                    PokerJ=11
    elif(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
        if(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                if(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                    PokerJ=12
    elif(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
        if(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                if(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                    PokerJ=13
    elif(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
        if(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                if(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                    PokerM=14
    elif(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
        if(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
            if(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                if(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                    PokerM=2
    elif(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
        if(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                if(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                    PokerM=3
    elif(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
        if(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
            if(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                    PokerM=4
    elif(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
        if(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
            if(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                if(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                    PokerM=5
    elif(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
        if(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                if(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                    PokerM=6
    elif(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
        if(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                if(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                    PokerM=7
    elif(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
        if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
            if(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                if(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                    PokerM=8
    elif(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
        if(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
            if(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                    PokerM=9
    elif(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
        if(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
            if(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                    PokerM=10
    elif(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
        if(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
            if(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                    PokerM=11
    elif(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
        if(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
            if(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                if(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                    PokerM=12
    elif(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
        if(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                if(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                    PokerM=13
    if(PokerJ>PokerM):
        if(JugadaJ<9):
            JugadaJ=8
    elif(PokerJ<PokerM):
        if(JugadaM<9):
            JugadaM=8
#Par ; Doble Par ; Terna y Full House
    TernaJ=0
    TernaM=0
    ParesJ=[]
    ParJ=0
    ParesM=[]
    ParM=0
#As
    if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
        if(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                TernaJ=14
            elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ) 
        elif(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
            if(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
                TernaJ=14
            elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                TernaJ=14
            elif(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
    elif(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
        if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                TernaJ=14
            elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
            if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
                TernaJ=14
            elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                TernaJ=14
            elif(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
    elif(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
        if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
            if(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
                TernaJ=14
            elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
            if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
                TernaJ=14
            elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
            if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
                TernaJ=14
            elif(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
    elif(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
        if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                TernaJ=14
            elif(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
            if(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
                TernaJ=14
            elif(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
        elif(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa):
            if(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa):
                TernaJ=14
            elif(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa):
                TernaJ=14
            else:
                ParJ=14
                ParesJ.append(ParJ)
    if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
        if(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                TernaM=14
            elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
            if(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
                TernaM=14
            elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                TernaM=14
            elif(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
    elif(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
        if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                TernaM=14
            elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
            if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
                TernaM=14
            elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                TernaM=14
            elif(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
    elif(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
        if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
            if(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
                TernaM=14
            elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
            if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
                TernaM=14
            elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
            if(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
                TernaM=14
            elif(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
    elif(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
        if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                TernaM=14
            elif(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
            if(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
                TernaM=14
            elif(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
        elif(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa):
            if(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa):
                TernaM=14
            elif(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa):
                TernaM=14
            else:
                ParM=14
                ParesM.append(ParM)
#2
    if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
        if(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                TernaJ=2
            elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
            if(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=2
            elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                TernaJ=2
            elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
    elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
        if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                TernaJ=2
            elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
            if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
                TernaJ=2
            elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                TernaJ=2
            elif(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
    elif(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
        if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
            if(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=2
            elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
            if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
                TernaJ=2
            elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
            if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
                TernaJ=2
            elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
    elif(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):
        if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                TernaJ=2
            elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
            if(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
                TernaJ=2
            elif(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
        elif(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa):
            if(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=2
            elif(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa):
                TernaJ=2
            else:
                ParJ=2
                ParesJ.append(ParJ)
    if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
        if(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
            if(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                TernaM=2
            elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
            if(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
                TernaM=2
            elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
            if(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
                TernaM=2
            elif(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
    elif(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
        if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
            if(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                TernaM=2
            elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                	TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
            if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
                TernaM=2
            elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
            if(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                TernaM=2
            elif(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
    elif(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
        if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
            if(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
                TernaM=2
            elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
            if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
                TernaM=2
            elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
            if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
                TernaM=2
            elif(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
    elif(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
        if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
            if(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                TernaM=2
            elif(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
            if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
                TernaM=2
            elif(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
        elif(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa):
            if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa):
                TernaM=2
            elif(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa):
                TernaM=2
            else:
                ParM=2
                ParesM.append(ParM)
#3
    if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
        if(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
            if(dd==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                TernaJ=3
            elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
            if(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
                TernaJ=3
            elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
            if(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                TernaJ=3
            elif(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
    elif(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
        if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
            if(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                TernaJ=3
            elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
            if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
                TernaJ=3
            elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
            if(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                TernaJ=3
            elif(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
    elif(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
        if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
            if(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
                TernaJ=3
            elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
            if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
                TernaJ=3
            elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
            if(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
                TernaJ=3
            elif(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
    elif(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
        if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
            if(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                TernaJ=3
            elif(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
            if(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
                TernaJ=3
            elif(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
        elif(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa):
            if(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa):
                TernaJ=3
            elif(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa):
                TernaJ=3
            else:
                ParJ=3
                ParesJ.append(ParJ)
    if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
        if(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                TernaM=3
            elif(tc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
            if(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
                TernaM=3
            elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                TernaM=3
            elif(tt==CartasM1)or(dt==CartasM2)or(tt in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
    elif(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
        if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                TernaM=3
            elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
            if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
                TernaM=3
            elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                TernaM=3
            elif(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
    elif(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
        if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
            if(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
                TernaM=3
            elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
            if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
                TernaM=3
            elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
            if(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
                TernaM=3
            elif(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
    elif(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
        if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                TernaM=3
            elif(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
            if(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
                TernaM=3
            elif(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
                TernaM=3
            else:
                ParM=3
                ParesM.append(ParM)
        elif(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa):
            if(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa):
                TernaM=3
            elif(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa):
                TernaM=3
            else:   
                ParM=3
                ParesM.append(ParM)
#4
    if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
        if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
            if(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                TernaJ=4
            elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
            if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
                TernaJ=4
            elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                TernaJ=4
            else:   
                ParJ=4
                ParesJ.append(ParJ)
        elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
            if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
                TernaJ=4
            elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
    elif(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
        if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
            if(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                TernaJ=4
            elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
            if(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                TernaJ=4
            elif(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
            if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
                TernaJ=4
            elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
    elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
        if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
            if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
                TernaJ=4
            elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
            if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
                TernaJ=4
            elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
            if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
                TernaJ=4
            elif(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
    elif(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
        if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
            if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
                TernaJ=4
            elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
            if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
                TernaJ=4
            elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
        elif(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa):
            if(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa):
                TernaJ=4
            elif(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa):
                TernaJ=4
            else:
                ParJ=4
                ParesJ.append(ParJ)
    if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
        if(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
            if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                TernaM=4
            elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
            if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                TernaM=4
            elif(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
            if(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
                TernaM=4
            elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
    elif(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
        if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
            if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                TernaM=4
            elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
            if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                TernaM=4
            elif(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
            if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
                TernaM=4
            elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
    elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
        if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
            if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                TernaM=4
            elif(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
            if(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                TernaM=4
            elif(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
            if(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
                TernaM=4
            elif(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
    elif(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
        if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
            if(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
                TernaM=4
            elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
            if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
                TernaM=4
            elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
        elif(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa):
            if(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa):
                TernaM=4
            elif(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa):
                TernaM=4
            else:
                ParM=4
                ParesM.append(ParM)
#5
    if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
        if(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
            if(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
            if(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
            if(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            elif(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
    elif(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
        if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
            if(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
            if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
            if(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            elif(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
    elif(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
        if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
            if(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
            if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                TernaJ=5
            else:   
                ParJ=5
                ParesJ.append(ParJ)
        elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
            if(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
                TernaJ=5
            elif(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
    elif(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
        if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
            if(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
                TernaJ=5
            elif(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa):
            if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
                TernaJ=5
            elif(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
        elif(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
            if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa):
                TernaJ=5
            elif(Cc==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa):
                TernaJ=5
            else:
                ParJ=5
                ParesJ.append(ParJ)
    if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
        if(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
            if(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                TernaM=5
            elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
            if(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
                TernaM=5
            elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
            if(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
                TernaM=5
            elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
    elif(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
        if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
            if(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                TernaM=5
            elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
            if(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                TernaM=5
            elif(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
            if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
                TernaM=5
            elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
    elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
        if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
            if(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
                TernaM=5
            elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
            if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
                TernaM=5
            elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
            if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
                TernaM=5
            elif(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
    elif(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
        if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
            if(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
                TernaM=5
            elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
            if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
                TernaM=5
            elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
        elif(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa):
            if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa):
                TernaM=5
            elif(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa):
                TernaM=5
            else:
                ParM=5
                ParesM.append(ParM)
#6
    if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
        if(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                TernaJ=6
            elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
            if(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
                TernaJ=6
            elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                TernaJ=6
            elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
    elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
        if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                TernaJ=6
            elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
            if(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                TernaJ=6
            elif(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                TernaJ=6
            elif(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
    elif(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
        if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
            if(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
                TernaJ=6
            elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
            if(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                TernaJ=6
            elif(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
            if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
                TernaJ=6
            elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
    elif(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
        if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                TernaJ=6
            elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
            if(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
                TernaJ=6
            elif(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
        elif(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa):
            if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa):
                TernaJ=6
            elif(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa):
                TernaJ=6
            else:
                ParJ=6
                ParesJ.append(ParJ)
    if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
        if(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                TernaM=6
            elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
            if(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
                TernaM=6
            elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                TernaM=6
            elif(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
    elif(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
        if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                TernaM=6
            elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
            if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
                TernaM=6
            elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                TernaM=6
            elif(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
    elif(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
        if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
            if(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
                TernaM=6
            elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
            if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
                TernaM=6
            elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
            if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
                TernaM=6
            elif(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
    elif(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
        if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                TernaM=6
            elif(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
            if(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
                TernaM=6
            elif(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
        elif(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa):
            if(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa):
                TernaM=6
            elif(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa):
                TernaM=6
            else:
                ParM=6
                ParesM.append(ParM)
#7
    if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
        if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
            if(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                TernaJ=7
            elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
            if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
                TernaJ=7
            elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
            if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
                TernaJ=7
            elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
    elif(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
        if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
            if(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                TernaJ=7
            elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
            if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
                TernaJ=7
            elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
            if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
                TernaJ=7
            elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
    elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
        if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
            if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
                TernaJ=7
            elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
            if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
                TernaJ=7
            elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
            if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
                TernaJ=7
            elif(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
    elif(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):
        if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
            if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
                TernaJ=7
            elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
        elif(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
            if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
                TernaJ=7
            elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
                TernaJ=7
            else:   
                ParJ=7
                ParesJ.append(ParJ)
        elif(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa):
            if(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa):
                TernaJ=7
            elif(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa):
                TernaJ=7
            else:
                ParJ=7
                ParesJ.append(ParJ)
    if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
        if(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                TernaM=7
            elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
            if(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
                TernaM=7
            elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                TernaM=7
            elif(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
    elif(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
        if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                TernaM=7
            elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
            if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
                TernaM=7
            elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                TernaM=7
            elif(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
    elif(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
        if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
            if(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
                TernaM=7
            elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
            if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
                TernaM=7
            elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
            if(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
                TernaM=7
            elif(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
    elif(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
        if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                TernaM=7
            elif(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
            if(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
                TernaM=7
            elif(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
        elif(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa):
            if(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa):
                TernaM=7
            elif(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa):
                TernaM=7
            else:
                ParM=7
                ParesM.append(ParM)
#8
    if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
        if(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                TernaJ=8
            elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
            if(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
                TernaJ=8
            elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                TernaJ=8
            elif(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
    elif(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
        if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                TernaJ=8
            elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
            if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
                TernaJ=8
            elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                TernaJ=8
            elif(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
    elif(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
        if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
            if(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
                TernaJ=8
            elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
            if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
                TernaJ=8
            elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
            if(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
                TernaJ=8
            elif(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
    elif(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
        if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                TernaJ=8
            elif(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
            if(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
                TernaJ=8
            elif(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
        elif(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa):
            if(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa):
                TernaJ=8
            elif(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa):
                TernaJ=8
            else:
                ParJ=8
                ParesJ.append(ParJ)
    if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
        if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
            if(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                TernaM=8
            elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
            if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
                TernaM=8
            elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
            if(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                TernaM=8
            elif(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
    elif(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
        if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
            if(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                TernaM=8
            elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
            if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
                TernaM=8
            elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
            if(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                TernaM=8
            elif(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
    elif(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
        if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
            if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
                TernaM=8
            elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
            if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
                TernaM=8
            elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
            if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
                TernaM=8
            elif(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
    elif(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
        if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
            if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
                TernaM=8
            elif(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
            if(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
                TernaM=8
            elif(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
        elif(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa):
            if(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa):
                TernaM=8
            elif(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa):
                TernaM=8
            else:
                ParM=8
                ParesM.append(ParM)
#9
    if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
        if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
            if(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                TernaJ=9
            elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
            if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
                TernaJ=9
            elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
            if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
                TernaJ=9
            elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
    elif(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
        if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
            if(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                TernaJ=9
            elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
            if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
                TernaJ=9
            elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
            if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
                TernaJ=9
            elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
    elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
        if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
            if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
                TernaJ=9
            elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
            if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
                TernaJ=9
            elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
            if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
                TernaJ=9
            elif(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
    elif(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
        if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
            if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
                TernaJ=9
            elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
            if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
                TernaJ=9
            elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
        elif(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa):
            if(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa):
                TernaJ=9
            elif(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa):
                TernaJ=9
            else:
                ParJ=9
                ParesJ.append(ParJ)
    if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
        if(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
            if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                TernaM=9
            elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
            if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                TernaM=9
            elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
            if(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                TernaM=9
            elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
    elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
        if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
            if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                TernaM=9
            elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
            if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                TernaM=9
            elif(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
            if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
                TernaM=9
            elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
    elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
        if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
            if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                TernaM=9
            elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
            if(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                TernaM=9
            elif(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
            if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
                TernaM=9
            elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
    elif(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
        if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
            if(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                TernaM=9
            elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
            if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
                TernaM=9
            elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
        elif(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa):
            if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa):
                TernaM=9
            elif(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa):
                TernaM=9
            else:
                ParM=9
                ParesM.append(ParM)
#10
    if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
        if(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
            if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                TernaJ=10
            elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
            if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                TernaJ=10
            elif(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
            if(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
                TernaJ=10
            elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
    elif(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
        if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
            if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                TernaJ=10
            elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
            if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                TernaJ=10
            elif(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
            if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
                TernaJ=10
            elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
    elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
        if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
            if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                TernaJ=10
            elif(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
            if(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                TernaJ=10
            elif(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
            if(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
                TernaJ=10
            elif(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
    elif(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
        if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
            if(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
                TernaJ=10
            elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
            if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
                TernaJ=10
            elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
        elif(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa):
            if(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa):
                TernaJ=10
            elif(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa):
                TernaJ=10
            else:
                ParJ=10
                ParesJ.append(ParJ)
    if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
        if(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
            if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
            if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
            if(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
                TernaM=10
            elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
    elif(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
        if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
            if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
            if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
                TernaM=10
            else:   
                ParM=10
                ParesM.append(ParM)
        elif(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
            if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
                TernaM=10
            elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
    elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
        if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
            if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
            if(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
            if(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
                TernaM=10
            elif(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
    elif(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
        if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
            if(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
                TernaM=10
            elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dt==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
            if(Dp==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                TernaM=10
            elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
        elif(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa):
            if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa):
                TernaM=10
            elif(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa):
                TernaM=10
            else:
                ParM=10
                ParesM.append(ParM)
#J
    if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
        if(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
            if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                TernaJ=11
            elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
            if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                TernaJ=11
            elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
            if(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
                TernaJ=11
            elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
    elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
        if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
            if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                TernaJ=11
            elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
            if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                TernaJ=11
            elif(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
            if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
                TernaJ=11
            elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
    elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
        if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
            if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                TernaJ=11
            elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
            if(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                TernaJ=11
            elif(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
            if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
                TernaJ=11
            elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
    elif(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
        if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
            if(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
                TernaJ=11
            elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
            if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):
                TernaJ=11
            elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
        elif(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa):
            if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa):

                TernaJ=11
            elif(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa):
                TernaJ=11
            else:
                ParJ=11
                ParesJ.append(ParJ)
    if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
        if(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
            if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
            if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                TernaM=11
            elif(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
            if(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
    elif(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
        if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
            if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
            if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                TernaM=11
            elif(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
            if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
    elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
        if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
            if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                TernaM=11
            elif(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
            if(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                TernaM=11
            elif(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
            if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
    elif(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
        if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
            if(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
            if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
                TernaM=11
            elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
        elif(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa):
            if(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa):
                TernaM=11
            elif(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa):
                TernaM=11
            else:
                ParM=11
                ParesM.append(ParM)
#Q
    if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
        if(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                TernaJ=12
            elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
            if(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
                TernaJ=12
            elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                TernaJ=12
            elif(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
    elif(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
        if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                TernaJ=12
            elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
            if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
                TernaJ=12
            elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                TernaJ=12
            elif(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
    elif(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
        if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
            if(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
                TernaJ=12
            elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
            if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
                TernaJ=12
            elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
            if(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
                TernaJ=12
            elif(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
    elif(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
        if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                TernaJ=12
            elif(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
            if(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
                TernaJ=12
            elif(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
        elif(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa):
            if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa):
                TernaJ=12
            elif(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa):
                TernaJ=12
            else:
                ParJ=12
                ParesJ.append(ParJ)
    if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
        if(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
            if(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                TernaM=12
            elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
            if(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
                TernaM=12
            elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
            if(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
                TernaM=12
            elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
    elif(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
        if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
            if(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                TernaM=12
            elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
                TernaM=12
            elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
                TernaM=12
            elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
    elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
        if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
            if(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
                TernaM=12
            elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
                TernaM=12
            elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
                TernaM=12
            elif(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
    elif(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
        if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
            if(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                TernaM=12
            elif(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
                TernaM=12
            elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
        elif(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa):
                TernaM=12
            elif(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa):
                TernaM=12
            else:
                ParM=12
                ParesM.append(ParM)
#K
    if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
        if(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                TernaJ=13
            elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
            if(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
                TernaJ=13
            elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                TernaJ=13
            elif(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
    elif(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
        if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                TernaJ=13
            elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kd==CartasJ1)or(kd==CartasJ2)or(qd in CartasSobreLaMesa):
            if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
                TernaJ=13
            elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kc==CartasJ1)or(kc==CartasJ2)or(qc in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                TernaJ=13
            elif(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
    elif(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
        if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
            if(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
                TernaJ=13
            elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
            if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
                TernaJ=13
            elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
            if(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
                TernaJ=13
            elif(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
    elif(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
        if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                TernaJ=13
            elif(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
            if(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
                TernaJ=13
            elif(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
        elif(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa):
            if(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa):
                TernaJ=13
            elif(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa):
                TernaJ=13
            else:
                ParJ=13
                ParesJ.append(ParJ)
    if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
        if(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                TernaM=13
            elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
            if(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
                TernaM=13
            elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                TernaM=13
            elif(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
    elif(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
        if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                TernaM=13
            elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
            if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
                TernaM=13
            elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                TernaM=13
            elif(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
    elif(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
        if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
            if(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
                TernaM=13
            elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
            if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
                TernaM=13
            elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
            if(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
                TernaM=13
            elif(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
    elif(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
        if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                TernaM=13
            elif(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
            if(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
                TernaM=13
            elif(kk==CartasM1)or(kk==CartasM2)or(kk in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
        elif(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa):
            if(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa):
                TernaM=13
            elif(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa):
                TernaM=13
            else:
                ParM=13
                ParesM.append(ParM)
    if(ParJ>1)and(TernaJ>1):
        if(ParM>1)and(TernaM>1):
            if(ParJ>ParM)or(TernaJ>TernaM):
                if(JugadaJ<8):
                    JugadaJ=7
            elif(ParJ<ParM)or(TernaJ<TernaM):
                if(JugadaM<8):
                    JugadaM=7
        else:
            if(JugadaJ<8):
                JugadaJ=7
    elif(ParM>1)and(TernaM>1):
        if(ParJ>1)and(TernaJ>1):
            if(ParJ>ParM)or(TernaJ>TernaM):
                if(JugadaJ<8):
                    JugadaJ=7
            elif(ParJ<ParM)or(TernaJ<TernaM):
                if(JugadaM<8):
                    JugadaM=7
        else:
            if(JugadaM<=8):
                JugadaM=7
    elif(TernaJ>TernaM):
        if(JugadaJ<5):
            JugadaJ=4
    elif(TernaJ<TernaM):
        if(JugadaM<5):
            JugadaM=4
    if(len(ParesJ)>=2):
        if(JugadaJ<4):
            JugadaJ=3
    elif(len(ParesM)>=2):
        if(JugadaM<4):
            JugadaM=3
    elif(len(ParesJ)==1)or(len(ParesM)==1):
        if(ParJ>ParM):
            if(JugadaJ<3):
                JugadaJ=2
        elif(ParJ<ParM):
            if(JugadaM<3):
                JugadaM=2
#Escalera
    EscaleraJ=0
    EscaleraM=0
    if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa)or(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa)or(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa)or(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
        if(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa)or(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa)or(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa)or(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):  
            if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa)or(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa)or(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa)or(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
                if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                    if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                        EscaleraJ=1
    elif(dp==CartasJ1)or(dp==CartasJ2)or(dp in CartasSobreLaMesa)or(dt==CartasJ1)or(dt==CartasJ2)or(dt in CartasSobreLaMesa)or(dd==CartasJ1)or(dd==CartasJ2)or(dd in CartasSobreLaMesa)or(dc==CartasJ1)or(dc==CartasJ2)or(dc in CartasSobreLaMesa):  
        if(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa)or(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa)or(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa)or(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
            if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
                if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                    if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                        EscaleraJ=2
    elif(tp==CartasJ1)or(tp==CartasJ2)or(tp in CartasSobreLaMesa)or(tt==CartasJ1)or(tt==CartasJ2)or(tt in CartasSobreLaMesa)or(td==CartasJ1)or(td==CartasJ2)or(td in CartasSobreLaMesa)or(tc==CartasJ1)or(tc==CartasJ2)or(tc in CartasSobreLaMesa):
        if(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
            if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
                if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                    if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):      
                        EscaleraJ=3
    elif(cp==CartasJ1)or(cp==CartasJ2)or(cp in CartasSobreLaMesa)or(ct==CartasJ1)or(ct==CartasJ2)or(ct in CartasSobreLaMesa)or(cd==CartasJ1)or(cd==CartasJ2)or(cd in CartasSobreLaMesa)or(cc==CartasJ1)or(cc==CartasJ2)or(cc in CartasSobreLaMesa):
        if(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
            if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
                if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):      
                    if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                        EscaleraJ=4
    elif(Cp==CartasJ1)or(Cp==CartasJ2)or(Cp in CartasSobreLaMesa)or(Ct==CartasJ1)or(Ct==CartasJ2)or(Ct in CartasSobreLaMesa)or(Cd==CartasJ1)or(Cd==CartasJ2)or(Cd in CartasSobreLaMesa)or(Cc==CartasJ1)or(Cc==CartasJ2)or(Cc in CartasSobreLaMesa):
        if(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
            if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):      
                if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                    if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                        EscaleraJ=5
    elif(sp==CartasJ1)or(sp==CartasJ2)or(sp in CartasSobreLaMesa)or(st==CartasJ1)or(st==CartasJ2)or(st in CartasSobreLaMesa)or(sd==CartasJ1)or(sd==CartasJ2)or(sd in CartasSobreLaMesa)or(sc==CartasJ1)or(sc==CartasJ2)or(sc in CartasSobreLaMesa):
        if(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):      
            if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
                if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                    if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                        EscaleraJ=6
    elif(Sp==CartasJ1)or(Sp==CartasJ2)or(Sp in CartasSobreLaMesa)or(St==CartasJ1)or(St==CartasJ2)or(St in CartasSobreLaMesa)or(Sd==CartasJ1)or(Sd==CartasJ2)or(Sd in CartasSobreLaMesa)or(Sc==CartasJ1)or(Sc==CartasJ2)or(Sc in CartasSobreLaMesa):      
        if(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
            if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
                if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                    if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                        EscaleraJ=7
    elif(op==CartasJ1)or(op==CartasJ2)or(op in CartasSobreLaMesa)or(ot==CartasJ1)or(ot==CartasJ2)or(ot in CartasSobreLaMesa)or(od==CartasJ1)or(od==CartasJ2)or(od in CartasSobreLaMesa)or(oc==CartasJ1)or(oc==CartasJ2)or(oc in CartasSobreLaMesa):
        if(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
            if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
                if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                    if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa)or(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa)or(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa)or(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                        EscaleraJ=8
    elif(np==CartasJ1)or(np==CartasJ2)or(np in CartasSobreLaMesa)or(nt==CartasJ1)or(nt==CartasJ2)or(nt in CartasSobreLaMesa)or(nd==CartasJ1)or(nd==CartasJ2)or(nd in CartasSobreLaMesa)or(nc==CartasJ1)or(nc==CartasJ2)or(nc in CartasSobreLaMesa):
        if(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
            if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
                if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa)or(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa)or(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa)or(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                    if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa)or(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa)or(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa)or(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                        EscaleraJ=9
    elif(Dp==CartasJ1)or(Dp==CartasJ2)or(Dp in CartasSobreLaMesa)or(Dt==CartasJ1)or(Dt==CartasJ2)or(Dt in CartasSobreLaMesa)or(Dd==CartasJ1)or(Dd==CartasJ2)or(Dd in CartasSobreLaMesa)or(Dc==CartasJ1)or(Dc==CartasJ2)or(Dc in CartasSobreLaMesa):
        if(jp==CartasJ1)or(jp==CartasJ2)or(jp in CartasSobreLaMesa)or(jt==CartasJ1)or(jt==CartasJ2)or(jt in CartasSobreLaMesa)or(jd==CartasJ1)or(jd==CartasJ2)or(jd in CartasSobreLaMesa)or(jc==CartasJ1)or(jc==CartasJ2)or(jc in CartasSobreLaMesa):
            if(qp==CartasJ1)or(qp==CartasJ2)or(qp in CartasSobreLaMesa)or(qt==CartasJ1)or(qt==CartasJ2)or(qt in CartasSobreLaMesa)or(qd==CartasJ1)or(qd==CartasJ2)or(qd in CartasSobreLaMesa)or(qc==CartasJ1)or(qc==CartasJ2)or(qc in CartasSobreLaMesa):
                if(kp==CartasJ1)or(kp==CartasJ2)or(kp in CartasSobreLaMesa)or(kt==CartasJ1)or(kt==CartasJ2)or(kt in CartasSobreLaMesa)or(kd==CartasJ1)or(kd==CartasJ2)or(kd in CartasSobreLaMesa)or(kc==CartasJ1)or(kc==CartasJ2)or(kc in CartasSobreLaMesa):
                    if(Ap==CartasJ1)or(Ap==CartasJ2)or(Ap in CartasSobreLaMesa)or(At==CartasJ1)or(At==CartasJ2)or(At in CartasSobreLaMesa)or(Ad==CartasJ1)or(Ad==CartasJ2)or(Ad in CartasSobreLaMesa)or(Ac==CartasJ1)or(Ac==CartasJ2)or(Ac in CartasSobreLaMesa):
                        EscaleraJ=10
    if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa)or(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa)or(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa)or(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
        if(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa)or(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa)or(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa)or(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):  
            if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa)or(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa)or(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa)or(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
                if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                    if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                        EscaleraM=1
    elif(dp==CartasM1)or(dp==CartasM2)or(dp in CartasSobreLaMesa)or(dt==CartasM1)or(dt==CartasM2)or(dt in CartasSobreLaMesa)or(dd==CartasM1)or(dd==CartasM2)or(dd in CartasSobreLaMesa)or(dc==CartasM1)or(dc==CartasM2)or(dc in CartasSobreLaMesa):  
        if(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa)or(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa)or(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa)or(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
            if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
                if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                    if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                        EscaleraM=2
    elif(tp==CartasM1)or(tp==CartasM2)or(tp in CartasSobreLaMesa)or(tt==CartasM1)or(tt==CartasM2)or(tt in CartasSobreLaMesa)or(td==CartasM1)or(td==CartasM2)or(td in CartasSobreLaMesa)or(tc==CartasM1)or(tc==CartasM2)or(tc in CartasSobreLaMesa):
        if(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
            if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
                if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                    if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                        EscaleraM=3
    elif(cp==CartasM1)or(cp==CartasM2)or(cp in CartasSobreLaMesa)or(ct==CartasM1)or(ct==CartasM2)or(ct in CartasSobreLaMesa)or(cd==CartasM1)or(cd==CartasM2)or(cd in CartasSobreLaMesa)or(cc==CartasM1)or(cc==CartasM2)or(cc in CartasSobreLaMesa):
        if(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
            if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
                if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                    if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                        EscaleraM=4
    elif(Cp==CartasM1)or(Cp==CartasM2)or(Cp in CartasSobreLaMesa)or(Ct==CartasM1)or(Ct==CartasM2)or(Ct in CartasSobreLaMesa)or(Cd==CartasM1)or(Cd==CartasM2)or(Cd in CartasSobreLaMesa)or(Cc==CartasM1)or(Cc==CartasM2)or(Cc in CartasSobreLaMesa):
        if(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
            if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
                if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                    if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                        EscaleraM=5
    elif(sp==CartasM1)or(sp==CartasM2)or(sp in CartasSobreLaMesa)or(st==CartasM1)or(st==CartasM2)or(st in CartasSobreLaMesa)or(sd==CartasM1)or(sd==CartasM2)or(sd in CartasSobreLaMesa)or(sc==CartasM1)or(sc==CartasM2)or(sc in CartasSobreLaMesa):
        if(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
            if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
                if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                    if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                        EscaleraM=6
    elif(Sp==CartasM1)or(Sp==CartasM2)or(Sp in CartasSobreLaMesa)or(St==CartasM1)or(St==CartasM2)or(St in CartasSobreLaMesa)or(Sd==CartasM1)or(Sd==CartasM2)or(Sd in CartasSobreLaMesa)or(Sc==CartasM1)or(Sc==CartasM2)or(Sc in CartasSobreLaMesa):
        if(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
            if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
                if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                    if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                        EscaleraM=7
    elif(op==CartasM1)or(op==CartasM2)or(op in CartasSobreLaMesa)or(ot==CartasM1)or(ot==CartasM2)or(ot in CartasSobreLaMesa)or(od==CartasM1)or(od==CartasM2)or(od in CartasSobreLaMesa)or(oc==CartasM1)or(oc==CartasM2)or(oc in CartasSobreLaMesa):
        if(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
            if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
                if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                    if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa)or(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa)or(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa)or(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                        EscaleraM=8
    elif(np==CartasM1)or(np==CartasM2)or(np in CartasSobreLaMesa)or(nt==CartasM1)or(nt==CartasM2)or(nt in CartasSobreLaMesa)or(nd==CartasM1)or(nd==CartasM2)or(nd in CartasSobreLaMesa)or(nc==CartasM1)or(nc==CartasM2)or(nc in CartasSobreLaMesa):
        if(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
            if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
                if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa)or(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa)or(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa)or(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                    if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa)or(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa)or(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa)or(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                        EscaleraM=9
    elif(Dp==CartasM1)or(Dp==CartasM2)or(Dp in CartasSobreLaMesa)or(Dt==CartasM1)or(Dt==CartasM2)or(Dt in CartasSobreLaMesa)or(Dd==CartasM1)or(Dd==CartasM2)or(Dd in CartasSobreLaMesa)or(Dc==CartasM1)or(Dc==CartasM2)or(Dc in CartasSobreLaMesa):
        if(jp==CartasM1)or(jp==CartasM2)or(jp in CartasSobreLaMesa)or(jt==CartasM1)or(jt==CartasM2)or(jt in CartasSobreLaMesa)or(jd==CartasM1)or(jd==CartasM2)or(jd in CartasSobreLaMesa)or(jc==CartasM1)or(jc==CartasM2)or(jc in CartasSobreLaMesa):
            if(qp==CartasM1)or(qp==CartasM2)or(qp in CartasSobreLaMesa)or(qt==CartasM1)or(qt==CartasM2)or(qt in CartasSobreLaMesa)or(qd==CartasM1)or(qd==CartasM2)or(qd in CartasSobreLaMesa)or(qc==CartasM1)or(qc==CartasM2)or(qc in CartasSobreLaMesa):
                if(kp==CartasM1)or(kp==CartasM2)or(kp in CartasSobreLaMesa)or(kt==CartasM1)or(kt==CartasM2)or(kt in CartasSobreLaMesa)or(kd==CartasM1)or(kd==CartasM2)or(kd in CartasSobreLaMesa)or(kc==CartasM1)or(kc==CartasM2)or(kc in CartasSobreLaMesa):
                    if(Ap==CartasM1)or(Ap==CartasM2)or(Ap in CartasSobreLaMesa)or(At==CartasM1)or(At==CartasM2)or(At in CartasSobreLaMesa)or(Ad==CartasM1)or(Ad==CartasM2)or(Ad in CartasSobreLaMesa)or(Ac==CartasM1)or(Ac==CartasM2)or(Ac in CartasSobreLaMesa):
                        EscaleraM=10
    if(EscaleraJ>EscaleraM):
        if(JugadaJ<6):
            JugadaJ=5
    elif(EscaleraJ<EscaleraM):
        if(JugadaM<6):
            JugadaM=5
#Color
    ColorJ=0
    ColorM=0
#Picas
    JugadaColorPicasJ=[]
    JugadaColorPicasM=[]
    if(Ap==CartasJ1)or(dp==CartasJ1)or(tp==CartasJ1)or(cp==CartasJ1)or(Cp==CartasJ1)or(sp==CartasJ1)or(Sp==CartasJ1)or(op==CartasJ1)or(np==CartasJ1)or(Dp==CartasJ1)or(jp==CartasJ1)or(qp==CartasJ1)or(kp==CartasJ1):
        CartasJ1='P'
        JugadaColorPicasJ.append(CartasJ1)
    elif(Ap==CartasJ2)or(dp==CartasJ2)or(tp==CartasJ2)or(cp==CartasJ2)or(Cp==CartasJ2)or(sp==CartasJ2)or(Sp==CartasJ2)or(op==CartasJ2)or(np==CartasJ2)or(Dp==CartasJ2)or(jp==CartasJ2)or(qp==CartasJ2)or(kp==CartasJ2):
        CartasJ2='P'
        JugadaColorPicasJ.append(CartasJ2)
    elif(Ap in CartasSobreLaMesa):
        JugadaColorPicasJ.append(Ap)
    elif(dp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(dp)
    elif(tp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(tp)
    elif(cp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(cp)
    elif(Cp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(Cp)
    elif(sp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(sp)
    elif(Sp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(Sp)
    elif(op in CartasSobreLaMesa):
        JugadaColorPicasJ.append(op)
    elif(np in CartasSobreLaMesa):
        JugadaColorPicasJ.append(np)
    elif(Dp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(Dp)
    elif(jp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(jp)
    elif(qp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(qp)
    elif(kp in CartasSobreLaMesa):
        JugadaColorPicasJ.append(kp)
    if(len(JugadaColorPicasJ)>=5):
        ColorJ=1
    if(Ap==CartasM1)or(dp==CartasM1)or(tp==CartasM1)or(cp==CartasM1)or(Cp==CartasM1)or(sp==CartasM1)or(Sp==CartasM1)or(op==CartasM1)or(np==CartasM1)or(Dp==CartasM1)or(jp==CartasM1)or(qp==CartasM1)or(kp==CartasM1):
        CartasM1='P'
        JugadaColorPicasM.append(CartasM1)
    elif(Ap==CartasM2)or(dp==CartasM2)or(tp==CartasM2)or(cp==CartasM2)or(Cp==CartasM2)or(sp==CartasM2)or(Sp==CartasM2)or(op==CartasM2)or(np==CartasM2)or(Dp==CartasM2)or(jp==CartasM2)or(qp==CartasM2)or(kp==CartasM2):
        CartasM2='P'
        JugadaColorPicasM.append(CartasM2)
    elif(Ap in CartasSobreLaMesa):
        JugadaColorPicasM.append(Ap)
    elif(dp in CartasSobreLaMesa):
        JugadaColorPicasM.append(dp)
    elif(tp in CartasSobreLaMesa):
        JugadaColorPicasM.append(tp)
    elif(cp in CartasSobreLaMesa):
        JugadaColorPicasM.append(cp)
    elif(Cp in CartasSobreLaMesa):
        JugadaColorPicasM.append(Cp)
    elif(sp in CartasSobreLaMesa):
        JugadaColorPicasM.append(sp)
    elif(Sp in CartasSobreLaMesa):
        JugadaColorPicasM.append(Sp)
    elif(op in CartasSobreLaMesa):
        JugadaColorPicasM.append(op)
    elif(np in CartasSobreLaMesa):
        JugadaColorPicasM.append(np)
    elif(Dp in CartasSobreLaMesa):
        JugadaColorPicasM.append(Dp)
    elif(jp in CartasSobreLaMesa):
        JugadaColorPicasM.append(jp)
    elif(qp in CartasSobreLaMesa):
        JugadaColorPicasM.append(qp)
    elif(kp in CartasSobreLaMesa):
        JugadaColorPicasM.append(kp)
    if(len(JugadaColorPicasM)>=5):
        ColorM=1
#Trebol
    JugadaColorTrebolJ=[]
    JugadaColorTrebolM=[]
    if(At==CartasJ1)or(dt==CartasJ1)or(tt==CartasJ1)or(ct==CartasJ1)or(Ct==CartasJ1)or(st==CartasJ1)or(St==CartasJ1)or(ot==CartasJ1)or(nt==CartasJ1)or(Dt==CartasJ1)or(jt==CartasJ1)or(qt==CartasJ1)or(kt==CartasJ1):
        CartasJ1='T'
        JugadaColorTrebolJ.append(CartasJ1)
    elif(At==CartasJ2)or(dt==CartasJ2)or(tt==CartasJ2)or(ct==CartasJ2)or(Ct==CartasJ2)or(st==CartasJ2)or(St==CartasJ2)or(ot==CartasJ2)or(nt==CartasJ2)or(Dt==CartasJ2)or(jt==CartasJ2)or(qt==CartasJ2)or(kt==CartasJ2):
        CartasJ2='T'
        JugadaColorTrebolJ.append(CartasJ2)
    elif(At in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(At)
    elif(dt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(dt)
    elif(tt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(tt)
    elif(ct in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(ct)
    elif(Ct in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(Ct)
    elif(st in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(st)
    elif(St in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(St)
    elif(ot in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(ot)
    elif(nt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(nt)
    elif(Dt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(Dt)
    elif(jt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(jt)
    elif(qt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(qt)
    elif(kt in CartasSobreLaMesa):
        JugadaColorTrebolJ.append(kt)
    if(len(JugadaColorTrebolJ)>=5):
        ColorJ=1
    if(At==CartasM1)or(dt==CartasM1)or(tt==CartasM1)or(ct==CartasM1)or(Ct==CartasM1)or(st==CartasM1)or(St==CartasM1)or(ot==CartasM1)or(nt==CartasM1)or(Dt==CartasM1)or(jt==CartasM1)or(qt==CartasM1)or(kt==CartasM1):
        CartasM1='T'
        JugadaColorTrebolM.append(CartasM1)
    elif(At==CartasM2)or(dt==CartasM2)or(tt==CartasM2)or(ct==CartasM2)or(Ct==CartasM2)or(st==CartasM2)or(St==CartasM2)or(ot==CartasM2)or(nt==CartasM2)or(Dt==CartasM2)or(jt==CartasM2)or(qt==CartasM2)or(kt==CartasM2):
        CartasM2='T'
        JugadaColorTrebolM.append(CartasM2)
    elif(At in CartasSobreLaMesa):
        JugadaColorTrebolM.append(At)
    elif(dt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(dt)
    elif(tt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(tt)
    elif(ct in CartasSobreLaMesa):
        JugadaColorTrebolM.append(ct)
    elif(Ct in CartasSobreLaMesa):
        JugadaColorTrebolM.append(Ct)
    elif(st in CartasSobreLaMesa):
        JugadaColorTrebolM.append(st)
    elif(St in CartasSobreLaMesa):
        JugadaColorTrebolM.append(St)
    elif(ot in CartasSobreLaMesa):
        JugadaColorTrebolM.append(ot)
    elif(nt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(nt)
    elif(Dt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(Dt)
    elif(jt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(jt)
    elif(qt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(qt)
    elif(kt in CartasSobreLaMesa):
        JugadaColorTrebolM.append(kt)
    if(len(JugadaColorTrebolM)>=5):
        ColorM=1
#Diamante
    JugadaColorDiamanteJ=[]
    JugadaColorDiamanteM=[]
    if(Ad==CartasJ1)or(dd==CartasJ1)or(td==CartasJ1)or(cd==CartasJ1)or(Cd==CartasJ1)or(sd==CartasJ1)or(Sd==CartasJ1)or(od==CartasJ1)or(nd==CartasJ1)or(Dd==CartasJ1)or(jd==CartasJ1)or(qd==CartasJ1)or(kd==CartasJ1):
        CartasJ1='D'
        JugadaColorDiamanteJ.append(CartasJ1)
    elif(Ad==CartasJ2)or(dd==CartasJ2)or(td==CartasJ2)or(cd==CartasJ2)or(Cd==CartasJ2)or(sd==CartasJ2)or(Sd==CartasJ2)or(od==CartasJ2)or(nd==CartasJ2)or(Dd==CartasJ2)or(jd==CartasJ2)or(qd==CartasJ2)or(kd==CartasJ2):
        CartasJ2='D'
        JugadaColorDiamanteJ.append(CartasJ2)
    elif(Ad in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(Ad)
    elif(dd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(dd)
    elif(td in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(td)
    elif(cd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(cd)
    elif(Cd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(Cd)
    elif(sd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(sd)
    elif(Sd in CartasSobreLaMesa):
         JugadaColorDiamanteJ.append(Sd)
    elif(od in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(od)
    elif(nd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(nd)
    elif(Dd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(Dd)
    elif(jd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(jd)
    elif(qd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(qd)
    elif(kd in CartasSobreLaMesa):
        JugadaColorDiamanteJ.append(kd)
    if(len(JugadaColorDiamanteJ)>=5):
        ColorJ=1
    if(Ad==CartasM1)or(dd==CartasM1)or(td==CartasM1)or(cd==CartasM1)or(Cd==CartasM1)or(sd==CartasM1)or(Sd==CartasM1)or(od==CartasM1)or(nd==CartasM1)or(Dd==CartasM1)or(jd==CartasM1)or(qd==CartasM1)or(kd==CartasM1):
        CartasM1='D'
        JugadaColorDiamanteM.append(CartasM1)
    elif(Ad==CartasM2)or(dd==CartasM2)or(td==CartasM2)or(cd==CartasM2)or(Cd==CartasM2)or(sd==CartasM2)or(Sd==CartasM2)or(od==CartasM2)or(nd==CartasM2)or(Dd==CartasM2)or(jd==CartasM2)or(qd==CartasM2)or(kd==CartasM2):
        CartasM2='D'
        JugadaColorDiamanteM.append(CartasM2)
    elif(Ad in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(Ad)
    elif(dd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(dd)
    elif(td in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(td)
    elif(cd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(cd)
    elif(Cd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(Cd)
    elif(sd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(sd)
    elif(Sd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(Sd)
    elif(od in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(od)
    elif(nd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(nd)
    elif(Dd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(Dd)
    elif(jd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(jd)
    elif(qd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(qd)
    elif(kd in CartasSobreLaMesa):
        JugadaColorDiamanteM.append(kd)
    if(len(JugadaColorDiamanteM)>=5):
        ColorM=1
#Corazon
    JugadaColorCorazonJ=[]
    JugadaColorCorazonM=[]
    if(Ac==CartasJ1)or(dc==CartasJ1)or(tc==CartasJ1)or(cc==CartasJ1)or(Cc==CartasJ1)or(sc==CartasJ1)or(Sc==CartasJ1)or(oc==CartasJ1)or(nc==CartasJ1)or(Dc==CartasJ1)or(jc==CartasJ1)or(qc==CartasJ1)or(kc==CartasJ1):
        CartasJ1='C'
        JugadaColorCorazonJ.append(CartasJ1)
    elif(Ac==CartasJ2)or(dc==CartasJ2)or(tc==CartasJ2)or(cc==CartasJ2)or(Cc==CartasJ2)or(sc==CartasJ2)or(Sc==CartasJ2)or(oc==CartasJ2)or(nc==CartasJ2)or(Dc==CartasJ2)or(jc==CartasJ2)or(qc==CartasJ2)or(kc==CartasJ2):
        CartasJ2='C'
        JugadaColorCorazonJ.append(CartasJ2)
    elif(Ac in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(Ac)
    elif(dc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(dc)
    elif(tc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(tc)
    elif(cc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(cc)
    elif(Cc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(Cc)
    elif(sc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(sc)
    elif(Sc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(Sc)
    elif(oc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(oc)
    elif(nc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(nc)
    elif(Dc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(Dc)
    elif(jc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(jc)
    elif(qc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(qc)
    elif(kc in CartasSobreLaMesa):
        JugadaColorCorazonJ.append(kc)
    if(len(JugadaColorCorazonJ)>=5):
        ColorJ=1
    if(Ac==CartasM1)or(dc==CartasM1)or(tc==CartasM1)or(cc==CartasM1)or(Cc==CartasM1)or(sc==CartasM1)or(Sc==CartasM1)or(oc==CartasM1)or(nc==CartasM1)or(Dc==CartasM1)or(jc==CartasM1)or(qc==CartasM1)or(kc==CartasM1):
        CartasM1='C'
        JugadaColorCorazonM.append(CartasM1)
    elif(Ac==CartasM2)or(dc==CartasM2)or(tc==CartasM2)or(cc==CartasM2)or(Cc==CartasM2)or(sc==CartasM2)or(Sc==CartasM2)or(oc==CartasM2)or(nc==CartasM2)or(Dc==CartasM2)or(jc==CartasM2)or(qc==CartasM2)or(kc==CartasM2):
        CartasM2='C'
        JugadaColorCorazonM.append(CartasM2)
    elif(Ac in CartasSobreLaMesa):
        JugadaColorCorazonM.append(Ac)
    elif(dc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(dc)
    elif(tc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(tc)
    elif(cc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(cc)
    elif(Cc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(Cc)
    elif(sc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(sc)
    elif(Sc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(Sc)
    elif(oc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(oc)
    elif(nc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(nc)
    elif(Dc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(Dc)
    elif(jc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(jc)
    elif(qc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(qc)
    elif(kc in CartasSobreLaMesa):
        JugadaColorCorazonM.append(kc)
    if(len(JugadaColorCorazonM)>=5):
        ColorM=1
    if(ColorJ==1):
        if(JugadaJ<7):
            JugadaJ=6
    elif(ColorM==1):
        if(JugadaM<7):
            JugadaM=6
#Carta Alta
    if(JugadaJ==0)or(JugadaM==0):
#Primera Carta de la mano Jugador y Maquina
        CartaAltaJ1=0
        CartaAltaJ2=0
        CartaAltaM1=0
        CartaAltaM2=0
        if(CartasJ1==dp)or(CartasJ1==dt)or(CartasJ1==dd)or(CartasJ1==dc):
            CartaAltaJ1=2
        elif(CartasJ1==tp)or(CartasJ1==tt)or(CartasJ1==td)or(CartasJ1==tc):
            CartaAltaJ1=3
        elif(CartasJ1==cp)or(CartasJ1==ct)or(CartasJ1==cd)or(CartasJ1==cc):
            CartaAltaJ1=4
        elif(CartasJ1==Cp)or(CartasJ1==Ct)or(CartasJ1==Cd)or(CartasJ1==Cc):
            CartaAltaJ1=5
        elif(CartasJ1==sp)or(CartasJ1==st)or(CartasJ1==sd)or(CartasJ1==sc):
            CartaAltaJ1=6
        elif(CartasJ1==Sp)or(CartasJ1==St)or(CartasJ1==Sd)or(CartasJ1==Sc):
            CartaAltaJ1=7
        elif(CartasJ1==op)or(CartasJ1==ot)or(CartasJ1==od)or(CartasJ1==oc):
            CartaAltaJ1=8
        elif(CartasJ1==np)or(CartasJ1==nt)or(CartasJ1==nd)or(CartasJ1==nc):
            CartaAltaJ1=9
        elif(CartasJ1==Dp)or(CartasJ1==Dt)or(CartasJ1==Dd)or(CartasJ1==Dc):
            CartaAltaJ1=10
        elif(CartasJ1==jp)or(CartasJ1==jt)or(CartasJ1==jd)or(CartasJ1==jc):
            CartaAltaJ1=11
        elif(CartasJ1==qp)or(CartasJ1==qt)or(CartasJ1==qd)or(CartasJ1==qc):
            CartaAltaJ1=12
        elif(CartasJ1==kp)or(CartasJ1==kt)or(CartasJ1==kd)or(CartasJ1==kc):
            CartaAltaJ1=13
        elif(CartasJ1==Ap)or(CartasJ1==At)or(CartasJ1==Ad)or(CartasJ1==Ac):
            CartaAltaJ1=14
        if(CartasM1==dp)or(CartasM1==dt)or(CartasM1==dd)or(CartasM1==dc):
            CartaAltaM1=2
        elif(CartasM1==tp)or(CartasM1==tt)or(CartasM1==td)or(CartasM1==tc):
            CartaAltaM1=3
        elif(CartasM1==cp)or(CartasM1==ct)or(CartasM1==cd)or(CartasM1==cc):
            CartaAltaM1=4
        elif(CartasM1==Cp)or(CartasM1==Ct)or(CartasM1==Cd)or(CartasM1==Cc):
            CartaAltaM1=5
        elif(CartasM1==sp)or(CartasM1==st)or(CartasM1==sd)or(CartasM1==sc):
            CartaAltaM1=6
        elif(CartasM1==Sp)or(CartasM1==St)or(CartasM1==Sd)or(CartasM1==Sc):
            CartaAltaM1=7
        elif(CartasM1==op)or(CartasM1==ot)or(CartasM1==od)or(CartasM1==oc):
            CartaAltaM1=8
        elif(CartasM1==np)or(CartasM1==nt)or(CartasM1==nd)or(CartasM1==nc):
            CartaAltaM1=9
        elif(CartasM1==Dp)or(CartasM1==Dt)or(CartasM1==Dd)or(CartasM1==Dc):
            CartaAltaM1=10
        elif(CartasM1==jp)or(CartasM1==jt)or(CartasM1==jd)or(CartasM1==jc):
            CartaAltaM1=11
        elif(CartasM1==qp)or(CartasM1==qt)or(CartasM1==qd)or(CartasM1==qc):
            CartaAltaM1=12
        elif(CartasM1==kp)or(CartasM1==kt)or(CartasM1==kd)or(CartasM1==kc):
            CartaAltaM1=13
        elif(CartasM1==Ap)or(CartasM1==At)or(CartasM1==Ad)or(CartasM1==Ac):
            CartaAltaM1=14
#Segunda Carta de la mano Jugador y Maquina
        if(CartasJ2==dp)or(CartasJ2==dt)or(CartasJ2==dd)or(CartasJ2==dc):
            CartaAltaJ2=2
        elif(CartasJ2==tp)or(CartasJ2==tt)or(CartasJ2==td)or(CartasJ2==tc):
            CartaAltaJ2=3
        elif(CartasJ2==cp)or(CartasJ2==ct)or(CartasJ2==cd)or(CartasJ2==cc):
            CartaAltaJ2=4
        elif(CartasJ2==Cp)or(CartasJ2==Ct)or(CartasJ2==Cd)or(CartasJ2==Cc):
            CartaAltaJ2=5
        elif(CartasJ2==sp)or(CartasJ2==st)or(CartasJ2==sd)or(CartasJ2==sc):
            CartaAltaJ2=6
        elif(CartasJ2==Sp)or(CartasJ2==St)or(CartasJ2==Sd)or(CartasJ2==Sc):
            CartaAltaJ2=7
        elif(CartasJ2==op)or(CartasJ2==ot)or(CartasJ2==od)or(CartasJ2==oc):
            CartaAltaJ2=8
        elif(CartasJ2==np)or(CartasJ2==nt)or(CartasJ2==nd)or(CartasJ2==nc):
            CartaAltaJ2=9
        elif(CartasJ2==Dp)or(CartasJ2==Dt)or(CartasJ2==Dd)or(CartasJ2==Dc):
            CartaAltaJ2=10
        elif(CartasJ2==jp)or(CartasJ2==jt)or(CartasJ2==jd)or(CartasJ2==jc):
            CartaAltaJ2=11
        elif(CartasJ2==qp)or(CartasJ2==qt)or(CartasJ2==qd)or(CartasJ2==qc):
            CartaAltaJ2=12
        elif(CartasJ2==kp)or(CartasJ2==kt)or(CartasJ2==kd)or(CartasJ2==kc):
            CartaAltaJ2=13
        elif(CartasJ2==Ap)or(CartasJ2==At)or(CartasJ2==Ad)or(CartasJ2==Ac):
            CartaAltaJ2=14
        if(CartasM2==dp)or(CartasM2==dt)or(CartasM2==dd)or(CartasM2==dc):
            CartaAltaM2=2
        elif(CartasM2==tp)or(CartasM2==tt)or(CartasM2==td)or(CartasM2==tc):
            CartaAltaM2=3
        elif(CartasM2==cp)or(CartasM2==ct)or(CartasM2==cd)or(CartasM2==cc):
            CartaAltaM2=4
        elif(CartasM2==Cp)or(CartasM2==Ct)or(CartasM2==Cd)or(CartasM2==Cc):
            CartaAltaM2=5
        elif(CartasM2==sp)or(CartasM2==st)or(CartasM2==sd)or(CartasM2==sc):
            CartaAltaM2=6
        elif(CartasM2==Sp)or(CartasM2==St)or(CartasM2==Sd)or(CartasM2==Sc):
            CartaAltaM2=7
        elif(CartasM2==op)or(CartasM2==ot)or(CartasM2==od)or(CartasM2==oc):
            CartaAltaM2=8
        elif(CartasM2==np)or(CartasM2==nt)or(CartasM2==nd)or(CartasM2==nc):
            CartaAltaM2=9
        elif(CartasM2==Dp)or(CartasM2==Dt)or(CartasM2==Dd)or(CartasM2==Dc):
            CartaAltaM2=10
        elif(CartasM2==jp)or(CartasM2==jt)or(CartasM2==jd)or(CartasM2==jc):
            CartaAltaM2=11
        elif(CartasM2==qp)or(CartasM2==qt)or(CartasM2==qd)or(CartasM2==qc):
            CartaAltaM2=12
        elif(CartasM2==kp)or(CartasM2==kt)or(CartasM2==kd)or(CartasM2==kc):
            CartaAltaM2=13
        elif(CartasM2==Ap)or(CartasM2==At)or(CartasM2==Ad)or(CartasM2==Ac):
            CartaAltaM2=14
        if(CartaAltaJ1>CartaAltaJ2):
            if(CartaAltaM1>CartaAltaM2):
                if(CartaAltaJ1>CartaAltaM1):
                    JugadaJ=1
                elif(CartaAltaJ1<CartaAltaM1):
                    JugadaM=1
            elif(CartaAltaM1<CartaAltaM2):
                if(CartaAltaJ1>CartaAltaM2):
                    JugadaJ=1
                elif(CartaAltaJ1<CartaAltaM2):
                    JugadaM=1
        elif(CartaAltaJ2>CartaAltaJ1):
            if(CartaAltaM1>CartaAltaM2):
                if(CartaAltaJ2>CartaAltaM1):
                    JugadaJ=1
                elif(CartaAltaJ2<CartaAltaM1):
                    JugadaM=1
            elif(CartaAltaM1<CartaAltaM2):
                if(CartaAltaJ2>CartaAltaM2):
                    JugadaJ=1
                elif(CartaAltaJ2<CartaAltaM2):
                    JugadaM=1
    if(JugadaJ>JugadaM):
        if(JugadaJ==1):
            print('Felicidades, has ganado por Carta Alta! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==2):
            print('Felicidades, has ganado con un Par! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==3):
            print('Felicidades, has ganado con un Doble Par! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==4):
            print('Felicidades, has ganado con una Terna! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==5):
            print('Felicidades, has ganado con una escalera! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==6):
            print('Felicidades, has ganado con un Color! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==7):
            print('Felicidades, has ganado con un Full House! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==8):
            print('Felicidades, has ganado con un Poker! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==9):
            print('Felicidades, has ganado con una Escalera de Color! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
        elif(JugadaJ==10):
            print('Felicidades, has ganado con una Flor Imperial, la jugada mas alta del juego!!! Te llevas',ApuestaTotal,'Dolares')
            DineroJ=DineroJ+ApuestaTotal
    elif(JugadaM>JugadaJ):
        if(JugadaM==1):
            print('Desgraciadamente tu oponente gana por Carta Alta, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==2):
            print('Desgraciadamente tu oponente gana con un Par, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==3):
            print('Desgraciadamente tu oponente gana con un Doble Par, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==4):
            print('Desgraciadamente tu oponente gana con una Terna, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==5):
            print('Desgraciadamente tu oponente gana con una escalera, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==6):
            print('Desgraciadamente tu oponente gana con un Color, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==7):
            print('Desgraciadamente tu oponente gana con un Full House, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==8):
            print('Desgraciadamente tu oponente gana con un Poker, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==9):
            print('Desgraciadamente tu oponente gana con una Escalera de Color, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
        elif(JugadaM==10):
            print('Desgraciadamente tu oponente gana con una Flor Imperial, la jugada mas alta del juego, se lleva',ApuestaTotal,'Dolares')
            DineroM=DineroM+ApuestaTotal
    elif(JugadaJ==JugadaM):
        print('Tenemos un empate, las ganacias se repartiran')
        DineroJ=(ApuestaTotal/2)+DineroJ
        DineroM=(ApuestaTotal/2)+DineroM
    if(DineroJ<=0):
        print('Has perdido todo tu dinero, perdiste la partida')
    elif(DineroM<=0):
        print('Has dejado a tu oponente sin dinero, ganas la partida')
    else:
        time.sleep(1)
        print('Las cartas se vuelven a barajar, tienes:',DineroJ,'dolares')
        time.sleep(1)
        print('Barajando.')
        time.sleep(1)
        print('Barajando..')
        time.sleep(1)
        print('Barajando...')
        time.sleep(1)
        print('Las cartas han sido barajadas')
    





        


    





