from discord.ext import commands
import discord
import random
import sqlite3
import time
from datetime import datetime
import json
import asyncio

with open('jeo_0150.json') as f:
  copy = json.load(f)

cat = []
len_copy = len(copy)
for i in range(len_copy):
  dog = copy[i]['category']
  if(i % 10000 == 0):
    print(len_copy - i)
  if(('MOON' in dog) or ('NASA' in dog) or ('PLANET' in dog) or ('SPACE' in dog) or ('COSMO' in dog) or ('ASTRO' in dog)):
    cat.append(copy[i])
cat_ = json.dumps(cat, sort_keys=True, indent=1)
print(len(cat_))

with open('SPACE_1.json', 'w') as outfile:
  outfile.write(cat_)
outfile.close()
