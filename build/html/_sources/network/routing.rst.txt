======================
Marshrutlash (Routing)
======================

Marshrutlash bo'limi tarmoq paketlari qaysi yo'nalish (interfeys yoki
keyingi tugun — next-hop) orqali yuborilishini belgilaydi. Bu bo'limga
o'tish uchun chap menyudagi **Network → Routes** bo'limini tanlang
(``/routes``).

.. image:: ../_static/routing.png
   :alt: Marshrutlash jadvali
   :align: center
   :width: 100%

Marshrutlash jadvali
====================

Sahifaning asosiy qismida joriy marshrutlash jadvali (FIB) ko'rsatiladi.
Har bir yozuv quyidagi ustunlardan iborat:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Ustun
     - Tavsifi
   * - **Manzil tarmog'i (Destination)**
     - Marshrut qaysi tarmoqqa tegishli ekani, CIDR ko'rinishida
       (masalan, ``10.20.0.0/16``). ``0.0.0.0/0`` — standart marshrut
       (default route), ya'ni boshqa hech bir marshrutga to'g'ri kelmaydigan
       trafik.
   * - **Keyingi tugun (Next-hop)**
     - Paket yuboriladigan keyingi gateway IP manzili
       (masalan, ``192.168.1.254``).
   * - **Chiquvchi interfeys (Interface)**
     - Paket qaysi interfeys orqali chiqib ketishi.
   * - **Manba (Protocol)**
     - Marshrut qanday paydo bo'lgani: statik (qo'lda kiritilgan) yoki ulangan
       (connected — interfeys IP manzilidan kelib chiqqan).

Statik marshrut qo'shish
========================

Yangi marshrut qo'shish uchun **Marshrut qo'shish (Add Route)** tugmasini
bosing va quyidagi maydonlarni to'ldiring:

- **Manzil tarmog'i** — yo'naltirilishi kerak bo'lgan tarmoq, CIDR ko'rinishida
  (masalan, ``172.16.0.0/24``).
- **Keyingi tugun (Next-hop)** — paket yuboriladigan gateway IP manzili.
- **Interfeys** — (ixtiyoriy) paket chiqishi kerak bo'lgan aniq interfeys.

So'ngra **Saqlash (Save)** tugmasini bosing. Marshrut darhol kuchga kiradi
va jadvalda paydo bo'ladi.

Standart marshrut (Default Gateway)
-----------------------------------

Internetga chiqish uchun odatda standart marshrut sozlanadi:

- **Manzil tarmog'i:** ``0.0.0.0/0``
- **Keyingi tugun:** internet-provayder gateway manzili (yoki WAN interfeys
  gateway).

Agar WAN interfeysi DHCP orqali manzil olsa, standart marshrut ko'pincha
avtomatik tarzda qo'shiladi.

Marshrutni o'chirish
====================

Marshrutni jadvaldan o'chirish uchun kerakli yozuv yonidagi **O'chirish
(Delete)** tugmasini bosing. Ulangan (connected) marshrutlarni qo'lda
o'chirib bo'lmaydi — ular interfeys IP manzili o'zgarganda yoki o'chirilganda
avtomatik yangilanib turadi.

.. note::

   Marshrutlash faqat paketning yo'nalishini belgilaydi. Trafikning ruxsat
   etilishi yoki bloklanishi esa firewall qoidalari (ACL) orqali nazorat
   qilinadi. To'liq ishlashi uchun marshrut va firewall qoidalari birga
   sozlanishi kerak.
