import numpy as np
import matplotlib.pyplot as plt
import scipy


# fig = plt.subplots(figsize=(14, 8))

# random_image = np.random.random([500, 500])
# plt.imshow(random_image, cmap='gray', interpolation='nearest')
# plt.show()

image = plt.imread('./images/red_panda.jpg')
# plt.imshow(image)
# print(image.shape)

# y = image.shape[0]
# x = image.shape[1]
# h = 7
# w = (y / x) * h
# plt.figure(figsize=(w, h))
# plt.imshow(image[1000:1500, 1200:2000, :])
# plt.imshow(1 - image[1000:1500, 1200:2000, :])
# plt.imshow(np.mean(image, axis=2), cmap='gist_gray')
# rotate_face = scipy.ndimage.rotate(image, -45)
# plt.imshow(rotate_face)

blurred_image_2 = scipy.ndimage.gaussian_filter(image, sigma=2)
blurred_image_4 = scipy.ndimage.gaussian_filter(image, sigma=4)

fig, axs = plt.subplots(1, 3, figsize=(50, 100))

axs[0].imshow(image)
axs[1].imshow(blurred_image_2)
axs[2].imshow(blurred_image_4)

plt.show()
