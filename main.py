import os
import discord
import random
from replit import db
from keep_alive import keep_alive

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)

hutao_quotes = [
  "Yoh, now why might you be looking for me, hm?",
  "Oh, you didn't know? I'm the 77th Director of the Wangsheng Funeral Parlor, Hu Tao.",
  "When the sun's out, bathe in sunlight. But when the moon's out, bathe in moonlight~",
  "Lemme show you some fire tricks. First... Fire! And then... Whoosh! Fire butterfly! Be free!",
  "Run around all you like during the day, but you should be careful during the night.",
  "When I'm not around, best keep your wits about you.",
  "Need a hand, need a hand? I'm here! If you need some assistance, I'm here to give it my all to the very end!",
  "Vision... Vision...? Oh, this thing? Yeah, whatever...",
  "Wangsheng Funeral Parlor is special, in that it carries a dual responsibility, to those both of this realm, and the next.",
  "Have you seen Qiqi? Tell me where she is, quickly. I need to go seal her away, hee-hee!",
  "♪Silly-churl, billy-churl, silly-billy hilichurl. Frilly-churl, willy-churl, frilly-willy hilichurl♪ Ah, hehe...",
  "Versemonger of the darkest alleys — that's me!",
  "I'm Wangsheng Funeral Parlor's 77th Funeral Director, my grandfather was the 75th.",
  "*sigh* I gotta find something fun to do... Sitting around doing nothing is a fate worse than death.",
]

if "responding" not in db.keys():
  db["responding"] = True


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"] is True:
    if msg.startswith('$yoh'):
      quote = random.choice(hutao_quotes)
      await message.channel.send(quote)

  if msg.startswith('$wake'):
    db["responding"] = True
    await message.channel.send("*Well are those who rise in the early morn, while those late to bed I shall forewarn~*")

  if msg.startswith('$sleep'):
    db["responding"] = False
    await message.channel.send("*Oh, you sleepy? Get some rest, I'm gonna take a walk by myself...*")


keep_alive()
client.run(os.environ['TOKEN'])