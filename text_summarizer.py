from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text, max_len=130, min_len=30, lang="en_XX"):
    try:
        tokenizer.src_lang = lang
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        summary_ids = model.generate(inputs["input_ids"], max_length=max_len, min_length=min_len, length_penalty=2.0)
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error summarizing: {e}"
