'''画像読み込みテスト'''
import cv2

#画像データのロード
img = cv2.imread('onnpu.jpeg')

#色空間の変更
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#二値化処理
ret, thresh = cv2.threshold(gray, 127,255, cv2.THRESH_BINARY_INV)

#輪郭検出
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#輪郭描画
cv2.drawContours(img, contours, -1, (255, 0, 255), 2)

#描画（以下3つでセット）
cv2.imshow('OpenCV', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
