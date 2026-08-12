from django.shortcuts import render
from translate import Translator

def home(request):
    translation = ""
    if request.method == "POST":
        text = request.POST.get("translate", "")
        from_lang = request.POST.get("from_language", "de")
        to_lang = request.POST.get("to_language", "am")

        if text.strip():
            try:
                # Pass both source and target languages
                translator = Translator(from_lang=from_lang, to_lang=to_lang)
                translation = translator.translate(text)
            except Exception:
                translation = "Translation service error. Please try again."

    return render(request, "main/index.html", {"translation": translation})