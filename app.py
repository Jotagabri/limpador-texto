import streamlit as st
import re

st.set_page_config(page_title="Limpa Texto", layout="centered", page_icon="🧹")

st.title("🧹 Limpa Texto")
st.caption("Remova padrões indesejados do seu texto de forma rápida e precisa.")

# --- Entrada ---
texto_original = st.text_area("Texto de entrada", height=180, placeholder="Cole aqui o texto que deseja limpar...")
if texto_original:
    st.caption(f"{len(texto_original):,} caracteres")

# --- Padrões personalizados ---
st.subheader("Padrões para remover")
palavras_personalizadas = st.text_input(
    "Palavras ou padrões (separados por vírgula)",
    placeholder="ex: Assunto:, ----, CONFIDENCIAL"
)

# --- Remoções rápidas (checkboxes) ---
st.write("**Remoções rápidas:**")
col1, col2, col3 = st.columns(3)
rm_acrescimos  = col1.checkbox("Acréscimos R$", value=True)
rm_linhas      = col1.checkbox("Linhas em branco extras")
rm_espacos     = col2.checkbox("Espaços duplos")
rm_tabs        = col2.checkbox("Tabulações")
rm_links       = col3.checkbox("Links HTTP")

# --- Limpeza ---
def limpar_texto(texto, palavras_adicionais):
    t = texto
    if rm_acrescimos:
        t = re.sub(r'Acréscimos:\s*R\$[\s\d\.,]+', '', t)
    if rm_linhas:
        t = re.sub(r'\n{2,}', '\n', t)
    if rm_espacos:
        t = re.sub(r' {2,}', ' ', t)
    if rm_tabs:
        t = t.replace('\t', '')
    if rm_links:
        t = re.sub(r'https?://\S+', '', t)
    for palavra in palavras_adicionais:
        t = t.replace(palavra, '')
    return t.strip()

# --- Ação ---
col_btn1, col_btn2 = st.columns([3, 1])
limpar = col_btn1.button("🪄 Limpar Texto", use_container_width=True, type="primary")
resetar = col_btn2.button("Resetar", use_container_width=True)

if limpar and texto_original:
    palavras = [p.strip() for p in palavras_personalizadas.split(",") if p.strip()]
    texto_limpo = limpar_texto(texto_original, palavras)

    st.divider()
    st.subheader("Resultado")

    # Estatísticas
    c1, c2, c3 = st.columns(3)
    c1.metric("Antes", f"{len(texto_original):,} chars")
    c2.metric("Depois", f"{len(texto_limpo):,} chars")
    c3.metric("Removidos", f"{len(texto_original) - len(texto_limpo):,} chars")

    st.text_area("Texto limpo:", value=texto_limpo, height=180, key="saida")
    st.download_button("⬇️ Baixar .txt", data=texto_limpo, file_name="texto-limpo.txt", mime="text/plain")
    st.info("💡 Selecione o texto acima e pressione Ctrl+C para copiar.")
elif limpar:
    st.warning("Cole um texto antes de limpar.")
