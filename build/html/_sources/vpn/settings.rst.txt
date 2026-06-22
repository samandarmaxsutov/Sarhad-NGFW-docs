==========================================
VPN umumiy sozlamalari (IPsec Settings)
==========================================

Bu bo'limda barcha VPN ulanishlariga (Remote Access va Site-to-Site) taalluqli
umumiy sozlamalar boshqariladi. Bu bo'limga o'tish uchun chap menyudagi
**VPN → Settings** bo'limini tanlang (``/vpn/settings``).

Asosiy sozlamalar
=================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Sozlama
     - Tavsifi
   * - **Tinglovchi interfeys (WAN)**
     - VPN tashqi ulanishlarni qabul qiladigan interfeys. Odatda WAN
       interfeysi tanlanadi.
   * - **IKE versiyasi**
     - Kalit almashinuvi protokoli versiyasi (tavsiya etiladigan — IKEv2).
   * - **Shifrlash algoritmlari**
     - Standart shifrlash to'plamlari: shifr (AES-128/192/256), xesh
       (SHA-256), Diffie-Hellman guruhi.
   * - **DPD (Dead Peer Detection)**
     - Javob bermayotgan ulanishlarni aniqlash uchun tekshirish davri.
   * - **Kalit yangilash muddati (Rekey)**
     - Xavfsizlik kalitlari avtomatik almashtirilish oralig'i.

IPsec va NAT
============

Agar VPN trafigi NAT ortida joylashgan tarmoqdan o'tsa, **NAT Traversal
(NAT-T)** funksiyasi avtomatik ishlaydi va trafikni UDP 4500-port orqali
uzatadi. IPsec trafigining NAT bilan to'qnashmasligi uchun tizim mos bypass
qoidalarini avtomatik yaratadi.

Sertifikatlar bilan bog'liqlik
==============================

VPN autentifikatsiyasi sertifikatlarga tayanadi. Server va mijoz
sertifikatlarini PKI bo'limida boshqaring:
:doc:`/security/certificates`.

.. note::

   Shifrlash algoritmlarini o'zgartirishda ehtiyot bo'ling: Remote Access
   mijozlari va Site-to-Site peer'lari shu algoritmlarni qo'llab-quvvatlashi
   shart. Mos kelmaslik ulanishlarning uzilishiga olib keladi. Shubha tug'ilsa,
   standart (tavsiya etilgan) qiymatlarni qoldiring.
