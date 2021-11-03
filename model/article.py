class Article():
    def __init__(self, name, shop, price, date, url):
        self.name = name
        self.shop = shop
        self.price = price
        self.date = date
        self.url = url
        
    def __str__(self):
        return self.name + ' : ' + self.shop + ' : ' + self.price + ' : ' + self.date + ' : ' + self.url

    def __eq__(self, other):
        return self.name == other.name and self.shop == other.shop and self.price == other.price and self.date == other.date and self.url == other.url

    def prettify(self):
        return "Name: " + self.name + ' \n' + "Shop: " + self.shop + ' \n' + "Price: " + self.price + ' \n' + "Date: " + self.date + ' \n' + "URL: " + self.url

    def to_dict(self):
        return {
            'name': self.name,
            'shop': self.shop,
            'price': self.price,
            'date': self.date,
            'url': self.url
        }
    
    @staticmethod
    def from_dict(d):
        return Article(d['name'], d['shop'], d['price'], d['date'], d['url'])
    
    @staticmethod
    def from_string(s):
        name, shop, price, date, url = s.split(' : ')
        return Article(name, shop, price, date, url)