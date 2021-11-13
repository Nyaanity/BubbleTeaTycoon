from shop import BubbleTeaShop
from sorts import *
from sales import *
import os
import asyncio


def main():
    loop.create_task(shop.work())
    loop.run_forever()


if __name__ == '__main__':
    os.system('clear' if not Exception else 'cls')
    loop = asyncio.get_event_loop()
    shop = BubbleTeaShop()
    main()
