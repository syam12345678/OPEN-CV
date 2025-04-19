import cv2
img = cv2.imread(r"C:\Users\Syam Prakash\OneDrive\Pictures\Screenshots\Screenshot (7).png")
cv2.imshow("hitman", img)
height = img.shape[0]
width = img.shape[1]
print ("The height of the image is: ", height)
print ("The width of the image is: ", width)
cv2.waitKey(0)
