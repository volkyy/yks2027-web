# YKS2027 WEB - Deployment Rehberi

Bu rehber, YKS2027 WEB uygulamasını production ortamında nasıl çalıştıracağınızı adım adım açıklar.

---

## 📋 İçindekiler

1. [Hızlı Başlangıç](#hızlı-başlangıç)
2. [Docker ile Deployment](#docker-ile-deployment)
3. [Manuel Deployment](#manuel-deployment)
4. [Bulut Platformları](#bulut-platformları)
5. [Güvenlik Ayarları](#güvenlik-ayarları)
6. [Performans Optimizasyonu](#performans-optimizasyonu)
7. [Sorun Giderme](#sorun-giderme)

---

## 🚀 Hızlı Başlangıç

### Yerel Geliştirme

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# .env dosyasını oluştur
cp .env.example .env

# Uygulamayı başlat
python run.py
```

Uygulama http://localhost:5000 adresinde çalışacaktır.

### Production (Waitress)

```bash
# Waitress ile production server başlat
python run_production.py
```

---

## 🐳 Docker ile Deployment

### Gereksinimler
- Docker Desktop (Windows/Mac) veya Docker Engine (Linux)
- Docker Compose

### Adım 1: Docker Image Oluştur

```bash
cd YKS2027_WEB
docker build -t yks2027-web:latest .
```

### Adım 2: Docker Compose ile Başlat

```bash
# PostgreSQL ve Redis ile birlikte başlat
docker-compose up -d
```

Bu komut şu servisleri başlatır:
- **db**: PostgreSQL 15 veritabanı
- **redis**: Redis 7 cache sunucusu
- **web**: Flask uygulaması

### Adım 3: Servisleri Kontrol Et

```bash
# Çalışan konteynerları listele
docker-compose ps

# Logları görüntüle
docker-compose logs -f web

# Veritabanına bağlan
docker-compose exec db psql -U yks2027_user -d yks2027
```

### Adım 4: Uygulamaya Eriş

- Uygulama: http://localhost:5000
- Health Check: http://localhost:5000/health

### Docker Compose Komutları

```bash
# Servisleri durdur
docker-compose down

# Verileri silerek durdur (DİKKAT!)
docker-compose down -v

# Yeniden başlat
docker-compose restart

# Logları temizle
docker-compose logs --tail=100
```

---

## 🔧 Manuel Deployment (Linux VPS)

### Adım 1: Sunucu Hazırlığı

```bash
# Ubuntu/Debian sunucuda
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y postgresql postgresql-contrib nginx
sudo apt install -y redis-server
```

### Adım 2: PostgreSQL Kurulumu

```bash
# PostgreSQL'e bağlan
sudo -u postgres psql

# Veritabanı ve kullanıcı oluştur
CREATE DATABASE yks2027;
CREATE USER yks2027_user WITH PASSWORD 'GUVENLI_SIFRE_BURAYA';
GRANT ALL PRIVILEGES ON DATABASE yks2027 TO yks2027_user;
\q
```

### Adım 3: Uygulamayı Yükle

```bash
# Proje dizini oluştur
sudo mkdir -p /opt/yks2027_web
sudo chown $USER:$USER /opt/yks2027_web

# Kodu kopyala (git veya SCP ile)
cd /opt/yks2027_web
git clone <repository-url> .

# Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# Bağımlılıkları yükle
pip install --upgrade pip
pip install -r requirements.txt
```

### Adım 4: Environment Ayarları

```bash
# .env.production dosyasını oluştur
nano .env.production

# Şu ayarları yap:
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=<openssl rand -hex 32 ile üret>
DATABASE_URL=postgresql://yks2027_user:PASSWORD@localhost:5432/yks2027
REDIS_URL=redis://localhost:6379/0
```

### Adım 5: Systemd Service Oluştur

```bash
sudo nano /etc/systemd/system/yks2027.service
```

```ini
[Unit]
Description=YKS2027 WEB Application
After=network.target postgresql.service redis.service

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/opt/yks2027_web
Environment="PATH=/opt/yks2027_web/venv/bin"
ExecStart=/opt/yks2027_web/venv/bin/waitress-serve --host=0.0.0.0 --port=5000 app:create_app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# Servisi etkinleştir
sudo systemctl daemon-reload
sudo systemctl enable yks2027
sudo systemctl start yks2027
sudo systemctl status yks2027
```

### Adım 6: Nginx Reverse Proxy

```bash
sudo nano /etc/nginx/sites-available/yks2027
```

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        
        # Timeouts
        proxy_connect_timeout 120s;
        proxy_send_timeout 120s;
        proxy_read_timeout 120s;
    }

    # Static files
    location /static {
        alias /opt/yks2027_web/app/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Health check
    location /health {
        proxy_pass http://127.0.0.1:5000/health;
        access_log off;
    }
}
```

```bash
# Site'i etkinleştir
sudo ln -s /etc/nginx/sites-available/yks2027 /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Adım 7: SSL Sertifikası (Let's Encrypt)

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

---

## ☁️ Bulut Platformları

### Railway.app (Önerilen - En Kolay)

1. GitHub repository'nizi Railway'e bağlayın
2. PostgreSQL add-on ekleyin
3. Environment variables ayarlayın:
   - `DATABASE_URL` (otomatik eklenir)
   - `SECRET_KEY`
   - `SMTP_USERNAME`
   - `SMTP_PASSWORD`
4. Deploy!

**Avantajlar:**
- Otomatik HTTPS
- Otomatik deployment (git push ile)
- PostgreSQL dahil
- Ücretsiz tier: 500 saat/ay

### Render.com

1. New Web Service oluşturun
2. Repository seçin
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `waitress-serve --host=0.0.0.0 --port=$PORT app:create_app`
5. PostgreSQL database ekleyin

### Heroku

```bash
# Heroku CLI kurulu olmalı
heroku login
heroku create yks2027-web
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY=<your-secret-key>
git push heroku main
heroku open
```

### Google Cloud Run

```bash
# Docker image push
docker build -t gcr.io/PROJECT_ID/yks2027-web .
docker push gcr.io/PROJECT_ID/yks2027-web

# Cloud Run'a deploy
gcloud run deploy yks2027-web \
  --image gcr.io/PROJECT_ID/yks2027-web \
  --platform managed \
  --region europe-west1 \
  --allow-unauthenticated
```

### AWS Elastic Beanstalk

```bash
# EB CLI kur
pip install awsebcli

# Initialize
eb init -p python-3.11 yks2027-web

# Create environment
eb create production

# Deploy
eb deploy
```

---

## 🔒 Güvenlik Ayarları

### 1. SECRET_KEY Güçlendirme

```bash
# Rastgele secret key üret
python -c "import secrets; print(secrets.token_hex(32))"
```

### 2. .env Dosyası Koruması

```bash
# Sadece owner okuyabilsin
chmod 600 .env.production
```

### 3. Database Güvenliği

- Production'da güçlü şifreler kullanın
- Firewall ile DB portunu dışarıya kapatın
- SSL ile bağlantıyı şifreleyin

### 4. HTTPS Zorunlu Kılma

```python
# app/__init__.py içinde
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
```

### 5. Rate Limiting

Zaten aktif - saatte 100 istek ile sınırlı.

---

## ⚡ Performans Optimizasyonu

### 1. Redis Cache

```bash
# Redis kurulumu
sudo apt install redis-server
```

`.env.production` dosyasına ekleyin:
```
REDIS_URL=redis://localhost:6379/0
```

### 2. Database Connection Pool

```python
# config/database_config.py
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
```

### 3. Static File Caching

Nginx config'inde:
```nginx
location /static {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

### 4. Gzip Compression

Nginx config'ine ekleyin:
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
gzip_min_length 1000;
```

### 5. Worker Sayısı

Waitress için:
```bash
# CPU core sayısının 2-4 katı
WAITRESS_THREADS=4
```

---

## 🐛 Sorun Giderme

### Uygulama Başlamıyor

```bash
# Logları kontrol et
journalctl -u yks2027 -f

# Port kullanımda mı?
sudo lsof -i :5000
```

### Database Bağlantı Hatası

```bash
# PostgreSQL çalışıyor mu?
sudo systemctl status postgresql

# Bağlantıyı test et
psql -h localhost -U yks2027_user -d yks2027
```

### Memory Issues

```bash
# Memory kullanımını kontrol et
docker stats
# veya
htop
```

### Nginx 502 Bad Gateway

```bash
# Uygulama çalışıyor mu?
sudo systemctl status yks2027

# Nginx logları
sudo tail -f /var/log/nginx/error.log
```

---

## 📊 Monitoring

### Health Check Endpoint

```bash
# Manuel kontrol
curl http://localhost:5000/health

# Uptime monitoring için
curl -f http://yourdomain.com/health || exit 1
```

### Log Yönetimi

```bash
# Application logs
journalctl -u yks2027 -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Docker logs
docker-compose logs -f web
```

### Sentry Entegrasyonu

`.env.production` dosyasına ekleyin:
```
SENTRY_DSN=https://your-dsn@sentry.io/project-id
```

---

## 🔄 Otomatik Deployment (CI/CD)

GitHub Actions pipeline'ı zaten mevcut:

1. `main` branch'e push yapın
2. Testler otomatik çalışır
3. Docker image build edilir
4. Production server'a deploy edilir

### Gerekli GitHub Secrets

- `PROD_SERVER_HOST`: Sunucu IP adresi
- `PROD_SERVER_USER`: SSH kullanıcı adı
- `PROD_SERVER_SSH_KEY`: SSH private key
- `PROD_SERVER_PORT`: SSH port (genelde 22)

---

## 📞 Destek

Sorularınız için proje dokümantasyonunu inceleyin veya issue açın.

**Son Güncelleme:** 2026-04-09
