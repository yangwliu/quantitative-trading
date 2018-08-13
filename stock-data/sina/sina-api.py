import requests


def get_stock_data(stock_market_id, stock_id):
    url = 'http://hq.sinajs.cn/list=' + stock_market_id + stock_id
    response = requests.get(url)

    if response.status_code == 200:
        return get_data_from_response(response.text)
    raise Exception('the api goes wrong!')


def get_data_from_response(response_text):
    valid_data = response_text[response_text.index('=') + 1: ]
    data_list = valid_data.split(',')
    return data_list


print(get_stock_data('sh', '601006'))
