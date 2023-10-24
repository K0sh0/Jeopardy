# importing necessary libraries
from discord.ext import commands
import discord
import random
import sqlite3
import time
from datetime import datetime
import json
import asyncio

# loading JSON file
with open('jeo_0150.json') as f:
    # parsing JSON file
    copy = json.load(f)

# dictionary to store categories count
cat = {}

# iterate through each item in copy
for i, item in enumerate(copy):
    # extracting category of the item
    dog = item['category']

    # printing remaining iterations for every 10,000th iteration
    if i % 10000 == 0:
        print(len(copy) - i)

    # updating count of each category in cat dictionary
    cat[dog] = cat.get(dog, 0) + 1

# converting dictionary of categories into JSON
cat_ = json.dumps(cat, sort_keys=True, indent=1)

# printing categories count and its JSON representation
print(cat)
print(cat_)

# saving JSON representation into file
with open('SORT_ALL_CAT.json', 'w') as outfile:
    outfile.write(cat_)
