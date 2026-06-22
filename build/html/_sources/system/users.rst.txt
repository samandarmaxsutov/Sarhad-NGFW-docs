=============================
Foydalanuvchilarni boshqarish
=============================

Bu bo'limda veb-panelga kirish huquqiga ega foydalanuvchi hisoblarini
yaratish, tahrirlash va o'chirish bo'yicha qo'llanma keltirilgan. Bu bo'limga
o'tish uchun chap menyudagi **System → User Management** bo'limini tanlang
(``/user-mgmt``).

Foydalanuvchi rollari
=====================

Sarhad NGFW da uchta rol mavjud bo'lib, har biri turli huquqlarni beradi:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Rol
     - Huquqlar
   * - **root**
     - Eng yuqori huquq. Barcha sozlamalarni o'zgartirish, foydalanuvchilarni
       boshqarish, litsenziyani boshqarish va tizim darajasidagi amallarni
       bajarish mumkin.
   * - **admin**
     - Konfiguratsiyani ko'rish va o'zgartirish, foydalanuvchilar yaratish va
       boshqarish mumkin. Ba'zi tizim darajasidagi amallar faqat root uchun.
   * - **readonly (user)**
     - Faqat ko'rish huquqi. Tizim holati, statistika va hisobotlarni ko'rish
       mumkin, lekin hech narsani o'zgartira olmaydi.

Yangi foydalanuvchi qo'shish
============================

1. **Foydalanuvchi qo'shish (Add User)** tugmasini bosing.
2. Quyidagilarni kiriting:

   - **Foydalanuvchi nomi (Username)** — kirish uchun noyob nom.
   - **Parol (Password)** — kuchli parol tanlang (qarang quyidagi tavsiyalar).
   - **Rol (Role)** — root, admin yoki readonly.

3. **Saqlash** tugmasini bosing.

Parolni o'zgartirish
====================

O'z parolingizni o'zgartirish uchun:

1. **Parolni o'zgartirish (Change Password)** bo'limini oching.
2. Joriy parolni va yangi parolni ikki marta kiriting.
3. **Saqlash** tugmasini bosing.

Administrator boshqa foydalanuvchining parolini ham o'zgartirishi mumkin.

Foydalanuvchini tahrirlash va o'chirish
=======================================

- **Tahrirlash (Edit)** — foydalanuvchi rolini yoki sozlamalarini o'zgartirish.
- **O'chirish (Delete)** — foydalanuvchi hisobini o'chirish.

.. warning::

   So'nggi **root** yoki **admin** hisobini o'chirib qo'ymang — aks holda
   tizimni boshqarish imkoniyatini yo'qotasiz.

Xavfsizlik tavsiyalari
======================

- Standart ``admin`` parolini birinchi kirishdayoq o'zgartiring.
- Kuchli parollardan foydalaning: kamida 12 ta belgi, katta-kichik harflar,
  raqamlar va maxsus belgilar aralashmasi.
- Har bir xodimga alohida hisob bering — umumiy hisoblardan foydalanmang.
- Faqat zarur huquqlarni bering: ko'rish kifoya bo'lsa, ``readonly`` rolini
  tanlang.
- Foydalanuvchilarning kirish/chiqish faoliyati :doc:`/monitoring/logs`
  bo'limida qayd etiladi — uni muntazam tekshirib turing.

.. note::

   Sessiyalar xavfsizlik uchun ma'lum vaqtdan keyin avtomatik tugaydi.
   Faolsizlikdan so'ng tizim sizdan qayta kirishni so'rashi mumkin.
