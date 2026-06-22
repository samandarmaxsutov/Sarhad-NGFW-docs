==============================
NAT (Manzil almashtirish)
==============================

NAT (Network Address Translation — tarmoq manzilini almashtirish) ichki
tarmoqdagi xususiy IP manzillarni tashqi (ommaviy) IP manzilga aylantirish
imkonini beradi. Bu bo'limga o'tish uchun chap menyudagi **Network → NAT**
bo'limini tanlang (``/nat``).

NAT turlari
===========

Sarhad NGFW quyidagi NAT rejimlarini qo'llab-quvvatlaydi:

- **Source NAT (SNAT)** — ichki tarmoqdan internetga chiquvchi trafikning
  manba (source) manzilini WAN manziliga almashtiradi. Bu eng keng tarqalgan
  rejim: ichki foydalanuvchilar bitta ommaviy IP orqali internetga chiqadi.

- **Destination NAT (DNAT)** — tashqaridan kelgan trafikni ichki serverga
  yo'naltiradi (port forwarding). Masalan, WAN'ning 443-portiga kelgan trafik
  ichki veb-serverga uzatiladi.

- **Statik tasvirlash (Static mapping)** — bitta ichki IP manzilni bitta
  tashqi IP manzilga doimiy ravishda bog'laydi (1:1).

Interfeyslarni sozlash (inside / outside)
=========================================

NAT ishlashi uchun har bir interfeys "ichki" yoki "tashqi" deb belgilanishi
kerak:

- **Inside (ichki)** — LAN tomonidagi interfeyslar. Bu interfeyslardan
  kelgan trafik manzili almashtiriladi.
- **Outside (tashqi)** — WAN tomonidagi interfeys. Almashtirilgan trafik shu
  interfeys orqali chiqadi.

.. tip::

   Aksariyat hollarda zona (WAN/LAN) tayinlanganda tizim mos NAT
   interfeyslarini avtomatik sozlaydi. Qo'shimcha qoidalar qo'shilganda kerakli
   ichki interfeyslar avtomatik qo'shiladi.

Manzillar puli (Address pool)
=============================

SNAT uchun tashqi (ommaviy) IP manzillar puli belgilanadi. Trafik shu puldagi
manzillar orqali tashqariga chiqariladi. Pulga bitta yoki bir nechta IP manzil
diapazoni qo'shilishi mumkin.

DNAT (Port forwarding) qoidasi qo'shish
=======================================

Tashqaridan ichki serverga kirishni ochish uchun:

1. **DNAT qoidasi qo'shish (Add DNAT Rule)** tugmasini bosing.
2. Quyidagilarni kiriting:

   - **Tashqi manzil/port** — WAN IP va port (masalan, ``203.0.113.5:443``).
   - **Ichki manzil/port** — paket yo'naltiriladigan ichki server
     (masalan, ``192.168.10.20:443``).
   - **Protokol** — TCP yoki UDP.

3. **Saqlash (Save)** tugmasini bosing.

Faol sessiyalar (NAT Sessions)
==============================

**NAT Sessions** bo'limida ayni paytda faol bo'lgan barcha NAT ulanishlari
ko'rsatiladi: manba va manzil manzillari, portlar, protokol va sessiya
davomiyligi. Kerak bo'lganda alohida sessiyani yoki barcha sessiyalarni
tozalash (clear) mumkin.

Qo'shimcha sozlamalar
=====================

- **Vaqt chegaralari (Timeouts)** — TCP, UDP va boshqa protokollar uchun
  sessiyaning bo'sh turish vaqtini sozlash.
- **IPFIX jurnali** — NAT hodisalarini Netflow orqali tashqi yig'uvchiga
  (collector) yuborish (qarang: :doc:`/monitoring/flow`).

.. note::

   NAT qoidalari firewall qoidalari bilan birga ishlaydi. DNAT qoidasi
   trafikni ichki serverga yo'naltirsa-da, trafik o'tishi uchun firewall'da
   ham mos ruxsat qoidasi bo'lishi kerak (qarang: :doc:`/policies/acl`).
