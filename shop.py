from sales import Sales
from sorts import *
from inventory import Inventory
from cash_register import CashRegister
from employee import Employee


class BubbleTeaShop(Sales, Inventory, CashRegister):
    """A class representing the main shop."""

    def __init__(self):
        """Initialize."""
        super(Sales, self).__init__()
        super(Inventory, self).__init__()
        super(CashRegister, self).__init__()

        self.employees = []
        self._break = False

    async def sell(self, item: BubbleTea):
        """Sell a bubble tea."""
        if item in self.inventory:
            self.sales.remove(item)
            self.money += item.price
            print(f'Sold {item} and earned ${item.price}')
        else:
            print(f'Item {item} ran out of stock!')

    async def makeTea(self, item: BubbleTea):
        """Make a bubble tea."""
        self.inventory.append(item)
        print(f'Made {item}')

    async def hireEmployee(self, employee: Employee):
        """Hire an employee."""
        self.employees.append(employee)
        print(f'Hired {employee}')

    async def work(self):
        while self._break is False:
            task = ...
