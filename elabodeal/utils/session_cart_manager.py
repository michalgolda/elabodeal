from dataclasses import dataclass

class SessionCartManager:
    
    @dataclass
    class Item:
        id: int
        price: float
        
        
    def __init__(self, request = None):
        self.request = request
        self._items = []

        self._load_data()

    @property
    def items(self):
        return self._items

    @property
    def item_count(self):
        return len(self._items)

    @property
    def total_price(self):
        sum = 0.00
        for item in self._items:
            sum += item.price

        return '{0:.2f}'.format(round(sum, 2))

    def add_item(self, item):
        self._items.append(item)

        return item

    def remove_item(self, item_id):
        items = []

        for item in self._items:
            if item_id != item.id:
                items.append(item)
        
        self._items = items

        return items
    
    def _load_data(self):
        session = self.request.session
        if not 'cart' in session:
            return
        
        cart = session.get('cart')

        items_dict = cart.get('items')
        for item in items_dict:
            cart_item = self.Item(item['id'], item['price'])
            self._items.append(cart_item)

    def to_dict(self):
        cart_dict = {
            'items': [], 
            'total_price': self.total_price,
            'item_count': self.item_count}

        for item in self._items:
            cart_dict['items'].append({
                'id': item.id, 
                'price': item.price})

        return cart_dict

    