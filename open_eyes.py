import requests
import cv2
import argparse
import webbrowser

def scan_cameras(api_key, location):
    """Shodan API kullanarak açık kameraları tarar."""
    query = f"webcam {location}" if location else "webcam"
    url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={query}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        camera_urls = []
        
        for match in data.get("matches", []):
            ip = match.get("ip_str", "Bilinmiyor")
            port = match.get("port", "Bilinmiyor")
            service = match.get("_shodan", {}).get("module", "unknown")
            
            camera_url = f"http://{ip}:{port}" if service == "http" else f"rtsp://{ip}:{port}"
            camera_urls.append((camera_url, ip, port, service))
        
        return camera_urls
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return []

def play_rtsp_stream(url):
    """RTSP yayını OpenCV ile açar."""
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Kamera yayını açılamadı!")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("RTSP Kamera Yayını", frame)
        if cv2.waitKey(1) == 27:  # ESC tuşuna basıldığında çık
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Kamera OSINT CLI Aracı")
    parser.add_argument("--api_key", required=True, help="Shodan API anahtarı")
    parser.add_argument("--location", default="", help="Bölge (örn: country:TR veya city:Istanbul)")
    args = parser.parse_args()
    
    cameras = scan_cameras(args.api_key, args.location)
    
    if not cameras:
        print("Açık kamera bulunamadı.")
        return
    
    for i, (url, ip, port, service) in enumerate(cameras):
        print(f"[{i}] IP: {ip} - Port: {port} ({service}) - {url}")
    
    choice = input("Bir kamera numarası seçin veya çıkmak için 'q' girin: ")
    if choice.lower() == 'q':
        return
    
    try:
        choice = int(choice)
        if 0 <= choice < len(cameras):
            url, _, _, service = cameras[choice]
            if url.startswith("http"):
                webbrowser.open(url)
            elif url.startswith("rtsp"):
                play_rtsp_stream(url)
        else:
            print("Geçersiz seçim!")
    except ValueError:
        print("Lütfen geçerli bir numara girin.")

if __name__ == "__main__":
    main()
