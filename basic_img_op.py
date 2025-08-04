import cv2

img = cv2.imread('image1.jpg')

resizing = cv2.resize(img,(640, 840)) #width, height
graying = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurring = cv2.GaussianBlur(img, (15,15), 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow("The original image ", img)
cv2.imshow("Resized Image ", resizing)
cv2.imshow("Gray Image ", graying)
cv2.imshow("Blurred Image ", blurring)
cv2.imshow("Marking Edges ", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
