import random

def trei_zaruri():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)

    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a,"-",b,"-",c, "\n" "Defender Dice:", d, "-", e )
    Def = (2)
    Atk = (3)

    if a > b:
        x = a
        y = max(b,c) 
    else:
        x = b
        y = max(a,c)   

    if max(x, y) >= max(d, e):
        Def = (Def - 1)
    elif max (x, y) == max(d,e):
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

    if min(x, y) >= min(d,e):    
        Def = (Def - 1)
    elif min(x, y) == min(d,e):   
        Atk = (Atk - 1)  
    else:   
        Atk = (Atk -1)
    
    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return

def trei_cu_unu():

    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)

    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a,"-",b,"-",c, "\n" "Defender Dice:", d)
    Def = (2)
    Atk = (3)
    y = max(a,b,c)   

    if y >= d :
        Def = (Def - 1)
    elif y == d:
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

   
    
    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return

def doi_cu_unu():

    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)

    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a,"-",b,"\n" "Defender Dice:", d)
    Def = (2)
    Atk = (3)
    y = max(a,b)   

    if y >= d :
        Def = (Def - 1)
    elif y == d:
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

   
    
    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return

def doi_cu_doi():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)
    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a,"-",b, "\n" "Defender Dice:", d, "-", e )
    Def = (2)
    Atk = (3)
 
    if max(a, b) >= max(d, e):
        Def = (Def - 1)
    elif max (a, b) == max(d,e):
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

    if min(a, b) >= min(d,e):    
        Def = (Def - 1)
    elif min(a, b) == min(d,e):   
        Atk = (Atk - 1)  
    else:   
        Atk = (Atk -1)

    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return

def unu_cu_doi():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)
    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a, "\n" "Defender Dice:", d, "-", e )
    Def = (2)
    Atk = (3)
 
    if a >= max(d, e):
        Def = (Def - 1)
    elif a == max(d,e):
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return

def unu_cu_unu():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)
    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a, "\n" "Defender Dice:", d)
    Def = (2)
    Atk = (3)
 
    if a >= d:
        Def = (Def - 1)
    elif a == d:
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return

def  start_meniu():
    z = input("How many units attack:")
    k = input ("How many units defend:")
    if z == ("3") and k == ("2"):
        trei_zaruri()
    elif z == ("3") and k ==("1"):
        trei_cu_unu()
    elif z == ("2") and k == ("1"):
        doi_cu_unu()
    elif z ==("2") and k == ("2"):
        doi_cu_doi()
    elif z == ("1") and k == ("2"):
        unu_cu_doi()
    elif z == ("1") and k == ("1"):
        unu_cu_unu()
    else:
        start_meniu()

i = 1
while i == 1:
    start_meniu()