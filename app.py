import streamlit as st
import re

st.set_page_config(page_title="Limpa Texto", layout="centered", page_icon="🧹")

st.title("🧹 Limpa Texto")
st.caption("Remova padrões indesejados do seu texto de forma rápida e precisa.")

# Entrada do texto original
texto_original = st.text_area("Cole aqui o texto que deseja limpar:", height=200)
if texto_original:
    st.caption(f"{len(texto_original):,} caracteres")

# Campo para padrões personalizados
palavras_personalizadas = st.text_input(
    "Outras palavras/padrões a remover (separadas por vírgula)", value=""
)

# Função principal de limpeza (original mantida)
def limpar_texto(texto, palavras_adicionais):
    # Remove "Acréscimos: R$ <valor>"
    texto_limpo = re.sub(r'Acréscimos: R\$[\s\d\.,]+', '', texto)
    # Remove palavras adicionais informadas pelo usuário
    for palavra in palavras_adicionais:
        texto_limpo = texto_limpo.replace(palavra, "")
    return texto_limpo

col1, col2 = st.columns([3, 1])
limpar = col1.button("🪄 Limpar Texto", use_container_width=True, type="primary")
resetar = col2.button("Resetar", use_container_width=True)

if limpar:
    if not texto_original.strip():
        st.warning("Cole um texto antes de limpar.")
    else:
        palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]
        texto_limpo = limpar_texto(texto_original, palavras)

        st.divider()

        c1, c2, c3 = st.columns(3)
        c1.metric("Antes", f"{len(texto_original):,} chars")
        c2.metric("Depois", f"{len(texto_limpo):,} chars")
        c3.metric("Removidos", f"{len(texto_original) - len(texto_limpo):,} chars")

        st.text_area("Texto limpo:", value=texto_limpo, height=200, key="saida")
        st.download_button("⬇️ Baixar .txt", data=texto_limpo, file_name="texto-limpo.txt", mime="text/plain")
        st.info("📋 Selecione o texto acima e pressione Ctrl+C para copiar.")
