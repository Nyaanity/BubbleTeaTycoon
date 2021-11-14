from shop import BubbleTeaShop
from sorts import *
from sales import *
import os
import asyncio
from employee import Employee


#os.system('clear' if not Exception else 'cls')
shop = BubbleTeaShop()


@shop.observer()
async def on_employee_hire(employee: Employee):
    ...


@shop.observer()
async def on_item_sell(item: BubbleTea, money_before: int, money_after: int):
    ...


@shop.observer()
async def on_item_creation(item: BubbleTea):
    ...


@shop.observer()
async def on_ready():
    ...


@shop.observer()
async def on_break():
    ...


def main():
    loop.create_task(shop.work())
    loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    main()
