from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

price_dict = {
    'dermatolog': 'Цена приема дерматолога - 1900р',
    'hirurg': 'Цена приема хирурга - 1900р',
    'okulist': 'Цена приема окулиста - 1360р',
    'terapevt': 'Цена приема терапевта - 1200р',
    'grummer': 'Цена приема груммер - 2920р',
    'vacine': 'Цена вакцинации - 1000р',
}


def get_price(request, price_param):
    description = price_dict.get(price_param)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Нет такой цены - {price_param}')


def get_price_by_num(request, price_param):
    price_list = list(price_dict)
    if price_param>len(price_list):
        return HttpResponseNotFound(f'Нет такой цены - {price_param}')
    name_price = price_list[price_param-1]
    return HttpResponseRedirect(f'/price/{name_price}')

