# Examples
This is a collection of examples of how to use the rocketbot module.

## Example 01: Ping bot
This is the most basic example. The bot reacts on:

user: `@botname ping`

in *any private or public room* it is part in. It then replys with:

bot: `Pong`

## Example 02: Poll bot
This more sophisticated example contains a poll bot. In a *direct message* type:

user: `poll "Do you like cookies?" Yes No "I :heart: :cookie:"`

The bot sends you a draft poll message. You can edit that message by editing your own or by sending a new one. When you are satisfied, write:

`poll_push #roomname`
