#!/usr/bin/env python3
"""公式特設ページから画像をダウンロードする。

  python3 scripts/fetch_images.py          # 既にあるファイルはスキップ
  python3 scripts/fetch_images.py --force  # 上書きして取り直す

保存先
  images/brand/<事業者キー>.jpg   … 事業者ごとのキービジュアル（地図のピンに使われる）
  images/brand/thumb/<キー>.jpg   … ↑からキャラクターの顔のあたりを正方形に切り抜いたもの（ピン・一覧用）
  images/official/<元のファイル名> … メインビジュアル・詳細画像（参考用、地図では使わない）

切り抜きには macOS 標準の sips を使います（Mac以外では切り抜きだけスキップ）。
"""
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

PAGE = "https://www.mwt.co.jp/kokunai/chubu/special/lovelive2026/"
ROOT = Path(__file__).resolve().parent.parent
BRAND_DIR = ROOT / "images" / "brand"
OFFICIAL_DIR = ROOT / "images" / "official"
UA = "panelmap-image-fetcher/1.0"
WAIT = 1.0  # サーバーに負担をかけないよう、1枚ごとに待つ秒数

# 公式ページの画像名（img/img_<名前>.jpg）→ index.html の BRAND_IMG のキー
BRAND_KEYS = {
    "mwt": "mwt", "aokis": "aokis", "aoyagi": "aoyagi", "ebisenbe": "ebisato",
    "kiyome": "kiyome", "kohgen": "kohgen", "sobajima": "sobajima", "kagakukan": "kagakukan",
    "convention": "conv", "uya": "uya", "myokoen": "myokoen", "meitetsukyosho": "mekyopa",
    "meitetsu-souken": "nagomiya", "yabaton": "yabaton", "yamamotoya": "yamamotoya",
    "wakashachiya": "wakashachiya",
}
# サムネイルの切り抜き範囲（1000×563 のキービジュアル上で、左上 x, y と正方形の一辺）
THUMB_CROPS = {
    "mwt": (515, 20, 480), "aokis": (560, 60, 400), "aoyagi": (560, 40, 400), "ebisato": (580, 40, 380),
    "kiyome": (545, 60, 420), "kohgen": (560, 20, 420), "sobajima": (570, 40, 300), "kagakukan": (620, 40, 300),
    "conv": (620, 30, 300), "uya": (560, 20, 400), "myokoen": (500, 50, 420), "mekyopa": (610, 10, 300),
    "nagomiya": (620, 40, 320), "yabaton": (560, 40, 360), "yamamotoya": (535, 10, 440), "wakashachiya": (560, 40, 380),
}
THUMB_SIZE = 200
# 参考用に保存する画像（パス名の一部で判定）
OFFICIAL_PATTERNS = [r"img/main_visual\.jpg$", r"img/detail/img_[\w-]+\.jpg$"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), r.headers.get("Content-Type", "")


def save(url, dest, force):
    if dest.exists() and not force:
        print(f"  skip  {dest.relative_to(ROOT)}（既にあり）")
        return
    data, ctype = get(url)
    if not ctype.startswith("image/"):
        print(f"  NG    {url}（画像ではない: {ctype}）")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print(f"  saved {dest.relative_to(ROOT)}  {len(data)//1024}KB")
    time.sleep(WAIT)


def main():
    force = "--force" in sys.argv
    html, _ = get(PAGE)
    html = html.decode("utf-8", "replace")
    # src= と href= の両方から .jpg / .png を拾い、絶対URLにする
    urls = {urllib.parse.urljoin(PAGE, m) for m in re.findall(r'(?:src|href)="([^"]+\.(?:jpg|png))"', html)}

    print("事業者ごとのキービジュアル → images/brand/")
    found = set()
    for url in sorted(urls):
        m = re.search(r"/img/img_([\w-]+)\.jpg$", url)
        if m and m.group(1) in BRAND_KEYS:
            key = BRAND_KEYS[m.group(1)]
            found.add(key)
            save(url, BRAND_DIR / f"{key}.jpg", force)
    for key in sorted(set(BRAND_KEYS.values()) - found):
        print(f"  見つからず: {key}（ページの構成が変わった可能性）")

    print("参考画像 → images/official/")
    for url in sorted(urls):
        if any(re.search(p, url) for p in OFFICIAL_PATTERNS):
            save(url, OFFICIAL_DIR / Path(urllib.parse.urlparse(url).path).name, force)


def make_thumbs():
    if not shutil.which("sips"):
        print("sips が無いため、サムネイルの切り抜きはスキップしました")
        return
    print("サムネイル → images/brand/thumb/")
    out_dir = BRAND_DIR / "thumb"
    out_dir.mkdir(parents=True, exist_ok=True)
    for key, (x, y, size) in THUMB_CROPS.items():
        src, dest = BRAND_DIR / f"{key}.jpg", out_dir / f"{key}.jpg"
        if not src.exists():
            continue
        q = dict(stdout=subprocess.DEVNULL, check=True)
        subprocess.run(["sips", "-c", str(size), str(size), "--cropOffset", str(y), str(x), str(src), "--out", str(dest)], **q)
        subprocess.run(["sips", "-Z", str(THUMB_SIZE), str(dest)], **q)
        print(f"  made  {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
    make_thumbs()
