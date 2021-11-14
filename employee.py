import names
import asyncio
from sorts import *
from random import choice


class Employee:
    """The base class of all employees."""

    def __init__(self, *a, **kw):
        """Initialize."""
        self.name = kw.get('name')
        self.shop = kw.get('shop')
        self.productivity = kw.get('productivity')

    def __repr__(self):
        return f'<Employee name={self.name} shop={self.shop} productivity={self.productivity}>'

    def __str__(self):
        return self.sort


class Maker(Employee):
    """A class representing an employee making bubbleteas."""

    def __init__(self, shop):
        """Initialize."""
        super().__init__(
            name=names.get_full_name(),
            shop=shop,
            productivity=choice([0.5, 0.75, 1.0, 1.25, 1.5])
        )

    async def work(self):
        while 1:
            item = choice([sort() for sort in BubbleTea.__subclasses__()])
            await self.shop.makeTea(item)
            await self.shop.printQuery(self.shop.__base__())
            await asyncio.sleep(self.productivity)


class Seller(Employee):
    """A class representing an employee selling bubbleteas."""

    def __init__(self, shop):
        """Initialize."""
        self.shop = shop
        super().__init__(
            name=names.get_full_name(),
            shop=self.shop,
            productivity=choice([0.5, 0.75, 1.0, 1.25, 1.5])
        )

    async def work(self):
        while 1:
            if len(self.shop.inventory) > 0:
                item = choice(self.shop.inventory)
                await self.shop.sell(item)
                await self.shop.printQuery(self.shop.__base__())
            await asyncio.sleep(self.productivity)
