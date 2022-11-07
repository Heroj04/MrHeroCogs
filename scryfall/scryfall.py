import scrython
from redbot.core import commands


class Scryfall(commands.Cog):
    """Cog to search for Magic The Gathering Cards on Scryfall"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scryfall(self, ctx:commands.Context, name: str):
        """Search for a card"""
        # Trigger typing to indicate web request
        ctx.trigger_typing()
        card = {}
        
        try:
            card = scrython.Named(fuzzy = name)
        except Exception as e:
            await ctx.send(f"Card not found: {str(e)}")
            return

        await ctx.send(card.oracle_text)
