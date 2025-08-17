Türkiye'nin Şehirlerini Bulma Oyunu
Bu Python tabanlı oyun, kullanıcıların Türkiye'nin 81 ilini bir harita üzerinde bularak coğrafya bilgilerini test etmelerini sağlayan interaktif bir uygulamadır. Oyun, tkinter ile oluşturulan basit bir grafik arayüzü (GUI) ve turtle modülü ile çalışan bir oyun ekranı olmak üzere iki ana bölümden oluşur.

Oyunun Akışı ve Özellikleri
Giriş Ekranı: Oyuna başlarken, kullanıcı tkinter ile oluşturulmuş basit bir karşılama ekranı ile karşılaşır. Bu ekranda kullanıcı adı girilir ve "Oyuna Başla" butonuyla ana ekrana geçiş yapılır.

Harita Ekranı: Ana oyun ekranında, Türkiye'nin illerini gösteren bir harita bulunur. Bu ekranda, turtle modülü kullanılarak bir oyun döngüsü başlatılır.

Şehir Tahminleri: Kullanıcı, oyun sırasında çıkan diyalog kutucuğuna bir şehir adı girer.

Eğer girilen şehir adı, veri setinde bulunan 81 ilden biri ise ve daha önce tahmin edilmediyse, şehrin adı harita üzerinde doğru konumuna yazılır.

Yanlış veya zaten girilmiş bir şehir adı girildiğinde ise kullanıcıya uyarı mesajı gösterilir.

Puanlama ve Sonuç: Doğru tahmin edilen her şehir için bir sayaç artar. Kullanıcı, 81 ilin tamamını doğru tahmin ettiğinde, oyun "Tebrikler!" mesajıyla sona erer.

Kullanılan Teknolojiler:

Python: Uygulamanın temel programlama dili.

Turtle: Harita üzerinde şehirlerin konumunu işaretlemek için kullanılan grafik modülü.

Pandas: Şehir adlarını ve koordinatlarını içeren CSV dosyasını okumak ve işlemek için kullanılır.

Tkinter: Oyun için basit bir giriş arayüzü (login ekranı) oluşturur.
