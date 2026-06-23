=============================
Foydalanuvchilarni boshqarish
=============================

Bu sahifa boshqaruv paneliga kirish huquqiga ega foydalanuvchi hisoblarini
boshqaradi. Bu bo'limga o'tish uchun chap menyudan **System → Firewall Users**
bo'limini tanlang (``/user-mgmt``).

.. image:: ../_static/users.png
   :alt: Foydalanuvchilarni boshqarish sahifasi
   :align: center
   :width: 100%

Rollar va ruxsatlar
===================

Tizimda uchta rol mavjud. Har bir rol turli ruxsat va ko'rish darajasiga ega:

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - Rol
     - Ruxsatlari
     - Ko'rish darajasi
   * - **Root**
     - Foydalanuvchilarni to'liq boshqarish (Full user-management access):
       hisob yaratish, tahrirlash, o'chirish, har qanday nom va parolni
       o'zgartirish.
     - Barcha hisoblarni ko'radi.
   * - **Admin**
     - Faqat firewall konfiguratsiyasiga kirish (Firewall configuration access
       only). Faqat ``read-only`` hisoblar yarata oladi.
     - Faqat ``read-only`` hisoblarni ko'radi.
   * - **Read-only**
     - Faqat ko'rish (View-only access): holat va sozlamalarni ko'radi, lekin
       o'zgartira olmaydi.
     - Foydalanuvchilar ro'yxatini umuman ko'ra olmaydi.

Rol qoidalari
-------------

- Tizimda **faqat bitta root** foydalanuvchi mavjud va u tizimning standart
  egasi.
- **Root** o'z va boshqa foydalanuvchilarning nomlari va parollarini
  o'zgartira oladi.
- Boshqa **adminlar** foydalanuvchi boshqaruvida nom va parollarni o'zgartira
  olmaydi.
- **Read-only** foydalanuvchilar tizimdagi hech qanday foydalanuvchini ko'ra
  olmaydi.

Hisoblar jadvali
================

**Accounts** jadvalida ko'rinadigan foydalanuvchilar ro'yxati keltiriladi:
**Username** (nom), **Role** (rol), **Permissions** (ruxsatlar), **Updated**
(oxirgi o'zgarish) va **Actions** (amallar). Joriy sessiya alohida belgilanadi.

Yangi foydalanuvchi qo'shish
============================

1. **Add User** tugmasini bosing.
2. **Create User** oynasida quyidagilarni kiriting:

   - **Role** — ``Admin`` yoki ``Read-only`` (root tomonidan yaratiladi;
     admin faqat ``Read-only`` qo'sha oladi).
   - **Username** — kirish nomi.
   - **Password** — parol.

3. **Create** tugmasini bosing.

.. image:: ../_static/add_user.png
   :alt: Yangi foydalanuvchi qo'shish oynasi
   :align: center
   :width: 100%

Foydalanuvchini tahrirlash
==========================

Hisob yonidagi tahrirlash tugmasi orqali **Edit User** oynasi ochiladi. U yerda
**Role** va **Username** ni o'zgartirish hamda **New Password** kiritish mumkin.
Parol maydonini bo'sh qoldirsangiz, joriy parol o'zgarmaydi.

Root parolini o'zgartirish
==========================

Root o'z parolini **Change Root Password** tugmasi orqali o'zgartiradi.

Support (vaqtinchalik SSH)
==========================

Texnik yordam zarur bo'lganda, root foydalanuvchi vaqtinchalik SSH kirishni
yoqishi mumkin. Bu **Support** paneli orqali amalga oshiriladi (faqat root
uchun) va xavfsizlik yuzasidan **4 soatdan keyin avtomatik o'chadi**
(**Enable SSH (4h)**). Yordam tugagach, uni **qo'lda ham o'chirib qo'yish**
tavsiya etiladi.

.. warning::

   So'nggi **root** hisobini o'chirib qo'ymang — aks holda tizimni boshqarish
   imkoniyatini butunlay yo'qotasiz.

Xavfsizlik tavsiyalari
======================

- Standart parolni birinchi kirishdayoq o'zgartiring.
- Kuchli parollardan foydalaning: kamida 12 ta belgi, katta-kichik harflar,
  raqamlar va maxsus belgilar aralashmasi.
- Har bir xodimga alohida hisob bering — umumiy hisoblardan foydalanmang.
- Faqat zarur huquqlarni bering: ko'rish kifoya qilsa, ``Read-only`` rolini
  tanlang.
- Kirish/chiqish faoliyati :doc:`/monitoring/logs` bo'limida qayd etiladi —
  uni muntazam tekshirib turing.

.. note::

   Sessiyalar xavfsizlik uchun ma'lum vaqtdan keyin avtomatik tugaydi.
   Faolsizlikdan so'ng tizim qayta kirishni so'rashi mumkin.
