import hist_functions as h
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

# Closing all open windows
cv2.destroyAllWindows()
