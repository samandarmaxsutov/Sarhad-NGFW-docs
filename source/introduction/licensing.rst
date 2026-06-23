============================
Litsenziya va faollashtirish
============================

Sarhad NGFW litsenziyalangan mahsulot bo'lib, boshqaruv interfeysidan
foydalanish uchun amaldagi litsenziya talab qilinadi. Litsenziya har bir
qurilmaga alohida bog'lanadi va internetsiz (offline) tekshiriladi.

.. image:: ../_static/licenses.png
   :alt: Litsenziyani faollashtirish sahifasi
   :align: center
   :width: 100%

Qanday ishlaydi
===============

- Har bir qurilma o'zining noyob **Machine ID** (qurilma identifikatori) sini
  hisoblaydi. U asbob-uskuna (anakart, tizim) ma'lumotlaridan kelib chiqadi va
  ``XXXX-XXXX-XXXX-XXXX`` ko'rinishida ko'rsatiladi.
- Litsenziya aynan shu Machine ID ga bog'lab beriladi va boshqa qurilmada
  ishlamaydi.
- Tizim litsenziyani to'liq oflayn tekshiradi — hech qanday litsenziya
  serveriga ulanish shart emas.
- Litsenziya amal qilmagunicha, boshqaruv paneli faqat **faollashtirish
  sahifasini** (``/license``) ko'rsatadi; qolgan barcha bo'limlar yopiq bo'ladi.

Litsenziyani faollashtirish
===========================

Litsenziyani faollashtirish **tizimga kirishdan oldin** bajariladi. Qurilma
litsenziyalanmaguncha, kirish (login) sahifasi ham ochilmaydi — brauzer
har qanday manzilda faqat ``/license`` faollashtirish sahifasini ko'rsatadi.

1. Brauzerda boshqaruv manzilini oching — litsenziya o'rnatilmagan bo'lsa,
   avtomatik ravishda ``/license`` sahifasi ochiladi.
2. Sahifada ko'rsatilgan **Machine ID** ni nusxalang.
3. Bu Machine ID ni mahsulot yetkazib beruvchiga (vendor) yuboring.
4. Yetkazib beruvchi sizning qurilmangiz uchun litsenziya kalitini (token)
   yaratib beradi.
5. Olingan litsenziya kalitini sahifadagi maydonga joylang va
   **Faollashtirish (Activate)** tugmasini bosing.

Litsenziya to'g'ri bo'lsa, tizim ochiladi va endi siz **tizimga kirishingiz**
(login) hamda barcha bo'limlardan foydalanishingiz mumkin
(qarang: :doc:`/introduction/login`).

Litsenziya muddati
==================

Litsenziya ikki turda bo'lishi mumkin:

- **Muddatli (time-boxed)** — belgilangan kunlardan keyin amal qilishi tugaydi.
  Muddat tugashidan oldin yangi litsenziya bilan uzaytirish kerak.
- **Doimiy (perpetual)** — muddati cheklanmagan.

Litsenziya holatini (amal qilish muddati, xususiyatlar) ``/license`` sahifasida
ko'rishingiz mumkin.

Litsenziyani uzaytirish
=======================

Muddatli litsenziyani uzaytirish uchun yetkazib beruvchidan yangi litsenziya
kaliti oling va uni ``/license`` sahifasida joylang. Buni joriy litsenziya
hali amal qilayotgan paytda bajarish mumkin.

.. note::

   Anakartni almashtirish yoki operatsion tizimni qayta o'rnatish Machine ID
   ni o'zgartiradi — bu holda mavjud litsenziya ishlamay qoladi va yangi
   Machine ID uchun yangi litsenziya kerak bo'ladi.
