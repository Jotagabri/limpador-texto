import streamlit as st
import re

# Configuração da página
st.set_page_config(page_title="Limpador de Texto", layout="centered")

# CSS customizado
st.markdown("""
<style>
    .block-container { max-width: 680px; padding-top: 2rem; }
    h1 { font-size: 1.6rem !important; font-weight: 500 !important; }
    .stTextArea textarea {
        font-family: monospace;
        background-color: #1e1e1e;
        border-radius: 8px;
    }
    .stTextInput input {
        border-radius: 8px;
    }
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        padding: 0.6rem;
        font-weight: 500;
        font-size: 0.95rem;
    }
    .stAlert { border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

st.title("🧹 Limpa Texto")

# Entrada do texto original
texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)

# Campo para padrões personalizados
palavras_personalizadas = st.text_input(
    "Outras palavras/padrões a remover (separadas por vírgula)", value=""
)

# Função principal de limpeza
def limpar_texto(texto, palavras_adicionais):
    # Remove "Acréscimos: R$ <valor>"
    texto_limpo = re.sub(r'Acréscimos: R\$[\s\d\.,]+', '', texto)
    # Remove palavras adicionais informadas pelo usuário
    for palavra in palavras_adicionais:
        texto_limpo = texto_limpo.replace(palavra, "")
    return texto_limpo

# Botão de ação
if st.button("🪄 Limpar Texto"):
    # Lista de palavras adicionais, separadas por vírgula
    palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]

    # Limpeza do texto
    texto_limpo = limpar_texto(texto_original, palavras)

    # Exibição do resultado
    st.text_area("Texto Limpo:", value=texto_limpo, height=200, key="texto_limpo")

    # Instrução para copiar manualmente
    st.info("📋 Selecione o texto acima e pressione Ctrl+C para copiar.")
