# キャラクター画像の置き方

このフォルダに、下の表のファイル名で画像を置くと、地図のピンと一覧が自動でその画像のサムネイルになります。
画像を探す順番：① 店舗ごとの画像 `images/<店舗>.jpg` → ② 事業者共通の画像 `images/brand/<事業者>.jpg` → ③ どちらも無ければ事業者の色の丸いアイコン。
どの店にどのキャラクターのパネルがあるかは公式ページに書かれていないため、まずは②の事業者ごとの画像（16枚）を置き、店ごとに分かったものから①を足していく使い方がおすすめです。

## 事業者共通の画像（images/brand/）

`python3 scripts/fetch_images.py` を実行すると、公式特設ページから自動でダウンロードされます。
あわせて、キャラクターの顔のあたりを正方形に切り抜いたピン用のサムネイル `brand/thumb/<キー>.jpg` も作られます。切り抜く範囲はスクリプト内の `THUMB_CROPS` で調整できます。
吹き出しには横長のキービジュアル全体が表示されます。

| ファイル名 | 事業者 |
|---|---|
| brand/mwt.jpg | 名鉄観光サービス |
| brand/aokis.jpg | アオキーズ・ピザ |
| brand/aoyagi.jpg | 青柳総本家 |
| brand/ebisato.jpg | えびせんべいの里 |
| brand/kiyome.jpg | きよめ餅総本家 |
| brand/kohgen.jpg | 香源 |
| brand/sobajima.jpg | 側島製罐 |
| brand/kagakukan.jpg | FUJIなごや科学館 |
| brand/conv.jpg | 名古屋観光コンベンションビューロー |
| brand/uya.jpg | ひつまぶし う家 |
| brand/myokoen.jpg | 妙香園 |
| brand/mekyopa.jpg | 名鉄協商 |
| brand/nagomiya.jpg | 名鉄生活創研 |
| brand/yabaton.jpg | 矢場とん |
| brand/yamamotoya.jpg | 山本屋 |
| brand/wakashachiya.jpg | 若鯱家 |

## 店舗ごとの画像（images/）

- 形式：JPEG（拡張子 .jpg）。PNGを使う場合は index.html の IMAGE_EXT を ".png" に変更
- おすすめサイズ：縦長 600×800px 程度。ピンでは中央が丸く切り抜かれます
- キャラクター名を吹き出しに出したいときは、index.html の SPOTS で該当行に chara:"名前" を追加
- 1店舗に複数デザインがある場合（矢場とんの全3種など）は、代表の1枚を置いてください

| ファイル名 | 事業者 | 店舗 |
|---|---|---|
| mwt-meieki.jpg | 名鉄観光サービス | 名駅地下支店 |
| mwt-kanayama.jpg | 名鉄観光サービス | 金山駅旅行センター |
| aokis-ikeshita.jpg | アオキーズ・ピザ | 池下店 |
| aokis-nakamurakoen.jpg | アオキーズ・ピザ | 中村公園店 |
| aokis-sakae.jpg | アオキーズ・ピザ | 栄店 |
| aokis-doko.jpg | アオキーズ・ピザ | 土古店 |
| aokis-oe.jpg | アオキーズ・ピザ | 大江店 |
| aoyagi-kitte.jpg | 青柳総本家 | KITTE名古屋店 |
| ebisato-nagaya.jpg | えびせんべいの里 | あつたnagAya店 |
| kiyome-jingumae.jpg | きよめ餅総本家 | 名鉄神宮前駅前店 |
| kohgen-nagoya.jpg | 香源 | 名古屋本店 |
| sobajima-shop.jpg | 側島製罐 | SOBAJIMA shop |
| kagakukan.jpg | FUJIなごや科学館 | 生命館地下2階「あいち・なごや ノーベル賞受賞者記念室」 |
| conv-oasis21.jpg | 名古屋観光コンベンションビューロー | オアシス21 iセンター |
| conv-kanayama.jpg | 名古屋観光コンベンションビューロー | 名古屋市金山観光案内所 |
| uya-yagoto.jpg | ひつまぶし う家 | 八事本店 |
| uya-meieki.jpg | ひつまぶし う家 | 名駅店 |
| myokoen-honten.jpg | 妙香園 | 本店 |
| myokoen-sunroad.jpg | 妙香園 | サンロード店 |
| myokoen-sakaechika.jpg | 妙香園 | サカエチカ店 |
| myokoen-nagaya.jpg | 妙香園 | あつたnagAya店 |
| mekyopa.jpg | 名鉄協商 | めきょぱセンター |
| nagomiya-esca.jpg | 名鉄生活創研 | なごみゃ エスカ店 |
| yabaton-shop.jpg | 矢場とん | YABATON SHOP |
| yabaton-lachic.jpg | 矢場とん | 栄LACHIC店 |
| yabaton-centrise.jpg | 矢場とん | 栄セントライズ店 |
| yabaton-kinshachi.jpg | 矢場とん | 名古屋城金シャチ横丁店 |
| yabaton-esca.jpg | 矢場とん | 名古屋駅エスカ店 |
| yabaton-mitsui.jpg | 矢場とん | 名古屋駅三井ビル北館店 |
| yabaton-centrair.jpg | 矢場とん | 中部国際空港店 |
| yabaton-dome.jpg | 矢場とん | イオンモールナゴヤドーム前店 |
| yamamotoya-okute.jpg | 山本屋 | 大久手店 |
| yamamotoya-otsu.jpg | 山本屋 | 桜通大津店 |
| yamamotoya-jingumae.jpg | 山本屋 | 神宮前店 |
| yamamotoya-ozone.jpg | 山本屋 | 大曽根店 |
| wakashachiya-bino.jpg | 若鯱家 | BINO栄店 |
