import bs4, requests

def convertUSDToRUB(amount):
    res = requests.get('https://finance.yahoo.com/quote/RUB=X/') #Обращается к ресурсу
    USD = bs4.BeautifulSoup(res.text, 'html.parser') #парсит html ресурса
    USDPrice = USD.select('span.Fw\(b\):nth-child(1)') #узнаёт курс доллара на ресурсе
    result = float(amount)  * float(USDPrice[0].text.strip()) #непосредственно конвертирует USD в RUB путём умножения суммы введённой пользователем на курс USD to RUB
    print('Стоимость одного доллара по данным ресурса finance.yahoo составляет', USDPrice[0].text.strip(), 'рублей.') #сообщает стоимость одного USD
    print(amount, 'американских долларов составляет', round(result, 2), 'российских рублей.') #выводит итоговую сумму на экран с точностью до 2 символов после запятой

amount = input('Введите сумму USD, которую необходимо конвертировать в RUB.\n') #Запрос пользователю на ввод сумму к конвертации
convertUSDToRUB(amount) #Выполнение функции
