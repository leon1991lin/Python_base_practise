#字串處理

docs = """上蓋顏色：黑色
處理器：Intel Core i7-10510U Processor ( 1.80GHz 8MB )
記憶體：16.0GB DDR4 SDRAM 2666 DDR4 SDRAM Onboard 2666MHz
光碟機：NA
硬碟機：512GB_SSD_M.2_2280_NVME_TLC_OP
顯示晶片：Intel UHD 顯示卡
螢幕：13.3"FHD, IPS, AntiGlare, LED Backlight, Non-Touch 1920x1080
音訊：Dolby Audio Premium®/降噪雙陣列遠場麥克風
網路攝影機：720p
有線網路：無
無線網路：Intel Wi-Fi 6 AX201 2x2a
藍芽：5.1 版
讀卡機：Y
連接埠： 2 x USB 3.1 Gen 1  2 x USB-C  HDMI：1 x HDMI
鍵盤：採用白色 LED 照明的背光功能
尺寸：311.5 公釐 x 219 公釐 x 17.6 公釐
重量：1.38kg
作業系統：Windows 10 PRO
電池：4 Cell 鋰聚合物電池 45Wh
指紋辨識：Y
快充：Y
國際條碼 (EAN)：195477313408
保固：1年台灣保固"""

#1.1 找出文章內最長的數字串,包含整數跟小數

#以正規表達式選出文章中的整數與小數
import re
num = re.findall("([\d]+[\.\d]*)",docs)
ans = "" 

#利用 for 逐一比較每個數值的長度，選出最長者
for i in num:

    if len(i) > len(ans):
        ans = i        
print(ans)

#答案是 195477313408

#1.2將文章內的數字全部替代成 '$'
#用 compile 將數字建立為 patten

docs1 = re.compile("([\d]+[\.\d]*)")

#以 sub 將以建立的 patten 替換成$

result = docs1.sub("$",docs)
print(result)
