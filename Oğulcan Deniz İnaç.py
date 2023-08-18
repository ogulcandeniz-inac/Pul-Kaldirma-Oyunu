print("---------------PUL KALDIRMA OYUNU---------------")
toplam_pul = int(input("Bu oyunu kaç pul ile oynamak istersiniz? (Sayı Değeri Giriniz): "))
max_pull = int(input("Bir oyuncu en fazla kaç pul çekebilsin? (Sayı Değeri Giriniz): "))

def pul_kaldirma_oyna(max_pull,toplam_pul_adedi):
    while max_pull != 0:
        kisi1 = int(input("1.Oyuncu (Sayı Değeri Giriniz): "))
        #girilen sayıyı kontrol eden sistem
        while toplam_pul_adedi<kisi1:
            if toplam_pul_adedi<kisi1:
                print("HATA::: En Fazla" , toplam_pul_adedi , "adet pul çekebilirsiniz.")
                kisi1 = int(input("1.Oyuncu (Sayı Değeri Giriniz): "))
        max_pull = max_pull-kisi1
        print("Ortada Kalan Pul Sayısı" , max_pull)

        #sıra 1. oyuncudayken pul sayısı 0 veya 0'ın altına düşerse bu koşul çalışır.
        if max_pull==0:
            print("Kazanan 1.Oyuncu WOWWWW")
            print("----------OYUN BİTTİ----------")
            break
        elif max_pull<0:
            print("----------OYUN BİTTİ----------")
            break

        kisi2 = int(input("2.Oyuncu (Sayı Değeri Giriniz): "))
        # girilen sayıyı kontrol eden sistem
        while toplam_pul_adedi<kisi2:
            if toplam_pul_adedi<kisi2:
                print("HATA::: En Fazla" , toplam_pul_adedi , "adet pul çekebilirsiniz.")
                kisi2 = int(input("2.Oyuncu (Sayı Değeri Giriniz): "))
        max_pull = max_pull-kisi2
        print("Ortada Kalan Pul Sayısı", max_pull)

        # sıra 2. oyuncudayken pul sayısı 0 veya 0'ın altına düşerse bu koşul çalışır.
        if max_pull==0:
            print("Kazanan 2.Oyuncu WOWWWW")
            print("----------OYUN BİTTİ----------")
            break
        elif max_pull<0:
            print("----------OYUN BİTTİ----------")
            break

pul_kaldirma_oyna(toplam_pul,max_pull)