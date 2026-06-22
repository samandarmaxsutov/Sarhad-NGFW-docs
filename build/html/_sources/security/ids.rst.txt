==================================================
Hujumlarni aniqlash va oldini olish (IDS/IPS)
==================================================

Sarhad NGFW tarmoqdagi shubhali va zararli faoliyatni aniqlash hamda to'sish
uchun o'rnatilgan IDS/IPS tizimidan foydalanadi. Bu bo'limga o'tish uchun chap
menyudagi **Security → Intrusion Prevention** bo'limini tanlang
(``/intrusion-prevention``).

Asosiy tushunchalar
===================

- **IDS (Intrusion Detection System)** — hujumlarni *aniqlaydi* va ogohlantirish
  (alert) yaratadi, lekin trafikni to'smaydi.
- **IPS (Intrusion Prevention System)** — hujumlarni aniqlash bilan birga
  zararli trafikni *to'sadi* (bloklaydi).

Tizim tarmoq paketlarini maxsus **qoidalar (rules)** to'plamiga solishtiradi.
Agar paket biror qoidaga mos kelsa (masalan, ma'lum bir virus yoki hujum
imzosi), tizim ogohlantirish yaratadi yoki paketni bloklaydi.

IDS/IPS ni yoqish va sozlash
============================

Konfiguratsiya bo'limida quyidagi asosiy parametrlarni sozlash mumkin:

- **Rejim** — IDS (faqat aniqlash) yoki IPS (aniqlash va bloklash).
- **HOME_NET** — himoyalanadigan ichki tarmoq(lar) (masalan,
  ``192.168.0.0/16``). Tizim qaysi tarmoq "ichki" ekanligini shu orqali biladi.
- **EXTERNAL_NET** — tashqi tarmoq ta'rifi (odatda HOME_NET'dan tashqari
  hammasi).
- **Jurnal rejimi** — ogohlantirishlarni qanday yozib borish.

Sozlashdan so'ng **Saqlash** tugmasini bosing va kerak bo'lsa IDS/IPS xizmatini
qayta ishga tushiring (restart).

Qoidalarni boshqarish
=====================

Qoidalar manbalari (Rule sources)
---------------------------------

Tizim qoidalarni tashqi manbalardan yuklab oladi va muntazam yangilab turadi.
Quyidagi manbalar qo'llab-quvvatlanadi:

- **Jamoaviy (Community) qoidalar** — bepul, ochiq qoidalar to'plami.
- **Obuna (Subscriber) qoidalar** — ro'yxatdan o'tgan foydalanuvchilar uchun
  qoidalar (obuna kaliti talab qiladi).
- **Maxsus (custom) manbalar** — boshqa tashqi qoida manbalari.

Manba qo'shish uchun:

1. **Manba qo'shish (Add Source)** tugmasini bosing.
2. Manba URL manzili va kerak bo'lsa **obuna kaliti** ni kiriting.
3. Yangilanish jadvalini (avtomatik yoki qo'lda) tanlang.

Qoidalarni yoqish/o'chirish
---------------------------

Qoidalar toifalarga (kategoriyalarga) bo'lingan (masalan, malware, exploit,
veb-hujumlar). Har bir toifani alohida yoqish yoki o'chirish mumkin. Bu
keraksiz ogohlantirishlarni kamaytirish va tizim yukini optimallashtirish
imkonini beradi.

Avtomatik qoidalar boshqaruvi
-----------------------------

Tizim qoidalarni avtomatik yuklab olish, yangilash va birlashtirish imkonini
beradi. U eskirgan qoidalarni almashtiradi va manbalar o'rtasidagi qoidalarni
muvofiqlashtiradi. Avtomatik yangilanishni yoqib qo'ysangiz, qoidalar muntazam
ravishda o'zi yangilanib turadi.

Maxsus qoidalar
---------------

Tashqi manbalardan tashqari, o'zingizning maxsus qoidalaringizni ham
qo'shishingiz mumkin. Bu o'ziga xos tahdidlarga qarshi maxsus himoya yaratish
uchun foydali.

Ogohlantirishlar (Alerts)
=========================

**Alerts** bo'limida tizim aniqlagan barcha hodisalar ko'rsatiladi:

- **Vaqt (Timestamp)** — hodisa qachon sodir bo'lgani.
- **Imzo (Signature / SID)** — ishga tushgan qoidaning identifikatori.
- **Xabar (Message)** — hodisaning tavsifi.
- **Muhimlik (Priority)** — tahdidning xavf darajasi.
- **Manba/Manzil** — hujumning kelib chiqishi va nishoni.

Ogohlantirishlarni muhimlik darajasi yoki vaqt bo'yicha filtrlash va tashqi
faylga (CSV) eksport qilish mumkin.

.. note::

   IPS rejimida noto'g'ri sozlangan qoidalar haqiqiy (zararsiz) trafikni
   bloklab qo'yishi mumkin (false positive). Yangi qoidalarni avval IDS
   (faqat aniqlash) rejimida sinab ko'rib, so'ngra IPS rejimiga o'tkazish
   tavsiya etiladi.
