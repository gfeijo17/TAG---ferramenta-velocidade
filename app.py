import streamlit as st
import streamlit.components.v1 as components
import qrcode
from io import BytesIO

# Configuração da página
st.set_page_config(
    page_title="GFS Info",
    page_icon="📶",
    layout="centered"
)

# Estilização: Fundo off-white, textos/botões em tom de marrom intermediário e diagramação harmonizada
st.markdown("""
    <style>
    /* Fundo da aplicação */
    .stApp {
        background-color: #FDFBF7;
        color: #5D4037;
    }

    /* Título Principal */
    .titulo-principal { 
        font-size: 32px !important; 
        font-weight: bold; 
        text-align: center; 
        color: #3E2723;
        margin-bottom: 5px;
    }

    /* Caixa com nome da Ferramenta/Rede/GFS/INFO */
    .caixa-rede { 
        font-size: 22px !important; 
        font-weight: bold; 
        text-align: center; 
        background-color: #EFEBE9; 
        color: #4E342E;
        padding: 14px; 
        border-radius: 10px; 
        margin-top: 10px;
        margin-bottom: 25px;
        border: 1px solid #D7CCC8;
    }

    /* Texto da Senha em fonte menor */
    .texto-senha {
        font-size: 16px !important;
        color: #5D4037;
        text-align: center;
        margin-top: 15px;
        font-weight: 500;
    }

    /* Estilização das Abas para combinar com a paleta */
    button[data-baseweb="tab"] {
        color: #5D4037 !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    button[aria-selected="true"] {
        color: #3E2723 !important;
        border-bottom-color: #5D4037 !important;
    }

    /* Títulos secundários */
    h3, .stSubheader {
        color: #4E342E !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Cabeçalho com o nome
st.markdown("<p class='titulo-principal'>GFS Info</p>", unsafe_allow_html=True)

# 2. Leitura da URL
query_params = st.query_params
ssid = query_params.get("ssid", "Ferramenta Redes")
senha = query_params.get("senha", "")

# Exibição da caixa com o nome da rede
st.markdown(f"<div class='caixa-rede'>{ssid}</div>", unsafe_allow_html=True)

# 3. Abas
aba_qr, aba_speed = st.tabs(["Rede", "Velocidade"])

with aba_qr:
    # Subtítulo
    st.markdown("<h3 style='margin-bottom: 20px;'>Para conectar na rede escaneie aqui!!</h3>", unsafe_allow_html=True)
    
    # Geração do QR Code
    wifi_payload = f"WIFI:S:{ssid};T:WPA;P:{senha};;"
    
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(wifi_payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#3E2723", back_color="#FDFBF7")
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    
    # Exibição centralizada do QR Code
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(buf.getvalue(), use_container_width=True)
        # Exibe apenas a senha abaixo do QR Code em fonte menor se houver uma senha cadastrada
        if senha:
            st.markdown(f"<p class='texto-senha'>Senha: <strong>{senha}</strong></p>", unsafe_allow_html=True)

with aba_speed:
    st.markdown("<h3 style='margin-bottom: 15px;'>Medidor de Velocidade</h3>", unsafe_allow_html=True)
    
    # Velocímetro Fast.com embutido
    components.iframe("https://fast.com", height=420, scrolling=True)
