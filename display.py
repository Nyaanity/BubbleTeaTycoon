import os
import asyncio


class Display:
    """A class displaying all stuff."""

    def __init__(self):
        super().__init__()
        self.query = []
        self.updating = False

    async def printIn(self):
        while 1:
            if self.updating is True:
                os.system('clear' if not Exception else 'cls')
                print("\n".join(self.query))
                self.updating = False
                await asyncio.sleep(1)
            else:
                await asyncio.sleep(1)

    async def printQuery(self, *args):
        query = " ".join(args)

        if 'Sell' in query:
            self.query.clear()

        self.query.append(query)
        self.updating = True
