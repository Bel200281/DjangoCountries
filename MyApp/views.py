from django.shortcuts import render

countries = ["Россия", "США", "Великобритания", "Китай", "Франция", "Германия", "Латвия", "Испания", "Япония", "Турция", "Польша", "Италия"]

def main_page(request):
    return render(request, 'main_page.html', {})

def countries_list_view(request):
    return render(request, 'countries_list.html', {"countries": countries})