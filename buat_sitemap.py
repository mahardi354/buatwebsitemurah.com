import os
from datetime import datetime

# Konfigurasi
BASE_URL = "https://buatwebsitemurah.com"
PUBLIC_DIR = "."

def generate_sitemap():
    print(f"🔍 Memindai folder '{PUBLIC_DIR}' untuk mencari file HTML...")
    
    # Pastikan foldernya ada
    if not os.path.exists(PUBLIC_DIR):
        print(f"❌ ERROR: Folder '{PUBLIC_DIR}' tidak ditemukan!")
        return

    # Ambil semua file berakhiran .html
    html_files = [f for f in os.listdir(PUBLIC_DIR) if f.endswith('.html')]
    
    if not html_files:
        print(f"⚠️ Tidak ada file HTML di folder '{PUBLIC_DIR}'. Sitemap batal dibuat.")
        return

    # Siapkan header XML
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    today = datetime.now().strftime("%Y-%m-%d")

    # Looping setiap file untuk dimasukkan ke sitemap
    for file in html_files:
        # Jika file adalah index.html (Homepage), berikan prioritas tertinggi dan URL root
        if file == "index.html":
            url = f"{BASE_URL}/"
            priority = "1.0"
        else:
            url = f"{BASE_URL}/{file}"
            priority = "0.8"

        sitemap_content += f'  <url>\n'
        sitemap_content += f'    <loc>{url}</loc>\n'
        sitemap_content += f'    <lastmod>{today}</lastmod>\n'
        sitemap_content += f'    <changefreq>weekly</changefreq>\n'
        sitemap_content += f'    <priority>{priority}</priority>\n'
        sitemap_content += f'  </url>\n'

    sitemap_content += '</urlset>'

    # Simpan file sitemap.xml langsung ke dalam folder public/
    with open(f"{PUBLIC_DIR}/sitemap.xml", 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print(f"✅ SITEMAP SELESAI! Berhasil mendaftarkan {len(html_files)} URL ke dalam /public/sitemap.xml")

if __name__ == "__main__":
    generate_sitemap()