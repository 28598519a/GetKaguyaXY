# GetKaguyaXY

用於Atelier kaguya

在解出 *.alp檔後，用此程式將可計算出 XY Offset list

使用方法及運用建議:
1. 建兩個主要資料夾放解包文件
2. 使用Garbro以as is先解一次至資料夾1
3. 使用Garbro以PNG解第二次至資料夾2 (子資料夾名稱命名須與資料夾1內的子資料夾相同)
4. 執行GetKaguyaXY.py，拖曳資料夾1至程式視窗中，此時程式內應顯示出資料夾1的完整路徑 (或是手動輸入資料夾1的絕對路徑亦可)
5. 執行完後在GetKaguyaXY.py的路徑下，應出現AlpXY_Offset.txt (此時資料夾1可刪，後續拿資料夾2裡的檔案去做合成即可)
6. 以GalPhotoAuto，選擇 常規合成規則 -> 方位與座標 -> X Y 特別設定 (此時參考AlpXY_Offset.txt去設定即可)

顯然有合成座標後，利用GalPhotoAuto進行手動合成會比猜測合成法快上許多，然而目前仍未找到自動合成的方法，因為沒合成表，只能用肉眼看去猜誰是底圖以及對應的分離圖來手動合成
