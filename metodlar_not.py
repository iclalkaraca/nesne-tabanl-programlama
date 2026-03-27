
class Kitap:
    def __init__(self,yazar,isim,sayfaSayisi:int):
        self.__yazar=yazar
        self.__isim=isim
        self.__sayfaSayisi=sayfaSayisi

    def getYazar(self):
        return self.__yazar

    def getIsim(self):
        return self.__isim

    def getsayfaSayisi(self):
        return self.__sayfaSayisi

    def __str__(self):                #str print edildiğinde ekrana basılacak stringi verir
        return self.__yazar + "" + self.__isim + "" + str(self.__sayfaSayisi)

    def __len__(self):         #uzunluk kitabın uzunluğunu verir
        return self.__sayfaSayisi

    def __del__(self):         #silmek için silinince ekrana basılması için
        print("{} yazarına ait olan {} isimli kitap silindi".format(self.__yazar,self.__isim))

x=Kitap("paulo coelho","aldatmak",250)
print(str(x))
print(len(x))
del x