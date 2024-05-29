# Noktalar Arasındaki Mesafelerin Hesaplanması

Bu Python programı, verilen bir nokta listesi içindeki noktalar arasındaki Öklid mesafelerini hesaplar ve bu mesafeler arasındaki en küçük mesafeyi bulur. Programın her adımı açıklamalarla belirtilmiştir.

## Adımlar

### Adım 1: Noktaların Tanımlanması

Programın başlangıcında, `points` adında bir liste tanımlanır. Bu liste, 2D uzaydaki noktaları temsil eden demetler içerir. Her bir demet, bir noktanın koordinatlarını içerir.

### Adım 2: Öklid Mesafesi İçin Bir Fonksiyon Yazma

Öklid mesafesi hesaplamak için `euclideanDistance` adında bir fonksiyon tanımlanır. Bu fonksiyon, iki nokta arasındaki Öklid mesafesini hesaplar ve bu mesafeyi döndürür.

### Adım 3: Mesafelerin Hesaplanması

Listedeki her nokta çifti için, Öklid mesafesi hesaplanır ve `distances` adlı bir listede saklanır. Her nokta çifti için mesafe hesaplanırken, aynı noktalar arası mesafeler tekrar hesaplanmaz.

### Adım 4: Minimum Mesafenin Bulunması

`distances` listesinden en küçük mesafe bulunur ve `min_distance` adlı bir değişkende saklanır.

### Adım 5: Sonuçların Yazdırılması

Hesaplamalar tamamlandıktan sonra, program tüm noktalar arasındaki mesafeleri ve en küçük mesafeyi ekrana yazdırır.

  ```python
    print("Tüm noktalar arasındaki mesafeler:", distances)
    print("En küçük mesafe:", min_distance)
```

## Nasıl Kullanılır?

1. Öncelikle, bilgisayarınızda Python'un yüklü olduğundan emin olun. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirip yükleyebilirsiniz.

2. Projeyi GitHub'dan indirin veya klonlayın:

   ```bash
   git clone https://github.com/melikeisk/oklid.git
   ```

3. İndirilen dizine gidin:

   ```bash
   cd oklid
   ```

4. Terminal veya komut istemcisinde şu komutu çalıştırarak programı başlatın:

   ```bash
   python oklid.py 
   ```