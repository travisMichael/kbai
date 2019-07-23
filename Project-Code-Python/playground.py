import numpy as np
from PIL import Image


for i in range(5, 10):
    print(i)

map = {'one': 1, 'two': 2}
del map['one']
result = map.get('one')

result = list(map.keys())

for i in result:
    print(i)
print('hi')
# for i in range(100, -1, -1):
#     print(i)
#
# for i in range(100):
#     print(i)

# image = Image.open('Problems/Basic Problems C/Basic Problem C-07/A.png').convert("L")
# image_copy = image.copy()
# # image.save('A.png')
#
# np_image = np.array(image)
# np_copy = np.array(image_copy)
#
#
#
# print('hello')


# 0,0   0,1  0,2  0,3  0,4
# 1,0   1,1  1,2  1,3  1,4
# 2,0   2,1  2,2  2,3  2,4
# 3,0   3,1  3,2  3,3  3,4
# 4,0   4,1  4,2  4,3  4,4

# height, width = np_image.shape
#
# for i in range(height):
#     for j in range(width):
#         sum = i + j
#         if sum < height:
#             diff = height - i - j - 1
#             np_copy[i + diff][j + diff] = np_image[i][j]
#             pass
#         if sum > height:
#             diff = i + j % (height - 1)
#             np_copy[i - diff][j - diff] = np_image[i][j]
#             pass
#
# new_image = Image.fromarray(np_copy, mode="L")
# new_image.save('result.png')
# print('done')