============================
Tizim vaqti va NTP
============================

To'g'ri sozlangan tizim vaqti juda muhim: u jurnallardagi (log) vaqt
belgilarining aniqligi, sertifikatlarning amal qilish muddatini tekshirish
va VPN ulanishlarining barqarorligi uchun zarur. Bu bo'limga o'tish uchun chap
menyudagi **System → Time** bo'limini tanlang (``/time``).

Vaqtni sozlash
==============

Vaqtni ikki usulda sozlash mumkin:

- **Avtomatik (NTP)** — tizim vaqtni internet orqali NTP (Network Time
  Protocol) serverlaridan avtomatik oladi va doimo aniq saqlab turadi.
  Tavsiya etiladigan usul.
- **Qo'lda (Manual)** — sanani va vaqtni qo'lda kiritish.

NTP serverlarini sozlash
========================

1. **NTP**'ni yoqing.
2. Bir yoki bir nechta NTP server manzilini kiriting (masalan,
   ``pool.ntp.org`` yoki mahalliy server).
3. **Vaqt mintaqasini (Timezone)** tanlang (masalan, ``Asia/Tashkent``).
4. **Saqlash** tugmasini bosing.

Sozlangandan so'ng tizim vaqtni avtomatik sinxronlashtiradi.

.. note::

   Agar tizim vaqti noto'g'ri bo'lsa, VPN sertifikatlari "amal muddati
   tugagan" deb noto'g'ri baholanishi va ulanishlar uzilishi mumkin. Shuning
   uchun NTP'ni yoqib qo'yish tavsiya etiladi.

.. tip::

   Vaqt mintaqasini to'g'ri tanlang — jurnal yozuvlaridagi vaqt belgilari shu
   mintaqaga mos ko'rsatiladi, bu hodisalarni tahlil qilishni osonlashtiradi.
