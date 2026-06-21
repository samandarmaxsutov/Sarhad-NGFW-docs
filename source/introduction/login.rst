==============
Tizimga kirish
==============

Bu bo'limda siz Sarhad NGFW mahsulotiga qanday kirish va foydalanuvchi rollari haqida ma'lumot olasiz.

Login sahifasi manzili:

    https://<ip>:8443/login

Masalan:

    https://192.168.1.1:8443/login

Default login ma'lumotlari:

- Username: admin
- Password: admin123

Foydalanuvchi rollari
---------------------

Sarhad NGFW tizimida uch xil foydalanuvchi toifasi mavjud:

- root
  - barcha huquqlarga ega.
  - tizimni to'liq boshqarish, konfiguratsiyani o'zgartirish, foydalanuvchilar yaratish va parollarni boshqarish mumkin.

- admin
  - tizim konfiguratsiyasini ko'rish va o'zgartirish huquqiga ega.
  - yangi foydalanuvchilar yaratish va mavjud foydalanuvchilarni boshqarish mumkin.
  - ammo ba'zi tizim darajasidagi funktsiyalar faqat root uchun bo'lishi mumkin.

- user
  - faqat ko'rish huquqiga ega.
  - tizim holatini, tarmoq statistikalarini va hisobotlarni ko'rishi mumkin.
  - konfiguratsiya yoki foydalanuvchi sozlamalarini o'zgartira olmaydi.

.. image:: ../_static/login_page.png
   :alt: Login Screen
   :align: center
   :width: 100%