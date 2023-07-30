from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

price_dict = {
    'dermatolog': 'Цена приема дерматолога - 1900р',
    'hirurg': 'Цена приема хирурга - 1900р',
    'okulist': 'Цена приема окулиста - 1360р',
    'terapevt': 'Цена приема терапевта - 1200р',
    'grummer': 'Цена приема груммер - 2920р',
    'vacine': 'Цена вакцинации - 1000р',
}

type_dict = {
    'lechenie': ['dermatolog', 'hirurg', 'okulist'],
    'terapiya': ['terapevt', 'vacine'],
    'krasota': ['grummer', ]
}


def index_price(request):
    price_list = list(price_dict)
    context = {
        'price_list': price_list,
    }
    return render(request, 'vet/index_price.html', context=context)


def index_type(request):
    price_type_list = list(type_dict)
    context = {
        'price_type_list': price_type_list,
    }
    return render(request, 'vet/index_type.html', context=context)


def get_type(request, price_type):
    description = type_dict.get(price_type)
    context = {
        'description': description,
    }
    if description:
        return render(request, 'vet/get_type.html', context=context)
    else:
        return HttpResponseNotFound(f'Нет такого - {price_type}')


def get_price(request, price_param):
    description = price_dict.get(price_param)
    data = {
        'description_data': description,
        'service_name': price_param.title()
    }
    if description:
        return render(request, 'vet/info_price.html', data)
    else:
        return HttpResponseNotFound(f'Нет такой цены - {price_param}')


def get_price_by_num(request, price_param):
    price_list = list(price_dict)
    if price_param > len(price_list):
        return HttpResponseNotFound(f'Нет такой цены - {price_param}')
    name_price = price_list[price_param - 1]
    reversed_url = reverse('price-name', args=[name_price, ])
    return HttpResponseRedirect(reversed_url)
