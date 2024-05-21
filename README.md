# BilliardProject

Bu Python kodu, video akışında bilardo toplarını, özellikle kırmızı topları tespit edip takip eder. Bu görüntü işleme projesinde OpenCV kullanarak topların izlerini takip eder ve çarpışma sayılarını hesaplar.

## Özellikler

Kırmızı Top Tespiti: Kod, HSV renk uzayında maskeleme kullanarak kırmızı bilardo toplarını tespit etmek üzere tasarlanmıştır.
Yol Takibi: Tespit edilen her topun yolunu takip eder ve izini çizer.
Çarpışma Tespiti: Topların yakınlığına göre çarpışmaları sayar.

## Geliştirilen önemli algoritmalar
Kırmızı topun tespitinde HSV renk aralığında 2 adet alanı temsil etmesinden dolayı 4 adet aralıkta kırmızı rengin tanımı yapılmıştır.
<img width="451" alt="image" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/a401853f-796c-4d1f-b3d9-a789ff852ec1">

![image](https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/ca9cf9a2-681a-4bb4-9c54-2741cb067045)

Tespit edilen kırmızı topların kaç defa diğer kırmızı toplarla çarpışmasını bulmak için topların merkezlerini bir sözlük yapısında tutarak diğer toplarının merkezleri arasındaki mesafe 20 pikselden az olunca çarpışma olduğunu kabul ederek çarpışma sayısını +1 yapmaktadır.
<img width="138" alt="Ekran Resmi 2024-05-21 11 33 38" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/ceae00db-24d9-4a3d-b74e-6b40b561e313">

<img width="558" alt="Ekran Resmi 2024-05-20 20 14 09" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/9dc13c47-7131-4770-9cef-8c52150ecf04">


## Kurulum

Python 3 ve gerekli kütüphanelerin kurulu olduğundan emin olun. Gerekli kütüphaneleri pip kullanarak yükleyebilirsiniz:

pip install opencv-python numpy
## Kullanım

python billiard_detection.py
Video dosyanızın yolunu camera = cv2.VideoCapture("/path/to/your/video.avi") satırında doğru şekilde güncellediğinizden emin olun.

## Kod Çıktıları
###           Tüm çıktılar
![Ekran Resmi 2024-05-20 17 54 09](https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/1a8b8041-4fe5-4e0e-b33d-ddc66e171f72)
<br> Top 1 tespiti <br>
<img width="639" alt="Ekran Resmi 2024-05-20 18 02 45" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/36d87991-39f9-4d77-8f27-d7fbcdc6541d">
<br> Top 2 tespiti <br>
<img width="639" alt="Ekran Resmi 2024-05-20 18 02 58" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/7337586f-d1a9-4226-83a9-4c44c5e6a09e">
<br> Top 3 tespiti <br>
<img width="644" alt="Ekran Resmi 2024-05-20 18 03 10" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/11af4769-015f-496d-8993-bf522b352f2b">
<br> Top 4 tespiti <br>
<img width="640" alt="Ekran Resmi 2024-05-20 18 03 19" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/e232977b-40a7-4574-b3f5-1e0e58a6234a">
<br> Top 5 tespiti <br>
<img width="638" alt="Ekran Resmi 2024-05-20 18 03 27" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/4771ffed-ffd0-4e4b-8167-27086a26021f">
<br> Top 6 tespiti <br>
<img width="640" alt="Ekran Resmi 2024-05-20 18 03 38" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/94a754ff-2b97-48db-886f-8e43f694b202">
<br> Top 7 tespiti <br>
<img width="642" alt="Ekran Resmi 2024-05-20 18 03 48" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/e3003127-7012-4f51-a6ae-571e0b2d7ccb">
<br> Başka bir video da algoritmanın doğru çalıştığını aşağıdaki resim de ispat etmiş oldum. <br>
<img width="1126" alt="Ekran Resmi 2024-05-21 10 20 50" src="https://github.com/sumeyyerginoz/BilliardProject/assets/112480236/3e7cdcfb-e300-4839-8402-8ec69c437e28">


#### Not:

HSV aralıklarını ve alan eşiklerini, özel kullanım durumunuza ve video koşullarınıza göre ayarlayın.
Betik şu anda sadece kırmızı topları takip etmektedir. Diğer renkler için ek HSV aralıkları tanımlayarak ve tespit mantığını güncelleyerek genişletebilirsiniz.
