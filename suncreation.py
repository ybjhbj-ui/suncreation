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
# 🎨 DESIGN LUXE
# ==========================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@800&family=Montserrat:wght@600;700&display=swap');
header, [data-testid="stHeader"], footer, [data-testid="stFooter"], #MainMenu {{ display: none !important; }}
.stApp {{ background-color: {THEME['bg_color']} !important; }}

.main-title {{
    font-family: 'Playfair Display', serif !important;
    color: {THEME['text_color']} !important;
    text-align: center;
    font-size: 3rem !important;
    font-weight: 800;
    margin-bottom: 5px;
}}

h1, h2, h3 {{ font-family: 'Playfair Display', serif !important; color: {THEME['text_color']} !important; }}
.stMarkdown, p, label {{
    font-family: 'Montserrat', sans-serif !important; color: #2D1E12 !important; font-weight: 700 !important;
}}

/* VISIBILITÉ MENUS DÉROULANTS & CHAMPS */
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, .stDateInput div, textarea {{
    background-color: #4A3728 !important; border: 1px solid #D4AF37 !important; color: white !important;
}}
div[data-baseweb="select"] span {{ color: white !important; font-weight: 600 !important; }}
input, textarea {{ color: white !important; -webkit-text-fill-color: white !important; }}
ul[data-baseweb="menu"] li {{ background-color: #4A3728 !important; color: white !important; }}

::placeholder {{ color: #D7CCC8 !important; opacity: 0.7; }}
[data-testid="stSidebar"] {{ display: none; }}

/* Bouton Valider plus gros */
button[kind="secondary"] {{
    background-color: {THEME['main_color']} !important; 
    color: white !important; 
    border-radius: 50px !important; 
    font-weight: bold !important;
    height: 3rem !important;
    border: none !important;
}}
</style>
""", unsafe_allow_html=True)

# --- ⚙️ SECRETS ---
EMAIL_PRO = st.secrets.get("EMAIL_RECEPTION", "sncreat24@gmail.com")
ETAT_VACANCES_GLOBAL = st.secrets.get("MODE_VACANCES", "NON") 

if ETAT_VACANCES_GLOBAL == "OUI":
    st.error("🏖️ **FERMETURE EXCEPTIONNELLE**")
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
    
    # 1. Slider avec prix affiché en gros
    taille = st.select_slider("Nombre de roses", options=list(PRIX_ROSES.keys()), format_func=lambda x: f"{x} Roses ({PRIX_ROSES[x]}€)")
    prix_base = PRIX_ROSES[taille]
    
    st.markdown(f"<h3 style='text-align:center; color:{THEME['main_color']}; margin-top:-10px;'>Prix Bouquet : {prix_base} €</h3>", unsafe_allow_html=True)
    
    try: st.image(f"bouquet_{taille}.jpg", use_container_width=True)
    except: st.caption("📷 (Image)")
    
    couleur_rose = st.selectbox("Couleur des roses", COULEURS_ROSES)
    choix_emballage = st.selectbox("Style d'emballage", ["Noir", "Blanc", "Rose", "Rouge", "Bordeaux", "Bleu", "Dior (+5€)", "Chanel (+5€)"])
    prix_papier = 5 if "(+5€)" in str(choix_emballage) else 0
    
    # 2. Options avec texte immédiat
    st.subheader("Ajouter des options")
    options_choisies = []
    details_sup_list = []
    
    for opt in ACCESSOIRES_BOUQUET.keys():
        if st.checkbox(opt):
            options_choisies.append(opt)
            if "Bande" in opt:
                val = st.text_input(f"📝 Écrire le prénom pour la bande :", key=f"txt_{opt}")
                if val: details_sup_list.append(f"Prénom Bande: {val}")
            elif "Carte" in opt:
                val = st.text_area(f"📝 Écrire le message de la carte :", key=f"txt_{opt}")
                if val: details_sup_list.append(f"Message Carte: {val}")
            elif "Initiale" in opt:
                val = st.text_input(f"📝 Quelle initiale ?", key=f"txt_{opt}")
                if val: details_sup_list.append(f"Initiale: {val}")
    
    prix_total = prix_base + prix_papier + sum(ACCESSOIRES_BOUQUET[o] for o in options_choisies)
    
    details_produit_mail = f"• Modèle : BOUQUET {taille} roses\n• Couleur : {couleur_rose}\n• Emballage : {choix_emballage}"
    details_options_mail = ", ".join(options_choisies)
    if details_sup_list: details_options_mail += "\n\n📋 PERSONNALISATION :\n" + "\n".join(details_sup_list)

# --- PARTIE 2 : BOX CHOCOLAT ---
elif choix == "🍫 Box Chocolat":
    st.header("🍫 Ma Box Chocolat")
    taille_box = st.selectbox("Taille :", list(PRIX_BOX_CHOCO.keys()))
    prix_base = PRIX_BOX_CHOCO[taille_box]
    try: st.image(f"box_{taille_box.lower()}.jpg", use_container_width=True)
    except: st.caption("📷 (Image)")
    
    liste_chocolats = st.multiselect("Chocolats :", ["Kinder Bueno", "Ferrero Rocher", "Milka", "Raffaello", "Schoko-Bons"])
    
    fleur_eternelle = st.checkbox("Ajouter des Roses Éternelles ?")
    couleur_fleur_info = st.selectbox("Couleur roses :", COULEURS_ROSES) if fleur_eternelle else ""
    
    options_choisies = []
    details_sup_list = []
    st.write("**Options supplémentaires :**")
    for opt in ACCESSOIRES_BOX_CHOCO.keys():
        if st.checkbox(opt, key=f"chk_box_{opt}"):
            options_choisies.append(opt)
            if "Initiale" in opt:
                val = st.text_input("📝 Quelle initiale ?", key=f"txt_box_{opt}")
                if val: details_sup_list.append(f"Initiale: {val}")
            if "Bande" in opt:
                val = st.text_input("📝 Texte de la bande :", key=f"txt_box_{opt}")
                if val: details_sup_list.append(f"Bande: {val}")

    prix_total = prix_base + sum(ACCESSOIRES_BOX_CHOCO[o] for o in options_choisies)
    
    details_produit_mail = f"• Modèle : BOX CHOCOLAT {taille_box}\n• Chocolats : {', '.join(liste_chocolats)}\n• Fleurs : {couleur_fleur_info}"
    details_options_mail = ", ".join(options_choisies)
    if details_sup_list: details_options_mail += "\n\n📋 PERSONNALISATION :\n" + "\n".join(details_sup_list)

# --- PARTIE 3 : BOX LOVE ---
else:
    st.header("❤️ Box Love Signature")
    try: st.image("box_love.jpg", use_container_width=True)
    except: pass
    
    couleur_love = st.selectbox("Couleur des fleurs", COULEURS_ROSES)
    liste_chocolats = st.multiselect("Chocolats :", ["Kinder Bueno", "Ferrero Rocher"])
    
    prix_total = PRIX_BOX_FIXE[choix]
    details_produit_mail = f"• Modèle : BOX LOVE\n• Fleurs : {couleur_love}\n• Chocolats : {', '.join(liste_chocolats)}"
    details_options_mail = "Aucune option sup."

# --- LIVRAISON (RESTE DEHORS DU FORMULAIRE POUR LE PRIX) ---
st.markdown("---")
st.subheader("🚚 Livraison")
mode_livraison = st.selectbox("Mode de réception", list(LIVRAISON_OPTIONS.keys()))
frais_port = LIVRAISON_OPTIONS[mode_livraison]

# CALCUL DU TOTAL
total_final = prix_total + frais_port
acompte = total_final * 0.40

st.markdown(f"""
<div style="background-color:white; padding:20px; border-radius:15px; text-align:center; border: 1px solid #E7D8D0; margin-bottom: 20px;">
    <h3 style="margin:0; color:{THEME['text_color']};">Total : {total_final} €</h3>
    <div style="background-color:{THEME['main_color']}; color:white; padding:10px 20px; border-radius:50px; margin-top:10px; font-weight:bold;">
        🔒 Acompte requis : {acompte:.2f} €
    </div>
</div>
""", unsafe_allow_html=True)

# --- FORMULAIRE CLIENT (RÉSOUT LE PROBLÈME "ENTRÉE") ---
st.subheader("👤 Vos Coordonnées")
with st.form("client_form"):
    # Adresse à l'intérieur du formulaire
    adresse_complete = ""
    if mode_livraison != "📍 Retrait Gonesse":
        rue = st.text_input("📍 Adresse (Rue, Ville, CP)")
        adresse_complete = f"{rue}"
        if "Hors France" in mode_livraison:
            pays = st.text_input("🌍 Pays de destination")
            adresse_complete += f" | PAYS : {pays}"
    else:
        st.info("Retrait à Gonesse (L'adresse exacte vous sera communiquée).")

    nom = st.text_input("Votre Nom & Prénom")
    tel = st.text_input("📞 Téléphone (Indispensable)")
    inst = st.text_input("Votre Instagram")
    
    # Bouton de validation unique
    submitted = st.form_submit_button("✅ VALIDER MA COMMANDE")

if submitted:
    if nom and inst and tel:
        # MISE EN PAGE DU MAIL PROPRE ET PARFAIT
        msg = f"""NOUVELLE COMMANDE SUN CREATION
================================
👤 CLIENT
Nom : {nom}
Tél : {tel}
Insta : {inst}
--------------------------------
📦 COMMANDE
{details_produit_mail}

➕ OPTIONS
{details_options_mail if details_options_mail else "Aucune"}
--------------------------------
🚚 LIVRAISON
Mode : {mode_livraison}
Adresse : {adresse_complete if adresse_complete else "Retrait sur place"}
--------------------------------
💰 PAIEMENT
TOTAL : {total_final} €
ACOMPTE (40%) : {acompte:.2f} €
================================"""
        
        st.success("Commande prête ! Cliquez ci-dessous :")
        st.markdown(f'<a href="{creer_lien_email(f"Commande {nom}", msg)}" style="background-color:{THEME["main_color"]}; color:white; padding:15px; display:block; text-align:center; border-radius:50px; font-weight:bold; text-decoration:none;">📨 ENVOYER LA COMMANDE</a>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("⚠️ Merci de remplir votre Nom, Téléphone et Instagram.")
