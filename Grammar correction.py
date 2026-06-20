from transformers import pipeline
corrector = pipeline("text2text-generation",model="prithivida/grammar_error_correcter_v1")
while True:
    text = input("\nEnter text (or 'exit'): ")
    if text.lower() == "exit":
        break
    result = corrector(text, max_length=256)
    print("\nCorrected Text:")
    print(result[0]["generated_text"])