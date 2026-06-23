==========================================
VPN — Umumiy ko'rinish (Dashboard)
==========================================

VPN ulanishlari ochiq internet orqali xavfsiz, shifrlangan tunnel yaratadi.
Sarhad NGFW **IKEv2 / IPsec** protokoliga asoslangan ikki turdagi VPN'ni
qo'llab-quvvatlaydi. Bu bo'limga o'tish uchun chap menyudan **VPN → Dashboard**
bo'limini tanlang (``/vpn``).

.. image:: ../_static/vpn_overview.png
   :alt: VPN Dashboard
   :align: center
   :width: 100%

**VPN Dashboard** — kuzatuv (monitoring) sahifasi. U yerda ulanishlar sozlanmaydi,
balki ayni paytdagi faol sessiyalar va trafik real vaqtda kuzatiladi. Sahifa
har 5 soniyada avtomatik yangilanadi.

VPN turlari
===========

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Tur
     - Tavsifi
   * - **Remote Access (RA)**
     - Alohida foydalanuvchilar o'z qurilmasidan korporativ tarmoqqa ulanadi.
       IKEv2 + EAP (foydalanuvchi nomi/parol) autentifikatsiyasi ishlatiladi.
       Qarang: :doc:`/vpn/ra`.
   * - **Site-to-Site (S2S)**
     - Ikki ofis tarmog'ini doimiy IKEv2 tunnel bilan bog'laydi.
       Qarang: :doc:`/vpn/s2s`.

Throughput grafigi
==================

Sahifaning yuqorisidagi **Throughput (kbps)** grafigi barcha SA (Security
Association) lar bo'yicha jami trafikni ko'rsatadi:

- **In** — kiruvchi trafik (kbit/s).
- **Out** — chiquvchi trafik (kbit/s).

Grafik RA va S2S ulanishlarining umumiy o'tkazuvchanligini real vaqtda aks
ettiradi.

Faol sessiyalar (Live sessions)
===============================

**Live sessions** jadvalida ayni paytda o'rnatilgan barcha IKE SA'lar
ko'rsatiladi. Ustunlar:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Ustun
     - Tavsifi
   * - **User / IKE**
     - RA sessiyasi uchun — foydalanuvchi nomi (EAP ID) va u ulangan gateway
       nomi. S2S uchun — tunnel (IKE ulanish) nomi.
   * - **VIP**
     - RA mijoziga manzillar pulidan berilgan virtual IP. S2S uchun bo'sh
       (``—``).
   * - **Public IP**
     - Mijoz yoki masofaviy peer'ning tashqi (WAN) IP manzili.
   * - **State**
     - IKE SA holati: **Established** (o'rnatilgan), **Connecting**
       (ulanmoqda), **Rekeying** (kalit yangilanmoqda), **Deleting**
       (uzilmoqda).
   * - **Bytes (in / out)**
     - Shu sessiyada uzatilgan va qabul qilingan ma'lumot hajmi.
   * - **Duration**
     - Sessiya o'rnatilganidan beri o'tgan vaqt.
   * - **Actions**
     - Sessiyani majburan uzish (**Disconnect**) tugmasi.

.. note::

   Terminlar haqida qisqacha: **IKE SA** — boshqaruv kanali (kalit almashinuvi);
   **Child SA (ESP)** — haqiqiy ma'lumotni shifrlovchi tunnel. Bitta IKE SA
   ostida bir nechta Child SA bo'lishi mumkin; jadvaldagi baytlar ularning
   yig'indisidir.

Tayyorgarlik
============

VPN'ni sozlashdan oldin quyidagilarni tayyorlang:

1. **Sertifikatlar (PKI)** — VPN autentifikatsiyasi uchun CA va server
   sertifikatlari. Qarang: :doc:`/vpn/authorities`.
2. **WAN interfeysi** — VPN tashqi ulanishlarni qabul qiladigan interfeys.
3. **Global sozlamalar** — shifrlash va vaqt parametrlari. Qarang:
   :doc:`/vpn/settings`.

Keyingi qadamlar: :doc:`/vpn/ra` (masofaviy foydalanuvchilar),
:doc:`/vpn/s2s` (ofislararo tunnel).
