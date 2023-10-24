# Import Modules
import requests
from bs4 import BeautifulSoup
import json


# Declare Global Variables
big_data = []
eps = 1
master_site = 'https://www.j-archive.com/showgame.php?game_id='


# Make HTTP request and parse the response
def get_soup(site):
    pull = requests.get(site)
    return BeautifulSoup(pull.text, 'html.parser')


# Find clues from HTML document
def get_clues(soup_):
    return [soup_.find('td', {'id': 'clue_' + round_ + '_' + str(i + 1) + '_' + str(j + 1)})
            if (round_:='DJ' if h else 'J')
            else 'Empty'
            for h in (0, 1) for i in range(6) for j in range(5)] \
           + [soup_.find('td', {'id': 'clue_FJ'})]


# Find Answers from HTML document
def get_answers(soup_):
    def get_response_answer(clue_id):
        try:
            clue = str(soup_.find('td', {'id':clue_id}))
            return clue.split('response">')[1].split('</em')[0]
        except:
            return 'Empty'

    return [get_response_answer(f'clue_{round_}_{i + 1}_{j + 1}_r')
            if (round_:='DJ' if h else 'J') 
            else 'Empty'
            for h in (0, 1) for i in range(6) for j in range(5)] \
           + [get_response_answer('clue_FJ_r')]


# Get amounts
def get_amounts():
    return [(h+1) * (j+1) * 100 for h in (0, 1) for _ in range(6) for j in range(5)] + [0]


# Get Categories from HTML document
def get_categories(soup_):
    categories = [cat.text for cat in soup_.find_all('td', {'class', 'category_name'})]
    return [categories[i] if (i <= 5 if h == 0 else 6 <= i < 12) else 'None'
            for h in (0, 1) for i in range(6) for _ in range(5)] + [categories[12]]


# Convert Audio, Pic, Video locations from Html to bool
def find_media(soup_, media_ext):
    find_media = lambda _: (_.index(media_ext) if media_ext in str(_) else False)
    return [find_media(soup_.find('td', {'id': f'clue_{round_}_{i + 1}_{j + 1}'}))
            if (round_:='DJ' if h else 'J')
            else False
            for h in (0, 1) for i in range(6) for j in range(5)] \
           + [find_media(soup_.find('td', {'id': 'clue_FJ'}))]


# Final formatting as a dictionary
def format_lib(*args):
    keys = ['code', 'clue', 'show_number', 'show_url', 'category',
            'answer', 'amount', 'audio', 'image', 'video']
    return [dict(zip(keys, data)) for data in zip(*args)]


# Write to JSON file
def write_to_json_file(file_name, big_data):
    with open(file_name, 'w') as f:
        json.dump(big_data, f, indent=1)


# Main Function
def main():
    for ep in range(9000):
        url = master_site + str(ep)
        soup = get_soup(url)
        title = soup.find('title').text[19:-18]
        row_col = [f'{title}_{"DJ" if h else "J"}_{i + 1}_{j + 1}' for h in (0, 1) for i in range(6) for j in range(5)]

        if (soup.find('div', {'id': 'content'}).text[:3] != 'ERR'):
            categories = get_categories(soup)
            clues = get_clues(soup)
            answers = get_answers(soup)
            amounts = get_amounts()
            audios = find_media(soup, 'mp3')
            images = find_media(soup, 'jpg')
            videos = find_media(soup, 'mp4')

            big_data.extend(format_lib(row_col, clues, [title]*61, [url]*61, categories, answers, amounts,
                                        audios, images, videos))
            print(f'{title} {ep}')
            write_to_json_file('jeo.json', big_data)


if __name__ == '__main__':
    main()
