"""
YKS2027 WEB - Production Başlatıcı Script
Waitress production server ile uygulama başlatma

Kullanım:
    python run_production.py
    
Production ortamı için:
    - Waitress WSGI server kullanılır
    - Çoklu worker desteği
    - Windows ve Linux uyumlu
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from database.models import Base

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    # Production ayarları
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    threads = int(os.getenv('WAITRESS_THREADS', 4))
    
    print("=" * 60)
    print("YKS2027 WEB - Production Server")
    print("=" * 60)
    print(f"Sunucu: http://{host}:{port}")
    print(f"Worker Threads: {threads}")
    print(f"Environment: {os.getenv('FLASK_ENV', 'production')}")
    print(f"Database: {os.getenv('DATABASE_URL', 'sqlite:///yks2027.db')}")
    print("=" * 60)
    print("")
    print("[INFO] Waitress production server başlatılıyor...")
    print("[INFO] Ctrl+C ile durdurabilirsiniz.")
    print("")
    
    # Waitress ile başlat (production-ready WSGI server)
    try:
        from waitress import serve
        serve(
            app,
            host=host,
            port=port,
            threads=threads,
            url_scheme='https' if os.getenv('FLASK_ENV') == 'production' else 'http',
            channel_timeout=120,
            cleanup_interval=30,
            _quiet=False
        )
    except ImportError:
        print("[ERROR] Waitress yüklü değil! Yüklemek için:")
        print("    pip install waitress==3.0.0")
        print("")
        print("[INFO] Geliştirme modunda Flask server başlatılıyor...")
        app.run(host=host, port=port, debug=False)
    except KeyboardInterrupt:
        print("")
        print("[INFO] Sunucu kapatıldı.")
        sys.exit(0)
