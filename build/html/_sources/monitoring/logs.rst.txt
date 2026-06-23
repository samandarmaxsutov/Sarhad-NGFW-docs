===================
Jurnallar (Logs)
===================

Sarhad NGFW tizimda sodir bo'layotgan barcha muhim hodisalarni batafsil yozib
boradi. Jurnallar tizim faoliyatini kuzatish, muammolarni aniqlash va
xavfsizlik tekshiruvlari uchun zarur. Bu bo'limga o'tish uchun chap menyudan
**Logs** guruhini oching (``/logs``).

Jurnallar turlar bo'yicha ajratilgan — har bir turi chap menyudagi alohida
bo'lim orqali ochiladi va o'ziga xos ustunlarga ega.

Firewall Logs
=============

Firewall qoidalari tomonidan bloklangan (drop) yoki ruxsat etilgan trafik
hodisalari.

.. image:: ../_static/firewall_logs.png
   :alt: Firewall jurnallari
   :align: center
   :width: 100%

Ustunlar: **Time** (vaqt), **Action** (amal — permit/deny), **Protocol**,
**Source** (manba), **Destination** (manzil), **Packets** (paketlar soni),
**Details** (tafsilotlar).

URL Logs
========

TLS tekshiruvi (:doc:`/security/tls-interception`) yoqilgan interfeyslarda
ko'rilgan veb-manzillar jurnali.

.. image:: ../_static/url_logs.png
   :alt: URL jurnallari
   :align: center
   :width: 100%

Ustunlar: **Time**, **Interface**, **Method** (GET/POST), **Client IP** (mijoz
IP), **Host** (sayt), **URL Path** (manzil yo'li), **Status** (HTTP holati).

Config Logs
===========

Konfiguratsiyadagi o'zgarishlar (firewall, NAT, marshrut, interfeys va h.k.).

.. image:: ../_static/config_logs.png
   :alt: Konfiguratsiya jurnallari
   :align: center
   :width: 100%

Ustunlar: **Time**, **User** (foydalanuvchi), **IP**, **Action** (amal),
**Target** (nishon — qaysi obyekt o'zgartirildi), **Details**.

Auth Logs
=========

Tizimga kirish va chiqish hamda parol o'zgarishlari.

.. image:: ../_static/auth_logs.png
   :alt: Kirish jurnallari
   :align: center
   :width: 100%

Ustunlar: **Time**, **User**, **IP**, **Action** (login/logout), **Status**
(muvaffaqiyatli yoki muvaffaqiyatsiz).

VPN Logs
========

VPN autentifikatsiyasi hamda sessiyalarning ochilishi va yopilishi.

.. image:: ../_static/vpn_logs.png
   :alt: VPN jurnallari
   :align: center
   :width: 100%

IDS/IPS Logs
============

Hujumlarni aniqlash tizimi (:doc:`/security/ids`) yaratgan ogohlantirishlar.

.. image:: ../_static/ids_ips_logs.png
   :alt: IDS/IPS jurnallari
   :align: center
   :width: 100%

Ustunlar: **Time**, **Priority** (muhimlik darajasi), **Action**, **Message**
(tavsif), **Source**, **Destination**.

Filtrlash, qidirish va yuklab olish
===================================

Barcha jurnal turlarida quyidagi vositalar mavjud:

- **Qidiruv** — kalit so'z bo'yicha yozuvlarni izlash.
- **Sana oralig'i** — boshlanish va tugash sanasini tanlab, ma'lum davr
  yozuvlarini ko'rish.
- **Protokol filtri** — Firewall jurnallarini protokol bo'yicha saralash.
- **Tafsilotlar** — yozuvning to'liq tafsilotini ko'rish uchun qatorni ikki
  marta bosing (yoki **View** tugmasini bosing).
- **Download** — joriy jurnalni tashqi faylga yuklab olish (hisobot yoki tashqi
  tahlil uchun).

Log settings (saqlash muddati)
==============================

Jurnallar vaqt o'tishi bilan ko'p joy egallaydi. **Log settings**
(``/logs/settings``) bo'limida avtomatik tozalash siyosatini sozlash mumkin.

.. image:: ../_static/log_settings.png
   :alt: Jurnal sozlamalari
   :align: center
   :width: 100%

- **Keep all logs for … days** — yozuvlar necha kun saqlanishi. Bundan eski
  yozuvlar avtomatik o'chiriladi.
- **Maximum disk for IDS/IPS … GiB** — IDS/IPS jurnallari uchun ajratilgan
  maksimal disk hajmi.
- **Emergency cleanup at … % disk used** — disk shu foizga to'lganda favqulodda
  tozalashni ishga tushirish.
- **Run cleanup now** — eski yozuvlarni darhol qo'lda tozalash.
- **Save** — sozlamalarni saqlash; **Restore defaults** — standart qiymatlarga
  qaytarish.

Sahifa pastida oxirgi tozalash (**Last cleanup pass**) qachon o'tkazilgani
ko'rsatiladi.

.. tip::

   Muvaffaqiyatsiz kirish urinishlari (Auth jurnalidagi "failure" yozuvlari)
   ni muntazam tekshirib turing — ko'p sonli muvaffaqiyatsiz urinishlar parolni
   topishga (brute-force) urinish belgisi bo'lishi mumkin.

Bog'liq bo'limlar
=================

- Tarmoq trafigi statistikasi: :doc:`/monitoring/flow`
- Xavfsizlik ogohlantirishlari (IDS/IPS): :doc:`/security/ids`
