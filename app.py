import streamlit as st
import streamlit.components.v1 as components
import qrcode
from io import BytesIO

st.set_page_config(
    page_title="Suporte Wi-Fi & Diagnóstico",
    page_icon="📶",
    layout="centered"
)

st.markdown("""
    <style>
    .titulo-principal { font-size: 30px !important; font-weight: bold; text-align: center; color: #1E88E5; }
    .caixa-rede { font-size: 22px !important; font-weight: bold; text-align: center; background-color: #E3F2FD; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: #0D47A1; }
    .senha-destaque { font-size: 24px !important; color: #D32F2F; font-weight: bold; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<p class='titulo-principal'>📶 Suporte Wi-Fi Simplificado</p>", unsafe_allow_html=True)

query_params = st.query_params
ssid = query_params.get("ssid", "Rede de Teste")
senha = query_params.get("senha", "SemSenha123")

st.markdown(f"<div class='caixa-rede'>Rede: {ssid}</div>", unsafe_allow_html=True)

aba_qr, aba_speed = st.tabs(["📲 QR Code de Conexão", "🚀 Testar Velocidade"])

with aba_qr:
    st.subheader("Conecte um novo aparelho")

    wifi_payload = f"WIFI:S:{ssid};T:WPA;P:{senha};;"

    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(wifi_payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format="PNG")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(buf.getvalue(), caption="Aponte a câmera do celular aqui", use_container_width=True)

    st.divider()
    st.markdown(f"<p class='senha-destaque'>🔑 Senha: {senha}</p>", unsafe_allow_html=True)

with aba_speed:
    st.subheader("Medidor de Velocidade em Tempo Real")
    st.info("Aguarde a medição carregar automaticamente abaixo:")
    components.iframe("https://fast.com", height=420, scrolling=True)
