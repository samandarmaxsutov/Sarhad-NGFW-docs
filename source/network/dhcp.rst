==============================
DHCP server va relay
==============================

DHCP (Dynamic Host Configuration Protocol) tarmoqdagi qurilmalarga IP
manzillarni avtomatik tarqatish imkonini beradi. Sarhad NGFW ichki **DHCP
server** hamda **DHCP relay** funksiyalarini taqdim etadi.
Bu bo'limga o'tish uchun chap menyudagi **Network → DHCP Server** bo'limini
tanlang (``/dhcp-server``).

DHCP server
===========

DHCP server ichki tarmoqdagi mijozlarga IP manzil, tarmoq niqobi, gateway va
DNS server kabi sozlamalarni avtomatik tarqatadi.

Subnet (tarmoq) qo'shish
------------------------

1. **Subnet qo'shish (Add Subnet)** tugmasini bosing.
2. Quyidagilarni kiriting:

   - **Tarmoq (Subnet)** — CIDR ko'rinishida (masalan, ``192.168.10.0/24``).
   - **Manzillar diapazoni (Pool)** — tarqatiladigan IP manzillar oralig'i
     (masalan, ``192.168.10.100`` — ``192.168.10.200``).
   - **Gateway** — mijozlar uchun standart shlyuz (odatda interfeys IP manzili).
   - **DNS serverlar** — mijozlarga beriladigan DNS manzillari.
   - **Ijara muddati (Lease time)** — IP manzil mijozga necha vaqtga beriladi.

3. **Saqlash (Save)** tugmasini bosing.

Ijaralar (Leases)
-----------------

**Leases** bo'limida ayni paytda tarqatilgan IP manzillar ro'yxati
ko'rsatiladi: mijoz MAC manzili, berilgan IP, qurilma nomi (hostname) va
ijara tugash vaqti. Bu orqali tarmoqqa ulangan qurilmalarni kuzatish mumkin.

DHCP relay
==========

Agar markaziy DHCP server boshqa tarmoqda joylashgan bo'lsa, DHCP relay
mijozlarning so'rovlarini shu serverga uzatadi. Bu, ayniqsa, VLANlarga
bo'lingan tarmoqlarda foydali — har bir VLAN'da alohida server saqlash shart
emas.

Relayni sozlash uchun:

- **Tinglovchi interfeys** — DHCP so'rovlari keladigan ichki interfeys yoki VLAN.
- **DHCP server manzili** — so'rovlar uzatiladigan markaziy server IP manzili.

.. note::

   Bitta tarmoqda DHCP server va DHCP relay bir vaqtning o'zida ishlamasligi
   kerak — ulardan faqat bittasini tanlang.
