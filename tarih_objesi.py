from datetime import date

class Kitap():
    def __init__(self,yazar,isim,basimTarihi:date,sayfaSayisi):
        self.yazar=yazar
        self.isim=isim
        self.basimTarihi=basimTarihi
        self.sayfaSayisi=sayfaSayisi

x= Kitap("paulo coelho","simyacı",date(2018,3,5),140)
print(x.sayfaSayisi)