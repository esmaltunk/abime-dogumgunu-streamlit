import streamlit as st
import random
import time

# --- Tkinter Kodundaki Sabitler ---
MY_NOTE = """canım abim, doğum günün kutlu olsun. Her zaman yanımızda olduğun için teşekkür ederim.💖
iyi ki varsın, iyi ki abimsin
seni çoook seviyorum 💕"""

# --- Streamlit Sayfa Ayarları ---
st.set_page_config(
    page_title="İYİ Kİ DOĞDUN CANIM ABİM 💖",
    page_icon="💌",
    layout="wide"
)

# --- CSS Stil Tanımları ve Kayan Kalplerin Oluşturulması (FloatingHeart sınıfı taklidi) ---

# Kalp animasyonu için renkler
HEART_COLORS = ['#ff6b6b', '#ff9aa2', '#ffb3c6', '#f08fb6', '#ffadc6']

def create_heart_animations():
    """Tkinter'daki FloatingHeart sınıfını taklit eden HTML/CSS oluşturur."""
    heart_html = ""
    # Tkinter'daki HEART_COUNT=60'ı taklit etmek için 60 kalp oluşturuyoruz.
    for i in range(60):
        x = random.uniform(5, 95) # Başlangıç yatay konumu
        size = random.uniform(20, 48) # Tkinter'daki boyut aralığı
        color = random.choice(HEART_COLORS)
        duration = random.uniform(10, 25) # Hız (daha yavaş veya daha hızlı uçuş)
        delay = random.uniform(0, 15) # Animasyon gecikmesi (aynı anda başlamamaları için)
        
        # Her kalbe rastgele değerler atıyoruz
        heart_html += f"""
        <div class="heart" style="
            left: {x}%; 
            font-size: {size}px; 
            color: {color}; 
            animation-duration: {duration}s;
            animation-delay: {delay}s;">
        ❤</div>
        """
    
    # Genel CSS stilleri (Tek bir HTML bloğu içinde)
    css_styles = f"""
    <style>
        /* Tkinter pencere arka planı: #fff7fb */
        .stApp {{
            background-color: #fff7fb;
            font-family: Arial, sans-serif;
        }}
        /* Kayan Kalplerin Arka Planı */
        .heart-bg {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1; 
            overflow: hidden;
        }}
        /* Tek bir kalp stili */
        .heart {{
            position: absolute;
            animation-name: floatUp;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
            transform: translateY(100vh); /* Pencere altından başla */
            opacity: 0.8;
            filter: drop-shadow(0 0 1px rgba(0,0,0,0.2));
        }}
        /* Kalbin uçuş animasyonu */
        @keyframes floatUp {{
            0% {{ transform: translateY(100vh); opacity: 0.8; }}
            100% {{ transform: translateY(-50vh); opacity: 0; }} /* Pencere üstünden çok yukarıya çık */
        }}
        
        /* Başlık Stili (Tkinter'daki gibi ortalı ve italik) */
        .birthday-title {{
            text-align: center;
            font-style: italic;
            font-weight: bold;
            font-size: 32px; /* Tkinter'daki boyutu taklit etmek için */
            color: #b33;
            margin-top: 50px;
            margin-bottom: 30px;
        }}
        /* Zarf Stili */
        .envelope-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 250px;
        }}
        .envelope-box {{
            position: relative;
            width: 200px;
            height: 140px;
            background-color: #fff;
            border: 2px solid #bbb;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            cursor: pointer;
        }}
        .flap {{
            position: absolute;
            top: -10px;
            left: 0;
            width: 100%;
            height: 80px;
            background-color: #f2dede;
            border-bottom: 2px solid #e0bcbc;
            clip-path: polygon(0% 100%, 50% 0%, 100% 100%);
            transition: transform 0.4s ease-out, background-color 0.4s ease-out;
            z-index: 10;
        }}
        /* Açılmış Zarf Durumu */
        .opened .flap {{
            transform: translateY(-25px); /* Kapak kalkar */
            background-color: #ffffff;
        }}
        
        /* Mesaj Kağıdı Stili */
        .note-paper {{
            background-color: #fffdf5;
            border: 2px solid #d8d2c4;
            padding: 40px 20px;
            border-radius: 8px;
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
            font-size: 14px;
            color: #3b2f2f;
            margin-top: 30px;
            line-height: 1.6;
            white-space: pre-wrap;
            width: 300px;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            opacity: 0;
            transform: translateY(50px);
            transition: opacity 0.7s ease-out 0.3s, transform 0.7s ease-out 0.3s; /* Gecikmeli kaydırma efekti */
        }}
        .opened .note-paper {{
            opacity: 1;
            transform: translateY(0);
        }}
    </style>
    """
    return css_styles + f'<div class="heart-bg">{heart_html}</div>'

# Kalp animasyonlarını ve genel CSS'i ekle
st.markdown(create_heart_animations(), unsafe_allow_html=True)

# --- State Yönetimi ---
if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- Başlık ---
st.markdown("<h2 class='birthday-title'>İYİ Kİ DOĞDUN CANIM ABİM 💖</h2>", unsafe_allow_html=True)
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)


# --- Zarf Bölümü (Ortalanmış) ---
# Ortalamak için sütunları kullan
col1, col_center, col3 = st.columns([1, 2, 1])

with col_center:
    
    # Zarfın CSS durumunu belirle
    envelope_class = 'opened' if st.session_state.opened else ''
    
    # Butona tıklanma fonksiyonu
    def open_envelope():
        st.session_state.opened = True

    # Zarfın kendisi bir Streamlit butonu olamaz, bu yüzden altındaki butonu kullanıyoruz
    st.markdown(f"""
    <div class="envelope-container">
        <div class="envelope-box {envelope_class}" onclick="document.getElementById('open_btn_streamlit').click()">
            <div class="flap"></div>
            <p style="text-align:center; position:absolute; top:40%; left:0; width:100%; font-size:12px; z-index:11; user-select:none;">
                Tıklamak için butonu kullanın
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Gizli (veya görünen) Streamlit butonu
    st.button("💌 Zarfa Tıkla", key="open_btn_streamlit", on_click=open_envelope)


# --- Mesaj ve Konfeti (Zarf Açıldıktan Sonra) ---
if st.session_state.opened:
    
    # 1. Konfeti Efekti (Tkinter'daki Confetti.animate() taklidi)
    st.balloons() 
    
    # Emoji Konfeti (Tkinter'daki parça çeşitliliğini yansıtmak için)
    confetti_emojis = ''.join(random.choices(["🎉", "✨", "💛", "💚", "💙", "💖", "🎁"], k=100))
    st.markdown(f"<p style='text-align:center; font-size:32px;'>{confetti_emojis}</p>", unsafe_allow_html=True)

    # 2. Mesaj Kağıdı (Tkinter'daki show_note_paper() taklidi)
    st.markdown(f"""
    <div class="note-paper">
        {MY_NOTE.strip()}
    </div>
    """, unsafe_allow_html=True)
    
    # 3. İkinci Konfeti (Efektin sürmesi için)
    st.snow()
