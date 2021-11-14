class BubbleTea:
    """The base bubble tea class."""

    def __init__(self, *a, **kw):
        self.sort = kw.get('sort')
        self.price = kw.get('price')

    def __repr__(self):
        return f'<BubbleTea sort={self.sort} price={self.price}>'

    def __str__(self):
        return self.sort


class MilkTea(BubbleTea):
    """
    This is a combination of brewed tea with milk.
    """

    def __init__(self):
        super().__init__(sort='MilkTea', price=2.75)


class FruitTea(BubbleTea):
    """
    This is a fruit-based drink without any caffeine or milk.
    Seasonal fruits or concentrates are used to make this drink.
    """

    def __init__(self):
        super().__init__(sort='FruitTea', price=2.50)


class Milkshake(BubbleTea):
    """
    Dairy-based or fruit-based blends.
    """

    def __init__(self):
        super().__init__(sort='Milkshake', price=3.00)


class FreshMilk(BubbleTea):
    """
    Usually, this refers to the use of fresh milk rather than creamer in the drink.
    This is usually caffeine-free.
    """

    def __init__(self):
        super().__init__(sort='FreshMilk', price=1.00)


class SaltedCream(BubbleTea):
    """
    Also, this drink is sometimes known as milk foam or cream crown.
    This is a sweet and savory foam top made from cream cheese, sea salt, or Himalayan salt.
    """

    def __init__(self):
        super().__init__(sort='SaltedCream', price=1.00)


class BlackTea(BubbleTea):
    """
    This broadly refers to brewed tea blends without milk.
    Also within this category, you can find fresh tea.
    This refers to freshly brewed loose teas.
    """

    def __init__(self):
        super().__init__(sort='BlackTea', price=2.00)


class ThaiTea(BubbleTea):
    """
    This broadly refers to brewed tea blends without milk.
    Also within this category, you can find fresh tea. This refers to freshly brewed loose teas.
    """

    def __init__(self):
        super().__init__(sort='ThaiTea', price=2.00)


class TaroBubbleTea(BubbleTea):
    """Incorporates puréed taro, a purple root similar to sweet potato that has a toasty, sweet flavor."""

    def __init__(self):
        super().__init__(sort='TaroBubbleTea', price=2.00)
