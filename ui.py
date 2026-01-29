import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

st.title("💬 Local LLM Chat")

model_name = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="cpu"
)

prompt = st.text_input("Ask something")

if prompt:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150)
    st.write(tokenizer.decode(outputs[0], skip_special_tokens=True))
