"""Function examples."""

"""Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, prinditakse konsooli I´m inside the function"""
def func():
    print("I´m inside the function")
func()


"""Funktsiooni sisendiks on string, mallis on muutuja nimeks name.
Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, prinditakse konsooli My name is [name], kus [name] asemel prinditakse functiooni sisendiks antud nimi. Näiteks kui kutsutakse välja funtiooni my_name_is("Mari"), prinditakse konsooli My name is Mari"""
def my_name_is(name):
    print(f"My name is {name}") 


"""Funktsiooni sisendiks on int
Funktsioon peab tagastama(return) number 6 ja funktiooni sisendi summa"""
def sum_six(num):
    return 6 + num


"""Funktsiooni sisendiks on kaks täisarvu int, need võib tähistada näiteks a ja b. Mitme funktsiooni sisendu puhul eraldatakse need sulgude sees komaga. Nt: func(a, b)
Funktsioon peab tagastama(return) sisendite summa.
"""
def sum_numbers(a, b):
    return a + b


"""Funktsiooni sisendiks on täisarv int
Kirjuta funktsioon nii, et kui sisendiks on rahasumma dollarites, tagastab funktsioon summa eurodes. Funktsooni testimiseks oletame, et antud hetkel on kurss 1USD = 0.8EUR. Näited:
print(usd_to_eur(100)) # --> 80"""
def usd_to_eur(usd):
    return usd * 0.8