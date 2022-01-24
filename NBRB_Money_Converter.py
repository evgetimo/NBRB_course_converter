import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

usd_url = 'https://www.nbrb.by/api/exrates/rates/usd?parammode=2'
usd_response = requests.get(usd_url, verify=False)
usd_json_data = json.loads(usd_response.text)
nbrb_usd_course = usd_json_data.get('Cur_OfficialRate')

eur_url = 'https://www.nbrb.by/api/exrates/rates/eur?parammode=2'
eur_response = requests.get(eur_url, verify=False)
eur_json_data = json.loads(eur_response.text)
nbrb_eur_course = eur_json_data.get('Cur_OfficialRate')

rub_url = 'https://www.nbrb.by/api/exrates/rates/rub?parammode=2'
rub_response = requests.get(rub_url, verify=False)
rub_json_data = json.loads(rub_response.text)
nbrb_rub_course = rub_json_data.get('Cur_OfficialRate')

usd_course = round(nbrb_usd_course + (nbrb_usd_course / 150), 3)
eur_course = round(nbrb_eur_course + (nbrb_eur_course / 150), 3)
rub_course = round(nbrb_rub_course + (nbrb_rub_course / 150), 3)

print('Доллар:', usd_course)
print('Евро:', eur_course)
print('Рубль:', rub_course)

byn = float(input("Сумма в белорусских рублях: "))

usd_coef = 0.3
eur_coef = 0.2
rub_coef = 0.5

byn_usd_buy = round((byn * usd_coef), 3)
byn_eur_buy = round((byn * eur_coef), 3)
byn_rub_buy = round((byn * rub_coef), 3)

usd_buy = round(byn_usd_buy / usd_course)
eur_buy = round(byn_eur_buy / eur_course)
rub_buy = round(byn_rub_buy / rub_course)

print('-----------------------------')
print("Потратить на USD:", byn_usd_buy, "BYN. Купить", usd_buy, 'доллар(ов).')
print("Потратить на EUR:", byn_eur_buy, "BYN. Купить", eur_buy, 'евро.')
print("Потратить на RUB:", byn_rub_buy, "BYN. Купить", rub_buy * 100, 'российских рублей.')
