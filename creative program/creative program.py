print("welcome to your sensai")

a1="katana"
a2="kunai"
weapon=input("enter your weapon type[katana/kunai]:")
if(weapon==a1):
    print("you have selected katana")

    b1="water"
    b2="fire"
    b3="thunder"
    b4="earth"
    b5="Wind"
    ElementalStyle=input("enter your elemental style[water,fire,thunder,earth,wind]:")
    if(ElementalStyle==b1):
        print("you added water element to your katana")
    elif(ElementalStyle==b2):
        print("you added fire element to your katana")
    elif(ElementalStyle==b3):
        print("you added thunder element to your katana")
    elif(ElementalStyle==b4):
        print("you added earth element to your katana")
    elif(ElementalStyle==b5):
        print("you adeed wind element to your katana")
        
    c1="tamahagane"
    c2="adamentium"
    material=input("enter the material for your katana[tamahagen/adamentium]:")
    if (material==c1):
        print("you have selected tamahagane metal for your katana")
    elif(material==c2):
        print("you have selected adamentium metal for your katana")
    print("your katana is ready")
elif(weapon==a2):
    print("you have selected kunai")
    
    b1="FlameExplosion"
    b2="ThunderExplosion"
    b3="FrostExplosion"
    b4="WaterExplosion"
    ExplosiveType=input("select your explosive type[FlameExplosion/ThunderExplosion/FrostExplosion/WaterExplosion]:")
    if(ExplosiveType==b1):
        print("you seelected flame explosion for your kunai")
    elif(ExplosiveType==b2):
        print("you seelected thunder explosion for your kunai")
    elif(ExplosiveType==b3):
        print("you seelected frost explosion for your kunai")
    elif(ExplosiveType==b4):
        print("you seelected water explosion for your kunai")

    c1="titanium"
    c2="adamentium"
    material=("enter the material for your kunai[titanium/adamentium]:")
    if(material==c1):
        print("you have selected titanium metal for your kunai")
    elif(material==c2):
        print("you have selected adamentium metal for your kunai")
    print("your kunai is ready")

print("THANK YOU")
