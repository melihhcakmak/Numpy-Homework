import numpy as np
arr1 = np.array([1,2,3,4,5,6])
print(arr1) #Virgüller yazdırılmaz.
arr2 = np.array((1,2,3,4,5,6))
print(arr1) #Her şekilde köşeli parantez ile yazdırır.
print(type(arr1)) #type yazdırma
#Oluşturduğumuz dizinin data tipini yazdırma
print(arr1.dtype)
#Arrayin tüm elemanlarını floatmışçasına yazdırma
arr1 = np.array([1,2,3,4,5,6],dtype = float)
print(arr1)
#Arrayin tüm elemanlarını complex tipinde yazdırma
arr1 = np.array([1,2,3,4,5,6],dtype = complex)
print(arr1)
#İki boyutlu dizi oluşturma (Dizi içerisinde dizi)
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.ndim)
#Çıktıyı yeniden şekillendirme
arr1 = np.array([[1,2,3,4,5,6]])
arr1 = arr1.reshape(6,1) #6satır,1sütun
print(arr1)
#Verdiğimiz aralıktaki sayıları yazdırma
arr1 = np.arange(0,10)
print(arr1)
#Verdiğimiz aralıktaki sayıları atlayarak yazdırma
arr1 = np.arange(0,10,2)
print(arr1)
#Dizi kopyalama
arr2 = arr1.copy()
print(arr2)
#0-1 arasında random sayılardan oluşan bir numpy dizisi oluşturma
arr1 = np.random.random((4,3,3))
print(arr1)
arr1 = np.random.random((4,3))
print(arr1)
arr1 = np.random.random((5))
print(arr1)
#10'dan küçük 6 tane sayı yazdıralım
arr2 = np.random.randint(10,size = 6)
print(arr2)
#İstediğimiz sütunu/satırı yazdırma
arr3 = np.arange(1,11)
arr3 = arr3.reshape(5,2)
ikinci_satır = arr3[1]
ilk_iki_satır = arr3[0:2]
print(ikinci_satır)
print(ilk_iki_satır)
birinci_sütun = arr3[:,0]
print(birinci_sütun)
ikinci_sütun = arr3[:,1]
print(ikinci_sütun)
print(arr3)
eleman = arr3[2,1] #3. satır 2. sütun
print(eleman)
#Diziyi ters çevirmek
tersi = arr3[::-1]
print(tersi)
#Sıfırlardan,1lerden oluşan matris oluşturmak
arr4 = np.zeros((6,3,2)) #6 satırlı, 3 sütunlu, 3 boyutlu
print(arr4)
print(arr4.ndim)
arr4 = np.ones((6,3,2))
print(arr4)
arr1 = np.eye(5) #5e 5 lik bir matriste 
print(arr1)
#Matris birleştirme
arr5 = np.arange(1,7)
arr5  = arr5.reshape(2,3)
arr6 = np.arange(7,13)
arr6  = arr6.reshape(2,3)
birlesme = np.concatenate([arr5,arr6], axis = 1) #yanyana birleştirme
print(birlesme)
birlesme = np.concatenate([arr5,arr6], axis = 0) #altalta birleştirme
print(birlesme)
#Max ve min eleman yazdırma
a = arr6.max() 
b = arr5.min()
print(a)
print(b)
#Elemanların toplamını yazdırma
c = arr6.sum()
print(c)
#Satır ve sütunların toplamını yazdırma
satirlarin_toplami = birlesme.sum(axis=1)
sütunlarin_toplami = birlesme.sum(axis=0)
print(satirlarin_toplami)
print(sütunlarin_toplami)
#Ortalama değer ve varyans ve standdart sapma alma
ortalama = birlesme.mean()
print(ortalama)
varyans = birlesme.var()
print(varyans)
standart_sapma = birlesme.std()
print(standart_sapma)
#Farkli dizilerin elemanlarıyle işlem yapma
print(arr5)
print(arr6)
islem = arr5 + arr6
print(islem)
islem2 = arr5 * arr6
print(islem2)
islem3 = arr6 % arr5
print(islem3)
islem4 = arr5 * 2
print(islem4)
islem5 = np.sin(arr5)
print(islem5)
islem6 = np.exp(arr6) #Her elemanı teker teker eulear sayısının üstüne alma
print(islem6)
islem7 = np.log(arr5) #Doğal logaritma
print(islem5)
#Matris çarpımı
arr1 = np.arange(1,7)
arr1  = arr1.reshape(2,3)
arr2 = np.arange(7,13)
arr2  = arr2.reshape(3,2)
result = np.dot(arr1,arr2)
print(result)
#Matris transpozu alma (Satırlar sütun, sütunlar satır olacak)
transpoz = arr1.T
print(transpoz)
#Array elemanlarını bool türüne dönüştürme
dogruluk = arr2 > 10
print(dogruluk)
dogruluk2 = arr2[arr2 > 9] # Sadece sağlayan elemanlar yazdırılır.
print(dogruluk2)
np.save("terminatör",arr2) # arr2 datasını terminatör adlı dosyaya kaydedecek
arr10 = np.load("terminatör.npy") # dosyada bulunan datayı arr10 a yükleyelim ve yazdıralım.
print(arr10)


