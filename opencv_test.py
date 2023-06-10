'''画像読み込みテスト'''
import cv2

#画像データのロード
img = cv2.imread('opencv_logo.png')

#色空間の変更
#cv2.COLOR_OOO2XXX ... OOO >> 変更前、XXX >> 変更後 の色空間の名前
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#二値化処理
# cv2.threshold(a, b, c, d)
# a ... グレースケール画像、b, c ... 閾値（今回の場合、画素が127以上なら白、以下なら黒）
ret, thresh = cv2.threshold(gray, 127,255, cv2.THRESH_BINARY_INV)

#輪郭検出
#二値化画像、輪郭検索モードの選択 を行う
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#輪郭描画
# cv2.drawContours(a, b, c, d, e)
# a ... 画像、b ... 輪郭（list）、c ... 描画する輪郭のインデックス
# d, e ... 描画する色、太さ
cv2.drawContours(img, contours, -1, (255, 0, 255), 2)

#描画（以下3つでセット）
#ウィンドウ名、画像データを指定
cv2.imshow('OpenCV', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
