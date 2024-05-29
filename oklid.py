# Noktaların Tanımlanması
points = [(3, 8), (5, 9), (1, 6), (2, 7)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print("Tüm noktalar arasındaki mesafeler:", distances)
print("En küçük mesafe:", min_distance)