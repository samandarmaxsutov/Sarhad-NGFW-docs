==================================================
Hujumlarni aniqlash va oldini olish (IDS/IPS)
==================================================

Sarhad NGFW tarmoqdagi shubhali va zararli faoliyatni aniqlash hamda oldini
olish uchun o'rnatilgan IDS/IPS tizimidan foydalanadi. Tizim **Snort** dvigateli
asosida ishlaydi, shuning uchun maxsus qoidalar Snort sintaksisida yoziladi.
Ushbu bo'limga o'tish uchun chap menyudan **Security → Intrusion Prevention**
bo'limini tanlang (``/intrusion-prevention``).

Asosiy tushunchalar
===================

- **IDS (Intrusion Detection System)** — hujumlarni *aniqlaydi* va ogohlantirish
  (alert) yaratadi, lekin trafikni to'xtatmaydi.
- **IPS (Intrusion Prevention System)** — hujumlarni aniqlash bilan birga
  zararli trafikni *to'xtatadi* (bloklaydi).

Tizim tarmoq paketlarini maxsus **qoidalar (rules)** to'plami bilan
solishtiradi. Agar paket biror qoidaga (masalan, ma'lum bir virus yoki hujum
imzosiga) mos kelsa, tizim ogohlantirish yaratadi yoki paketni bloklaydi.

Sahifa uch tabdan iborat: **Settings** (sozlash), **Rules** (qoidalar manbalari)
va **Alerts** (ogohlantirishlar). Yuqorida xizmatni boshqarish tugmalari
(**Start**, **Stop**, **Restart**) joylashgan.

.. tip::

   Agar kiritilgan o'zgarishlar darhol ko'rinmasa, sahifaning yuqori
   burchagidagi **Refresh** tugmasini bosing.

Settings tabi — yoqish va sozlash
=================================

.. image:: ../_static/idps_start.png
   :alt: IDS/IPS ni yoqish va sozlash
   :align: center
   :width: 100%

Tekshiriladigan interfeyslar
----------------------------

**Interfaces** bo'limida IDS/IPS qaysi interfeyslar trafigini tekshirishi
belgilanadi. Kerakli interfeysni tanlab, **Add** tugmasi bilan qo'shing.
Tekshiruv faqat shu interfeyslarga qo'llaniladi.

Tekshiruv siyosati
------------------

