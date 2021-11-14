from sales import Sales
from sorts import *
from inventory import Inventory
from cash_register import CashRegister
from employee import *
from display import Display
import aioconsole
from events import Events
from random import choice
import os
import asyncio


class BubbleTeaShop(Sales, Inventory, CashRegister, Display, Events):
    """A class representing the main shop."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.employees = []
        self._break = False

    def __base__(self):
        """The shop's base information."""
        return '\n'.join([
            '------ Sales ------',
            f'Sold: {len(self.sales)}',
            f'Money: {self.money}',
            f'Left: {len(self.inventory)}',
            f'Employees: {len(self.employees)}',
            '------ Shop ------',
            '1> Make bubbletea',
            '2> Sell bubbletea (+$1-3)',
            '3> Hire random employee (=$100)',
            '4> Hire maker (=250$)',
            '5> Hire seller (=250$)',
            '6> Restart',
            '7> Break\n'
        ])

    async def sell(self, item: BubbleTea):
        """Sell a bubble tea."""
        self.inventory.remove(item)
        money_before = self.money
        self.money += item.price
        self.sales.append(item)
        await self.dispatch('item_sell', item, money_before, self.money)

    async def makeTea(self, item: BubbleTea):
        """Make a bubble tea."""
        self.inventory.append(item)
        await self.dispatch('item_creation', item)

    async def hireEmployee(self, employee: Employee):
        """Hire an employee."""
        self.employees.append(employee)
        await self.dispatch('employee_hire', employee)
        loop = asyncio.get_event_loop()
        loop.create_task(employee.work())

    async def work(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.printIn())
        await self.dispatch('ready')
        await self.printQuery(self.__base__())

        while self._break is False:
            await self.printQuery(self.__base__())
            
            task = await aioconsole.ainput('> ')

            if task == '1':
                item = choice([sort() for sort in BubbleTea.__subclasses__()])
                await self.makeTea(item)

            elif task == '2':
                if len(self.inventory) > 0:
                    item = choice(self.inventory)
                    await self.sell(item)

            elif task == '3':
                if self.money >= 100:
                    self.money -= 100
                    await self.hireEmployee(choice([employee(self) for employee in Employee.__subclasses__()]))

            elif task == '4':
                if self.money >= 250:
                    self.money -= 250
                    await self.hireEmployee(Maker(self))

            elif task == '5':
                if self.money >= 250:
                    self.money -= 250
                    await self.hireEmployee(Seller(self))

            elif task == '6':
                os.system('clear' if not Exception else 'cls')
                os.system(__file__)

            elif task == '7':
                exit(code=0)

        await self.dispatch('break')
