==========================================
Remote Access VPN (Masofaviy kirish)
==========================================

Remote Access (RA) VPN alohida foydalanuvchilarga o'z qurilmasidan (noutbuk,
telefon) korporativ tarmoqqa xavfsiz ulanish imkonini beradi. Ulanish **IKEv2**
protokoli va **EAP** (foydalanuvchi nomi/parol) autentifikatsiyasi asosida
ishlaydi. Bu bo'limga o'tish uchun chap menyudan **VPN → Remote Access**
bo'limini tanlang (``/vpn/ra``).

.. image:: ../_static/vpn_remote_access.png
   :alt: Remote Access VPN sahifasi
   :align: center
   :width: 100%

Sahifa uch tabdan iborat: **Gateways** (kirish nuqtalari), **Users**
(foydalanuvchilar) va **Groups** (guruhlar).

VPN stekini yoqish
==================

Sahifaning yuqorisida umumiy boshqaruv elementlari joylashgan:

- **Enable VPN stack** — VPN tizimini yoqadigan/o'chiradigan asosiy tugmacha.
  O'chirilgan holatda hech bir gateway mijozlarni qabul qilmaydi.
- **WAN** — VPN tashqi ulanishlarni tinglaydigan interfeys (standart holatda
  "Auto — first WAN"). Bu interfeysni faqat VPN stek o'chirilgan holatda
  o'zgartirish mumkin.

Holat satrida tizim qaysi interfeysda tinglayotgani ko'rsatiladi.

1. Gateway yaratish
===================

Gateway — foydalanuvchilar ulanadigan kirish nuqtasi. **Gateways** tabida
**New Gateway** tugmasini bosing va quyidagilarni to'ldiring.

Asosiy maydonlar
----------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Maydon
     - Tavsifi
   * - **Name**
     - Gateway nomi (masalan, ``ra-main``).
   * - **Server certificate**
     - Gateway o'zini tasdiqlaydigan server sertifikati (PKI'dan tanlanadi;
       imzolagan CA avtomatik biriktiriladi). Qarang: :doc:`/vpn/authorities`.
   * - **Virtual-IP pool**
     - Ulangan mijozlarga beriladigan ichki IP manzillar diapazoni, CIDR
       ko'rinishida (masalan, ``10.10.10.0/24``).
   * - **Route mode**
     - **Split-tunnel** — faqat ko'rsatilgan ichki tarmoqlarga trafik VPN
       orqali ketadi (standart). **Full-tunnel** — mijozning butun trafigi VPN
       orqali o'tadi.

Qo'shimcha maydonlar
--------------------

- **Public address** — mijozlar ulanadigan tashqi manzil yoki domen nomi
  (masalan, ``vpn.example.com``). Mijoz konfiguratsiyasiga yoziladi.
- **Listen interface** — IKE tinglovchi aniq WAN interfeysi (bo'sh qoldirilsa,
  barcha WAN interfeyslari).
- **DNS servers** — mijozlarga beriladigan DNS manzillari (Cloudflare, Google,
  Quad9 uchun tezkor tugmalar mavjud).
- **Reachable LAN/DMZ interfaces** — mijozlar kira oladigan ichki interfeyslar;
  split-tunnel rejimida ularning tarmoqlari mijozga marshrut sifatida
  yuboriladi.
- **Crypto profile** — shifrlash to'plami. Standart "Recommended" qiymati
  global sozlamalardan (:doc:`/vpn/settings`) olinadi; kerak bo'lsa
  "Custom" orqali IKE/ESP proposal va vaqtlarni qo'lda kiriting.

Saqlangach, gateway jadvalidagi **Enabled** ustuni orqali uni yoqing.

2. Guruhlar (Groups)
====================

Guruhlar foydalanuvchilarni birlashtiradi va ularga umumiy siyosat beradi.
**Groups** tabida **New Group** tugmasini bosib quyidagilarni belgilang:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Maydon
     - Tavsifi
   * - **Name**
     - Guruh nomi (masalan, ``developers``).
   * - **Route mode**
     - Split-tunnel yoki full-tunnel.
   * - **Allowed subnets**
     - Guruh a'zolari kira oladigan ichki tarmoqlar (har qatorda bitta CIDR).
   * - **Allowed protocols**
     - Ruxsat etilgan protokol/portlar (masalan, ``tcp/443, udp/53, icmp,
       any``).
   * - **Idle timeout (s)**
     - Faolsizlikdan so'ng sessiyani uzish vaqti (0 — cheksiz).
   * - **Max concurrent**
     - Bir a'zo uchun bir vaqtdagi maksimal sessiyalar soni (0 — cheksiz).

3. Foydalanuvchilar (Users)
===========================

**Users** tabida **New User** tugmasini bosing:

- **Username** — kirish nomi (yaratilgandan keyin o'zgartirib bo'lmaydi).
- **Password** — parol (kamida 8 belgi; **Generate** tugmasi bilan kuchli
  parol yaratish mumkin).
- **Group** — foydalanuvchi qaysi guruhga tegishli (ixtiyoriy).
- **Gateway** — qaysi gateway'ga biriktirilishi (ixtiyoriy; bo'sh qoldirilsa,
  birinchi yoqilgan gateway).

Qo'shimcha (overrides) bo'limida bu foydalanuvchi uchun **Static virtual IP**,
**Expires at** (amal qilish muddati) hamda ruxsat etilgan tarmoq/protokollarni
alohida belgilash mumkin.

Ulanish konfiguratsiyasini tarqatish
====================================

Har bir foydalanuvchi yonidagi **yuklab olish** tugmasi orqali uning qurilmasi
uchun tayyor konfiguratsiya faylini olasiz. Platforma bo'yicha to'rt format
mavjud:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Platforma
     - Fayl
   * - **iOS / macOS**
     - ``.mobileconfig`` — avtomatik o'rnatiladigan profil.
   * - **Windows**
     - ``.zip`` — sozlash skripti va mijoz sertifikati (``.pfx``).
   * - **Linux**
     - ``.zip`` — ``swanctl.conf`` parchasi va sertifikat.
   * - **Android**
     - ``.sswan`` — strongSwan ilovasi uchun profil.

Har bir yuklab olishda mijoz uchun yangi sertifikat yaratiladi va uning
``.p12`` paroli ko'rsatiladi. Faylni foydalanuvchiga **xavfsiz** yo'l bilan
yetkazing.

Boshqa amallar
==============

Foydalanuvchi qatorida quyidagi amallar mavjud: tahrirlash, **parolni
yangilash** (rotate), yoqish/o'chirish va o'chirish. Faol sessiyalarni
:doc:`/vpn/overview` (VPN Dashboard) sahifasida kuzatish va kerak bo'lsa uzish
mumkin.

.. note::

   Foydalanuvchi parolini yangilasangiz yoki hisobini o'chirsangiz, uning faol
   sessiyasini ham uzishni unutmang — aks holda u keyingi qayta ulanishigacha
   tarmoqda qoladi.