- **Inspection policy** — tekshiruv qat'iyligi darajasi.
- **Detection effort** — aniqlash chuqurligi (yuqori daraja ko'proq tahdidni
  topadi, biroq ko'proq resurs talab qiladi).

Advanced — HOME tarmog'i (network scope)
----------------------------------------

**Advanced** bo'limida himoyalanadigan ichki tarmoq (HOME network) belgilanadi.
Tizim tanlangan interfeyslar asosida mos tarmoqni avtomatik **taklif qiladi**:

1. Taklif qilingan qiymatni qo'llash uchun **Apply** tugmasini bosing
   (yoki tarmoqni qo'lda kiriting, masalan ``192.168.0.0/16``).
2. So'ngra **Save network scope** tugmasini bosib, tarmoq doirasini saqlang.

To'g'ri belgilangan HOME tarmog'i tizimga "ichki" va "tashqi" trafikni farqlash
imkonini beradi.

Maxsus qoidalar (custom rules)
------------------------------

Tashqi manbalardan tashqari, o'zingizning maxsus qoidalaringizni Snort
sintaksisida yozishingiz mumkin. Buni ikki usulda qilish mumkin:

- **Quick add (namunaviy qoidalar)** — tayyor namunalar yordamida qoida tuzish.
  Tayyor namunalardan birini tanlasangiz (masalan, ``SSH (22) log``,
  ``DNS (53) log``, ``Block TCP port`` yoki QUIC trafigini bloklash), maydonlar
  avtomatik to'ldiriladi. So'ngra quyidagilarni moslang:

  - **Action** — ``Log (alert)`` (ogohlantirish), ``Drop`` (tashlab yuborish)
    yoki ``Reject`` (rad etish).
  - **Protocol** — TCP, UDP, ICMP yoki IP (any).
  - **Source / Destination** — manba va manzil (yoki ``any``).
  - **Dest port** — manzil porti.
  - **Message** — qoida ishga tushganda yoziladigan izoh.

  So'ng **Append to editor** tugmasini bosing — qoida quyidagi tahrirlagichga
  qo'shiladi.

- **Qo'lda yozish** — qoidalarni to'g'ridan-to'g'ri tahrirlagich (editor)
  oynasiga Snort sintaksisida yozish.

Qoidalarni yozib bo'lgach, **Save rules** tugmasini bosing. Faol qoidalarni
qayta yuklash uchun **Reload active rules** tugmasidan foydalaning.

.. important::

   Maxsus qoidalar ishlashi uchun pastdagi **Additional rule packs** bo'limida
   **local rules** (mahalliy qoidalar) yoqilgan bo'lishi shart. Aks holda siz
   yozgan qoidalar qo'llanmaydi.

Rules tabi — qoidalar manbalari
===============================

.. image:: ../_static/idps_rules.png
   :alt: IDS/IPS qoidalar manbalari
   :align: center
   :width: 100%

Bu tabda tayyor qoidalar to'plamlari (rule sources) yuklab olinadi va yangilab
turiladi:

- **Community** — bepul, ochiq qoidalar to'plami (kalit talab qilmaydi).
- **Talos** — kengaytirilgan qoidalar to'plami (obuna kaliti talab qilishi
  mumkin; kalitni manba kartasidagi maydonga kiriting).

Har bir manba uchun:

1. **Download** tugmasini bosib qoidalarni yuklab oling. Holat ko'rsatkichi
   yuklangan qoidalar sonini (``N rules``) yoki ``Not downloaded`` ni ko'rsatadi.
2. **Auto-update** tugmachasini yoqib, yangilanish oralig'ini (``Every 6h``,
   ``12h`` yoki ``24h``) tanlang — shunda qoidalar muntazam avtomatik
   yangilanib turadi.

Alerts tabi — ogohlantirishlar
==============================

.. image:: ../_static/idps_alerts.png
   :alt: IDS/IPS ogohlantirishlari
   :align: center
   :width: 100%

**Alerts** tabida tizim aniqlagan barcha hodisalar jadval ko'rinishida
ko'rsatiladi. Ustunlar:

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Ustun
     - Tavsifi
   * - **Time**
     - Hodisa sodir bo'lgan sana va vaqt.
   * - **Pri**
     - Muhimlik darajasi (priority). Raqam qancha kichik bo'lsa, tahdid shuncha
       jiddiy.
   * - **ID**
     - Ishga tushgan qoidaning identifikatori (signature ID / SID).
   * - **Proto**
     - Hodisaga tegishli protokol (TCP, UDP, ICMP va h.k.).
   * - **Source**
     - Trafikning manba IP manzili (va porti) — hujum qayerdan kelgani.
   * - **Destination**
     - Trafikning manzil IP manzili (va porti) — nishon.
   * - **Action**
     - Tizim bajargan amal: ``alert`` (ogohlantirish), ``drop`` (tashlangan)
       yoki ``reject`` (rad etilgan).
   * - **Message**
     - Hodisaning tavsifi — qaysi tahdid yoki holat aniqlangani.

Ogohlantirishlarni ko'rib chiqib, takror yoki noto'g'ri (false positive)
qoidalarni sozlash orqali tizimni aniqlashtirib borish mumkin.

.. note::

   IPS rejimida (``Drop`` / ``Reject``) noto'g'ri sozlangan qoidalar haqiqiy
   (zararsiz) trafikni ham bloklab qo'yishi mumkin. Shu sababli yangi
   qoidalarni avval ``Log (alert)`` rejimida sinab ko'rib, ishonch hosil
   qilgandan so'ng bloklash rejimiga o'tkazish tavsiya etiladi.
