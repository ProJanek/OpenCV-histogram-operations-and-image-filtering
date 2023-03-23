import hist_functions as h
import filter_functions as f
import cv2

# Create a list of paths to noisy images
images = h.create_image_path_list("filters\\gray")

# Convert images to grey scale and save one of them
grey_images = h.convert_to_grey_scale(images)
image_grey = grey_images[2]
cv2.imwrite("Image_in_grey_scale.jpg", image_grey)

# Stretch the histogram of images and save one of them
hist_str_images = h.histogram_stretch(grey_images)
image_str_hist = hist_str_images[2]
cv2.imwrite("Image_with_stretched_histogram.jpg", image_str_hist)

# Equalize histogram of images and save one of them
hist_equal_images = h.histogram_equalization(grey_images)
image_eqal_hist = hist_equal_images[2]
cv2.imwrite("Image_with_equalized_histogram.jpg", image_eqal_hist)

# Save histogram 
h.save_histogram(image_grey, "Histogram of a greyscale image")
h.save_histogram(image_eqal_hist, "Histogram after equalization")

# Smooth images with 3x3 mask and save one of them
smooth_images_3 = f.averaging_filter(grey_images, 3)
image_smooth_3 = smooth_images_3[2]
cv2.imwrite("Image_after_smoothing_with_3x3_mask.jpg", image_smooth_3)

# Smooth images with 5x5 mask and save one of them
smooth_images_5 = f.averaging_filter(grey_images, 5)
image_smooth_5 = smooth_images_5[2]
cv2.imwrite("Image_after_smoothing_with_5x5_mask.jpg", image_smooth_5)

# Create a list of paths to noisy images
images = h.create_image_path_list("filters\\ga")

# Convert noisy images to grey scale and save one of them
noisy_grey_images = h.convert_to_grey_scale(images)
noisy_image_grey = noisy_grey_images[2]
cv2.imwrite("Noisy_image_in_grey_scale.jpg", noisy_image_grey)

# Smooth noisy images with gauss filter and save one of them
gauss_images = f.gauss_filter(5, 1, noisy_grey_images)
image_gauss = gauss_images[2]
cv2.imwrite("Noisy_image_after_smoothing_with_gauss_filter.jpg", image_gauss)

# Closing all open windows
cv2.destroyAllWindows()
