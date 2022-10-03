'''WEB SCRAPING EXERCISE (solution by luan-brav0)'''

import requests
import bs4
# google = requests.get("https://www.google.com")
# print(google.text)

quotes_page = requests.get("http://quotes.toscrape.com/")   
quotes_soup = bs4.BeautifulSoup(quotes_page.text,"lxml")

'''Get authors: '''
author_class = quotes_soup.select('.author')
authors = []
for au in author_class:
    authors.append(au.text)

print("Authors: \n")
print(authors)
print('\n\n')

'''Get quotes: '''

quote_class = quotes_soup.select(".text")
quotes = []
for quo in quote_class:
    quotes.append(quo.text)

print("Quotes: \n")
print(quotes)
print('\n\n')

'''zipping quotes and authors (also prints page)'''
quotes_and_authors = list(zip(quotes, authors))

print("Quotes and Authors: \n")
print(quotes_and_authors)
print('\n\n')

'''Tags'''
tag_class = quotes_soup.select(".tag")
tags = []
for tag in tag_class:
    tags.append(tag.text)   

print("Top 10 Tags: \n")
print(tags)
print('\n\n')

print('\n\n')
print("Page .quotes: \n")
# print(quotes_soup)
# print(quotes_soup.select(".quote"))
# # print(quote_class)

print('\n\n')

quotes_pages_url = "http://quotes.toscrape.com/page/{}/"
formated_url = quotes_pages_url.format(3)
quotes_page = requests.get(formated_url)
quotes_soup = bs4.BeautifulSoup(quotes_page.text, 'lxml')
print("Multi Page .quotes: \n")
# print(quotes_soup)
# print(quotes_soup.select(".quote"))

def getQuotes(base_url = quotes_pages_url):
    '''Assumes str base_url
    Returns None
    Access and iterates through pages looking for tags .text , .author , span .tag
    finally, prints them nicely :).'''
    n = 1
    res = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    quote_class = soup.select(".quote")
    tags = []
    quotes = []
    authors = []
    
    while quote_class != []:
        '''Gets tags, quotes and authors from pages until page has no quotes'''
        tag_class = soup.select(".tags > .tag")
        for tag in tag_class:
            tags.append(tag.text)  

        quote_class = soup.select(".text")
        for quo in quote_class:
            quotes.append(quo.text)
        
        author_class = soup.select('.author')
        for au in author_class:
            authors.append(au.text)
        
        # next page
        n +=1
        res = requests.get(base_url.format(n))
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        quote_class = soup.select(".quote")    


    print("Quotes: \n")
    # list with quote-author tuples
    quotes_and_authors = list(zip(quotes, authors))
    for quote in quotes_and_authors:
        # [quote] by [author]
        print(quote[0],"\n\tby", quote[1])


    # # getting top 10 tag
    # get all tags
    unique_tags = {}
    for tag in tags:
        if tag in unique_tags:
            unique_tags[tag]  += 1 
        else:
            unique_tags[tag] = 1
    # print(unique_tags)
    unique_tags = dict(sorted(unique_tags.items(), key=lambda item: item[1])[::-1])
    # print(unique_tags)
    #for printing the top 10 tags
    rank = 10
    for key, value in unique_tags.items():
        # '10: comedy (8)'
        print(f'{rank}: {key} ({value})\n')
        rank -= 1
        if rank < 1:
            break
    return None    
    
    

getQuotes()

'''
    # # getting top 10 tag
    # get all tags
    unique_tags = {}
    for tag in tags:
        if tag in unique_tags:
            unique_tags[tag]  += 1 
        else:
            unique_tags[tag] = 1

    # Sorting tags in  unique tags by value (frequency)
    unique_tags = dict(sorted(unique_tags.items(), key=lambda item: item[1]))[::-1]
'''
        