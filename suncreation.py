import streamlit as st
from datetime import date
from urllib.parse import quote

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Sun Creation - Devis", page_icon="🌹", layout="centered")

# ==========================================
# 🧠 OPTIONS INTELLIGENTES (SAISONS)
# ==========================================
aujourdhui = date.today()
THEME = {"nom": "Standard", "bg_color": "#FDF8F5", "main_color": "#D4AF37", "text_color": "#5D4037", "icon": "🌹"}
EFFET_SPECIAL = None

if aujourdhui.month == 2 and 1 <= aujourdhui.day <= 15:
    THEME = {"nom": "Saint-Valentin", "bg_color": "#FFF0F5", "main_color": "#E91E63", "text_color": "#880E4F", "icon": "💖"}
    EFFET_SPECIAL = "hearts"
elif aujourdhui.month == 12:
    THEME = {"nom": "Noël", "bg_color": "#F5FFFA", "main_color": "#C0392B", "text_color": "#145A32", "icon": "🎄"}
    EFFET_SPECIAL = "snow"

# ==========================================
# 🎨 DESIGN LUXE + VISIBILITÉ TOTALE (FORCÉE)
# ==========================================
css_hearts = ""
if EFFET_SPECIAL == "hearts":
    css_hearts = """
    <div class="hearts-container">
        <div class="heart">❤️</div><div class="heart">💖</div><div class="heart">❤️</div>
    </div>
    <style>
    .hearts-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
    .heart { position: absolute; top: -10%; font-size: 20px; animation: heartRain 10s linear infinite; opacity: 0; }
    .heart:nth-child(1) { left: 10%; animation-delay: 0s; } .heart:nth-child(2) { left: 50%; animation-delay: 4s; } .heart:nth-child(3) { left: 85%; animation-delay: 8s; }
    @keyframes heartRain { 0% { opacity: 0; } 10% { opacity: 0.5; } 100% { transform: translateY(110vh); opacity: 0; } }
    </style>
    """

st.markdown(f"""
{css_hearts}
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Montserrat:wght@400;700;800&display=swap');
header, [data-testid="stHeader"], footer, [data-testid="stFooter"], #MainMenu {{ display: none !important; }}
.stApp {{ background-color: {THEME['bg_color']} !important; }}

.main-title {{
    font-family: 'Playfair Display', serif !important;
    color: {THEME['text_color']} !important;
    text-align: center;
    font-size: 3rem !important;
    font-weight: 800;
    margin-bottom: 0px;
}}

/* --- FORCE LA VISIBILITÉ DES BOUTONS (PILLS) --- */
/* État normal (Non cliqué) : Fond Blanc + Texte Noir/Marron */
[data-testid="stPills"] button {{
    background-color: #FFFFFF !important;
    border: 2px solid #D4AF37 !important;
    padding: 10px 15px !important;
    transition: all 0.2s ease-in-out;
}}

[data-testid="stPills"] button p {{
    color: #2D1E12 !important; /* Marron Noir très lisible */
    -webkit-text-fill-color: #2D1E12 !important;
    font-weight: 800 !important;
    font-size: 1.1rem !important;
}}

/* État Sélectionné (Cliqué) : Fond Rose Poudré + Bordure Or */
[data-testid="stPills"] button[aria-checked="true"] {{
    background-color: #FFF0F5 !important;
    border: 3px solid #D4AF37 !important;
    box-shadow: 0 0 10px rgba(212, 175, 55, 0.4) !important;
}}

h1, h2, h3 {{ font-family: 'Playfair Display', serif !important; color: {THEME['text_color']} !important; }}
.stMarkdown, p, label {{
    font-family: 'Montserrat', sans-serif !important; color: #2D1E12 !important; font-weight: 700 !important;
}}

/* Champs de saisie reste marron pour le contraste du texte blanc */
div[data-baseweb="input"] > div, textarea {{
    background-color: #4A3728 !important; border: 1px solid #D4AF37 !important; border-radius: 8px !important;
}}
input, textarea {{ color: white !important; -webkit-text-fill-color: white !important; }}
::placeholder {{ color: #D7CCC8 !important; opacity: 0.7; }}

button[kind="primary"], .stButton > button {{
    background-color: {THEME['main_color']} !important; color: white !important; border-radius: 50px !important; font-weight: bold !important;
}}
</style>
""", unsafe_allow_html=True)

