import os
import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist         # библиотека базы выборок Mnist
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
import emnist
from pathlib import Path
from pytesseract import image_to_string

model = keras.models.load_model('../semple/model_char_degit.h5')

# '../data/test/test_image_6.jpg'
path_file = open("$temp_path_file.txt", "r")
image = cv2.imread(path_file.read())
os.remove('$temp_path_file.txt')
print(path_file.read())
grey = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)

# обрезка шума               изображение, порог, светлые, темные
ret, thresh = cv2.threshold(grey.copy(), 160, 255, cv2.THRESH_BINARY_INV)
# поиск контуров
_, contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
preprocessed_digits = []

for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    # пропуск шумов
    if (w < 10 or h < 50):
        continue

    # Создание прямоугольника вокруг цифры на исходном изображении (для отображения цифр, выбранных с помощью контуров)
    cv2.rectangle(image, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)

    # Вырезание цифры из изображения, соответствующей текущим контурам в цикле for
    digit = thresh[y:y + h, x:x + w]

    # Изменение размера этой цифры на (18, 18)
    resized_digit = cv2.resize(digit, (18, 18))

    # Дополняем цифру 5 пикселями черного цвета (нулями) с каждой стороны, чтобы в конечном итоге получить изображение (28, 28)
    padded_digit = np.pad(resized_digit, ((5, 5), (5, 5)), "constant", constant_values=0)

    # Добавление предварительно обработанной цифры в список предварительно обработанных цифр
    preprocessed_digits.append(padded_digit)
    # print("\n\n\n----------------Contoured Image--------------------")
plt.imshow(image, cmap="gray")
plt.show()

inp = np.array(preprocessed_digits)

# ----------------------------------------recognising chars--------------------------------------------------------------

diction = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9', \
           '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F', '16':'J', '17':'H', \
            '33':'*', '34':'/', '46':'+'}

my_file = open("$temp_recognised_char.txt", "w+")

for digit in preprocessed_digits:
    print ("=========PREDICTION============ \n\n")
    prediction = model.predict(digit.reshape(1, 28, 28, 1))

#   вывод картинки
    plt.imshow(digit.reshape(28, 28), cmap="gray")
    plt.show()
#   вывод результата
#     print("\nFinal Output: {}".diction(format(np.argmax(prediction))))
    print("\nFinal Output: ")
    print(diction[format(np.argmax(prediction))])
    my_file.write(diction[format(np.argmax(prediction))])

    # hard_maxed_prediction = np.zeros(prediction.shape)
    # hard_maxed_prediction[0][np.argmax(prediction)] = 1
    # print ("\nHard-maxed form of the prediction: \n {}".format(hard_maxed_prediction))

  # вывод вектора
  #   print ("\nPrediction (Softmax) from the neural network:\n\n {}".format(prediction))
  #   hard_maxed_prediction = np.zeros(prediction.shape)
  #   hard_maxed_prediction[0][np.argmax(prediction)] = 1
  #   print ("\nHard-maxed form of the prediction: \n {}".format(hard_maxed_prediction))
    print ("\n---------------------------------------\n")

my_file.close()