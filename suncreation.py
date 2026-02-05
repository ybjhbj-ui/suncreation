import streamlit as st
from datetime import date, timedelta
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
# 🎨 DESIGN LUXE + ADMIN INVISIBLE
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
h1, h2, h3, [data-testid="stSidebar"] h1 {{ font-family: 'Playfair Display', serif !important; color: {THEME['text_color']} !important; }}
.stMarkdown, p, label, .stRadio label, .stSelectbox label, .stCheckbox label, .stMultiSelect label {{
    font-family: 'Montserrat', sans-serif !important; color: #2D1E12 !important; font-weight: 600 !important;
}}
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, .stDateInput div, textarea {{
    background-color: #4A3728 !important; border: 1px solid #D4AF37 !important; border-radius: 8px !important;
}}
input, .stSelectbox div div, textarea {{
    color: white !important; -webkit-text-fill-color: white !important; caret-color: white !important; font-weight: 500 !important;
}}
::placeholder {{ color: #D7CCC8 !important; opacity: 0.7; }}
[data-testid="stSidebar"] {{ background-color: #F8F0EB !important; border-right: 1px solid #E7D8D0; }}
button[kind="primary"], .stButton > button {{
    background-color: {THEME['main_color']} !important; color: white !important; border-radius: 50px !important; font-weight: bold !important;
}}
</style>
""", unsafe_allow_html=True)

if EFFET_SPECIAL == "snow": st.snow()

# --- ⚙️ RÉCUPÉRATION DES SECRETS (SÉCURISÉ) ---
# Si le secret n'existe pas, on met une valeur par défaut pour éviter que le site plante
MDP_DE_SECOURS = "SunCreation-Ultra-Secure-2026-!!#"
SECRET_PASSWORD = st.secrets.get("ADMIN_PASSWORD", MDP_DE_SECOURS)
EMAIL_PRO = st.secrets.get("EMAIL_RECEPTION", "sncreat24@gmail.com") # <- SÉCURISÉ ICI

def creer_lien_email(sujet, corps): return f"mailto:{EMAIL_PRO}?subject={quote(sujet)}&body={quote(corps)}"

# --- DONNÉES ---
PRIX_BOX_FIXE = {"❤️ Box Love (I ❤️ U)": 50}
PRIX_BOX_CHOCO = {"20cm": 53, "30cm": 70}
PRIX_ROSES = {7: 20, 10: 25, 15: 30, 20: 35, 25: 40, 30: 45, 35: 50, 40: 55, 45: 60, 50: 65, 55: 70, 60: 75, 65: 80, 70: 90, 75: 95, 80: 100, 85: 105, 90: 110, 95: 115, 100: 120}
COULEURS_ROSES = ["Rouge ❤️", "Blanc 🤍", "Rose Poudré 🌸", "Fuchsia 💗", "Noir 🖤", "Bleu Roi 💙", "Or (Gold) ✨", "Argent (Silver) 💍", "Mix"]
ACCESSOIRES_BOUQUET = {"🎗️ Bande avec un prénom (+15€)": 15, "💌 Carte + Enveloppe (+5€)": 5, "🦋 Papillon (+2€)": 2, "🎀 Noeud Papillon (+2€)": 2, "✨ Diamants (+2€)": 2, "🏷️ Sticker (+10€)": 10, "👑 Couronne (+10€)": 10, "🧸 Peluche (+3€)": 3, "📸 Photo (+5€)": 5, "💡 LED (+5€)": 5, "🍫 Ferrero (+1€)": 1, "🅰️ Initiale (+3€)": 3}
ACCESSOIRES_BOX_CHOCO = {"🅰️ Initiale (+5€)": 5, "🧸 Doudou (+3.50€)": 3.5, "🧸🧸 2 Doudous (+7€)": 7, "🎗️ Bande personnalisée (+10€)": 10, "🎂 Topper (+2€)": 2}
LIVRAISON_OPTIONS = {"📍 Retrait Gonesse": 0, "📦 Colis IDF - 12€": 12, "📦 Colis France - 12€": 12, "🌍 Hors France - 15€": 15, "🚗 Uber / Chauffeur (À VOTRE CHARGE)": 0}

# --- SIDEBAR + ADMIN INVISIBLE ---
with st.sidebar:
    try: st.image("logo.jpg", width=250)
    except: st.write("🌹 **Sun Creation**")
    st.title("Sun Creation")
    if THEME['nom'] != "Standard": st.markdown(f"<p style='color:{THEME['main_color']};font-weight:bold;'>✨ {THEME['nom']}</p>", unsafe_allow_html=True)
    choix = st.radio("Je souhaite commander :", ["🌹 Un Bouquet", "🍫 Box Chocolat", "❤️ Box Love (I ❤️ U)"])
    st.markdown("---")
    
    # --- LOGIQUE ADMIN FANTÔME ---
    params = st.query_params
    en_vacances = False
    if params.get("admin") == "oui":
        with st.expander("⚙️ Configuration Secrète"):
            input_pwd = st.text_input("Code de sécurité", type="password")
            if input_pwd == SECRET_PASSWORD: 
                st.success("Accès Direction")
                en_vacances = st.checkbox("🔴 Activer Mode Vacances")
            elif input_pwd: st.error("Code erroné")
    
    st.warning("💳 **Acompte 40% requis**")

# --- BLOQUAGE VACANCES ---
if en_vacances:
    st.error("🏖️ **FERMETURE EXCEPTIONNELLE**")
    st.stop()

# --- VARIABLES MAIL ---
details_produit_mail = ""
details_options_mail = ""

# --- PARTIE 1 : BOUQUET ---
if choix == "🌹 Un Bouquet":
    st.title("🌹 Configurer mon Bouquet")
    col1, col2 = st.columns(2)
    with col1:
        taille = st.selectbox("Nombre de roses", list(PRIX_ROSES.keys()), format_func=lambda x: f"{x} Roses ({PRIX_ROSES[x]}€)")
        prix_base = PRIX_ROSES[taille]
    with col2:
        try: st.image(f"bouquet_{taille}.jpg", use_container_width=True)
        except: st.caption("📷 (Image)")
    couleur_rose = st.selectbox("Couleur des roses", COULEURS_ROSES)
    choix_emballage = st.selectbox("Style d'emballage", ["Noir", "Blanc", "Rose", "Rouge", "Bordeaux", "Vert", "Bleu", "Crème", "Dior Noir (+5€)", "Dior Rose (+5€)", "Chanel (+5€)", "LV (+5€)"])
    prix_papier = 5 if "(+5€)" in choix_emballage else 0
    options_choisies = st.multiselect("Ajouter des éléments :", list(ACCESSOIRES_BOUQUET.keys()))
    
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
    st.title("🍫 Ma Box Chocolat")
    col1, col2 = st.columns(2)
    with col1:
        taille_box = st.selectbox("Quelle taille ?", list(PRIX_BOX_CHOCO.keys()), format_func=lambda x: f"Taille {x} ({PRIX_BOX_CHOCO[x]}€)")
        prix_base = PRIX_BOX_CHOCO[taille_box]
    with col2:
        try: st.image(f"box_{taille_box.lower()}.jpg", use_container_width=True)
        except: st.caption("📷 (Image)")
    liste_chocolats = st.multiselect("Choisissez les chocolats :", ["Kinder Bueno", "Ferrero Rocher", "Milka", "Raffaello", "Schoko-Bons", "Mixte"])
    fleur_eternelle = st.checkbox("Ajouter des Roses Éternelles ?")
    couleur_fleur_info = st.text_input("Couleur des roses éternelles :") if fleur_eternelle else ""
    options_choisies = st.multiselect("Ajouter des options :", list(ACCESSOIRES_BOX_CHOCO.keys()))
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
    st.title("❤️ Box Love")
    try: st.image("box_love.jpg", use_container_width=True)
    except: pass
    couleur_love = st.selectbox("Couleur des fleurs", COULEURS_ROSES)
    liste_chocolats = st.multiselect("Quels chocolats ?", ["Kinder Bueno", "Ferrero Rocher", "Mixte"])
    prix_total = PRIX_BOX_FIXE[choix]
    details_produit_mail = f"BOX LOVE (I ❤️ U)\n- Fleurs : {couleur_love}\n- Chocolats : {', '.join(liste_chocolats)}"
    details_options_mail = "Aucune option sup."

# --- LIVRAISON ---
st.markdown("---")
mode_livraison = st.selectbox("Mode de réception", list(LIVRAISON_OPTIONS.keys()))
frais_port = LIVRAISON_OPTIONS[mode_livraison]
adresse_complete = ""
if mode_livraison != "📍 Retrait Gonesse":
    rue = st.text_input("Adresse (Rue, Ville, CP)")
    tel = st.text_input("Téléphone")
    adresse_complete = f"{rue} | Tél: {tel}"

nom = st.text_input("Votre Nom & Prénom")
inst = st.text_input("Votre Instagram")
total_final = prix_total + frais_port
acompte = total_final * 0.40

st.markdown(f"""
<div style="background-color:white; padding:20px; border-radius:15px; text-align:center; border: 1px solid #E7D8D0;">
    <h3 style="margin:0; color:{THEME['text_color']};">Total : {total_final} €</h3>
    <div style="background-color:{THEME['main_color']}; color:white; padding:10px 20px; border-radius:50px; margin-top:10px; font-weight:bold;">
        🔒 Acompte : {acompte:.2f} €
    </div>
</div>
""", unsafe_allow_html=True)

if st.button("✅ VALIDER MA COMMANDE", type="primary", use_container_width=True):
    if nom and inst:
        msg = f"COMMANDE SUN CREATION 🌹\nClient : {nom} ({inst})\nAdresse : {adresse_complete if adresse_complete else 'Retrait place'}\nProduit : {choix}\nDétails :\n{details_produit_mail}\nOptions :\n{details_options_mail}\nTotal : {total_final}€ | Acompte : {acompte:.2f}€"
        st.balloons()
        st.markdown(f'<a href="{creer_lien_email(f"Commande {nom}", msg)}" style="background-color:{THEME["main_color"]}; color:white; padding:15px; display:block; text-align:center; border-radius:50px; font-weight:bold; text-decoration:none;">📨 ENVOYER LA COMMANDE</a>', unsafe_allow_html=True)