
from django.shortcuts import render
from myapp.models import Electronics
# from django.core.serializers import serialize
from django.views.generic import View
import json
from django.http import JsonResponse
# Create your views here.


class ElectronicsDetails(View):
	def get(self, request):
		s = Electronics.objects.all()
		category = request.GET.get('category')
		if category:
			s = s.filter(category__iexact = category)
		data = []
		for i in s:
			data.append({
				"id": i.id,
				"name": i.name,
				"brand": i.brand,
				"category": i.category,
				"rating": i.rating,
				"description": i.description,
				"price": i.price,
				"discount_price": i.discount_price,
				"stock": i.stock,
				"available": i.available,
				"image": request.build_absolute_uri(i.image.url) if i.image else None,  # ✅ added		
			})
		return JsonResponse(data, safe=False)