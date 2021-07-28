n = ['Crypto IDX', '82%', '82%', 'EUR/USD', '83%', '80%', 'Altcoin IDX', '82%', '82%', 'AUD/JPY', '81%', '80%', 'NZD/JPY', '80%', '80%', 'AUD/NZD', '79%', '80%', 'USD/CHF', '79%', '80%', 'EUR IDX', '78%', '80%', 'EUR/JPY', '78%', '80%', 'CHF/JPY', '78%', '80%', 'EUR/MXN', '77%', '80%', 'NZD/USD', '77%', '80%', 'JPY IDX', '75%', '80%', 'EUR/NZD', '73%', '80%', 'AUD/USD', '71%', '80%', 'AUD/CAD', '71%', '80%', 'Bitcoin', '30%', '30%', 'Apple', '—', '75%', 'Twitter', '—', '75%', 'NASDAQ 100', '—', '70%', 'Dow Jones IA', '—', '70%', 'Google', '—', '65%', 'Gold', '—', '60%', 'Disponible para Standard', 'GBP/JPY', '82%', '80%', 'EUR/CAD', '81%', '80%', 'USD/NOK', '80%', '80%', 'EUR/GBP', '79%', '80%', 'BCH/USDT', '30%', '30%', 'Litecoin', '30%', '30%', 'Microsoft', '—', '75%', 'McDonalds', '—', '75%', 'AIG', '—', '75%', 'PayPal', '—', '75%', 'Boeing', '—', '73%', 'JD', '—', '73%', 'AEX', '—', '70%', 'CAC', '—', '70%', 'Vodafone', '—', '65%', 'IBM', '—', '65%', 'Silver', '—', '50%', 'Coca Cola', '—', '30%', 'Disponible para Gold', 'USD/DKK', '74%', '81%', 'GBP/CHF', '73%', '81%', 'Twitter', '—', '76%', 'Nvidia', '—', '76%', 'Yum Brands', '—', '74%', 'Intel', '—', '71%', 'Starbucks', '—', '71%', 'Visa', '—', '71%', 'Weibo', '—', '71%', 'Qualcomm', '—', '71%', 'JPMorgan C', '—', '66%', 'Ferrari', '—', '31%', 'Disponible para VIP', 'EUR/HKD', '82%', '82%', 'EUR/CHF', '82%', '82%', 'EUR/AUD', '82%', '82%', 'CAD/CHF', '68%', '82%', 'GBP/AUD', '31%', '82%', 'Apple', '—', '77%', 'Alibaba', '—', '77%', 'Netflix', '—', '75%', 'Facebook', '—', '75%', 'Tesla', '—', '75%', 'CitiGroup', '—', '72%', 'Yandex', '—', '67%', 'eBay', '—', '62%']
n.remove('Disponible para Standard')
n.remove('Disponible para Gold')
n.remove('Disponible para VIP')
ndos = {}
for i in range(0, len(n), 3):
    ndos[n[i]] = []
    ndos[n[i]].append(n[i + 1])
    ndos[n[i]].append(n[i + 2])

print(ndos)