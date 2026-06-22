import json
import os
import matplotlib.pyplot as plt
from shapely.geometry import shape

def plot_all_10_geojson():
    print("\n📊 MEMULAI PROSES PLOT GRAFIK GEOMETRI KOORDINAT SPASIAL 2D 📊")
    print("="*70)
    
    for i in range(1, 11):
        geojson_path = f"output/deteksi_objek_{i}.geojson"
        if not os.path.exists(geojson_path):
            continue
            
        with open(geojson_path, 'r') as f:
            data = json.load(f)
            
        if len(data['features']) == 0:
            print(f"⚠️ File ke-{i} kosong, melewati pembuatan plot.")
            continue
            
        fig, ax = plt.subplots(figsize=(6, 6))
        
        for feature in data['features']:
            geom = shape(feature['geometry'])
            kategori = feature['properties']['kategori']
            
            x, y = geom.exterior.xy
            ax.plot(x, y, color='blue', linewidth=1.5)
            ax.fill(x, y, color='cyan', alpha=0.3)
            ax.text(x[0], y[0], kategori, fontsize=8, color='black', weight='bold')
            
        ax.set_title(f"Plot Geometri Spasial AI - Citra Udara {i}")
        ax.grid(True, linestyle='--', alpha=0.5)
        
        path_save_grafik = f"output/plot_grafik_spasial_{i}.png"
        plt.savefig(path_save_grafik, dpi=150)
        plt.close()
        print(f"   ↳ 🖼️ Grafik poligon spasial ke-{i} berhasil disimpan di: {path_save_grafik}")
        
    print("\n✅ SELESAI: Seluruh plot visualisasi geometri laporan siap digunakan!")

if __name__ == "__main__":
    plot_all_10_geojson()