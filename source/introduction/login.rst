==============
Tizimga kirish
==============

Sarhad NGFW boshqaruvi veb-brauzer orqali amalga oshiriladi. Kirish sahifasi
manzili:

.. code-block:: text

   https://<ip>:8443/login

Masalan: ``https://192.168.1.1:8443/login``

Tizimda standart (bootstrap) holatda ikkita hisob yaratiladi. Ikkalasining
ham boshlang'ich paroli bir xil:

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Foydalanuvchi nomi
     - Parol
     - Rol
   * - ``root``
     - ``admin123``
     - root (to'liq huquq)
   * - ``admin``
     - ``admin123``
     - admin (boshqaruv)

``readonly`` rolidagi hisoblar standart holda yaratilmaydi — ularni root yoki
admin qo'lda qo'shadi (qarang: :doc:`/system/users`).

.. warning::

   Birinchi kirishdan so'ng **ikkala** hisobning (``root`` va ``admin``)
   standart parolini darhol o'zgartiring — aks holda tizim jiddiy xavf
   ostida qoladi.

Foydalanuvchi rollari
---------------------

Tizimda uchta rol mavjud:

**root**
   Barcha huquqlarga ega: tizimni to'liq boshqarish, konfiguratsiyani
   o'zgartirish, foydalanuvchilar va litsenziyani boshqarish.

**admin**
   Konfiguratsiyani ko'rish va o'zgartirish hamda foydalanuvchilarni boshqarish
   huquqiga ega. Ayrim tizim darajasidagi amallar faqat root uchun.

**readonly**
   Faqat ko'rish huquqi: tizim holati, statistika va hisobotlarni ko'radi,
   lekin sozlamalarni o'zgartira olmaydi.

.. image:: ../_static/login_page.png
   :alt: Kirish sahifasi
   :align: center
   :width: 100%
