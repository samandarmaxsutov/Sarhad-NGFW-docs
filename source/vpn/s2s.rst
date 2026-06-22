==========================================
Site-to-Site VPN (Ofislararo tunnel)
==========================================

Site-to-Site (S2S) VPN ikki tarmoqni (masalan, bosh ofis va filial) internet
orqali doimiy shifrlangan tunnel bilan bog'laydi. Ikkala tomon foydalanuvchilari
xuddi bitta lokal tarmoqdagidek bir-biri bilan aloqa qila oladi. Bu bo'limga
o'tish uchun chap menyudagi **VPN → Site-to-Site** bo'limini tanlang
(``/vpn/s2s``).

Tunnel yaratish
===============

1. **Tunnel qo'shish (Add Tunnel)** tugmasini bosing.
2. Quyidagi parametrlarni kiriting:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Maydon
        - Tavsifi
      * - **Nom (Name)**
        - Tunnelning tushunarli nomi (masalan, ``Bosh-ofis—Filial``).
      * - **Masofaviy gateway (Peer IP)**
        - Ikkinchi tomon (filial) qurilmasining ommaviy IP manzili.
      * - **Local subnet**
        - Bu tomondagi (mahalliy) tarmoq, CIDR ko'rinishida.
      * - **Remote subnet**
        - Narigi tomondagi (masofaviy) tarmoq, CIDR ko'rinishida.
      * - **Autentifikatsiya**
        - Oldindan kelishilgan kalit (PSK) yoki sertifikat.
      * - **Shifrlash algoritmlari**
        - IKE va ESP shifrlash to'plamlari. Ikkala tomonda bir xil bo'lishi
          shart.

3. **Saqlash** tugmasini bosing.

.. important::

   Tunnel ishlashi uchun ikkala tomonning sozlamalari bir-biriga mos kelishi
   shart: bir tomonning "local subnet"i ikkinchi tomonning "remote subnet"i
   bo'lishi, autentifikatsiya kaliti va shifrlash algoritmlari bir xil bo'lishi
   kerak.

Tunnelni boshqarish
===================

Yaratilgan tunnellar ro'yxatida har biri uchun quyidagi amallar mavjud:

- **Yoqish/O'chirish (Enable/Disable)** — tunnelni o'chirmasdan vaqtincha
  faolsizlantirish.
- **Ishga tushirish (Initiate)** — tunnelni qo'lda ko'tarish.
- **To'xtatish (Terminate)** — tunnelni qo'lda tushirish.
- **Tahrirlash / O'chirish** — parametrlarni o'zgartirish yoki tunnelni
  o'chirish.

Holatni kuzatish
================

Har bir tunnel uchun joriy holat ko'rsatiladi:

- **UP** — tunnel faol, shifrlangan aloqa o'rnatilgan.
- **DOWN** — tunnel ishlamayapti (sozlamalar mosligini va peer mavjudligini
  tekshiring).
- **Connecting** — ulanish o'rnatilmoqda.

Qo'shimcha parametrlar
======================

- **DPD (Dead Peer Detection)** — narigi tomon javob bermay qolsa, buni
  aniqlash va tunnelni qayta tiklash.
- **Avtomatik kalit yangilash (Rekey)** — xavfsizlik kalitlarini belgilangan
  vaqt oralig'ida avtomatik almashtirish.

.. note::

   Agar tunnel "DOWN" holatida qolsa, eng ko'p uchraydigan sabablar: ikki
   tomondagi shifrlash algoritmlarining mos kelmasligi, noto'g'ri PSK, yoki
   WAN tomonidagi firewall IPsec portlarini (UDP 500 va 4500) bloklab
   qo'ygani.
