from django.shortcuts import render, reverse, redirect

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
    return render(request, 'countries_list.html', {"alphabet": alphabet, "countries": countries})

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