import pandas as pd
import random

def generate_visual_data():
    """
    Menjana data simulasi trend keperluan industri untuk tempoh 5 tahun akan datang.
    Data ini digunakan oleh Plotly Express di dalam App.py.
    """
    # Menukar label masa daripada bulanan (Jan, Feb...) kepada tahun jangkaan masa depan
    years = ["Tahun 1", "Tahun 2", "Tahun 3", "Tahun 4", "Tahun 5"]
    
    # Menjana data simulasi peratusan keperluan pasaran kerja (antara 60% hingga 95%)
    # Kita susun secara menaik sedikit demi sedikit untuk memberi visual "Trend Meningkat"
    demand_growth = [
        random.randint(60, 70),
        random.randint(68, 78),
        random.randint(75, 85),
        random.randint(80, 90),
        random.randint(88, 98)
    ]
    
    # Bina DataFrame dengan nama kolum yang sepadan dengan kod di App.py
    # NOTA: Kekalkan nama kolum 'Bulan' dan 'Minat Pasaran' supaya anda TIDAK PERLU 
    # mengubah kod Plotly di dalam App.py (Kekal selamat & tiada error).
    data = {
        'Bulan': years,              # Mewakili paksi X (Timeline)
        'Minat Pasaran': demand_growth # Mewakili paksi Y (Keperluan Industri %)
    }
    
    return pd.DataFrame(data)