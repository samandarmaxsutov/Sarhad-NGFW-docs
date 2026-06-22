============================================
Firewall qoidalari (Firewall Policies / ACL)
============================================

Firewall qoidalari tarmoq trafigining qaysi qismi ruxsat etilishi (permit)
yoki bloklanishi (deny) kerakligini belgilaydi. Sarhad NGFW da bu qoidalar
**siyosatlar (policies)** ko'rinishida boshqariladi va ular avtomatik ravishda
interfeyslarga qo'llaniladi. Bu bo'limga o'tish uchun chap menyudagi
**Firewall → ACL** bo'limini tanlang (``/acl``).

Qoidalar qanday ishlaydi
========================

- Har bir siyosat (policy) — nomlangan, tartiblangan qoida bo'lib, u trafikning
  ma'lum belgilariga mos kelganda ma'lum amalni bajaradi.
- Qoidalar **yuqoridan pastga** qarab tekshiriladi. Trafik birinchi mos kelgan
  qoidaning amalini oladi (permit yoki deny), keyingi qoidalar tekshirilmaydi.
- Ro'yxat oxirida yashirin "barchasini taqiqlash" (implicit deny) qoidasi
  amal qiladi: hech qaysi qoidaga mos kelmagan trafik bloklanadi.
- Bundan tashqari, zonalar (WAN/LAN/DMZ) o'rtasidagi trafik uchun tizim
  avtomatik **zona qoidalarini** yaratadi.

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
   * - **Amal (Action)**
     - ``Permit`` (ruxsat) yoki ``Deny`` (taqiq).
   * - **Manba (Source)**
     - Trafik qayerdan kelishi: IP manzil yoki tarmoq (CIDR).
   * - **Manzil (Destination)**
     - Trafik qayerga borishi: IP manzil yoki tarmoq (CIDR).
   * - **Protokol**
     - TCP, UDP, ICMP yoki "barchasi" (any).
   * - **Portlar**
     - Manba va/yoki manzil portlari (masalan, ``80``, ``443``,
       ``1000-2000``).
   * - **Holati (Enabled)**
     - Qoida yoqilgan yoki o'chirilgan. O'chirilgan qoida o'chirilmasdan
       vaqtincha ishlamay turadi.

Yangi qoida qo'shish
====================

1. **Qoida qo'shish (Add Rule)** tugmasini bosing.
2. Yuqorida keltirilgan maydonlarni to'ldiring.
3. Amalni (Permit yoki Deny) tanlang.
4. **Saqlash (Save)** tugmasini bosing.

Qoida darhol kuchga kiradi va kerakli interfeyslarga avtomatik bog'lanadi.

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

Qoidalar tartibi muhim ahamiyatga ega, chunki trafik birinchi mos kelgan
qoidaga bo'ysunadi. Qoidani yuqoriga yoki pastga surish uchun ro'yxatdagi
strelkalardan (yoki sudrab tashlash — drag and drop) foydalaning.

.. tip::

   Aniqroq (spetsifik) qoidalarni ro'yxatning yuqorisiga, umumiyroq qoidalarni
   pastiga joylashtiring. Masalan, "bitta IP'ni bloklash" qoidasini "butun
   tarmoqqa ruxsat berish" qoidasidan yuqoriga qo'ying.

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
