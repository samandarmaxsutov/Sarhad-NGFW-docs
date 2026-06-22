==========================================
Sertifikatlar va PKI
==========================================

Sarhad NGFW raqamli sertifikatlarni boshqarish uchun ichki **PKI** (Public Key
Infrastructure — ochiq kalitlar infratuzilmasi) tizimiga ega. Sertifikatlar
TLS trafigini tekshirish hamda VPN ulanishlarini autentifikatsiya qilish uchun
ishlatiladi. Bu bo'limga o'tish uchun chap menyudagi **Security → Certificates**
yoki **PKI → Authorities** bo'limini tanlang
(``/certificates``, ``/pki/authorities``).

Asosiy tushunchalar
===================

- **CA (Certificate Authority)** — sertifikat beruvchi markaz. CA boshqa
  sertifikatlarni imzolaydi va ularning haqiqiyligini tasdiqlaydi.
- **Server sertifikati** — server (masalan, VPN gateway) o'zini tasdiqlash
  uchun ishlatadigan sertifikat.
- **Mijoz sertifikati** — foydalanuvchi yoki qurilmani tasdiqlash uchun
  ishlatiladigan sertifikat.
- **CRL (Certificate Revocation List)** — bekor qilingan sertifikatlar ro'yxati.

Sertifikat markazini (CA) yaratish
==================================

1. **PKI → Authorities** sahifasiga o'ting.
2. **CA yaratish (Create CA)** tugmasini bosing.
3. Quyidagilarni kiriting:

   - **Nom (CN — Common Name)** — CA nomi (masalan, ``Sarhad-Root-CA``).
   - **Tashkilot (Organization)** — tashkilot nomi.
   - **Amal qilish muddati** — sertifikat necha kun amal qilishi.

4. **Yaratish** tugmasini bosing.

Mavjud CA'ni import qilish ham mumkin — buning uchun PEM formatidagi
sertifikat va maxfiy kalit fayllarini yuklang.

Sertifikat berish (issue)
=========================

CA yaratilgandan so'ng undan server yoki mijoz sertifikatlarini berishingiz
mumkin:

1. CA'ni tanlang va **Sertifikat berish (Issue Certificate)** tugmasini bosing.
2. Sertifikat turini (server yoki mijoz) va CN (egasi nomi) ni kiriting.
3. Amal qilish muddatini belgilang va **Berish** tugmasini bosing.

Berilgan sertifikatni yuklab olish (download) yoki VPN sozlamalarida ishlatish
mumkin.

TLS Interception uchun CA
=========================

TLS trafigini tekshirish (:doc:`/security/tls-interception`) uchun maxsus CA
sertifikati kerak. Bu sertifikatni **Certificates** sahifasida yuklang
(upload) yoki PKI orqali yarating. So'ngra bu CA sertifikatini barcha mijoz
qurilmalariga **ishonchli** sifatida o'rnating — aks holda foydalanuvchilar
brauzerda sertifikat xatoliklarini ko'radi.

Sertifikatni bekor qilish (revoke)
==================================

Agar sertifikat xavf ostida qolsa yoki kerak bo'lmasa, uni bekor qilish
mumkin:

1. Sertifikatlar ro'yxatidan kerakli sertifikatni tanlang.
2. **Bekor qilish (Revoke)** tugmasini bosing.

Bekor qilingan sertifikat CRL'ga qo'shiladi va undan keyin ishonchsiz deb
hisoblanadi.

.. note::

   CA'ning maxfiy kalitini xavfsiz saqlang. Agar maxfiy kalit o'g'irlansa,
   tajovuzkor soxta sertifikatlar yaratishi mumkin. Shubha tug'ilsa, CA'ni
   bekor qilib, yangisini yarating.
