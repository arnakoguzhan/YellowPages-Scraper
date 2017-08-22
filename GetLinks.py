import YPClass

# 32 kategori dizisi
categories = ["restoranlar", "turk-mutfagi", "dunya-mutfagi", "balik-lokantalari", "kebapcilar", "evlere-yemek-servisi",
              "akdeniz-mutfagi", "italyan-mutfagi", "kafeler", "uzakdogu-mutfagi", "meyhaneler",
              "fast-food", "diger-mutfaklar", "brunch", "pizza", "otel-ve-restoran-yonetimi",
              "pilic-cevirme-ve-tavuk-restoranlari", "fransiz-mutfagi", "firinlar-ve-pastaneler",
              "meksika-mutfagi", "yunan-mutfagi", "otel-ve-restoran-ekipmanlari",
              "hazir-yemek-firmalari-ve-catering-hizmetleri", "vejetaryen-mutfagi", "biftek-restoranlari",
              "gurme-dukkanlari-ve-sarkuteriler", "nargile-kafeler", "tatlicilar", "icki-magazalari",
              "organik-yiyecekler-ve-urunler", "ispanyol-mutfagi", "balikcilar"]

# 79 il olacak
iller = ["istanbul", "ankara", "izmir"]

URL = "https://yellowpages.com.tr/"

j = 0

while j < 3:

    for i in categories:
        url = URL + i + "-" + iller[j] + "-c?page="
        YPClass.getLinks(url)
    j += 1
