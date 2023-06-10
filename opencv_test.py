'''画像読み込みテスト'''
import cv2

#画像データのロード
img = cv2.imread('onnpu.jpeg')

#描画
cv2.imshow('OpenCV', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('save.jpeg', img)
