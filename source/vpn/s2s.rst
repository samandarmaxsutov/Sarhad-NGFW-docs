==========================================
Site-to-Site VPN (Ofislararo tunnel)
==========================================

Site-to-Site (S2S) VPN ikki tarmoqni (masalan, bosh ofis va filial) internet
orqali doimiy **IKEv2 / IPsec** tunnel bilan bog'laydi. Ikkala tomon
foydalanuvchilari xuddi bitta lokal tarmoqdagidek aloqa qila oladi. Bu bo'limga
o'tish uchun chap menyudan **VPN → Site-to-Site** bo'limini tanlang
(``/vpn/s2s``).

.. image:: ../_static/vpn_site_to_site.png
   :alt: Site-to-Site VPN sahifasi
   :align: center
   :width: 100%

Tunnel yaratish
===============

**New Tunnel** tugmasini bosing va quyidagi maydonlarni to'ldiring.

Asosiy maydonlar
----------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Maydon
     - Tavsifi
   * - **Name**
     - Tunnel nomi (masalan, ``branch-london``). IKE ulanish nomi sifatida
       ishlatiladi.
   * - **Auth**
     - Autentifikatsiya usuli: **Pre-shared key** (umumiy maxfiy kalit),
       **RSA certificate** yoki **ECDSA certificate**.
   * - **Enabled**
     - Tunnelni darhol yoqish belgisi.
   * - **Remote gateway(s)**
     - Masofaviy (peer) qurilmaning ommaviy IP yoki domen nomi. Har qatorda
       bittadan — bir nechtasi failover (zaxira) sifatida ishlatiladi.
   * - **Listen on (this side)**
     - Bu tomon tinglaydigan WAN interfeysi (standart "Any interface" ko'pchilik
       holatda yetarli).
   * - **Pre-shared key**
     - (Agar Auth = PSK bo'lsa) umumiy maxfiy kalit. **Ikkala tomonda bir xil**
       va kamida 16 belgidan iborat bo'lishi shart. **Generate** tugmasi bilan
       yaratish mumkin.
   * - **Server certificate**
     - (Agar Auth = sertifikat bo'lsa) PKI'dan server sertifikati. Qarang:
       :doc:`/vpn/authorities`.
   * - **Local subnets**
     - Bu tomondagi (mahalliy) tarmoqlar, har qatorda bitta CIDR.
   * - **Remote subnets**
     - Narigi tomondagi (masofaviy) tarmoqlar, har qatorda bitta CIDR.

Bu tarmoqlar **traffic selector** vazifasini bajaradi: faqat Local va Remote
tarmoqlar o'rtasidagi trafik IPsec orqali shifrlanadi.

Shifrlash va qo'shimcha sozlamalar
----------------------------------

- **Crypto profile** — shifrlash to'plami. Standart "Recommended" qiymati
  global sozlamalardan olinadi (:doc:`/vpn/settings`).
- **Show advanced** ostida: **Mode** (Policy-based yoki Route-based), **Role**
  (Auto — ham boshlaydi ham qabul qiladi, yoki Responder only — faqat qabul
  qiladi), IKE/ESP proposal, lifetime va DPD parametrlari.

.. important::

   Tunnel ishlashi uchun ikkala tomon sozlamalari bir-biriga mos kelishi shart:

   - Bir tomonning **Local subnets** i ikkinchi tomonning **Remote subnets** i
     bo'lishi (ya'ni teskari).
   - **Auth** usuli bir xil; PSK ishlatilsa, kalit aynan bir xil.
   - Shifrlash proposal'lari mos kelishi.

Tunnelni boshqarish
===================

Yaratilgan tunnellar jadvalda **Name**, **Peer**, **Auth**, **Subnets**,
**Status** va **Enabled** ustunlari bilan ko'rsatiladi. Har bir tunnel uchun
amallar:

- **Enabled** belgisi — tunnelni yoqish yoki o'chirish.
- **Initiate** — IKE ulanishini qo'lda boshlash (tunnel "Connecting" da
  qotib qolsa foydali).
- **Terminate** — IPsec SA'ni qo'lda tushirish (konfiguratsiya saqlanadi).
- **Edit / Delete** — tahrirlash yoki o'chirish.

Holat (Status)
==============

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Holat
     - Ma'nosi
   * - **Up**
     - Tunnel faol, trafik shifrlanmoqda.
   * - **Connecting**
     - Tunnel yoqilgan, ulanish o'rnatilmoqda.
   * - **Down**
     - Tunnel yoqilgan, lekin faol SA yo'q (peer mavjud emas yoki Terminate
       bosilgan).
   * - **Failed**
     - Ulanish urinishi muvaffaqiyatsiz (odatda sozlamalar mos kelmaganda).
   * - **Disabled**
     - Tunnel o'chirilgan (Enabled belgisi olib tashlangan).

.. note::

   Tunnel "Down" yoki "Failed" da qolsa, eng ko'p uchraydigan sabablar: ikki
   tomondagi shifrlash proposal'larining mos kelmasligi, noto'g'ri PSK,
   teskari yozilmagan subnetlar, yoki WAN firewall'i IPsec portlarini (UDP 500
   va 4500) bloklab qo'ygani.