# --- ⚙️ SECRETS ---
EMAIL_PRO = st.secrets.get("EMAIL_RECEPTION", "sncreat24@gmail.com")
ETAT_VACANCES_GLOBAL = st.secrets.get("MODE_VACANCES", "NON") 

if ETAT_VACANCES_GLOBAL == "OUI":
    st.error("🏖️ **FERMETURE EXCEPTIONNELLE**\n\nSun Creation prend quelques jours de repos. À très bientôt !")
    st.stop()

def creer_lien_email(sujet, corps): return f"mailto:{EMAIL_PRO}?subject={quote(sujet)}&body={quote(corps)}"

# --- DONNÉES ---
PRIX_BOX_FIXE = {"❤️ Box Love (I ❤️ U)": 50}
PRIX_BOX_CHOCO = {"20cm": 53, "30cm": 70}
PRIX_ROSES = {7: 20, 10: 25, 15: 30, 20: 35, 25: 40, 30: 45, 35: 50, 40: 55, 45: 60, 50: 65, 55: 70, 60: 75, 65: 80, 70: 90, 75: 95, 80: 100, 85: 105, 90: 110, 95: 115, 100: 120}
COULEURS_ROSES = ["Noir 🖤", "Blanc 🤍", "Rouge ❤️", "Rose 🌸", "Bleu Clair ❄️", "Bleu Foncé 🦋", "Violet 💜"]
ACCESSOIRES_BOUQUET = {"🎗️ Bande (+15€)": 15, "💌 Carte (+5€)": 5, "🦋 Papillon (+2€)": 2, "🎀 Noeud (+2€)": 2, "✨ Diamants (+2€)": 2, "🏷️ Sticker (+10€)": 10, "👑 Couronne (+10€)": 10, "🧸 Peluche (+3€)": 3, "📸 Photo (+5€)": 5, "💡 LED (+5€)": 5, "🍫 Ferrero (+1€)": 1, "🅰️ Initiale (+3€)": 3}
ACCESSOIRES_BOX_CHOCO = {"🅰️ Initiale (+5€)": 5, "🧸 Doudou (+3.50€)": 3.5, "🎗️ Bande (+10€)": 10, "🎂 Topper (+2€)": 2}
LIVRAISON_OPTIONS = {"📍 Retrait Gonesse": 0, "📦 Colis IDF - 12€": 12, "📦 Colis France - 12€": 12, "🌍 Hors France - 15€": 15, "🚗 Uber (À CHARGE)": 0}

