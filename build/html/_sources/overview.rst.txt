============================
Tezkor boshlash
============================

Sarhad NGFW — yuqori unumdorlikka ega yangi avlod tarmoq xavfsizlik devori.
Barcha sozlamalar HTTPS veb-interfeysi (``https://<ip>:8443``) orqali
boshqariladi. Bu bo'lim qurilmani birinchi marta ishga tushirish uchun
asosiy qadamlarni ketma-ket ko'rsatadi.

Birinchi sozlash qadamlari
==========================

1. Qurilmaga ulanish
--------------------

Qurilma birinchi marta yoqilganda boshqaruv (MGMT) interfeysiga IP manzil
berish kerak. Buni qurilmaga ulangan fizik konsol (monitor/klaviatura) orqali
bajaring: konsol menyusida IP manzil va niqobni kiriting.

So'ngra shu tarmoqdagi kompyuter brauzeridan boshqaruv panelini oching:

.. code-block:: text

   https://<mgmt-ip>:8443

2. Litsenziyani faollashtirish
------------------------------

Litsenziya o'rnatilmagan bo'lsa, tizim avtomatik ``/license`` sahifasini
ko'rsatadi. Qurilmaning **Machine ID** sini nusxalab, yetkazib beruvchidan
litsenziya kalitini oling va uni faollashtiring.

Batafsil: :doc:`/introduction/licensing`.

3. Tizimga kirish va parolni almashtirish
-----------------------------------------

Standart hisob (``admin`` / ``admin123``) bilan kiring va birinchi ishda
**root va admin parollarini darhol o'zgartiring**.

Batafsil: :doc:`/introduction/login`, :doc:`/system/users`.

4. Interfeys va zonalarni sozlash
---------------------------------

Tarmoq interfeyslariga zona (WAN/LAN/DMZ) tayinlang va IP manzillarni bering.
WAN — internet tomon, LAN — ichki tarmoq.

Batafsil: :doc:`/network/interface`.

5. Marshrut va NAT
------------------

Internetga chiqish uchun standart marshrut (default gateway) qo'shing va ichki
tarmoq internetga chiqishi uchun NAT (SNAT) ni sozlang.

Batafsil: :doc:`/network/routing`, :doc:`/network/nat`.

6. Firewall qoidalari
---------------------

Tarmoqlar o'rtasidagi trafikni boshqarish uchun firewall qoidalarini yarating.
Zonalar o'rtasidagi asosiy qoidalar avtomatik yaratiladi, qolganini o'zingiz
qo'shasiz.

Batafsil: :doc:`/policies/acl`.

7. Qo'shimcha xizmatlar (ixtiyoriy)
-----------------------------------

Asosiy tarmoq ishlaganidan so'ng kerakli qo'shimcha funksiyalarni yoqing:

- Masofaviy xodimlar uchun VPN: :doc:`/vpn/overview`
- Hujumlarni aniqlash va oldini olish: :doc:`/security/ids`
- IP manzillarni avtomatik tarqatish: :doc:`/network/dhcp`

Qo'llanma tuzilishi
====================

Qo'llanma quyidagi bo'limlardan iborat:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Bo'lim
     - Mazmuni
   * - **Kirish**
     - Tizimga kirish, Dashboard va litsenziya.
   * - **Tarmoq sozlamalari**
     - Interfeyslar, marshrutlash, NAT, DHCP.
   * - **Firewall qoidalari**
     - ACL qoidalari, MAC filtr, trafik cheklash (Policer).
   * - **Xavfsizlik**
     - IDS/IPS, TLS tekshiruvi, sertifikatlar (PKI).
   * - **VPN**
     - Remote Access, Site-to-Site va umumiy sozlamalar.
   * - **Tizim sozlamalari**
     - Foydalanuvchilarni boshqarish.
   * - **Monitoring**
     - Jurnallar va trafik monitoringi.

.. tip::

   Har bir sozlash bosqichidan so'ng yuqori paneldagi **Konfiguratsiyani
   saqlash** tugmasini bosing — shunda o'zgarishlar qurilma qayta ishga
   tushganidan keyin ham saqlanib qoladi.
