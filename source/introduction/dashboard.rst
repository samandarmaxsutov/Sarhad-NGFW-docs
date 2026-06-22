================
Dashboard oynasi
================

Tizimga muvaffaqiyatli kirgandan so'ng siz avtomatik ravishda **Dashboard**
sahifasiga o'tasiz. Bu — boshqaruv panelining bosh sahifasi bo'lib, qurilmaning
umumiy holatini va tarmoq faoliyatini bir qarashda ko'rish imkonini beradi.
Sahifadagi ma'lumotlar real vaqtda, bir necha soniyada bir avtomatik yangilanib
turadi.

.. image:: /_static/dashboard.png
   :alt: Dashboard
   :align: center
   :width: 100%

Statistika kartalari
====================

Sahifaning yuqori qismida qurilmaning asosiy holati to'rtta karta ko'rinishida
ko'rsatiladi:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Ko'rsatkich
     - Nimani bildiradi
   * - **Active Interfaces** (Faol interfeyslar)
     - Ayni paytda faol (UP holatdagi) tarmoq interfeyslari soni.
   * - **CPU Usage** (CPU yuki)
     - Protsessorning band qilingan qismi (foizda). Doimiy yuqori qiymat
       qurilma chegaraga yaqinlashayotganini bildiradi.
   * - **Memory Usage** (Xotira)
     - Ishlatilayotgan operativ xotira (RAM) miqdori.
   * - **System Uptime** (Ish vaqti)
     - Qurilma so'nggi qayta yuklanishdan beri uzluksiz necha vaqtdan beri
       ishlayotgani.

Interfeys grafiklari va statistikasi
====================================

Kartalardan pastda tarmoq trafigi ikki ko'rinishda taqdim etiladi.

**Trafik grafiklari** — interfeyslar bo'yicha trafikning vaqt davomida
o'zgarishini ko'rsatadigan real vaqtdagi grafiklar. Ular orqali qaysi interfeys
qancha yuklanganini va trafikdagi keskin o'zgarishlarni (masalan, kutilmagan
portlashlarni) tezda payqash mumkin.

**Interface Statistics jadvali** — har bir interfeys uchun aniq raqamli
ko'rsatkichlar:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Ustun
     - Tavsifi
   * - **RX Bytes / TX Bytes**
     - Qabul qilingan (RX) va yuborilgan (TX) ma'lumot hajmi (baytlarda).
   * - **RX Pkts / TX Pkts**
     - Qabul qilingan va yuborilgan paketlar soni.
   * - **Drops**
     - Tashlab yuborilgan (qabul qilinmagan) paketlar soni. Yuqori qiymat
       tarmoqda muammo borligidan dalolat berishi mumkin.

Navigatsiya
===========

Sidebar (chap menyu)
--------------------

Chap tomondagi menyu orqali tizimning barcha bo'limlariga o'tiladi:

- **Tarmoq (Network)** — interfeyslar, marshrutlash, NAT, DHCP.
- **Firewall** — ACL qoidalari, MAC filtr, Policer.
- **Xavfsizlik (Security)** — IDS/IPS, TLS tekshiruvi, sertifikatlar.
- **VPN** — Remote Access, Site-to-Site, sozlamalar.
- **Tizim (System)** — foydalanuvchilar, vaqt.
- **Monitoring** — jurnallar va trafik monitoringi.

Yuqori panel (Top bar)
----------------------

Yuqori o'ng burchakda quyidagi elementlar joylashgan:

- **Save** — joriy sozlamalarni doimiy saqlash (qurilma qayta yuklanganda
  yo'qolmasligi uchun).
- **Restore** — saqlangan oldingi sozlamalarga qaytarish.
- **Mavzu (Theme)** — yorug' va qorong'i ko'rinish o'rtasida almashtirgich.
- **Foydalanuvchi menyusi** — joriy foydalanuvchi nomi, profil va xavfsizlik
  sozlamalari (Profile & Security) hamda tizimdan chiqish (Sign out).

.. tip::

   Dashboard kuzatuv uchun qulay boshlang'ich nuqta: agar biror ko'rsatkich
   (masalan, CPU yuki yoki trafik) odatdagidan keskin farq qilsa, tegishli
   bo'limga (interfeyslar, jurnallar yoki IDS/IPS) o'tib batafsil tekshiring.
