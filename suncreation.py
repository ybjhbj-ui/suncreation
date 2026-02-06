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
# 🎨 DESIGN LUXE + AFFICHAGE HAUT (MOBILE)
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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Montserrat:wght@300;400;600&display=swap');
header, [data-testid="stHeader"], footer, [data-testid="stFooter"], #MainMenu {{ display: none !important; }}
.stApp {{ background-color: {THEME['bg_color']} !important; }}

/* Style du titre principal Sun Creation */
.main-title {{
    font-family: 'Playfair Display', serif !important;
    color: {THEME['text_color']} !important;
    text-align: center;
    font-size: 3.5rem !important;
    font-weight: 800;
    margin-bottom: 0px;
    letter-spacing: -1px;
}}

h1, h2, h3 {{ font-family: 'Playfair Display', serif !important; color: {THEME['text_color']} !important; }}
.stMarkdown, p, label, .stRadio label, .stSelectbox label, .stCheckbox label, .stMultiSelect label {{
    font-family: 'Montserrat', sans-serif !important; color: #2D1E12 !important; font-weight: 600 !important;
}}

/* Style de base des champs */
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, .stDateInput div, textarea {{
    background-color: #4A3728 !important; border: 1px solid #D4AF37 !important; border-radius: 8px !important;
    transition: all 0.3s ease;
}}

/* Effet GLOW doré quand on clique dans une case */
div[data-baseweb="select"] > div:focus-within,
div[data-baseweb="input"] > div:focus-within,
.stDateInput div:focus-within,
textarea:focus {{
    border-color: #FFD700 !important;
    box-shadow: 0 0 12px #D4AF37, 0 0 20px #FFD700 !important;
}}

