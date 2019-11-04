from bs4 import BeautifulSoup
import csv
import requests
import time
source = requests.get('https://jovemnerd.com.br/nerdcast/').text

soup = BeautifulSoup(source, 'lxml')

# creating csv file
csv_file = open('nerdcast_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Summary', 'Link', 'Time'])

# tudo
for mainpg in soup.find_all('article'):
   
    # episode title
    title = mainpg.h2.a.text 
    print(title)

    # episode summary
    summary = mainpg.find('p', class_="entry-card__content-excerpt").text
    summary_split = summary.split('Clique para continuar lendo')[0]
    summary_split = summary_split.split(':')[1]
    print(summary_split)

    # episode page link
    link = mainpg.h3.p
    link = mainpg.find('a', href=True)
    link = link['href']
    print(link)

    # printing date and time
    time_date = mainpg.find('time')
    if time_date.has_attr('datetime'):
        # converting date format
        fix_date = time_date['datetime']
        fix_date = fix_date.replace('T', ' ')
        fix_date = fix_date.replace('-03:00', '')
        year = time.strptime(fix_date, "%Y-%m-%d %H:%M:%S").tm_year
        month = time.strptime(fix_date, "%Y-%m-%d %H:%M:%S").tm_mon
        day = time.strptime(fix_date, "%Y-%m-%d %H:%M:%S").tm_mday
        fix_date = ('%i/%i/%i' %(day, month, year))
        print('%i/%i/%i' %(day, month, year))

    print()

    csv_writer.writerow([title, summary_split, link, fix_date])

csv_file.close()