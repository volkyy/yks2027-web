"""
YKS2027 WEB - Flask Uygulaması Başlatıcı
TYT ve AYT Hazırlık Takip Sistemi - Web Versiyonu

📌 ÖNEMLİ: Desktop uygulama ile aynı database'i kullanır.
Database path'i config/database_config.py'den yönetilir.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from database.models import Base, User, Subject, Topic

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        # Create tables using Flask-SQLAlchemy
        from database.models import Base
        Base.metadata.create_all(bind=db.engine)
        
        print(f"[INFO] Database tables created successfully")
        
        # Load topics from config using Flask's db
        from config.database_config import DEFAULT_DATABASE_URL
        from database.db_manager import DatabaseManager
        
        # Use the same database URL from Flask config
        db_url = db.engine.url.render_as_string(hide_password=False)
        print(f"[INFO] Database URL: {db_url}")
        
        try:
            db_manager = DatabaseManager(db_url)
            db_manager.load_topics_from_config()
            db_manager.close()
            print(f"[INFO] Konular başarıyla yüklendi")
        except Exception as e:
            print(f"[WARNING] Konu yükleme hatası: {e}")
            print(f"[INFO] Konu yükleme atlanıyor, devam ediliyor...")
        
        # =====================================================
        # MASAÜSTÜ UYGULAMASINDAN TÜM KULLANICILARI AKTAR
        # =====================================================
        print(f"[INFO] Masaüstü kullanıcılar kontrol ediliyor...")
        
        try:
            import sqlite3
            
            # Masaüstü veritabanına bağlan
            desktop_db_path = r"C:\AI PROJECTS\yks2027.db"
            desktop_conn = sqlite3.connect(desktop_db_path)
            desktop_conn.row_factory = sqlite3.Row
            desktop_cursor = desktop_conn.cursor()
            
            # TÜM kullanıcıları al (sadece admin değil!)
            desktop_cursor.execute("SELECT * FROM users")
            all_users = desktop_cursor.fetchall()
            
            if all_users:
                print(f"[INFO] {len(all_users)} kullanıcı bulundu (masaüstü)")
                
                # Web veritabanına aktar
                for user in all_users:
                    # Web DB'de zaten var mı kontrol et
                    existing_user = db.session.query(User).filter_by(username=user['username']).first()
                    
                    if not existing_user:
                        # Yeni kullanıcı oluştur - aynı yetkilerle
                        new_user = User(
                            id=user['id'],
                            username=user['username'],
                            password_hash=user['password_hash'],
                            is_admin=bool(user['is_admin']),  # Yetkiyi koru!
                            alan_secimi=user.get('alan_secimi', 'sayisal'),
                            full_name=user.get('full_name', ''),
                            education_status=user.get('education_status', 'ogrenci'),
                            hedef_bolum=user.get('hedef_bolum', '')
                        )
                        db.session.add(new_user)
                        role = "ADMIN" if user['is_admin'] else "Kullanıcı"
                        print(f"[INFO] {role} '{user['username']}' aktarıldı")
                    else:
                        print(f"[INFO] Kullanıcı '{user['username']}' zaten mevcut")
                
                db.session.commit()
                print(f"[INFO] TÜM kullanıcı aktarımı tamamlandı!")
            else:
                print(f"[INFO] Masaüstü DB'de kullanıcı bulunamadı")
            
            desktop_conn.close()
        except Exception as e:
            print(f"[WARNING] Kullanıcı aktarım hatası: {e}")
            print(f"[INFO] Kullanıcı aktarımı atlanıyor...")
        # =====================================================
        
        # Initialize scheduler for background tasks (email automation, etc.)
        print(f"[INFO] Arka plan görevleri başlatılıyor...")
        # Scheduler will be initialized with proper app context
        # For now, just print info message
        print(f"[INFO] Not: E-posta otomasyonu için .env dosyasında SMTP ayarlarını yapılandırın.")
    
    # Run the app
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    port = int(os.getenv('PORT', 5000))
    
    print(f"")
    print(f"[INFO] YKS2027 WEB başlatılıyor...")
    print(f"[INFO] Sunucu: http://localhost:{port}")
    print(f"[INFO] Debug Mode: {debug}")
    print(f"[INFO] Database: {DEFAULT_DATABASE_URL}")
    print(f"")
    print(f"   Desktop uygulama ile aynı database kullanılıyor.")
    print(f"   Veriler otomatik olarak senkronize edilecek.")
    print(f"")
    print(f"   Arka plan görevleri aktif (e-posta otomasyonu, vb.)")
    print(f"")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
