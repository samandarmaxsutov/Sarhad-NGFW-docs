==================================================
Manbaga asoslangan marshrutlash (ABF)
==================================================

ABF (Access-Based Forwarding) — bu siyosatga asoslangan marshrutlash
(policy-based routing). Oddiy marshrutlash faqat manzil (destination) IP'ga
qarab yo'l tanlaydi; ABF esa trafikni boshqa belgilari (manba IP, port,
protokol) bo'yicha tanlab, uni maxsus keyingi tugunga (next-hop) yo'naltirish
imkonini beradi. Ushbu bo'limga o'tish uchun chap menyudan **Firewall → ABF**
bo'limini tanlang (``/abf``).

.. image:: ../_static/abf.png
   :alt: Access-Based Forwarding sahifasi
   :align: center
   :width: 100%

Qachon ishlatiladi
==================

ABF quyidagi holatlarda foydali bo'ladi:

- Ma'lum bir tarmoq yoki foydalanuvchilar trafigini boshqa kanal (masalan,
  ikkinchi internet provayder) orqali yuborish.
- Ayrim ilovalar trafigini alohida yo'nalishga ajratish.

ABF ikki bosqichda sozlanadi
============================

1. **ACL Match Rule** — qaysi trafikni tanlash kerakligini aniqlaydi.
2. **ABF Policy** — tanlangan trafikni qayerga (next-hop) yo'naltirishni
   belgilaydi va interfeysga qo'llaydi.

1-bosqich: ACL Match Rule yaratish
==================================

1. **Create ACL** tugmasini bosing.
2. **ACL Name** maydoniga nom kiriting (masalan, ``match-http-from-lan``).
3. **Add Rule** orqali bir yoki bir nechta qoida qo'shing. Har bir qoida
   quyidagi maydonlardan iborat:

   .. list-table::
      :header-rows: 1
      :widths: 28 72

      * - Maydon
        - Tavsifi
      * - **Action**
        - ``PERMIT`` (mos trafikni ABF'ga olish) yoki ``DENY``.
      * - **Protocol**
        - Any, TCP, UDP, ICMP yoki boshqa protokol raqami (0–255).
      * - **Source IP/CIDR**
        - Manba tarmoq (masalan, ``0.0.0.0/0`` — barchasi).
      * - **Src Port**
        - Manba porti (yoki ``any``).
      * - **Dest IP/CIDR**
        - Manzil tarmoq (masalan, ``0.0.0.0/0``).
      * - **Dst Port**
        - Manzil porti (yoki ``any``).

4. **Save ACL** tugmasini bosing.

.. image:: ../_static/add_abf_rule.png
   :alt: ACL Match Rule yaratish oynasi
   :align: center
   :width: 100%

2-bosqich: ABF Policy yaratish
==============================

ABF Policy yuqorida yaratilgan ACL'ni keyingi tugun (next-hop) bilan bog'laydi
va interfeysga qo'llaydi.

1. **Create Policy** tugmasini bosing.
2. Quyidagilarni belgilang:

   - **ACL** — qaysi trafik mos kelishini (yuqorida yaratilgan ACL).
   - **Next-Hop IP** — mos trafik yo'naltiriladigan keyingi tugun manzili
     (masalan, ``10.10.0.1``).
   - **Apply to Interface (input)** — siyosat qo'llaniladigan interfeys
     (kiruvchi yo'nalishda).
   - **Priority** — siyosat ustuvorligi (bir nechta siyosat bo'lganda tartibni
     belgilaydi).

3. **Create & Apply** tugmasini bosing.

.. image:: ../_static/apply_abf_policy.png
   :alt: ABF siyosatini yaratish va qo'llash oynasi
   :align: center
   :width: 100%

Yaratilgan siyosatlar **ABF Policies** jadvalida ACL, Next-Hop, interfeys va
ustuvorligi bilan ko'rsatiladi.

.. note::

   ABF tanlangan trafikni odatiy marshrutlash jadvalini chetlab o'tib,
   ko'rsatilgan next-hop'ga yuboradi. Shuning uchun next-hop manzili shu
   interfeys orqali yetib boradigan ishlaydigan manzil ekanligiga ishonch
   hosil qiling.
