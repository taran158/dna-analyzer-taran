import streamlit as st
from Bio.Seq import Seq
import matplotlib.pyplot as plt
from collections import Counter

# App configuration
st.set_page_config(page_title="DNA Analyzer by Taran", layout="centered")
st.title("🧬 DNA Sequence Analyzer")
st.caption("Developed by Taran | 2nd Semester Bioinformatics Mini Project")

st.subheader("Enter a DNA Sequence (A, T, C, G):")
user_input = st.text_area("Paste or type the DNA sequence here:", height=150)

def clean_sequence(seq):
    return ''.join(filter(lambda x: x in "ATCGatcg", seq.upper()))

def codon_usage_table(seq):
    codons = [seq[i:i+3] for i in range(0, len(seq) - len(seq)%3, 3)]
    codon_count = Counter(codons)
    return codon_count

if user_input:
    seq = clean_sequence(user_input)
    dna_seq = Seq(seq)

    st.markdown("### ✅ Basic Analysis:")
    st.write(f"🔹 Length: {len(dna_seq)} bases")
    st.write(f"🔹 GC Content: {100 * (seq.count('G') + seq.count('C')) / len(seq):.2f}%")
    
    st.markdown("### 🔁 Reverse Complement:")
    st.code(str(dna_seq.reverse_complement()))

    st.markdown("### 🧬 Transcription (DNA → mRNA):")
    st.code(str(dna_seq.transcribe()))

    st.markdown("### 🧫 Translation (mRNA → Protein):")
    st.code(str(dna_seq.translate(to_stop=True)))

    st.markdown("### 📊 Nucleotide Frequency:")
    freq = Counter(seq)
    labels = list(freq.keys())
    values = list(freq.values())

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["#4CAF50", "#2196F3", "#FFC107", "#F44336"])
    ax.set_ylabel("Count")
    ax.set_title("Nucleotide Count")
    st.pyplot(fig)

    st.markdown("### 🧾 Codon Usage Table:")
    codons = codon_usage_table(seq)
    for codon, count in sorted(codons.items()):
        st.write(f"{codon}: {count}")

else:
    st.info("Enter a DNA sequence to start analysis.")

# Footer
st.markdown("---")
st.markdown("🧪 Created with ❤️ by **Taran** — Bioinformatics Student, 2nd Semester")
