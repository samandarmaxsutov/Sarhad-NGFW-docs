==========================================
Trafik tezligini cheklash (Policer)
==========================================

Policer (trafik cheklovchi) tarmoq trafigining tezligini (bandwidth)
cheklash imkonini beradi. Bu orqali ayrim interfeyslar yoki ulanishlar tarmoq
resurslarini haddan tashqari band qilib qo'yishining oldi olinadi. Bu bo'limga
o'tish uchun chap menyudagi **Firewall → Policer** bo'limini tanlang
(``/policer``).

Qanday ishlaydi
===============

Policer "token bucket" (token chelaki) algoritmidan foydalanadi: trafik
belgilangan tezlikdan oshib ketsa, ortiqcha paketlar yo belgilanadi (mark) yoki
tashlab yuboriladi (drop). Bu interfeysga kiruvchi yoki chiquvchi trafikning
maksimal tezligini kafolatlash imkonini beradi.

Policer profili yaratish
========================

1. **Profil qo'shish (Add Policer)** tugmasini bosing.
2. Quyidagi parametrlarni kiriting:

   - **Nom (Name)** — profilning tushunarli nomi (masalan, ``Mehmon-tarmoq-10M``).
   - **CIR (Committed Information Rate)** — kafolatlangan o'rtacha tezlik
     (masalan, 10 Mbit/s).
   - **CBS (Committed Burst Size)** — bir vaqtning o'zida ruxsat etilgan
     maksimal portlash hajmi (baytlarda).
   - **Amal (Action)** — chegaradan oshgan trafik bilan nima qilish:
     ``drop`` (tashlab yuborish) yoki ``mark`` (belgilash).

3. **Saqlash (Save)** tugmasini bosing.

Profilni interfeysga bog'lash
=============================

Profil yaratilgandan so'ng uni bir yoki bir nechta interfeysga bog'lash kerak:

- **Yo'nalish (Direction)** — kiruvchi (ingress) yoki chiquvchi (egress)
  trafikni cheklash.
- **Interfeys** — profil qaysi interfeysga qo'llanishi.

Misol: Mehmon tarmog'ini cheklash
---------------------------------

Mehmon foydalanuvchilari tarmog'i internetning butun kanalini band qilmasligi
uchun unga 10 Mbit/s lik cheklov qo'yish mumkin. Buning uchun ``CIR = 10 Mbit/s``
bo'lgan profil yaratib, uni mehmon VLAN interfeysiga chiquvchi yo'nalishda
bog'lang.

.. note::

   Policer trafikni cheklaydi, lekin uni navbatga qo'yib kechiktirmaydi
   (shaping emas). Chegaradan oshgan paketlar darhol belgilanadi yoki tashlab
   yuboriladi.
