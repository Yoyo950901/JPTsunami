### 效果

從**気象庁防災情報XML**擷取有關**海嘯觀測**的資料，並依海嘯高度及時間排序輸出到文字檔，讓OBS擷取


### 使用方法

##### 下載檔案
* 下載`JMATsunami.pyw`(建議不要放在系統碟)
* 在**同個資料夾**新增`JMAlog.txt`及`JMAoutput.txt`

##### 工作排程器設定
* 在**工作排程器**點`建立工作`(名稱可以隨意)
* `觸發程序`頁面
    * 新增觸發程序
    * 開始工作：`依排程執行`
    * 重複工作時間：依需求設定
    * 持續時間：`不限制`
* `動作`頁面
    * 新增動作
    * 程式或指令碼：`pythonw`
    * 新增引數：`JMATsunami.pyw`(檔名更改的話這裡也須更改)
    * 開始位置：放置檔案的資料夾路徑
* `條件`頁面
    * 依需求設定
* `設定`頁面
    * 如果工作已在執行中，下列規則將會套用：`以平行方式執行新執行個體`

##### OBS設定
* 新增文字(GDI+)
* `屬性`
    * 勾選`從檔案讀取`
    * 選取剛剛新增的`JMAoutput.txt`
* 其餘文字屬性依需求設定

### 注意事項
* 重複工作時間最低1分鐘，要精確到秒的話可以新增多個觸發程序，並在開始時間調秒數
* 檔案前面沒有JMA的是舊版檔案，使用P2P地震情報的API