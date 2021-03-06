# IoTtalk-Demo-Frame
這個專案的主要目的是重建位於台北天龍的展架。<br/>
程式碼參考自 [IoTtalk/SensorBox](https://github.com/IoTtalk/SensorBox) 以及 [IoTtalk/Dummy_Device_IoTtalk_v1_py](https://github.com/IoTtalk/Dummy_Device_IoTtalk_v1_py) (取用程式碼風格、bridge client 和 IoTtalk v1 python SDK)<br/>
另外，這是一份備忘錄，如果之後需要重建類似的展架，可以直接取用。

## 規格
- 開發板 : Arduino Yun
- Python 2
- Arduino韌體使用到的函式庫
  - [Grove BME280](https://github.com/Seeed-Studio/Grove_BME280)
- Arduino Yun上的感測器
  - Grove - BME280
  - Grove - Light Sensor
  - 土壤濕度感測器 (目前失效)
  - 繼電器

## 接線

### Grove - BME280
Grove - BME280| Arduino Yun
--------------|------------
紅            | VCC
黑            | GND
白            | D2
黃            | D3

<br/>

### Grove - Light Sensor
Grove - BME280| Arduino Yun
--------------|------------
紅            | VCC
黑            | GND
白            | X (不接)
黃            | A1

### 土壤濕度感測器 (目前失效)
土壤濕度感測器 | Arduino Yun
--------------|------------
粉紅          | VCC
黑            | GND
橘            | A0

### 繼電器1 (接智慧開關)
繼電器1 | Arduino Yun
-----------|----
VCC        | VCC
GND        | GND
DC+ (訊號) | D4

### 繼電器2 (接智慧開關)
繼電器1 | Arduino Yun
-----------|----
VCC        | VCC
GND        | GND
DC+ (訊號) | D5

### 繼電器3 (接智慧開關)
繼電器1 | Arduino Yun
-----------|----
VCC        | VCC
GND        | GND
DC+ (訊號) | D6

## IoTtalk Server 設定
創建下列Device Feature:

名稱                | df  | 型態
--------------------|-----|-----
temperatures        | idf | float
atmosphericPressure | idf | float
altitude            | idf | float
humidity            | idf | float
lightSensor         | idf | int
moisture            | idf | float
relay1              | odf | int
relay2              | odf | int
relay3              | odf | int

創建Device Model :
- 名稱 : `Tano_Demo`
- Input Device Features (idf) : 見上表，共6個
- Output Device Features (odf) : 見上表，共3個

## 韌體
### 燒錄 Arduino 韌體
Arduino韌體負責接收來自感測器的數值，再透過Yun Bridge將資料送給Linux系統。<br/>
.ino檔可以在這個[repository裡面](https://github.com/twbrandon7/IoTtalk-Demo-Frame/tree/master/TanoDemo)找到，在燒錄上Arduino Yun之前，請先確保在IDE已經安裝完[Grove BME280](https://github.com/Seeed-Studio/Grove_BME280)。<br/>

### 上傳Linux系統中的python程式
python負責與IoTtalk Server連線。<br/>
請使用SFTP連線到Arduino Yun，並且把下列檔案上傳到 `/~` 目錄 : 
- DAI.py
- DAN.py
- autoStart.py
- config.py
- csmapi.py
- wrt_lib.py

*上傳之前請先更改 `config.py` 檔裡面的IoTtalk Server IP

## 後記
設定完成之後，Arduino Yun上的紅色LED燈會長亮，藍色LED燈會以固定頻率閃爍。

