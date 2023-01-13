import cv2 

img = cv2.imread("solar-system.jpg")

print(img)

cv2.putText(img, "Sun", (41, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Mercury", (90, 220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (180, 220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (270, 220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Moon", (340, 180), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255))
cv2.putText(img, "Mars", (360, 220), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (470, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Saturn", (670, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Uranus", (900, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Neptune", (1100, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.imshow("Image", img)
cv2.waitKey(0)