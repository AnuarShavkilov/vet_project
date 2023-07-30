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
    index_list = ''
    for sign in price_list:
        reversed_path = reverse('price-name', args=[sign, ])
        index_list += f'<li> <a href = {reversed_path}>{sign.title()}</a> </li>'
    responce = f"""
    <ul>
        {index_list}
    </ul>
    """
    return HttpResponse(responce)


def index_type(request):
    price_type_list = list(type_dict)
    index_list = ''
    for sign in price_type_list:
        reversed_path = reverse('type-name', args=[sign, ])
        index_list += f'<li> <a href = {reversed_path}>{sign.title()}</a> </li>'
    responce = f"""
        <ul>
            {index_list}
        </ul>
        """
    return HttpResponse(responce)


def get_type(request, price_type):
    reversed_url = reverse('type-name', args=[price_type, ])
    description = type_dict.get(price_type)
    index_list = ''
    for sign in description:
        reversed_path = reverse('price-name', args=[sign, ])
        index_list += f'<li> <a href = {reversed_path}>{sign.title()}</a> </li>'
    responce = f"""
        <ul>
            {index_list}
        </ul>
        """
    if reversed_url:
        return HttpResponse({responce})
    else:
        return HttpResponseNotFound(f'Нет такого - {price_type}')


def get_price(request, price_param):
    description = price_dict.get(price_param)
    if description:
        return HttpResponse(f'<h2>{description}<h2>')
    else:
        return HttpResponseNotFound(f'Нет такой цены - {price_param}')


def get_price_by_num(request, price_param):
    price_list = list(price_dict)
    if price_param > len(price_list):
        return HttpResponseNotFound(f'Нет такой цены - {price_param}')
    name_price = price_list[price_param - 1]
    reversed_url = reverse('price-name', args=[name_price, ])
    return HttpResponseRedirect(reversed_url)
