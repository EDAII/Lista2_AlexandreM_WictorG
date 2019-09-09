import cv2
import random
import numpy as np

def convert_image(img_tuple, lines, columns):
    new_image = np.empty([lines, columns, 3], dtype="uint8")
    for i in range(lines):
        line = np.empty([columns, 3], dtype="uint8")
        for j in range(columns):
            line[j] = img_tuple[i][j][1]
        new_image[i] = line
    return new_image

def convert_line(original_line):
    size = len(original_line)
    new_line = np.empty([size, 3], dtype="uint8")
    for i in range(size):
        new_line[i] = original_line[i][1]
    return new_line

# def bubblesort(rand_tuples):
#     size = len(rand_tuples) -1
#     for i in range(size):
#         for j in range(size -i):
#             if rand_tuples[j] > rand_tuples[j+1]:
#                 rand_tuples[j], rand_tuples[j+1] = rand_tuples[j+1], rand_tuples[j]
#     return rand_tuples



def selection_sort(rand_tuples, new_image, pos):
    size = len(rand_tuples)
    for i in range(size):
        for j in range(i+1, size):
            if rand_tuples[j][0] < rand_tuples[i][0]:
                aux = rand_tuples[i]
                rand_tuples[i] = rand_tuples[j]
                rand_tuples[j] = aux

    return rand_tuples





if __name__ == "__main__":
    img = cv2.imread('arya.jpeg')
    # cv2.imshow('Arya, The Cat', img)

    linhas = len(img)
    colunas = len(img[0])
    new_image = np.empty([linhas, colunas, 3], dtype="uint8")
    img_tuples = []
    img_random_tuples = []

    #Create img vector with tuples information
    for i in range(linhas):
        line_tuple = []
        for j in range(colunas):
            line_tuple.append((j, img[i][j]))
        img_tuples.append(line_tuple)

    #Randomiz vector with tuples
    for i in range(linhas):
        line_tuple = img_tuples[i]
        random.shuffle(line_tuple)
        img_random_tuples.append(line_tuple)

    #Convert vector with tuples to printable numpy vector
    # for i in range(linhas):
    #     line = np.empty([colunas, 3], dtype="uint8")
    #     for j in range(colunas):
    #         line[j] = img_random_tuples[i][j][1]
    #     new_image[i] = line

    # print('linhas: ' + str(linhas) + '\ncolunas: ' + str(colunas))
    # print(img)
    # print(new_image)

    new_image = convert_image(img_random_tuples, linhas, colunas)
    for i in range(linhas):
        tuple_line = selection_sort(img_random_tuples[i], new_image, i)
        converted_line = convert_line(tuple_line)
        if i == 1:
            print(tuple_line)
        new_image[i] = converted_line
        cv2.imshow('Something', new_image)
        cv2.waitKey(1)
        print('passou')
