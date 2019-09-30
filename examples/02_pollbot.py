import asyncio
import logging

import configloader as c
import rocketbot.bots as bots
import rocketbot.commands as com
import rocketbot.master as master
import rocketbot.models as m
import rocketbot.utils.poll as pollutil


async def main() -> None:
    loop = asyncio.get_event_loop()

    masterbot = master.Master(c.SERVER, c.BOTNAME, c.PASSWORD, loop=loop)

    # Get room info of the statusroom
    await masterbot.rest.login(c.BOTNAME, c.PASSWORD)
    result = (await masterbot.rest.rooms_info(room_name=c.POLL_STATUS_ROOM)).json()
    statusroom = m.create(m.Room, result['room'])
    pollmanager = await pollutil.PollManager.create_pollmanager(
        master=masterbot, botname=c.BOTNAME, statusroom=statusroom.to_roomref())

    # Create commands
    usage = com.Usage(master=masterbot)
    ping = com.Ping(master=masterbot)
    poll = com.Poll(master=masterbot, pollmanager=pollmanager)

    # Add a bot reacting on direct messages
    masterbot.bots.append(
        bots.RoomTypeCommandBot(
            master=masterbot, username=c.BOTNAME,
            enable_direct_message=True,
            commands=[usage, ping, poll]))

    async with masterbot:
        logging.info(f'{c.BOTNAME} is ready')
        await masterbot.ddp.disconnection()


if __name__ == '__main__':
    asyncio.run(main())
