from django.shortcuts import render

countries = ["Россия", "США", "Великобритания", "Китай", "Франция", "Германия", "Латвия", "Испания", "Япония", "Турция", "Польша", "Италия"]

languages_by_country = {
    "Россия": ["Русский"],
    "США": ["Английский"],
    "Великобритания": ["Английский"],
    "Китай": ["Китайский"],
    "Франция": ["Французский"],
    "Германия": ["Немецкий"],
    "Латвия": ["Латышский"],
    "Испания": ["Испанский"],
    "Япония": ["Японский"],
    "Турция": ["Турецкий"],
    "Польша": ["Польский"],
    "Италия": ["Итальянский"]
}



def main_page(request):
    return render(request, 'main_page.html', {})

def countries_list_view(request):
    return render(request, 'countries_list.html', {"countries": countries})

def country_detail_view(request, country):
    languages = languages_by_country.get(country)
    if not languages:
        return render(request, 'country_not_found.html')
    context = {'country': country, 'languages': languages}
    return render(request, 'country_detail.html', context)

