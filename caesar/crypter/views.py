from django.http import JsonResponse
from django.shortcuts import render
import logic


def index(request):
    return render(request, template_name="index.html")


def ajax_func(request):
    if request.is_ajax():
        text = request.POST.get("text")
        number = request.POST.get("number")
        if text and number >= 0 and is_english_string(text):
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
        if text and number >= 0:
            crypted_text = logic.get_crypt_text(text, number)
        else:
            crypted_text = text
        chart_text = logic.symbol_count(crypted_text)
        context = {
            "chart_text": chart_text
        }
        return JsonResponse(context)


def is_english_string(entered_text):
    """
   Checks whether given string
   containing only English characters
   :type entered_text: str
   """
    try:
        entered_text.decode("ascii")
    except UnicodeDecodeError:
        return False
    else:
        return True
