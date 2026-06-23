==========================================
VPN umumiy sozlamalari (Settings)
==========================================

Bu sahifa barcha VPN ulanishlariga (Remote Access va Site-to-Site) standart
qiymat sifatida qo'llaniladigan global parametrlarni boshqaradi. Alohida
gateway yoki tunnel bu qiymatlarni o'zining sozlamalari bilan almashtirishi
mumkin. Bu bo'limga o'tish uchun chap menyudan **VPN → Settings** bo'limini
tanlang (``/vpn/settings``).

.. image:: ../_static/vpn_settings.png
   :alt: VPN umumiy sozlamalari sahifasi
   :align: center
   :width: 100%

Shifrlash to'plami (Crypto profile)
===================================

**Crypto profile** har bir tunnel uchun standart IKE va ESP proposal'larini
tanlaydi:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Profil
     - Tavsifi
   * - **Modern**
     - Faqat zamonaviy algoritmlar: AES-256-GCM, ECP384. Eng xavfsiz, lekin
       peer ham zamonaviy bo'lishini talab qiladi.
   * - **Compatible**
     - Zamonaviy algoritmlar + MODP3072 zaxira varianti. Ko'pchilik
       qurilmalar bilan mos.
   * - **Legacy**
     - Eskirgan algoritmlar (3DES, SHA1, MODP1024). **Xavfsiz emas** — faqat
       yangilab bo'lmaydigan eski uskunalar uchun.
   * - **Custom**
     - IKE va ESP proposal'larini hamda vaqtlarni qo'lda kiritish.

Custom rejimida **IKE proposal** (autentifikatsiya bosqichi) va **ESP
proposal** (ma'lumotni shifrlash bosqichi) ni vergul bilan ajratib kiritasiz
(masalan, ``aes256gcm16-prfsha384-ecp384``).

Vaqt va bayroqlar (Timers & flags)
==================================

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Sozlama
     - Tavsifi
   * - **IKE lifetime (s)**
     - IKE SA (boshqaruv kanali) amal qilish muddati. Standart: ``14400`` (4
       soat).
   * - **ESP lifetime (s)**
     - Child SA (ma'lumot tunneli) amal qilish muddati. Standart: ``3600`` (1
       soat).
   * - **Rekey margin (s)**
     - Kalit muddat tugashidan necha sekund oldin yangilanishi. Standart:
       ``540``. Ulanish uzilmasligi uchun kalit oldindan yangilanadi.
   * - **DPD delay (s)**
     - Dead Peer Detection — peer'ni tekshirish oralig'i. Standart: ``30``.
   * - **DPD timeout (s)**
     - Peer javob bermasa, uni "o'lik" deb hisoblash vaqti. Standart: ``120``.
   * - **DPD action**
     - Peer javob bermaganda nima qilish: ``clear`` (uzish), ``hold``
       (ushlab turish) yoki ``restart`` (qayta ulanish).
   * - **NAT traversal (NAT-T)**
     - NAT ortidagi peer'lar uchun UDP 4500 inkapsulyatsiyasi: ``auto`` (kerak
       bo'lganda), ``force`` (doimo) yoki ``disable``.
   * - **Fragmentation**
     - IKE paketlarini bo'laklash: ``yes``, ``accept`` yoki ``no``.
   * - **MOBIKE**
     - Mijoz IP manzili o'zgarganda (masalan, Wi-Fi'dan mobil internetga)
       ulanishni uzmasdan davom ettirish (RFC 4555). Mobil mijozlar uchun
       foydali.
   * - **Allow legacy crypto**
     - Eskirgan zaif algoritmlarga ruxsat berish. Standart holatda
       **o'chirilgan** (tavsiya etiladi).

Remote Access standart qiymatlari
=================================

Bu maydonlar yangi RA gateway yaratishda avtomatik to'ldiriladi (har bir
gateway ularni o'zgartirishi mumkin):

- **Default virtual-IP pool** — RA mijozlariga beriladigan IP diapazoni
  (masalan, ``10.10.10.0/24``).
- **Default DNS** — mijozlarga beriladigan DNS manzillari.
- **Default banner** — mijozga autentifikatsiyadan oldin ko'rsatiladigan
  xabar (masalan, foydalanish siyosati).

Saqlash
=======

- **Save** — o'zgarishlarni saqlaydi va kuchga kiritadi.
- **Reset to defaults** — barcha sozlamalarni zavod (tavsiya etilgan)
  qiymatlariga qaytaradi (saqlash uchun keyin **Save** ni bosish kerak).

.. note::

   Shifrlash sozlamalarini o'zgartirishda ehtiyot bo'ling: Remote Access
   mijozlari va Site-to-Site peer'lari bu algoritmlarni qo'llab-quvvatlashi
   shart. Mos kelmaslik ulanishlarni uzadi. Shubha tug'ilsa, **Modern** yoki
   **Compatible** profilini qoldiring.
