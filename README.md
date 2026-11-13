# コラボパネル設置場所マップ

『ラブライブ！シリーズ』×「ラブナゴヤ！フェス」のパネル設置場所、スタンプ数、ノベルティカードの配布条件を表示する地図ページです。

## ファイル
- `index.html` … 地図ページ本体（このファイル1つで動きます）
- `images/` … キャラクター画像の置き場所。ファイル名の一覧は `images/README.md` にあります

## Google マップで表示する手順
APIキーが空のままだと OpenStreetMap で表示されます。Google マップにする場合：

1. Google Cloud コンソールでプロジェクトを作り、請求先アカウントを設定する
2. 「Maps JavaScript API」を有効にする
3. 「認証情報」で APIキーを作り、**HTTPリファラー制限**に公開先のURL（例：`https://example.github.io/*`）を設定する
   ※キーはページのソースから誰でも見えるため、制限をかけないと他人に使われるおそれがあります
4. 「マップ管理」で Map ID を作る（地図の種類は JavaScript／ベクター）
5. `index.html` 冒頭の設定欄に書き込む
   ```js
   const GOOGLE_MAPS_API_KEY = "取得したキー";
   const GOOGLE_MAP_ID = "作成した Map ID";
   ```

`GOOGLE_MAP_ID` は動作確認だけなら `DEMO_MAP_ID` のままでも動きます。

## 公開方法（Cloudflare Pages）
APIキーはリポジトリに入れず、Cloudflare Pages のビルド時に書き込みます。

- フレームワーク：なし
- ビルドコマンド：`sed -i "s/__GOOGLE_MAPS_API_KEY__/$GOOGLE_MAPS_API_KEY/g" index.html`
- 出力ディレクトリ：`/`
- 環境変数：`GOOGLE_MAPS_API_KEY` にキーを登録（種類は「シークレット」）
- 閲覧者の限定：Cloudflare Zero Trust → Access でアプリケーションを作り、許可するメールアドレスを登録

## ローカルで確認する
`config.local.js`（git管理外）にキーを書き、`python3 -m http.server 8000` で http://localhost:8000 を開きます。
```js
window.LOCAL_CONFIG = { GOOGLE_MAPS_API_KEY: "取得したキー" };
```

## データを直すとき
`index.html` の中にある次の部分を編集します。
- `SPOTS` … 店舗と座標。`approx:true` が付いた店は推定位置です
- `STAMPS` … 店舗ごとのスタンプ数
- `NOVELTY` … 事業者ごとのノベルティカードの配布条件
