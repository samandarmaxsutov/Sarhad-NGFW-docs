==========================================
VPN — Umumiy ko'rinish
==========================================

VPN (Virtual Private Network — virtual xususiy tarmoq) ochiq internet orqali
xavfsiz, shifrlangan ulanish yaratish imkonini beradi. Sarhad NGFW **IPsec
(IKEv2)** protokoli asosida ikki turdagi VPN'ni qo'llab-quvvatlaydi.
Bu bo'limga o'tish uchun chap menyudagi **VPN → Overview** bo'limini tanlang
(``/vpn``).

VPN turlari
===========

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Tur
     - Tavsifi
   * - **Remote Access (RA)**
     - Alohida foydalanuvchilar (masalan, masofadan ishlovchi xodimlar)
       o'z qurilmasidan korporativ tarmoqqa xavfsiz ulanadi.
       Qarang: :doc:`/vpn/ra`.
   * - **Site-to-Site (S2S)**
     - Ikki ofis yoki tarmoqni internet orqali doimiy xavfsiz tunnel bilan
       bog'laydi. Qarang: :doc:`/vpn/s2s`.

VPN holati dashboardi
=====================

Overview sahifasida VPN tizimining umumiy holati ko'rsatiladi:

- **Faol sessiyalar** — ayni paytda ulangan foydalanuvchilar va tunnellar soni.
- **Tunnel holati** — har bir Site-to-Site tunnelning holati (UP/DOWN).
- **Statistika** — uzatilgan va qabul qilingan ma'lumotlar hajmi.
- **So'nggi hodisalar** — autentifikatsiya va ulanish hodisalari.

Tayyorgarlik
============

VPN'ni sozlashdan oldin quyidagilarni tayyorlang:

1. **Sertifikatlar (PKI)** — VPN autentifikatsiyasi uchun CA va server
   sertifikatlari kerak. Qarang: :doc:`/security/certificates`.
2. **WAN interfeysi** — VPN tashqi internetdan ulanishlarni qabul qiladigan
   interfeys. Qarang: :doc:`/vpn/settings`.
3. **Firewall qoidalari** — VPN trafigi uchun mos ruxsatlar (odatda tizim
   avtomatik yaratadi).

Keyingi qadamlar
================

- Masofaviy foydalanuvchilar uchun: :doc:`/vpn/ra`
- Ofislarni bog'lash uchun: :doc:`/vpn/s2s`
- Umumiy VPN sozlamalari: :doc:`/vpn/settings`
