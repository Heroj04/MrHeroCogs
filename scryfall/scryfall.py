import scrython
from redbot.core import commands


class Scryfall(commands.Cog):
    """Cog to search for Magic The Gathering Cards on Scryfall"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx:commands.Context, name: str):
        """This does stuff!"""
        # Trigger typing to indicate web request
        ctx.trigger_typing()
        card = {}
        
        try:
            card = scrython.Named(fuzzy = name)
        except:
            await ctx.send("Card not found")
            return

        await ctx.send(card.oracle_text)
