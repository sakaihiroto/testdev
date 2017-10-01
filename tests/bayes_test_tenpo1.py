from bayes import BayesianFilter
import pickle

bf = BayesianFilter()
# テキストを学習
bf.fit("兵庫県伊丹市中央4丁目3-9","住所")
bf.fit("072-773-5526","電話番号")
bf.fit("9：30～19：50","営業時間")
bf.fit("サンドラッグ　伊丹中央店","店舗名")
bf.fit("富山県富山市五福3640番地5","住所")
bf.fit("076-471-7646","電話番号")
bf.fit("9:00～:21:00","営業時間")
bf.fit("中部薬品　五福店","店舗名")
bf.fit("佐賀県佐賀市新中町6-11","住所")
bf.fit("0952-32-7111","電話番号")
bf.fit("9:00～3:00","営業時間")
bf.fit("ドン・キホーテ佐賀店","店舗名")
bf.fit("東京都新宿区新宿３丁目３８番１号","住所")
bf.fit("03-5269-1111","電話番号")
bf.fit("10時30分～22時30分","営業時間")
bf.fit("ルミネエスト新宿","店舗名")

f = open('./tenpo1.textfile','wb')
pickle.dump(bf,f)
f.close


# 予測
pre, scorelist = bf.predict("埼玉県新都心市ラーメン太郎")


print("結果=", pre)
print(scorelist)

