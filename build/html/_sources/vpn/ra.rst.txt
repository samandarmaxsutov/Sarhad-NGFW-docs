==========================================
Remote Access VPN (Masofaviy kirish)
==========================================

Remote Access (RA) VPN alohida foydalanuvchilarga o'z qurilmasidan (noutbuk,
telefon) korporativ tarmoqqa xavfsiz ulanish imkonini beradi. Sarhad NGFW
**IKEv2** protokoli va EAP autentifikatsiyasidan foydalanadi. Bu bo'limga
o'tish uchun chap menyudagi **VPN → Remote Access** bo'limini tanlang
(``/vpn/ra``).

Sozlash bosqichlari
===================

RA VPN'ni ishga tushirish uchun uchta asosiy qadam bajariladi:

1. **Gateway** (kirish nuqtasi) yaratish.
2. **Guruhlar** va **foydalanuvchilar** qo'shish.
3. Foydalanuvchilarga **ulanish to'plamini (bundle)** tarqatish.

1. Gateway yaratish
===================

Gateway — foydalanuvchilar ulanadigan VPN kirish nuqtasi.

1. **Gateway qo'shish (Add Gateway)** tugmasini bosing.
2. Quyidagilarni kiriting:

   - **Nom (Name)** — gateway nomi.
   - **Tinglovchi interfeys** — odatda WAN interfeysi (tashqi ulanishlarni
     qabul qiladi).
   - **Server sertifikati** — gateway o'zini tasdiqlaydigan sertifikat
     (PKI'dan, qarang: :doc:`/security/certificates`).
   - **Manzillar puli (Client pool)** — ulangan mijozlarga beriladigan ichki
     IP manzillar diapazoni (masalan, ``10.10.10.0/24``).
   - **DNS serverlar** — mijozlarga beriladigan DNS manzillari.
   - **Shifrlash algoritmlari** — IKE va ESP uchun shifrlash to'plamlari
     (standart qiymatlar tavsiya etiladi).

3. **Saqlash** tugmasini bosing.

2. Guruh va foydalanuvchi qo'shish
==================================

Guruhlar
--------

Guruhlar foydalanuvchilarni birlashtiradi va ularga qaysi ichki tarmoqlarga
kirish ruxsat etilishini belgilaydi. Masalan, ``Buxgalteriya`` guruhi faqat
buxgalteriya serverlariga kira oladi.

1. **Guruh qo'shish (Add Group)** tugmasini bosing.
2. Guruh nomi va ruxsat etilgan tarmoqlarni (allowed subnets) kiriting.

Foydalanuvchilar
----------------

1. **Foydalanuvchi qo'shish (Add User)** tugmasini bosing.
2. Quyidagilarni kiriting:

   - **Foydalanuvchi nomi (Username)**.
   - **Parol (Password)** — EAP autentifikatsiyasi uchun.
   - **Guruh** — foydalanuvchi qaysi guruhga tegishli.

3. **Saqlash** tugmasini bosing.

3. Ulanish to'plamini tarqatish (Bundle)
========================================

Har bir foydalanuvchi uchun tizim avtomatik **ulanish to'plamini** (bundle)
yaratadi. Bu to'plam mijoz qurilmasiga VPN'ni sozlash uchun kerakli barcha
ma'lumotlarni o'z ichiga oladi:

- Mijoz sertifikati (``.p12`` fayli).
- macOS/iOS uchun avtomatik sozlash profili (``.mobileconfig``).
- Server manzili va ulanish parametrlari.

To'plamni yuklab olish uchun foydalanuvchi yonidagi **To'plamni yuklab olish
(Download Bundle)** tugmasini bosing va uni foydalanuvchiga xavfsiz yo'l bilan
yetkazing.

Faol sessiyalarni kuzatish
==========================

Sahifaning quyi qismida ayni paytda ulangan foydalanuvchilar ko'rsatiladi:

- Foydalanuvchi nomi.
- Berilgan virtual IP manzil.
- Mijozning haqiqiy (tashqi) IP manzili.
- Uzatilgan/qabul qilingan ma'lumot hajmi.
- Ulanish vaqti.

Kerak bo'lganda foydalanuvchini majburan uzish (disconnect) mumkin.

.. note::

   Foydalanuvchi parolini yoki sertifikatini bekor qilsangiz, uning faol
   sessiyasini ham uzishni unutmang — aks holda u keyingi qayta ulanishgacha
   tarmoqda qoladi.
