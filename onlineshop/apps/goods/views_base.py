__author__ = 'kevin.xie'

import json

from django.http import JsonResponse
from django.views.generic.base import View
from django.core import serializers

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request
        :return
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data, )

        return JsonResponse(json_data, safe=False)

