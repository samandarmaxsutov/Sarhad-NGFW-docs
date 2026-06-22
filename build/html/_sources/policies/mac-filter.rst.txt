==============================
MAC manzili bo'yicha filtrlash
==============================

MAC filtrlash qurilmaning fizik (MAC) manzili asosida tarmoqqa kirishini
ruxsat berish yoki taqiqlash imkonini beradi. Bu IP manzildan farqli ravishda
qurilmaning o'ziga (tarmoq adapteriga) bog'langan nazorat usulidir. Bu bo'limga
o'tish uchun chap menyudagi **Firewall → MAC Filter** bo'limini tanlang
(``/mac-filter``).

Qachon ishlatiladi
==================

MAC filtrlash quyidagi holatlarda foydali:

- Faqat ma'lum (ro'yxatga olingan) qurilmalarga tarmoqqa ulanishga ruxsat
  berish.
- Aniq bir qurilmani (masalan, ruxsatsiz noutbukni) tarmoqdan bloklash.
- IP manzilini o'zgartirib aylanib o'tishga urinadigan qurilmalarni nazorat
  qilish.

MAC qoidasi qo'shish
====================

1. **Qoida qo'shish (Add Rule)** tugmasini bosing.
2. Quyidagilarni kiriting:

   - **MAC manzil** — qurilmaning fizik manzili
     (masalan, ``00:1A:2B:3C:4D:5E``).
   - **Amal (Action)** — ``Permit`` (ruxsat) yoki ``Deny`` (taqiq).
   - **Interfeys** — qoida qaysi interfeysda amal qilishi.

3. **Saqlash (Save)** tugmasini bosing.

Ishlash tartibi
===============

MAC qoidalari ham firewall qoidalari kabi yuqoridan pastga tekshiriladi.
Ikki asosiy strategiya mavjud:

- **Oq ro'yxat (whitelist)** — ruxsat etilgan MAC'larni sanab, qolganlarini
  bloklash. Eng xavfsiz, lekin har bir yangi qurilmani qo'lda qo'shish kerak.
- **Qora ro'yxat (blacklist)** — faqat aniq qurilmalarni bloklab, qolganlariga
  ruxsat berish.

.. note::

   MAC manzilini ba'zi qurilmalarda almashtirish (spoofing) mumkin, shuning
   uchun MAC filtrlashni yagona himoya chorasi sifatida emas, balki qo'shimcha
   xavfsizlik qatlami sifatida ishlatish tavsiya etiladi.
