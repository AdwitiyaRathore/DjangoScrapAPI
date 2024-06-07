from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .scrap import *


class StartScrapingView(APIView):
    def post(self, request, format=None):
        coin_names = request.data.get('coins', [])
        if not isinstance(coin_names, list) or not all(isinstance(coin, str) for coin in coin_names):
            return Response({'error': 'Invalid payload. Expected a list of strings.'}, status=status.HTTP_400_BAD_REQUEST)

        job_ids = []
        for coin_name in coin_names:
            scraper = GetMarketLink(coin_name)
            market_detail = scraper.get_source_code()
            if market_detail:
                job_ids.append(market_detail.job_id)  # Assuming MarketDetail has an 'id' field

        return Response({'job_ids': job_ids}, status=status.HTTP_200_OK)

class ScrapingStatusView(APIView):
    def get(self, request, job_id, *args, **kwargs):
        try:
            market_detail = MarketDetail.objects.get(job_id=job_id)
            serializer = MarketDetailSerializer(market_detail)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except MarketDetail.DoesNotExist:
            return Response({'error': 'Job ID not found'}, status=status.HTTP_404_NOT_FOUND)
