from django.http import JsonResponse
from django.shortcuts import render
import logic


def index(request):
    return render(request, template_name="index.html")


def ciphertext(request):
    if request.is_ajax():
        text = request.POST.get("text")
        number = request.POST.get("number")
        if not is_english_string(text):
            crypted_text = "Only english character are allowed"
        elif text and number:
            crypted_text = logic.get_crypt_text(text, number)
        else:
            crypted_text = text
        context = {
            "code_text": crypted_text
        }
        return JsonResponse(context)


def chart(request):
    if request.is_ajax():
        text = request.POST.get("text")
        number = request.POST.get("number")
        if not is_english_string(text):
            crypted_text = "Only english character are allowed"
        elif text and number:
            crypted_text = logic.get_crypt_text(text, number)
        else:
            crypted_text = text
        chart_text = logic.symbol_count(crypted_text)
        context = {
            "chart_text": chart_text
        }
        return JsonResponse(context)


def is_english_string(text):
    try:
        text.decode("ascii")
    except UnicodeEncodeError:
        return False
    else:
        return True
