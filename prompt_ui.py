from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables from a .env file
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header("Research Tool")

paper_input = st.selectbox("Select a research paper Name", ["Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "RoBERTa: A Robustly Optimized BERT Pretraining Approach", "XLNet: Generalized Autoregressive Pretraining for Language Understanding", "ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators", "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations", "Diffusion Models for Text-to-Image Generation", "CLIP: Connecting Text and Images"])

style_input = st.selectbox("Select a writing style", ["Select...", "Beginner-friendly", "Technical", "Concise","Code-Oriented", "Mathematical" ])

length_input = st.selectbox("Select response length", ["Select...", "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


template = load_prompt("research_paper_summary_template.json")

# fill the placeholders
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})


if st.button("Generate Response"):
    result = model.invoke(prompt)
    st.subheader("Generated Summary")
    st.write(result.content)