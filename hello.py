#print("Show them wha I am ") 
#1-task print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")
#2-task print(22%4)
#3-task
# a = 125
# s= a**2
# l = 4*a
# print(s,"and ", l)

#4-task
# d = 12
# p = 3.14
# S = p*d/4
# print(S)


# 5-task
# a = 6
# b = 7
# c = (a**2 + b**2)**(1/2)
# print(c)

# ism = input(str("Ismingiz nma "))
# familiya = "Bond"
# print("Tanishganimdan hursandman" + " " + ism.capitalize())

# # Sonlar 
# a = 20
# b = -2.4
# temp = 36.6
# print(type(temp))
# Katta harflar bilan yozilgan bulsa Canstanta hisoblanadi 



# t_yil = input("Tug'ilgan yilingizni kiriting ")
# yosh = 2025 - int(t_yil)
# print("Siz", yosh, "yoshdasiz")

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# #Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
# print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")





# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
# print("Men tarixiy shaxslardan "+ z_shaxslar.pop(1) + " bilan uchrashdim")





# friends = []
# friends.append("Sardor")
# friends.append("Rasul")
# friends.append("Ma'ruf")

# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(-1))


# 13.03.2025
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
# davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
# print(len(davlatlar))
# print(sorted(davlatlar, reverse=True))


# a = list(range(120,1200,2))
# print(sum(a))
# print(min(a) - max(a))
# print(a[:20])

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# ismlar = ['Ali','Vali','Hasan','Husan','Olim']
# for ism in ismlar:
#     print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# a = list(range(11,100,2))
# kub = []
# for n in a:
#     kub.append(n**3)
# print(kub)

# kinolar = []
# for kino in range(0,5):
#     kinolar.append(input(f"{ kino+1 }- kino  ismini kiriting:" ))
# print(kinolar)


# 14.03.2025

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
   

# ism = input("Ism kiriting ")
# if ism.lower() != 'ali':
#     print("Uzr biz Alini kutyapmiz")
# else:
#     print("Salom Ali")


# login = input("Login kiriting ")
# if len(login)<=5 :
#     print("login 5 harfdan kup bilishi kerak")


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())




# user = input("Ismingizni kiriting ")
# if user.lower() == 'admin' :
#     print("Salom admin")
# else:
#     print("Xush kelibsiz" + " " + user)



# a = int(input("1-Son Kiriting "))
# b = int(input("2-Son Kiriting "))

# if a==b:
#     print("Sonlar teng ekan")


#15.03.2025 Dict
# car = {'model':'BMW', 'rangi':'qora'}
# print(car['model'])

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# car1= car.get('model1', 'Bu dict da yuq')
# print(car1)


#task one
# otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }

# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")



# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

# 1- task
# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}
# key_list = []

# for key in python_words.keys():
#     key_list.append(key)
    
# print(sorted(key_list))


davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)


# for davlat in sorted(davlatlar.keys()):
#     print(davlat)

davlat_nomi = str(input("DaVLAT NOMINI KIRITING "))
if davlat_nomi.lower() in davlatlar.keys():
    print(davlatlar[davlat_nomi.lower()].upper())

else:
    print(davlat_nomi.upper() + "degan davlat list da yuq")