input, .stSelectbox div div, textarea {{
    color: white !important; -webkit-text-fill-color: white !important; caret-color: white !important; font-weight: 500 !important;
}}
::placeholder {{ color: #D7CCC8 !important; opacity: 0.7; }}
[data-testid="stSidebar"] {{ display: none; }}
button[kind="primary"], .stButton > button {{
    background-color: {THEME['main_color']} !important; color: white !important; border-radius: 50px !important; font-weight: bold !important;
}}
</style>
""", unsafe_allow_html=True)

if EFFET_SPECIAL == "snow": st.snow()

# --- ⚙️ SECRETS & TÉLÉCOMMANDE ---
MDP_DE_SECOURS = "SunCreation-Ultra-Secure-2026-!!#"
SECRET_PASSWORD = st.secrets.get("ADMIN_PASSWORD", MDP_DE_SECOURS)
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
ACCESSOIRES_BOUQUET = {"🎗️ Bande avec un prénom (+15€)": 15, "💌 Carte + Enveloppe (+5€)": 5, "🦋 Papillon (+2€)": 2, "🎀 Noeud Papillon (+2€)": 2, "✨ Diamants (+2€)": 2, "🏷️ Sticker (+10€)": 10, "👑 Couronne (+10€)": 10, "🧸 Peluche (+3€)": 3, "📸 Photo (+5€)": 5, "💡 LED (+5€)": 5, "🍫 Ferrero (+1€)": 1, "🅰️ Initiale (+3€)": 3}
ACCESSOIRES_BOX_CHOCO = {"🅰️ Initiale (+5€)": 5, "🧸 Doudou (+3.50€)": 3.5, "🧸🧸 2 Doudous (+7€)": 7, "🎗️ Bande personnalisée (+10€)": 10, "🎂 Topper (+2€)": 2}
LIVRAISON_OPTIONS = {"📍 Retrait Gonesse": 0, "📦 Colis IDF - 12€": 12, "📦 Colis France - 12€": 12, "🌍 Hors France - 15€": 15, "🚗 Uber / Chauffeur (À VOTRE CHARGE)": 0}

# =========================================================
# 🏠 EN-TÊTE (HEADER) - TITRE EN HAUT + LOGO
# =========================================================
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
    st.header("🌹 Configurer mon Bouquet")
    col1, col2 = st.columns(2)
    with col1:
        taille = st.selectbox("Nombre de roses", list(PRIX_ROSES.keys()), format_func=lambda x: f"{x} Roses ({PRIX_ROSES[x]}€)")
        prix_base = PRIX_ROSES[taille]
    with col2:
        try: st.image(f"bouquet_{taille}.jpg", use_container_width=True)
        except: st.caption("📷 (Image)")
        
    # MODIF: st.pills au lieu de selectbox/multiselect pour éviter le clavier
    couleur_rose = st.pills("Couleur des roses", COULEURS_ROSES, selection_mode="single")
    if not couleur_rose: couleur_rose = "Non défini"
    
    choix_emballage = st.pills("Style d'emballage", ["Noir", "Blanc", "Rose", "Rouge", "Bordeaux", "Vert", "Bleu", "Crème", "Dior Noir (+5€)", "Dior Rose (+5€)", "Chanel (+5€)", "LV (+5€)"], selection_mode="single")
    if not choix_emballage: choix_emballage = "Noir"
    
    prix_papier = 5 if "(+5€)" in choix_emballage else 0
    
    options_choisies = st.pills("Ajouter des éléments :", list(ACCESSOIRES_BOUQUET.keys()), selection_mode="multi")
    if not options_choisies: options_choisies = []
    
    details_sup = ""
    if "🎗️ Bande avec un prénom (+15€)" in options_choisies:
        txt = st.text_input("📝 Prénom pour la bande :")
        details_sup += f"\n   -> Prénom bande : {txt}"
    if "💌 Carte + Enveloppe (+5€)" in options_choisies:
        txt = st.text_area("📝 Votre message pour la carte :")
        details_sup += f"\n   -> Message carte : {txt}"
    if "🅰️ Initiale (+3€)" in options_choisies:
        txt = st.text_input("📝 Quelle initiale ?")
        details_sup += f"\n   -> Initiale : {txt}"
    prix_total = prix_base + prix_papier + sum(ACCESSOIRES_BOUQUET[o] for o in options_choisies)
    details_produit_mail = f"BOUQUET : {taille} roses\n- Couleur : {couleur_rose}\n- Emballage : {choix_emballage}"
    details_options_mail = ", ".join(options_choisies) + details_sup

# --- PARTIE 2 : BOX CHOCOLAT ---
elif choix == "🍫 Box Chocolat":
    st.header("🍫 Ma Box Chocolat")
    col1, col2 = st.columns(2)
    with col1:
        taille_box = st.selectbox("Quelle taille ?", list(PRIX_BOX_CHOCO.keys()), format_func=lambda x: f"Taille {x} ({PRIX_BOX_CHOCO[x]}€)")
        prix_base = PRIX_BOX_CHOCO[taille_box]
    with col2:
        try: st.image(f"box_{taille_box.lower()}.jpg", use_container_width=True)
        except: st.caption("📷 (Image)")
        
    liste_chocolats = st.pills("Choisissez les chocolats :", ["Kinder Bueno", "Ferrero Rocher", "Milka", "Raffaello", "Schoko-Bons"], selection_mode="multi")
    if not liste_chocolats: liste_chocolats = []
    
    fleur_eternelle = st.checkbox("Ajouter des Roses Éternelles ?")
    couleur_fleur_info = st.pills("Couleur des roses :", COULEURS_ROSES, selection_mode="single") if fleur_eternelle else ""
    
    options_choisies = st.pills("Ajouter des options :", list(ACCESSOIRES_BOX_CHOCO.keys()), selection_mode="multi")
    if not options_choisies: options_choisies = []
    
    details_sup = ""
    if "🅰️ Initiale (+5€)" in options_choisies:
        txt = st.text_input("📝 Quelle initiale ?")
        details_sup += f"\n   -> Initiale : {txt}"
    if "🎗️ Bande personnalisée (+10€)" in options_choisies:
        txt = st.text_input("📝 Texte pour la bande :")
        details_sup += f"\n   -> Bande : {txt}"
    prix_total = prix_base + sum(ACCESSOIRES_BOX_CHOCO[o] for o in options_choisies)
    txt_fleurs = f"Roses Éternelles ({couleur_fleur_info})" if fleur_eternelle else "Pas de fleurs"
    details_produit_mail = f"BOX CHOCOLAT : {taille_box}\n- Chocolats : {', '.join(liste_chocolats)}\n- Fleurs : {txt_fleurs}"
    details_options_mail = ", ".join(options_choisies) + details_sup

# --- PARTIE 3 : BOX LOVE ---
else:
    st.header("❤️ Box Love Signature")
    try: st.image("box_love.jpg", use_container_width=True)
    except: pass
    
    couleur_love = st.pills("Couleur des fleurs", COULEURS_ROSES, selection_mode="single")
    if not couleur_love: couleur_love = "Non défini"
    
    liste_chocolats = st.pills("Quels chocolats ?", ["Kinder Bueno", "Ferrero Rocher"], selection_mode="multi")
    if not liste_chocolats: liste_chocolats = []
    
    prix_total = PRIX_BOX_FIXE[choix]
    details_produit_mail = f"BOX LOVE (I ❤️ U)\n- Fleurs : {couleur_love}\n- Chocolats : {', '.join(liste_chocolats)}"
    details_options_mail = "Aucune option sup."

# --- LIVRAISON ---
st.markdown("---")
st.subheader("🚚 Livraison")
mode_livraison = st.selectbox("Mode de réception", list(LIVRAISON_OPTIONS.keys()))
frais_port = LIVRAISON_OPTIONS[mode_livraison]

adresse_complete = ""
if mode_livraison != "📍 Retrait Gonesse":
    if "Hors France" in mode_livraison:
        pays = st.text_input("🌍 Pays de destination")
        rue = st.text_input("Adresse (Rue, Ville, CP)")
        adresse_complete = f"{rue} | PAYS : {pays}"
    else:
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
__________________________________

👤 INFOS CLIENT
• Nom : {nom}
• Instagram : {inst}
• Tél : {tel}

📦 COMMANDE
• Produit : {choix}
{details_produit_mail}

➕ OPTIONS & PERSONNALISATION
{details_options_mail if details_options_mail else "Aucune option."}

🚚 RÉCEPTION
• Mode : {mode_livraison}
• Adresse : {adresse_complete if adresse_complete else 'Retrait place (Gonesse)'}

💰 PAIEMENT
• TOTAL À RÉGLER : {total_final} €
• 🔒 ACOMPTE À VERSER (40%) : {acompte:.2f} €
__________________________________"""
        st.markdown(f'<a href="{creer_lien_email(f"Commande {nom}", msg)}" style="background-color:{THEME["main_color"]}; color:white; padding:15px; display:block; text-align:center; border-radius:50px; font-weight:bold; text-decoration:none;">📨 ENVOYER LA COMMANDE</a>', unsafe_allow_html=True)
    else:
        st.error("Merci de remplir Nom, Téléphone et Instagram pour valider.")
