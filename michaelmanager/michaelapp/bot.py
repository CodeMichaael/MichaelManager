from interactions import OptionType, slash_option, slash_command
from .models import *
import requests

api_url = 'http://127.0.0.1:8000/connections'
platform = interactions.Client(token="token")


@interactions.slash_command(name='connect', description='Connect to MichaelManager', default_member_permissions=interactions.Permissions.ADMINISTRATOR)
@interactions.slash_option(name="connection_id", description="Enter the connection ID given to you.", required=True, opt_type=OptionType.STRING)
async def connect(ctx, connectionid: str):
    validate = ConnectionManager.objects.filter(connection_id=connectionid)
    if validate:
        manager = ConnectionManager.objects.get(connection_id=connectionid)
        manager.user_id = ctx.author.id
        comp_id = manager.to_computer_id
        manager.save()
        await ctx.send(f"<:planet:1152445018259329034> **Connection Status** Sucessfully connected to {comp_id}")
    else:
        await ctx.send("<:planet:1152445018259329034> **Connection Status** Connection ID not found.")

# You can choose how you'd like to use the task command.

platform.start()