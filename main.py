import hist_functions as h
import filter_functions as f
import cv2

# Create image path list
images = h.create_image_path_list("filters\\gray")

# Convert images to grey scale and show/save one of them
grey_images = h.convert_to_grey_scale(images)
image_grey = grey_images[2]
#window_name = "image_grey"
#cv2.imshow(window_name, image_grey)
cv2.imwrite("Image_in_grey_scale.jpg", image_grey)

# Stretch the histogram of images and show/save one of them
hist_str_images = h.histogram_stretch(grey_images)
image_str_hist = hist_str_images[2]
#window_name = "image_str_hist"
#cv2.imshow(window_name, image_hist)
cv2.imwrite("Image_with_stretched_histogram.jpg", image_str_hist)

# Equalize histogram of images and show/save one of them
hist_equal_images = h.histogram_equalization(grey_images)
image_eqal_hist = hist_equal_images[2]
#window_name = "image_equal_hist"
#cv2.imshow(window_name, image_eqal_hist)
cv2.imwrite("Image_with_equalized_histogram.jpg", image_eqal_hist)

# Save histogram 
h.save_histogram(image_grey, "Histogram of a greyscale image")
h.save_histogram(image_eqal_hist, "Equalized histogram")

# Smooth images with 3x3 mask and show/save one of them
smooth_images_3 = f.averaging_filter(grey_images, 3)
image_smooth_3 = smooth_images_3[2]
#window_name = "image_smooth_3"
#cv2.imshow(window_name, image_smooth_3)
cv2.imwrite("Image_after_smoothing_with_3x3_mask.jpg", image_smooth_3)

# Smooth images with 5x5 mask and show/save one of them
smooth_images_5 = f.averaging_filter(grey_images, 5)
image_smooth_5 = smooth_images_5[2]
#window_name = "image_smooth_5"
#cv2.imshow(window_name, image_smooth_5)
cv2.imwrite("Image_after_smoothing_with_5x5_mask.jpg", image_smooth_5)

# Closing all open windows
cv2.destroyAllWindows()
