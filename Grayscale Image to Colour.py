import cv2
color_image = cv2.imread(r"C:\Users\Syam Prakash\OneDrive\Pictures\Screenshots\Screenshot (7).png")
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
colorized_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)
cv2.imshow('Color Image', color_image)
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Colorized Image', colorized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
