#!/bin/sh
# Cloudflare Pages に直接アップロードする。
#   sh scripts/deploy.sh
# 初回だけ先に `npx wrangler login` でログインしておく。
# APIキーは config.local.js から読み、アップロード用のコピー（dist/）にだけ書き込む。
set -eu
cd "$(dirname "$0")/.."

PROJECT=panelmap
KEY=$(sed -n 's/.*GOOGLE_MAPS_API_KEY: *"\([^"]*\)".*/\1/p' config.local.js)
[ -n "$KEY" ] || { echo "config.local.js にキーがありません"; exit 1; }

rm -rf dist && mkdir -p dist/images
sed "s/__GOOGLE_MAPS_API_KEY__/$KEY/g" index.html > dist/index.html
cp -R images/brand dist/images/brand   # images/official は地図で使わないので上げない
# config.local.js は上げない（本番は index.html に書き込んだキーを使う）
printf 'window.LOCAL_CONFIG = null;\n' > dist/config.local.js

npx wrangler pages deploy dist --project-name "$PROJECT" --branch main
