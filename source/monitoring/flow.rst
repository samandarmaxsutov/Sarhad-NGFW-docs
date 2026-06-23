==========================================
Trafik monitoringi (Flow / IPFIX)
==========================================

Flow monitoringi tarmoqdan o'tayotgan trafik haqida statistik ma'lumotlarni
(oqimlarni) yig'adi va ularni tashqi tahlil tizimiga yuboradi. Bu orqali
tarmoqdan kim, qayerga va qancha ma'lumot uzatayotganini ko'rish mumkin. Bu
bo'limga o'tish uchun chap menyudan **Firewall → Flow Monitoring** bo'limini
tanlang (``/flow-monitoring``).

.. image:: ../_static/flow_monitoring.png
   :alt: Flow Monitoring sahifasi
   :align: center
   :width: 100%

Asosiy tushunchalar
===================

- **Flow (oqim)** — bir xil belgilarga ega (manba/manzil IP, port, protokol)
  paketlar ketma-ketligi. Masalan, bitta kompyuterning bitta saytga ulanishi —
  bu bitta oqim.
- **Flowprobe** — qurilma ichidagi oqimlarni yig'uvchi modul.
- **IPFIX** — yig'ilgan oqim ma'lumotlarini standart formatda tashqi
  yig'uvchiga (collector) uzatish protokoli.
- **Collector** — oqim ma'lumotlarini qabul qilib saqlaydigan va tahlil
  qiladigan tashqi server.

Sahifa ikki qismdan iborat: oqimlarni qayerga yuborishni belgilaydigan
**IPFIX exporter** va oqim yig'ishni yoqadigan **Flowprobe**.

1-qadam: IPFIX exporter sozlash
===============================

**IPFIX exporter** bo'limida oqim ma'lumotlari yuboriladigan manzilni belgilang:

- **Collector IP** — tashqi yig'uvchi server IP manzili (masalan,
  ``192.168.1.50``).
- **Port** — yig'uvchi server porti (IPFIX uchun odatda ``4739``).
- **Source IP** — oqimlar yuboriladigan manba manzili (masalan, qurilma
  interfeysining IP manzili).

So'ngra **Save** tugmasini bosing.

2-qadam: Flowprobe'ni yoqish
============================

**Flowprobe** bo'limidagi **Enable Flowprobe** tugmachasini yoqing. Yonidagi
ko'rsatkich holatni bildiradi: **On** (yoqilgan) yoki **Off** (o'chiq).

Flowprobe yoqilgach, tizim oqimlarni yig'a boshlaydi va yuqorida ko'rsatilgan
collector'ga IPFIX orqali yuboradi.

Nimaga foydali
==============

- **Tarmoqdan foydalanishni tahlil qilish** — qaysi qurilmalar va ilovalar eng
  ko'p trafik hosil qilayotganini aniqlash.
- **Anomaliyalarni aniqlash** — odatdagidan ko'p trafik xavfsizlik hodisasi
  (masalan, ma'lumot sizib chiqishi) belgisi bo'lishi mumkin.
- **Sig'imni rejalashtirish** — tarmoq kanalini kengaytirish zarurligini
  baholash.

.. note::

   Flow monitoringi trafik *mazmunini* emas, balki uning *metama'lumotlarini*
   (kim, qayerga, qancha) yig'adi. Trafik mazmunini tekshirish uchun
   :doc:`/security/ids` (IDS/IPS) yoki :doc:`/security/tls-interception`
   funksiyalaridan foydalaning.
