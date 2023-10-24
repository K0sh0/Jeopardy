import json

# Initialize all arrays
goods, finals, audios, videos, images = [], [], [], [], []

# Open and load the json file
with open('jeo_0_6646.json') as f:
  copy = json.load(f)

# Loop through the data, and append to the appropriate array based on conditions
for item in copy:
    if item['answer'] == 'Empty':
        finals.append(item)
    elif item['audio']:
        audios.append(item)
    elif item['image']:
        images.append(item)
    elif item['video']:
        videos.append(item)
    else:
        goods.append(item)

# Print out the length of each array for verification
print(len(goods), len(finals), len(audios), len(videos), len(images))

# Function to write each list to a file
def write_to_file(data, filename):
  with open(filename, 'w') as f:
    json.dump(data, f, indent = 1)

# Write the arrays to json files
write_to_file(goods, 'goods.json')
write_to_file(finals, 'finals.json')
write_to_file(audios, 'audios.json')
write_to_file(videos, 'videos.json')
write_to_file(images, 'images.json')
