#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2 as cv
import matplotlib.pyplot as plt

# Charger les classificateurs en cascade pré-entrainés
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Charger les images
img = cv.imread('youngMenandWomen.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Exécution de la détection de visage
# detectMultiScale(image, scale factor, number of neighbors)
faces = face_cascade.detectMultiScale(gray, 1.1, 8)

# Affichage des visages
i = 0
for (x, y, w, h) in faces:
    # Dessiner le rectangle sur l'image principale
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Extraire les visages de l'image principale
    face = img[y:y+h, x:x+w]
    
    # Afficher chaque visage détecté avec matplotlib
    plt.figure()
    plt.imshow(cv.cvtColor(face, cv.COLOR_BGR2RGB))
    plt.title('Face {}'.format(i))
    plt.axis('off')  # Masquer les axes
    i += 1

# Afficher l'image principale avec les rectangles autour des visages
plt.figure()
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Image Principale')
plt.axis('off')  # Masquer les axes
plt.show()
