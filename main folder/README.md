# Détection de Visage avec OpenCV

Ce projet a été réalisé par **Patrick HOUNTON** et utilise OpenCV pour détecter des visages dans des images en utilisant des classificateurs en cascade pré-entrainés. Il est conçu pour les développeurs travaillant dans un environnement d'intelligence artificielle sous Anaconda.

## Prérequis

- Python 3.10 ou version supérieure
- Anaconda
- OpenCV
- TensorFlow

## Installation d'Anaconda

### Guide d'installation Anaconda

1. Aller sur la [page d'installation d'Anaconda](https://www.anaconda.com/products/distribution) et choisir l'installateur correspondant à votre système d'exploitation (Windows, Mac ou Linux). Sélectionner **Python 3.10** ou une version supérieure.
   
2. Suivre les instructions d'installation (très similaire à l'installation de tout autre logiciel).
   
3. Une fois installé, ouvrir le logiciel **Anaconda Navigator** via une recherche sur votre machine.

## Mise en place de l'environnement pour la formation en IA

1. Télécharger le fichier `formation-IA.yml` (fourni avec ce projet).
2. Ouvrir Anaconda Navigator, aller dans l'onglet **Environments**, puis sélectionner **Import**.
3. Sélectionner le fichier `formation-IA.yml`, importer l'environnement et l'activer.
4. Ouvrir **Spyder** depuis l'environnement `formation-IA`.

## Tester l'installation d'OpenCV et TensorFlow

### Test OpenCV

Ouvrir Spyder et exécuter le code suivant pour vérifier que OpenCV est correctement installé :

`python
import cv2
print(cv2.__version__)
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

hello = tf.constant('Hello, TensorFlow!')
with tf.Session() as sess:
    print(sess.run(hello))`
    
##  Exécution du projet
Après avoir configuré l'environnement, vous pouvez exécuter le projet en lançant le script face-detection.py. Celui-ci utilisera les classificateurs en cascade d'OpenCV pour détecter des visages dans une image.

 \`\`\` python face-detection.py \`\`\`

L'image principale avec les visages détectés sera affichée, ainsi que des fenêtres contenant les visages extraits.
