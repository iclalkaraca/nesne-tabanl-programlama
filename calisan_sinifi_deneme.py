from pickle import PROTO


class Birey():
    def __init__(self,isim,soyisim,tcno):
        self.isim=isim
        self.soyisim=soyisim
        self.tcno=tcno

class Calismayan(Birey):
    pass

class Calisan(Birey):
    def __init__(self,isim,soyisim,tcno,idno,maas):
        Birey.__init__(self,isim,soyisim,tcno)    #yukarıdaki birey tek trk yazmqmqk için
        self.idno=idno
        self.maas=maas

    def zam(self,deger):
        self.maas += deger


class Muhendis(Calisan):
    def __init__(self,isim,soyisim,tcno,idno,maas,yazilim_dilleri,yabanci_diller,bilinen_programlar):
        Calisan.__init__(self,isim,soyisim,tcno,idno,maas)
        self.yazilimDilleri=yazilim_dilleri
        self.yabanciDiller=yabanci_diller
        self.bilinenProgramlar=bilinen_programlar


class Muhasebeci(Calisan):
    def __init__(self,isim,soyisim,tcno,idno,maas,bilinen_programlar):
        Calisan.__init__(self,isim,soyisim,tcno,idno,maas)
        self.bilinenProgramlar=bilinen_programlar

x= Muhendis("asya","elmas",12345678,4321,80000,("python","c#"),"ingilizce","MS office")
y= Muhasebeci("aslı","kara",87654321,6578,50000,("CNR",))
print(x.yazilimDilleri)
print(y.bilinenProgramlar)

print("X Maaş:",x.maas)
print("Y Maaş:",y.maas)
x.zam(500)
print("X Maaş:",x.maas)
print("Y Maaş:",y.maas)