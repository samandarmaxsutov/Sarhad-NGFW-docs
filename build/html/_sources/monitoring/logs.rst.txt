===================
Jurnallar (Logs)
===================

Sarhad NGFW tizimda sodir bo'layotgan barcha muhim hodisalarni — sozlama
o'zgarishlari, kirish urinishlari, xavfsizlik voqealari — batafsil yozib
boradi. Bu jurnallar tizim faoliyatini kuzatish, muammolarni aniqlash va
xavfsizlik tekshiruvlari uchun zarur. Bu bo'limga o'tish uchun chap menyudagi
**Monitoring → Logs** bo'limini tanlang (``/logs``).

Jurnal toifalari
================

Hodisalar quyidagi toifalarga ajratilgan:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Toifa
     - Tavsifi
   * - **Config**
     - Sozlamalardagi o'zgarishlar (firewall qoidalari, NAT, marshrutlar,
       interfeyslar va h.k.).
   * - **Auth**
     - Tizimga kirish va chiqish, parol o'zgarishlari, muvaffaqiyatsiz kirish
       urinishlari.
   * - **Admin**
     - Foydalanuvchilarni boshqarish amallari (yaratish, o'chirish, tahrirlash).
   * - **System**
     - Tizim hodisalari (qayta yuklash, xizmatlarning ishga tushishi/to'xtashi).
   * - **VPN**
     - VPN autentifikatsiyasi, sessiyalarning ochilishi va yopilishi.

Jurnal yozuvi tarkibi
=====================

Har bir yozuv quyidagi ma'lumotlarni o'z ichiga oladi:

- **Vaqt (Timestamp)** — hodisa qachon sodir bo'lgani.
- **Toifa va muhimlik** — info, ogohlantirish (warn) yoki xato (error).
- **Aktyor (Actor)** — amalni bajargan foydalanuvchi va uning IP manzili.
- **Hodisa va amal** — nima sodir bo'lgani.
- **Nishon (Target)** — hodisa qaysi obyektga taalluqli.
- **Natija (Status)** — muvaffaqiyatli (success) yoki muvaffaqiyatsiz (failure).

Jurnallarni filtrlash va eksport qilish
=======================================

- **Filtrlash** — toifa, sana oralig'i yoki kalit so'z bo'yicha yozuvlarni
  saralash.
- **Eksport** — jurnallarni tashqi faylga (CSV yoki JSON) yuklab olish.
  Bu hisobotlar tayyorlash yoki tashqi tahlil tizimlariga uzatish uchun
  foydali.

Saqlash muddati (Retention)
===========================

Jurnallar vaqt o'tishi bilan ko'p joy egallaydi. **Log Settings**
(``/logs/settings``) bo'limida saqlash siyosatini sozlashingiz mumkin:

- **Saqlash muddati** — yozuvlar necha kun saqlanishi (masalan, 90 kun).
  Bundan eski yozuvlar avtomatik o'chiriladi.
- **Qo'lda tozalash** — eski yozuvlarni darhol tozalash.

.. tip::

   Muvaffaqiyatsiz kirish urinishlari (Auth toifasidagi "failure" yozuvlari)
   ni muntazam tekshirib turing — ko'p sonli muvaffaqiyatsiz urinishlar
   parolni topishga (brute-force) urinish belgisi bo'lishi mumkin.

Bog'liq bo'limlar
=================

- Tarmoq trafigi statistikasi: :doc:`/monitoring/flow`
- Xavfsizlik ogohlantirishlari (IDS/IPS): :doc:`/security/ids`
