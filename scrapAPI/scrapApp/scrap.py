import requests
from bs4 import BeautifulSoup

from .models import MarketDetail
from .serializers import MarketDetailSerializer


class GetMarketLink:
    def __init__(self, coin_name):
        self.coin_name = coin_name
        self.url = f'https://coinmarketcap.com/currencies/{coin_name}/'

    def get_source_code(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return self.beautiful_soup_process(r.content)
        return None

    def beautiful_soup_process(self, context):
        soup = BeautifulSoup(context, 'lxml')
        return self.detail_scrap(soup)

    def detail_scrap(self, soup):
        price = soup.find('span', attrs={'class':'sc-d1ede7e3-0 fsQm base-text'}).text
        dataChange = soup.find('p', attrs={'class':'sc-71024e3e-0 sc-58c82cf9-1 bgxfSG iPawMI'}).text

        marketCap = soup.find('dd', attrs={'class':'sc-d1ede7e3-0 hPHvUM base-text'}).text
        for i in range(len(marketCap)-1, 0, -1):
            if marketCap[i] != '$':
                i -= 1
            else:
                break
        marketCap = marketCap[i:]

        rankValues = soup.find_all('span', attrs={'class': 'text slider-value rank-value'})
        ranks = [i.text for i in rankValues]

        volume = soup.find('dd', attrs={'class': 'sc-d1ede7e3-0 hPHvUM base-text'}).text
        for i in range(len(volume)-1, 0, -1):
            if volume[i] != '$':
                i -= 1
            else:
                break
        volume = volume[i:]

        statics = soup.find_all('dd', attrs={'class': 'sc-d1ede7e3-0 hPHvUM base-text'})
        vmRatio = statics[2].text
        circulatingSupply = statics[3].text
        totalSupply = statics[4].text
        dilutedMC = statics[6].text

        contractorName = soup.find('span', attrs={'class': 'sc-71024e3-0 dEZnuB'}).text
        contractorAddress = soup.find('span', attrs={'class': 'sc-71024e3-0 eESYbg address'}).text

        webiste = soup.find('div', attrs={'class': 'sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf'}).find('a').get('href')
        social = soup.find_all('div', attrs={'class': 'sc-d1ede7e3-0 sc-7f0f401-2 bwRagp kXjUeJ'})
        social = social[-2].find_all('a')
        socialLinks = [i.get('href') for i in social]

        market_detail = MarketDetail.objects.create(
            coin_name=self.coin_name,
            price=price,
            data_change=dataChange,
            market_cap=marketCap,
            rank_values=ranks,
            volume=volume,
            vm_ratio=vmRatio,
            circulating_supply=circulatingSupply,
            total_supply=totalSupply,
            diluted_mc=dilutedMC,
            contractor_name=contractorName,
            contractor_address=contractorAddress,
            website=webiste,
            social_links=socialLinks
        )

        serialized_data = MarketDetailSerializer(market_detail).data

        return serialized_data
