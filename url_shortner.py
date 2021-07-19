__author__ = "Lokanath Reddy E"
import sys
import csv
from hashids import Hashids
hashids = Hashids(min_length=4, salt="KanB@n")

# Writting code by accessing the file.
# Assuming 1st line will be as below
# id,url,short_url
# I am considering my project website as https://local.urlshortner.com

class ShortUrlGenerator(object):
    def shorten_url(self, url):
        if not url:
            return "Invalid URL"
        with open('short_urls.csv', 'r') as short_urls_file:
            data = csv.DictReader(short_urls_file)
            for each_url in data:
                if url == each_url["url"]:
                    return each_url["short_url"]

        with open('short_urls.csv', 'ab+') as short_urls_file:  # Since i use windows machine its appending extra \
                                                                # new line so i am opening in append in binarymode.
            file_content = list(csv.reader(short_urls_file))
            url_id = len(file_content)+1                        # +1 because we are assuming 1st line will be headings of each column.
            short_url_id = hashids.encode(url_id)
            short_url = "https://local.urlshortener.com/"+ short_url_id
            short_url_writter = csv.writer(short_urls_file)
            short_url_writter.writerow([url_id,url,short_url])
            short_urls_file.close()
            return short_url

short_url_obj = ShortUrlGenerator()
print short_url_obj.shorten_url(sys.argv[1])