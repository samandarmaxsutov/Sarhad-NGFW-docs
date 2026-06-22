===========================================
TLS trafigini tekshirish (TLS Interception)
===========================================

Bugungi kunda internet trafigining katta qismi shifrlangan (HTTPS/TLS).
Bu xavfsizlikni oshirsa-da, zararli dasturlar ham o'z aloqasini shu shifr
ostida yashirishi mumkin. **TLS Interception** funksiyasi shifrlangan
trafikni vaqtincha ochib, tekshirib, qaytadan shifrlash imkonini beradi —
shunda IDS/IPS va filtrlash tizimlari shifrlangan trafik ichini ham ko'ra
oladi. Bu bo'limga o'tish uchun chap menyudagi **Security → TLS Interception**
bo'limini tanlang (``/tls-interception``).

Qanday ishlaydi
===============

TLS Interception "o'rtadagi ishonchli vositachi" (man-in-the-middle) tamoyili
asosida ishlaydi:

1. Mijoz qurilmasi HTTPS sayt bilan bog'lanmoqchi bo'ladi.
2. Sarhad NGFW ulanishni ushlab, o'zining sertifikati bilan mijozga ulanadi
   va alohida ravishda haqiqiy sayt bilan ulanadi.
3. Trafik tizim ichida ochilib tekshiriladi, so'ngra qaytadan shifrlanadi.

Ishlashi uchun mijoz qurilmalariga tizimning **CA sertifikati** ishonchli
sifatida o'rnatilgan bo'lishi shart (qarang: :doc:`/security/certificates`).

Sozlash
=======

1. **TLS Interception** sahifasiga o'ting.
2. Funksiyani **yoqing (Enable)**.
3. Quyidagilarni sozlang:

   - **CA sertifikati** — trafikni qaytadan shifrlash uchun ishlatiladigan
     sertifikat to'plami. Uni :doc:`/security/certificates` bo'limida yuklang.
   - **Tekshiriladigan interfeyslar** — qaysi LAN interfeyslari trafigi
     tekshirilishi.
   - **Tarmoq (Subnet) override** — kerak bo'lsa, interfeysning standart
     tarmog'i o'rniga maxsus tarmoqni ko'rsatish.
   - **QUIC bloklash** — HTTP/3 (QUIC, UDP) protokolini bloklash. Bu brauzerlarni
     tekshirilishi mumkin bo'lgan oddiy HTTPS (TCP) ga qaytishga majbur qiladi.

4. **Saqlash** tugmasini bosing.

.. warning::

   TLS Interception maxfiylikka ta'sir qiluvchi sezgir funksiya. Uni yoqishdan
   oldin tashkilotingizning xavfsizlik siyosati va qonuniy talablariga rioya
   qilinishiga ishonch hosil qiling. Bank, sog'liqni saqlash kabi maxfiy
   saytlar trafigini tekshirishdan istisno qilish tavsiya etiladi.

.. note::

   Ba'zi ilovalar sertifikatni qattiq tekshiradi (certificate pinning) va
   TLS Interception yoqilganda ishlamay qolishi mumkin. Bunday ilovalar uchun
   istisno (bypass) qoidalarini qo'shing.