# --- HEADER ---
st.markdown('<p class="main-title">Sun Creation</p>', unsafe_allow_html=True)
col_logo_l, col_logo_c, col_logo_r = st.columns([1, 1.5, 1])
with col_logo_c:
    try: st.image("logo.jpg", use_container_width=True)
    except: st.markdown("<h2 style='text-align: center;'>🌹</h2>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
choix = st.radio("Je souhaite commander :", ["🌹 Un Bouquet", "🍫 Box Chocolat", "❤️ Box Love (I ❤️ U)"])
st.markdown("---")

details_produit_mail = ""
details_options_mail = ""

# --- PARTIE 1 : BOUQUET ---
if choix == "🌹 Un Bouquet":
    st.header("🌹 Mon Bouquet")
    taille = st.pills("Nombre de roses", list(PRIX_ROSES.keys()), format_func=lambda x: f"{x} Roses", selection_mode="single")
    if not taille: taille = 7
    prix_base = PRIX_ROSES[taille]
    try: st.image(f"bouquet_{taille}.jpg", use_container_width=True)
    except: st.caption("📷 (Image)")
    couleur_rose = st.pills("Couleur des roses", COULEURS_ROSES, selection_mode="single")
    choix_emballage = st.pills("Style d'emballage", ["Noir", "Blanc", "Rose", "Rouge", "Bordeaux", "Bleu", "Dior (+5€)", "Chanel (+5€)"], selection_mode="single")
    prix_papier = 5 if "(+5€)" in str(choix_emballage) else 0
    options_choisies = st.pills("Options :", list(ACCESSOIRES_BOUQUET.keys()), selection_mode="multi")
    if not options_choisies: options_choisies = []
    prix_total = prix_base + prix_papier + sum(ACCESSOIRES_BOUQUET[o] for o in options_choisies)
    details_produit_mail = f"BOUQUET : {taille} roses\n- Couleur : {couleur_rose}\n- Emballage : {choix_emballage}"
    details_options_mail = ", ".join(options_choisies)

# --- PARTIE 2 : BOX CHOCOLAT ---
elif choix == "🍫 Box Chocolat":
    st.header("🍫 Ma Box Chocolat")
    taille_box = st.pills("Taille :", list(PRIX_BOX_CHOCO.keys()), selection_mode="single")
    if not taille_box: taille_box = "20cm"
    prix_base = PRIX_BOX_CHOCO[taille_box]
    try: st.image(f"box_{taille_box.lower()}.jpg", use_container_width=True)
    except: st.caption("📷 (Image)")
    liste_chocolats = st.pills("Chocolats :", ["Kinder Bueno", "Ferrero Rocher", "Milka", "Raffaello", "Schoko-Bons"], selection_mode="multi")
    fleur_eternelle = st.checkbox("Ajouter des Roses Éternelles ?")
    couleur_fleur_info = st.pills("Couleur roses :", COULEURS_ROSES, selection_mode="single") if fleur_eternelle else ""
    options_choisies = st.pills("Options :", list(ACCESSOIRES_BOX_CHOCO.keys()), selection_mode="multi")
    if not options_choisies: options_choisies = []
    prix_total = prix_base + sum(ACCESSOIRES_BOX_CHOCO[o] for o in options_choisies)
    details_produit_mail = f"BOX CHOCOLAT : {taille_box}\n- Chocolats : {', '.join(liste_chocolats if liste_chocolats else [])}\n- Fleurs : {couleur_fleur_info}"
    details_options_mail = ", ".join(options_choisies)

# --- PARTIE 3 : BOX LOVE ---
else:
    st.header("❤️ Box Love Signature")
    try: st.image("box_love.jpg", use_container_width=True)
    except: pass
    couleur_love = st.pills("Couleur des fleurs", COULEURS_ROSES, selection_mode="single")
    liste_chocolats = st.pills("Chocolats :", ["Kinder Bueno", "Ferrero Rocher"], selection_mode="multi")
    prix_total = PRIX_BOX_FIXE[choix]
    details_produit_mail = f"BOX LOVE\n- Fleurs : {couleur_love}\n- Chocolats : {liste_chocolats}"
    details_options_mail = "Standard"

# --- LIVRAISON & INFOS ---
st.markdown("---")
st.subheader("🚚 Livraison & Client")
mode_livraison = st.selectbox("Mode de réception", list(LIVRAISON_OPTIONS.keys()))
frais_port = LIVRAISON_OPTIONS[mode_livraison]

adresse_complete = ""
if mode_livraison != "📍 Retrait Gonesse":
    rue = st.text_input("Adresse (Rue, Ville, CP)")
    adresse_complete = f"{rue}"

nom = st.text_input("Votre Nom & Prénom")
tel = st.text_input("📞 Téléphone (Indispensable)")
inst = st.text_input("Votre Instagram")

total_final = prix_total + frais_port
acompte = total_final * 0.40

st.markdown(f"""
<div style="background-color:white; padding:20px; border-radius:15px; text-align:center; border: 1px solid #E7D8D0;">
    <h3 style="margin:0; color:{THEME['text_color']};">Total : {total_final} €</h3>
    <div style="background-color:{THEME['main_color']}; color:white; padding:10px 20px; border-radius:50px; margin-top:10px; font-weight:bold;">
        🔒 Acompte requis : {acompte:.2f} €
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("✅ VALIDER MA COMMANDE", type="primary", use_container_width=True):
    if nom and inst and tel:
        msg = f"""✨ NOUVELLE COMMANDE SUN CREATION ✨
👤 CLIENT : {nom}
📱 TEL : {tel}
📸 INSTA : {inst}
📦 PRODUIT : {choix}
{details_produit_mail}
➕ OPTIONS : {details_options_mail}
🚚 LIVRAISON : {mode_livraison} ({adresse_complete})
💰 TOTAL : {total_final}€
🔒 ACOMPTE (40%) : {acompte:.2f}€"""
        st.markdown(f'<a href="{creer_lien_email(f"Commande {nom}", msg)}" style="background-color:{THEME["main_color"]}; color:white; padding:15px; display:block; text-align:center; border-radius:50px; font-weight:bold; text-decoration:none;">📨 ENVOYER LA COMMANDE</a>', unsafe_allow_html=True)
    else:
        st.error("Merci de remplir Nom Téléphone et Instagram pour valider.")
