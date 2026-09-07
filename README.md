# YKS2027 WEB - TYT & AYT Hazırlık Takip Sistemi

🎓 **YKS 2027'ye hazırlanan öğrenciler için kapsamlı bir web tabanlı takip sistemi**

> **📢 Production-Ready!** Bu uygulama artık Docker, PostgreSQL, Redis, CI/CD pipeline ve otomatik deployment desteği ile production ortamına hazır!

## 📋 İçindekiler

- [Hızlı Başlangıç](#hızlı-başlangıç)
- [Özellikler](#özellikler)
- [Teknolojiler](#teknolojiler)
- [🐳 Docker ile Çalıştırma](#-docker-ile-çalıştırma)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Veritabanı Modelleri](#veritabanı-modelleri)
- [API Endpoint'leri](#api-endpointleri)
- [Güvenlik](#güvenlik)
- [Deployment](#deployment)
- [Sorun Giderme](#sorun-giderme)
- [Lisans](#lisans)

---

## 🚀 Hızlı Başlangıç

### Windows Kullanıcıları (En Kolay Yol)
```bash
# start.bat dosyasına çift tıklayın veya:
start.bat
```

### Docker ile (Önerilen - Production)
```bash
# Tüm servisleri başlat (PostgreSQL, Redis, Flask)
docker-compose up -d

# Uygulamaya eriş: http://localhost:5000
```

### Manuel Kurulum
```bash
pip install -r requirements.txt
python run.py
```

📖 **Detaylı deployment rehberi için:** [DEPLOYMENT.md](DEPLOYMENT.md)

---

## ✨ Özellikler

### 📚 Konu Takibi
- TYT ve AYT konu başlıklarının detaylı takibi
- Konu ilerleme durumu (Çalışılmadı, Çalışıldı, Tamamlandı)
- Çalışma süresi ve tarih takibi
- Konu bazlı not ekleme

### 📝 Soru Çözüm Takibi
- Günlük soru çözüm kayıtları
- Doğru/Yanlış/Bos analizi
- Konu bazlı soru dağılımı
- Başarı yüzdesi hesaplama

### 📊 Deneme Sınavları
- TYT ve AYT deneme sınavı kayıtları
- Ders bazlı sonuç analizi
- İlerleme grafikleri
- Puan hesaplama

### 🎯 Akıllı Çalışma Koçu
- Otomatik görev önerileri
- Öncelik bazlı çalışma planı
- Tekrar zamanı hatırlatmaları
- Haftalık hedef takibi

### 📧 E-posta Otomasyonu
- Haftalık rapor gönderimi
- Özelleştirilebilir gönderim zamanı
- HTML şablon desteği

### 🎥 Online Hoca
- YouTube video ders entegrasyonu
- Konu bazlı video kategorizasyonu
- Admin panel ile video yönetimi

### 🔐 Kullanıcı Yönetimi
- Kayıt/Giriş sistemi
- Profil yönetimi
- Admin yetkilendirmesi
- Session yönetimi

---

## 🛠️ Teknolojiler

### Backend
- **Python 3.10+**
- **Flask 3.0.0** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM
- **Flask-Login 0.6.3** - Kimlik doğrulama
- **Flask-WTF 1.2.1** - Form işleme
- **SQLAlchemy 2.0+** - Veritabanı
- **psycopg** - PostgreSQL desteği

### Frontend
- **Bootstrap 5.3.2** - UI framework
- **Bootstrap Icons** - İkonlar
- **Google Fonts (Inter)** - Tipografi
- **Custom CSS/JS** - Özel stiller

### Veritabanı
- **SQLite** (varsayılan)
- **PostgreSQL** (production için desteklenir)

---

## 📦 Kurulum

### Gereksinimler
- Python 3.10 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Projeyi Klonlayın
```bash
cd "C:\AI PROJECTS\YKS2027_WEB"
```

### Adım 2: Sanal Ortam Oluşturun (Önerilir)
```bash
python -m venv venv
```

### Adım 3: Sanal Ortamı Aktifleştirin
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Adım 4: Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 5: .env Dosyasını Yapılandırın
`.env.example` dosyasını `.env` olarak kopyalayın ve ayarları yapın:
```bash
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=yksi2027-gizli-anahtar-kelime-buraya-degistirin-xyz123!

# Database Configuration
DATABASE_URL=sqlite:///yks2027.db

# Server Configuration
PORT=5000
HOST=0.0.0.0

# Email Configuration (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
```

### Adım 6: Uygulamayı Başlatın
```bash
python run.py
```

Uygulama http://localhost:5000 adresinde çalışacaktır.

---

## 📖 Kullanım

### İlk Kayıt
1. http://localhost:5000 adresine gidin
2. "Kayıt Ol" butonuna tıklayın
3. Kullanıcı bilgilerinizi girin
4. Alan seçiminizi yapın (Sayısal, Eşit Ağırlık, Sözel)

### Konu Takibi
1. Dashboard'dan TYT veya AYT Konuları'na gidin
2. Konu başlıklarını görüntüleyin
3. Çalışılan konuları işaretleyin
4. Notlar ekleyin

### Soru Çözümü
1. "Soru Takibi" menüsüne gidin
2. Yeni soru çözümü ekleyin
3. Tarih, ders, konu seçin
4. Doğru/Yanlış/Bos sayılarını girin

### Deneme Sınavı
1. "Deneme Sınavları" menüsüne gidin
2. Yeni deneme ekleyin
3. Ders bazlı sonuçları girin
4. Analizleri görüntüleyin

### E-posta Otomasyonu
1. "Ayarlar" > "E-posta Bildirimleri" ne gidin
2. Alıcı bilgilerini girin
3. Gönderim gününü ve saatini seçin
4. Otomasyonu aktif edin

---

## 📁 Proje Yapısı

```
YKS2027_WEB/
├── app/                      # Ana uygulama dizini
│   ├── __init__.py          # App factory
│   ├── routes/              # Route tanımları
│   │   ├── __init__.py
│   │   ├── auth.py          # Kimlik doğrulama
│   │   ├── main.py          # Ana sayfa
│   │   ├── dashboard.py     # Dashboard
│   │   ├── topics.py        # Konu yönetimi
│   │   ├── questions.py     # Soru takibi
│   │   ├── mock_exams.py    # Deneme sınavları
│   │   ├── scores.py        # Puan hesaplama
│   │   ├── settings.py      # Ayarlar
│   │   └── online_hoca.py   # Video dersler
│   ├── templates/           # HTML şablonları
│   │   ├── base.html        # Ana şablon
│   │   ├── index.html       # Ana sayfa
│   │   ├── auth/            # Kimlik doğrulama
│   │   ├── dashboard/       # Dashboard
│   │   ├── topics/          # Konular
│   │   ├── questions/       # Sorular
│   │   ├── mock_exams/      # Denemeler
│   │   ├── scores/          # Puanlar
│   │   ├── settings/        # Ayarlar
│   │   ├── online_hoca/     # Video dersler
│   │   └── errors/          # Hata sayfaları
│   └── static/              # Statik dosyalar
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── images/
├── database/                # Veritabanı katmanı
│   ├── __init__.py
│   ├── models.py            # SQLAlchemy modelleri
│   ├── db_manager.py        # Veritabanı yönetimi
│   ├── email_service.py     # E-posta servisi
│   └── scheduler.py         # Zamanlanmış görevler
├── config/                  # Yapılandırma
│   ├── __init__.py
│   ├── database_config.py   # DB yapılandırması
│   ├── tyt_topics.json      # TYT konuları
│   └── ayt_topics.json      # AYT konuları
├── utils/                   # Yardımcı fonksiyonlar
│   └── __init__.py
├── instance/                # Instance-specific dosyalar
│   └── yks2027.db           # SQLite veritabanı
├── .env                     # Environment variables
├── .env.example             # Örnek environment
├── .gitignore               # Git ignore
├── requirements.txt         # Python bağımlılıkları
├── run.py                   # Uygulama başlatıcı
└── README.md                # Bu dosya
```

---

## 🗄️ Veritabanı Modelleri

| Model | Açıklama |
|-------|----------|
| User | Kullanıcı bilgileri |
| Subject | Dersler (TYT/AYT) |
| Topic | Konu başlıkları |
| TopicProgress | Konu ilerleme durumu |
| QuestionRecord | Soru çözüm kayıtları |
| MockExam | Deneme sınavları |
| MockExamResult | Deneme ders sonuçları |
| ScoreCalculation | Puan hesaplamaları |
| DailyTask | Günlük görevler |
| WeeklyGoal | Haftalık hedefler |
| AutoEmailSettings | E-posta otomasyonu |
| EmailLog | E-posta logları |
| YoutubeVideo | Video dersler |

---

## 🔌 API Endpoint'leri

### Kimlik Doğrulama
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /auth/register | Kayıt sayfası |
| POST | /auth/register | Kayıt ol |
| GET | /auth/login | Giriş sayfası |
| POST | /auth/login | Giriş yap |
| GET | /auth/logout | Çıkış yap |

### Dashboard
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /dashboard | Ana dashboard |

### Konular
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /topics/tyt | TYT konuları |
| GET | /topics/ayt | AYT konuları |
| POST | /topics/update | Konu durumu güncelle |

### Sorular
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /questions/list | Soru listesi |
| POST | /questions/add | Soru ekle |
| GET | /questions/analysis | Soru analizi |

### Denemeler
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /mock-exams/list | Deneme listesi |
| POST | /mock-exams/add | Deneme ekle |
| GET | /mock-exams/analysis | Deneme analizi |

### Puan
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /scores/calculator | Puan hesaplama |
| POST | /scores/calculate | Puan hesapla |

### Ayarlar
| Method | Endpoint | Açıklama |
|--------|----------|----------|
| GET | /settings | Ayarlar sayfası |
| POST | /settings/update | Ayarları güncelle |

---

## 🔒 Güvenlik

### Önemli Ayarlar

1. **SECRET_KEY**: Production'da mutlaka değiştirin
2. **SESSION_COOKIE_SECURE**: HTTPS kullanıyorsanız True yapın
3. **DATABASE_URL**: Production PostgreSQL kullanın
4. **SMTP_PASSWORD**: E-posta için App Password kullanın

### CSRF Koruması
Tüm formlar CSRF token ile korunmaktadır.

### Rate Limiting
Varsayılan olarak saatte 100 istek ile sınırlıdır.

---

## 🐛 Sorun Giderme

### Flask Modülü Bulunamadı
```bash
pip install -r requirements.txt
```

### Veritabanı Hatası
```bash
# Veritabanını sıfırla
python reset_database.py
```

### Port Zaten Kullanılıyor
```bash
# .env dosyasında PORT'u değiştirin
PORT=5001
```

### E-posta Gönderimi Çalışmıyor
1. Gmail için 2FA aktif edin
2. App Password oluşturun
3. `.env` dosyasında SMTP bilgilerini kontrol edin

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

## 👥 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'i push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

---

## 📞 İletişim

Sorularınız için proje yöneticisi ile iletişime geçebilirsiniz.

---

**YKS2027 WEB** - Başarıya giden yolda güvenilir çalışma arkadaşınız! 🎓
