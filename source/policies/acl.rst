============================================
Firewall qoidalari (Firewall Policies / ACL)
============================================

Firewall qoidalari tarmoq trafigining qaysi qismiga ruxsat berilishini (permit)
yoki bloklanishini (deny) belgilaydi. Sarhad NGFW da bu qoidalar
**siyosatlar (policies)** sifatida boshqariladi va interfeyslarga avtomatik
qo'llaniladi. Ushbu bo'limga o'tish uchun chap menyudagi
**Firewall → ACL** bo'limini tanlang (``/acl``).

.. image:: ../_static/acl.png
   :alt: Firewall qoidalari sahifasi
   :align: center
   :width: 100%

Qoidalar qanday ishlaydi
========================

- Har bir siyosat (policy) — bu nomlangan va tartiblangan qoida bo'lib, trafik
  uning belgilariga mos kelganda tegishli amalni bajaradi.
- Qoidalar **yuqoridan pastga** qarab tekshiriladi. Trafik birinchi mos kelgan
  qoidaning amaliga (permit yoki deny) bo'ysunadi, keyingi qoidalar tekshirilmaydi.
- Ro'yxat oxirida yashirin "barchasini taqiqlash" (implicit deny) qoidasi
  amal qiladi: hech bir qoidaga mos kelmagan trafik bloklanadi.
- Bundan tashqari, zonalar (WAN/LAN/DMZ) o'rtasidagi trafik uchun tizim
  **zona qoidalarini** avtomatik yaratadi.

Qoida tarkibi
=============

Har bir firewall qoidasi quyidagi maydonlardan iborat:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Maydon
     - Tavsifi
   * - **Nom (Name)**
     - Qoidaning tushunarli nomi (masalan, ``Veb-serverga ruxsat``).
   * - **Yo'nalish (From / To)**
     - Trafik qayerdan (From — kiruvchi) va qayerga (To — chiquvchi) yo'nalishi.
   * - **Manba (Source)**
     - Trafik qayerdan kelishi: ``any``, IP manzil yoki tarmoq (CIDR).
   * - **Manzil (Destination)**
     - Trafik qayerga borishi: ``any``, IP manzil yoki tarmoq (CIDR).
   * - **Protokol (Protocol)**
     - TCP, UDP, ICMP yoki "barchasi" (any).
   * - **Portlar (Ports)**
     - Manzil portlari (masalan, ``80``, ``443``, ``1000-2000``).
   * - **Amal (Action)**
     - ``Permit`` (ruxsat) yoki ``Deny`` (taqiq).
   * - **Tartib (Order)**
     - Qoidaning tekshirilish tartibi. Raqam qancha kichik bo'lsa, qoida shuncha
       oldin tekshiriladi (``lower = first``).
   * - **Holati (Enabled)**
     - Qoida yoqilgan yoki o'chirilgan. O'chirilgan qoida ro'yxatdan
       olib tashlanmasdan vaqtincha ishlamay turadi.

Yangi qoida qo'shish
====================

1. **Add Policy** tugmasini bosing.
2. Yuqorida keltirilgan maydonlarni to'ldiring.
3. Amalni (Permit yoki Deny) tanlang.
4. **Saqlash (Save)** tugmasini bosing.

.. image:: ../_static/add_policy.png
   :alt: Yangi firewall qoidasini qo'shish oynasi
   :align: center
   :width: 100%

Qoidalarni qo'shib yoki o'zgartirib bo'lgach, ularni kuchga kiritish uchun
**Apply rules** tugmasini bosing — shundan so'ng qoidalar interfeyslarga
qo'llaniladi.

.. warning::

   Qoidani saqlash (**Save**) — uni faqat ro'yxatga qo'shadi, lekin hali
   ishga tushirmaydi. **Apply rules** tugmasi bosilmaguncha qoidalar
   **ishlamaydi**. Har qanday o'zgarish (qo'shish, tahrirlash, o'chirish,
   yoqish/o'chirish yoki tartibni o'zgartirish) dan so'ng **Apply rules**
   tugmasini bosishni unutmang.

Misol: Tashqaridan veb-serverga ruxsat berish
---------------------------------------------

- **Nom:** ``HTTPS ruxsat``
- **Amal:** Permit
- **Manba:** ``any`` (istalgan manzil)
- **Manzil:** ``192.168.10.20`` (ichki veb-server)
- **Protokol:** TCP
- **Manzil porti:** ``443``

Qoidalar tartibini o'zgartirish
===============================

Qoidalar tartibi muhim, chunki trafik birinchi mos kelgan qoidaga bo'ysunadi.
Tartib **Order** maydoni orqali belgilanadi: bu raqam qancha kichik bo'lsa,
qoida shuncha oldin tekshiriladi (``lower = first``). Tartibni o'zgartirish
uchun qoidani tahrirlab, uning **Order** qiymatini o'zgartiring.

.. tip::

   Aniqroq (spetsifik) qoidalarga kichikroq **Order** raqamini bering, shunda
   ular umumiyroq qoidalardan oldin tekshiriladi. Masalan, "bitta IP'ni
   bloklash" qoidasiga "butun tarmoqqa ruxsat berish" qoidasidan kichikroq
   Order qiymatini qo'ying.

Qoidani tahrirlash va o'chirish
===============================

- **Tahrirlash (Edit)** — mavjud qoidaning parametrlarini o'zgartirish.
- **O'chirish (Delete)** — qoidani butunlay olib tashlash.
- **Yoqish/O'chirish (Enable/Disable)** — qoidani o'chirmasdan vaqtincha
  faolsizlantirish.

Bog'liq bo'limlar
=================

- MAC manzillari bo'yicha filtrlash: :doc:`/policies/mac-filter`
- Trafik tezligini cheklash: :doc:`/policies/policer`
