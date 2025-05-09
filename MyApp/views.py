from django.shortcuts import render, reverse, redirect
from django.http import Http404

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
    alphabet = sorted(set(c[0].upper() for c in countries))
    PAGE_SIZE = 10 

    total_countries = len(countries)
    total_pages = (total_countries + PAGE_SIZE - 1) // PAGE_SIZE  

    try:
        current_page = int(request.GET.get("page", 1))  
    except ValueError:
        current_page = 1

    if current_page < 1 or current_page > total_pages:
        raise Http404("Номер страницы вне допустимых пределов.")

    start_idx = (current_page - 1) * PAGE_SIZE
    end_idx = min(start_idx + PAGE_SIZE, total_countries)

    paginated_countries = countries[start_idx:end_idx]  # Выборка стран нужной страницы

    pages_numbers = list(range(1, total_pages + 1))  # Массив номеров страниц

    context = {
        "alphabet": alphabet,
        "paginated_countries": paginated_countries,
        "current_page": current_page,
        "pages_numbers": pages_numbers,
        "full_countries": countries,
    }

    return render(request, 'countries_list.html', context)

def country_detail_view(request, country):
    if len(country) > 1: 
        languages = languages_by_country.get(country)
        if not languages:
            return render(request, 'country_not_found.html')
       
        context = {'country': country, 'languages': languages}
        return render(request, 'country_detail.html', context)
    else:
        return redirect(reverse('filtered-countries', args=(country,)))

def filtered_countries_view(request, letter):
    filtered_countries = [c for c in countries if c.startswith(letter)]
    return render(request, 'filtered_countries.html', {"letter": letter, "countries": filtered_countries})

def language_details_view(request, language):
    """
    Возвращает список стран, говорящих на данном языке
    """
    speaking_countries = []
    for country, langs in languages_by_country.items():
        if language in langs:
            speaking_countries.append(country)
    return render(request, 'language_details.html', {'language': language, 'countries': speaking_countries})

def all_languages_view(request):
    """Возвращает уникальный список всех языков"""
    unique_languages = set()
    for langs in languages_by_country.values():
        unique_languages.update(langs)
    return render(request, 'all_languages.html', {'languages': list(unique_languages)})
