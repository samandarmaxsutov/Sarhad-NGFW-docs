================
Dashboard oynasi
================

Tizimga muvaffaqiyatli kirgandan so'ng siz avtomatik ravishda **Dashboard**
sahifasiga o'tasiz. Bu — boshqaruv panelining bosh sahifasi bo'lib, qurilmaning
umumiy holatini va tarmoq faoliyatini bir qarashda ko'rish imkonini beradi.
Sahifadagi ma'lumotlar real vaqtda, har necha soniyada avtomatik
yangilanib turadi.

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
     - Qurilma oxirgi qayta ishga tushishidan beri uzluksiz qancha vaqt
       ishlayotganini ko'rsatadi.

Interfeys grafiklari va statistikasi
====================================

Kartalardan pastda tarmoq trafigi ikki ko'rinishda taqdim etiladi.

**Trafik grafiklari** — interfeyslar bo'yicha trafikning vaqt davomida
o'zgarishini ko'rsatadigan real vaqtdagi grafiklar. Ular orqali qaysi interfeys
qancha yuklanganini va trafikdagi keskin o'zgarishlarni (masalan, kutilmagan
burstlarni) tezda payqash mumkin.

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

Chap tomondagi menyu bo'limlarga (guruhlarga) ajratilgan. Quyida har bir
guruh va undagi sahifalar keltirilgan:

**Dashboard**
   - *Status* — bosh sahifa (tizimning umumiy holati).

**Network (Tarmoq)**
   - *Interfaces* — tarmoq interfeyslari.
   - *Routes* — marshrutlash.
   - *NAT* — manzil almashtirish.
   - *DHCP* — DHCP server va relay.

**Firewall Policies (Firewall qoidalari)**
   - *ACL* — firewall qoidalari.
   - *MAC Filter* — MAC manzili bo'yicha filtrlash.
   - *ABF* — manbaga asoslangan marshrutlash (policy-based routing).
   - *Policer* — trafik tezligini cheklash.
   - *Flow Monitoring* — trafik oqimlari monitoringi.

**Security Profiles (Xavfsizlik)**
   - *IDS/IPS* — hujumlarni aniqlash va oldini olish.
   - *SSL/TLS Inspection* — shifrlangan trafikni tekshirish.
   - *Inspection Certificates* — tekshiruv sertifikatlari.

**VPN**
   - *Dashboard* — VPN umumiy holati.
   - *Site-to-Site* — ofislararo tunnel.
   - *Remote Access* — masofaviy kirish.
   - *Authorities* — sertifikat markazlari (PKI).
   - *Settings* — VPN sozlamalari.

**System (Tizim)**
   - *Firewall Users* — foydalanuvchilarni boshqarish.

**Logs (Jurnallar)**
   - *Firewall Logs* — firewall hodisalari jurnali.
   - *URL Logs* — ko'rilgan URL manzillar jurnali.
   - *Config Logs* — konfiguratsiya o'zgarishlari jurnali.
   - *Auth Logs* — kirish/chiqish jurnali.
   - *VPN Logs* — VPN hodisalari jurnali.
   - *IDS/IPS Logs* — hujum ogohlantirishlari jurnali.
   - *Log settings* — jurnal saqlash sozlamalari.

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
