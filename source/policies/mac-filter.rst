==============================
MAC manzili bo'yicha filtrlash
==============================

MAC filtrlash qurilmaning fizik (MAC) manzili asosida uning tarmoqqa kirishiga
ruxsat berish yoki uni taqiqlash imkonini beradi. IP manzildan farqli ravishda,
bu nazorat usuli qurilmaning o'ziga (tarmoq adapteriga) bog'langan. Ushbu
bo'limga o'tish uchun chap menyudan **Firewall → MAC Filter** bo'limini tanlang
(``/mac-filter``).

.. image:: ../_static/mac_filter.png
   :alt: MAC Filter siyosatlari sahifasi
   :align: center
   :width: 100%

Qachon ishlatiladi
==================

MAC filtrlash quyidagi holatlarda foydali bo'ladi:

- Faqat ma'lum (ro'yxatga olingan) qurilmalarga tarmoqqa ulanishga ruxsat
  berish.
- Aniq bir qurilmani (masalan, ruxsatsiz noutbukni) tarmoqdan bloklash.
- **Anti-spoofing** — ma'lum bir MAC manzilni faqat ma'lum IP manzil bilan
  ishlashga majburlash (IP yoki MAC'ni soxtalashtirishning oldini olish).

MAC siyosati qanday tuzilgan
============================

MAC filtrlash **siyosatlar (policies)** asosida ishlaydi. Har bir siyosat:

- nomga ega bo'ladi;
- bir yoki bir nechta **interfeysga** (kiruvchi — input yo'nalishda)
  qo'llaniladi;
- ichida bir yoki bir nechta **qoida (rule)** saqlaydi.

**MAC Filter Policies** jadvalida har bir siyosatning ID raqami, nomi,
qoidalari soni va qo'llanilgan interfeyslari ko'rsatiladi.

MAC siyosatini yaratish
=======================

1. **Create Policy** tugmasini bosing.
2. **Policy Name** maydoniga siyosat nomini kiriting
   (masalan, ``anti-spoof-lan``).
3. **Apply to interfaces (input direction)** bo'limida siyosat qo'llaniladigan
   interfeyslarni tanlab, **Add** tugmasi bilan qo'shing.
4. **Rules** bo'limida **Add Rule** tugmasi orqali bir yoki bir nechta qoida
   qo'shing (quyida).
5. **Save** tugmasini bosing.

.. image:: ../_static/add_mac_policy.png
   :alt: MAC siyosatini yaratish oynasi
   :align: center
   :width: 100%

Qoida (Rule) maydonlari
-----------------------

Har bir qoida quyidagi maydonlardan iborat:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Maydon
     - Tavsifi
   * - **Action**
     - ``PERMIT`` (ruxsat) yoki ``DENY`` (taqiq).
   * - **Source MAC**
     - Qurilmaning fizik manzili (masalan, ``00:11:22:33:44:55``).
   * - **MAC Mask**
     - MAC manzilning qaysi qismi solishtirilishini belgilovchi niqob
       (bir guruh MAC'ni qamrab olish uchun ishlatiladi).
   * - **IP Prefix**
     - Shu MAC bog'lanadigan IP tarmoq (masalan, ``10.0.0.0/8``) yoki ``any``.
       Anti-spoofing uchun MAC va IP shu yerda o'zaro bog'lanadi.

Ishlash tartibi
===============

Bir siyosat ichidagi qoidalar yuqoridan pastga tekshiriladi va trafik birinchi
mos kelgan qoidaga bo'ysunadi. Ikkita asosiy strategiya mavjud:

- **Oq ro'yxat (whitelist)** — ruxsat etilgan MAC'larga ``PERMIT`` qoidalari
  beriladi, qolganlari esa bloklanadi. Bu eng xavfsiz usul, biroq har bir yangi
  qurilmani qo'lda qo'shish talab etiladi.
- **Qora ro'yxat (blacklist)** — faqat ayrim qurilmalarga ``DENY`` qoidasi
  beriladi, qolganlariga ruxsat etiladi.

.. note::

   Ba'zi qurilmalarda MAC manzilini almashtirish (spoofing) mumkin, shuning
   uchun MAC filtrlashni yagona himoya chorasi sifatida emas, balki qo'shimcha
   xavfsizlik qatlami sifatida ishlatish tavsiya etiladi. Anti-spoofing uchun
   MAC bilan birga **IP Prefix** ni ham belgilang.
