import os
import logging
from linelib import Client
from my_cogs import Main,EasterEgg
import time
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

client = Client(os.environ['cs'], os.environ['at'])
client.load_cog(Main)
client.load_cog(EasterEgg)

@client.event("ready")
def ready():
  clear()
  print("牛牛Line v0.0.2")
  f = open("readytime.txt", "w")
  f.write(str(time.time()*1000))
  f.close()

client.run(
  host="0.0.0.0", 
  port=8080,
  LOG_LEVEL=logging.ERROR
)
