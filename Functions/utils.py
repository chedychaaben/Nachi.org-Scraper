def clean_text(text):
    if type(text) == str:
        return " ".join(text.split())