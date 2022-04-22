class script(object):
    START_TXT = """👋  Merhaba {}\n
 🔎 Ara Butonunu Kullanın.."""
    HELP_TXT = """👋 Merhaba {}
Komutlarım İçin Yardım ."""
    ABOUT_TXT = """✯ Kutuphane Botu
✯ Yaratıcı: kamileecher
✯ Kütüphane: Pyrogram
✯ Dil: Python 3
✯ Veri Tabanı: db
✯ Bot 𝚂unucusu: xxxx
✯ Yapı Durumu: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Yonetici - https://t.me/kamileecher 
<b>BILGI:</b>
- <a href=https://t.me/sanaldisk>Livebox</a>"""
    MANUELFILTER_TXT = """Yardım: <b>Filters</b>
<b>NOT:</b>
1. Kutuphane yönetici  olmalı.
2. Bir sohbete yalnızca yöneticiler filtre ekleyebilir.
3. Uyarı düğmelerinin sınırı 64 karakterdir. 
<b>Komutlar Ve Kullanım:</b>
• /filter - <code>Sohbet için bir filtre ekle</code>
• /filters - <code>Tüm Filtrelerin listesi</code>
• /del - <code>sohbette belirli bir filtreyi silme</code>
• /delall - <code>sohbetteki tüm filtreleri silme (Sohbet Kurucusu Sadece)</code>"""
    BUTTON_TXT = """Yardım: <b>Butonlar</b>
- Kutuphane Botu Hem URL hem de uyarı satır içi düğmelerini destekler .
<b>NOT:</b>
1. Telegram herhangi bir içerik olmadan düğme göndermenize izin vermez, bu nedenle içerik zorunludur.
2. Quickwaste Film Botu, herhangi bir telegram medya türüne sahip düğmeleri destekler.
3. Düğmeler markdown biçimi olarak düzgün bir şekilde ayrıştırılmalıdır
<b>URL Butonları:</b>
<code>[Button Text](buttonurl:https://t.me/kamileecher)</code>
<b>Uyarı Butonları:</b>
<code>[Button Text](buttonalert:Uyarı Butonu)</code>"""
    AUTOFILTER_TXT = """Yardım: <b>Auto Filter</b>
<b>NOT:</b>
1. Özelse beni kanalınızın yöneticisi yap.
2. Kanalınızın kam rip, porno ve sahte dosyalar içermediğinden emin olun.
3. Son mesajı bana alıntılarla iletin.
 O kanaldaki tüm dosyaları veritabanıma ekleyeceğim. ."""
    CONNECTION_TXT = """Help: <b>Baglantılar</b>
- Filtreleri yönetmek için botu PM'ye bağlamak için kullanılır 
- gruplar halinde spam'leri önlemeye yardımcı olur. 
<b>NOT:</b>
1. Yalnızca yöneticiler bağlantı ekleyebilir .
2. Ozelden <code>/connect</code> komutunu gönder
<b>Komutlar Ve Kullanım:</b>
• /connect  - <code>belirli bir sohbeti özel sohbetinize bağlama</code>
• /disconnect  - <code>sohbetten Bağlantıyı Kopartma</code>
• /connections - <code>Tüm Bağlantılarının Listesi</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Ozellik</b>
<b>NOT:</b>
Ekstra özellikler
<b>Komutlar ve Kullanımı:</b>
• /id - <code>Belirli Bir kullanıcının İd sini getirir.</code>
• /info  - <code>Kulanıcıların Bilgisini Getirir.</code>
• /imdb  - <code>İmdb Kaynağından Film Bilgisi getirir.</code>
• /search  - <code>film bilgilerini çeşitli kaynaklardan almak.</code>"""
    ADMIN_TXT = """Yardım: <b>Admin modu</b>
<b>NOT:</b>
Bu modül yalnızca yöneticim için çalışır. 
<b>Komutlar ve Kullanımı:</b>
• /logs - <code>rescent hatalarını almak için</code>
• /stats - <code>DB'deki dosyaların durumunu almak için.</code>
• /users - <code>kullanıcılarımın ve kimliklerimin listesini almak için.</code>
• /chats - <code>sohbetlerimin ve kimliklerimin listesini almak için</code>
• /leave  - <code>sohbetten ayrılmak için.</code>
• /disable  -  <code>sohbeti devre dışı bırakma.</code>
• /ban  - <code>kullanıcıyı yasaklamak için.</code>
• /unban  - <code>Kullanıcının Banını Açma.</code>
• /channnel - <code>toplam bağlı kanalların listesini almak için</code>
• /broadcast - <code>Tüm Kutuphane kullanıcılarına mesaj yayınlamak için</code>"""
    STATUS_TXT = """★ Toplam Dosya: <code>{}</code>
★ Toplam Kullanıcı: <code>{}</code>
★ 𝚃oplam Sohbet: <code>{}</code>
★ Kullanılan Alan: <code>{}</code> 𝙼𝚒𝙱
★ Boş Alan: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Grup = {}(<code>{}</code>)
Toplam Üyeler = <code>{}</code>
Eklendi tarafından - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
ADI - {}
"""
