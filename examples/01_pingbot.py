import asyncio
import logging

import configloader as c
import rocketbot.bots as bots
import rocketbot.commands as com
import rocketbot.master as master


async def main() -> None:
    loop = asyncio.get_event_loop()

    masterbot = master.Master(c.SERVER, c.BOTNAME, c.PASSWORD, loop=loop)

    # Create a dummy command. On commmand 'ping' reply with 'pong'
    ping = com.Ping(master=masterbot)

    # Add a bot reacting on '@botname command' with the ping command
    masterbot.bots.append(
        bots.RoomTypeMentionCommandBot(
            master=masterbot, username=c.BOTNAME,
            enable_public_channel=True, enable_private_groups=True,
            commands=[ping]))

    # Start the masterbot and wait for messages
    async with masterbot:
        logging.info(f'{c.BOTNAME} is ready')
        await masterbot.ddp.disconnection()


if __name__ == '__main__':
    asyncio.run(main())
