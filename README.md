# Kamera-OSINT-Aracı-

Bu Python betiği, Shodan API kullanarak internet üzerindeki açık IP kameralarını tespit eder ve canlı yayınlarını görüntülemeye olanak tanır.

🔥 Özellikler
✅ Shodan API ile açık kameraları tarama
✅ HTTP kameraları tarayıcıda açma
✅ RTSP kameraları OpenCV ile oynatma
✅ Kullanıcı dostu CLI arayüzü

⚠️ Yasal Uyarı
Bu araç etik hackerlar ve siber güvenlik uzmanları için tasarlanmıştır. İzinsiz olarak üçüncü şahısların kameralarına erişmek yasa dışıdır. Kullanımınızdan doğabilecek hukuki sonuçlardan sorumluluk size aittir!

📦 Gereksinimler
Python 3.x
Gerekli kütüphaneler:
pip install requests opencv-python argparse

Shodan API Anahtarı (Almak için: https://www.shodan.io/)

🚀 Kullanım
Komut satırından çalıştırın:
python camera_osint.py --api_key <SHODAN_API_KEY> --location "country:TR"
--api_key: Shodan API anahtarınızı girin.
--location: (Opsiyonel) Arama filtresi ekleyin, örneğin:
country:TR → Sadece Türkiye'deki kameraları gösterir.
city:Istanbul → İstanbul’daki kameraları gösterir.

🛑 Örnek Çalıştırma
python camera_osint.py --api_key "YOUR_SHODAN_API_KEY" --location "country:US"

