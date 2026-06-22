==========================================
Trafik monitoringi (Flow / IPFIX)
==========================================

Flow monitoringi tarmoqdan o'tayotgan trafik haqida batafsil statistik
ma'lumotlarni (oqimlarni) yig'adi va ularni tashqi tahlil tizimiga yuborishi
mumkin. Bu tarmoqdan kim, qayerga va qancha ma'lumot uzatayotganini ko'rish
imkonini beradi. Bu bo'limga o'tish uchun chap menyudagi
**Monitoring → Flow Monitoring** bo'limini tanlang (``/flow-monitoring``).

Asosiy tushunchalar
===================

- **Flow (oqim)** — bir xil belgilarga ega (manba/manzil IP, port, protokol)
  paketlar ketma-ketligi. Masalan, bitta kompyuterning bitta saytga ulanishi —
  bu bitta oqim.
- **IPFIX / NetFlow** — oqimlar haqidagi ma'lumotni standart formatda tashqi
  yig'uvchiga (collector) uzatish protokoli.
- **Collector** — oqim ma'lumotlarini qabul qilib, saqlaydigan va tahlil
  qiladigan tashqi server.

Flow eksportini sozlash
=======================

1. **Flow Monitoring** sahifasiga o'ting.
2. Quyidagilarni sozlang:

   - **Interfeyslar** — qaysi interfeyslar trafigi kuzatilishi.
   - **Collector manzili** — oqim ma'lumotlari yuboriladigan tashqi server
     IP manzili va porti (masalan, ``192.168.1.50:4739``).
   - **Vaqt chegaralari (Timeouts)** — faol va passiv oqimlar uchun eksport
     oralig'i.

3. **Saqlash** tugmasini bosing.

Nimaga foydali
==============

- **Tarmoqdan foydalanishni tahlil qilish** — qaysi qurilmalar va ilovalar
  eng ko'p trafik hosil qilayotganini aniqlash.
- **Anomaliyalarni aniqlash** — odatdagidan ko'p trafik xavfsizlik hodisasi
  (masalan, ma'lumot sizib chiqishi yoki DDoS) belgisi bo'lishi mumkin.
- **Sig'imni rejalashtirish** — tarmoq kanalini kengaytirish zarurligini
  baholash.

.. note::

   Flow monitoringi trafik *mazmunini* emas, balki uning *metama'lumotlarini*
   (kim, qayerga, qancha) yig'adi. Trafik mazmunini tekshirish uchun
   :doc:`/security/ids` (IDS/IPS) yoki :doc:`/security/tls-interception`
   funksiyalaridan foydalaning.
