# IMPORTING LIBRARIES
import requests
from bs4 import BeautifulSoup
import json
import re

# OPENING THE SOURCE JSON FILE
with open('jeo_0_6646.json') as f:
  data = json.load(f)

# DEFINING JSON FILES FOR EACH CATEGORY
files = {
    'goods.json': [],
    'finals.json': [],
    'audios.json': [],
    'videos.json': [],
    'images.json': []
}

# FILTERING DATA
for entry in data:
  if entry['answer'] == 'Empty':
    files['finals.json'].append(entry)
  elif entry['audio'] != False:
    files['audios.json'].append(entry)
  elif entry['image'] != False:
    files['images.json'].append(entry)
  elif entry['video'] != False:
    files['videos.json'].append(entry)
  else:
    files['goods.json'].append(entry)

# PRINTING THE NUMBER OF ITEMS IN EACH CATEGORY
for file_name, entries in files.items():
  print(f"{file_name}: {len(entries)} items")

# SAVING FILTERED DATA INTO SEPARATE JSON FILES
for file_name, entries in files.items():
  with open(file_name, 'w') as f:
    json.dump(entries, f, indent=1)
