#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:53:01 2024

@author: sumeyye
"""

import cv2
import numpy as np
from collections import defaultdict

global ball_trajectories, ball_colors, collision_count

# Kırmızı topun HSV renk aralığı
lower_red1 = np.array([0, 100, 150])
upper_red1 = np.array([5, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

# Önceki top merkezlerini ve zaman damgalarını tutmak için sözlük
ball_trajectories = defaultdict(list)  # Topların izlediği yollar
ball_colors = {}  # Her topun rengi
collision_count = 0  # Çarpışma sayısı

def detect_billiard_balls(frame): #vize ödevinde hazırlanan fonksiyon 
    # Kareyi HSV renk uzayına dönüştürün
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk maskeleri oluşturun
    red_mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    combined_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # Maskeleri kullanarak nesnelerin konturlarını bulma
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Belirli bir boyut aralığındaki nesneleri tespit etmek için filtreleme
    min_area = 77  # En küçük kabul edilebilir kontur alanı
    max_area = 777  # En büyük kabul edilebilir kontur alanı

    detected_centers = []  # Tespit edilen top merkezleri

    for contour in contours:
        area = cv2.contourArea(contour)  # Kontur alanını hesapla

        if min_area < area < max_area:
            # Konturun merkezini ve boyutlarını al
            x, y, w, h = cv2.boundingRect(contour)
            centroid_x = x + w // 2
            centroid_y = y + h // 2
            center = (centroid_x, centroid_y)

            # Eğer daha önce başka bir topun merkeziyle çok yakınsa, aynı top olduğunu varsay
            is_duplicate = False
            for prev_center in detected_centers:
                if np.linalg.norm(np.array(center) - np.array(prev_center)) < 20:
                    is_duplicate = True
                    break

            if not is_duplicate:
                detected_centers.append(center)
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)  # Yeşil renkte kontur çiz
                cv2.circle(frame, center, 3, (255, 0, 0), -1)  # Merkezi işaretle

    # Top merkezlerini eşleştir ve izlerini güncelle
    update_trajectories(detected_centers)

    return frame

def update_trajectories(detected_balls):
    global collision_count

    # Yeni tespit edilen topların merkez noktalarını mevcut topların merkez noktalarına eşleştir
    for center in detected_balls:
        # Mevcut toplar arasında en yakın merkezi bul
        closest_id = None
        min_distance = float('inf')  # Başlangıçta tüm topların aynı anda olduğu durumu göz önüne alarak infinity den başlatıyor

        for ball_id, trajectory in ball_trajectories.items():
            if len(trajectory) > 0:
                last_position = trajectory[-1]
                distance = np.linalg.norm(np.array(center) - np.array(last_position))

                if distance < min_distance:
                    min_distance = distance
                    closest_id = ball_id

        # Eşik mesafeye göre yeni bir top veya mevcut bir top olarak değerlendir
        if closest_id is not None and min_distance < 30:  # Eşik mesafesi 30 piksel
            # Çarpışma kontrolü
            for other_id, other_trajectory in ball_trajectories.items():
                if other_id != closest_id and len(other_trajectory) > 0:
                    ### Eğer iki topun merkezi arasındaki mesafe 20 pikselden küçükse, çarpışma olduğunu varsay
                    if np.linalg.norm(np.array(center) - np.array(other_trajectory[-1])) < 20:
                        collision_count += 1

            ball_trajectories[closest_id].append(center)  # Mevcut topun yoluna yeni merkezi ekle
        else:
            new_id = len(ball_trajectories) + 1
            ball_trajectories[new_id].append(center)  # Yeni bir top ekle
            ball_colors[new_id] = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))  # Yeni topa rastgele renk ata

# Video dosyasını açın veya kamera bağlantısını başlatın
camera = cv2.VideoCapture("/Users/sumeyye/Desktop/imageProcesswork/vid_2 kopyası.avi")

while True:
    ret, frame = camera.read()  # Video karesini oku
    if not ret: #bir sorun olduğunda döngüyü kır (break yap)
        break

    # Topları tespit et
    detected_frame = detect_billiard_balls(frame)

    # Tüm topların hareket izlerini çiz ve her top için ayrı bir pencere göster
    for ball_id, trajectory in ball_trajectories.items():
        color = ball_colors[ball_id]
        ball_frame = frame.copy() # her frame de çalışma yapılması adına kopyalandı

        for i in range(1, len(trajectory)):
            cv2.line(ball_frame, trajectory[i - 1], trajectory[i], color, 2)  # Topun izini çiz

        # Top ID'sini yaz
        if trajectory:
            cv2.putText(ball_frame, f"Top {ball_id}", trajectory[-1], cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # Top ID'sini yaz
            cv2.putText(detected_frame, f"Top {ball_id}", trajectory[-1], cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # Ana kareye de top ID'sini yaz

        # Topların tespiti ve hareket izlerini ayrı pencerelerde göster
        cv2.imshow(f"Top {ball_id} Tespiti", ball_frame)

    # Çarpışma sayısını yaz
    cv2.putText(detected_frame, f"Collisions: {collision_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)  # Çarpışma sayısını göster
   
    cv2.imshow("Detected Red Ball", detected_frame) # detected red ball penceresinde kaç çarpışma olduğunu yaz

    # 'q' tuşuna basıldığında çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera serbest bırakma ve pencereleri kapatma
camera.release()
cv2.destroyAllWindows()