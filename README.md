# Web Scraping

In this project, I do a Web Scraping on the blog site of Digital Innovation One, using python 3.

## What is Web-Scraping?[1]

Web scraping is the process of collecting structured data from the web in an automated way. Also known as web data extraction. Some of the top web scraping use cases include price tracking, price intelligence, news tracking, lead generation, and market research, among many other uses.

In general, web data mining is used by people and companies who want to use the vast amount of publicly available web data to make smarter decisions.

If you've ever copied and pasted information from a website, you've performed the same function as any “scraper” on the web, just on a microscopic, manual scale. Unlike the mundane and mind-numbing process of manually extracting data, web scraping uses intelligent automation to retrieve hundreds, millions, or even billions of data points from the Internet's seemingly infinite frontier.

And it shouldn't be surprising, because web scraping provides something really valuable that nothing else can: it provides structured web data from any public site.

More than a modern convenience, the real power of web scraping lies in its ability to create and power some of the most revolutionary business applications in the world. “Transformative” doesn't even begin to describe how some companies use data collected from the web to improve their operations, from informing executive decisions to individual customer service experiences.

## Technologies used

The construction of the algorithm was entirely done in python, using the following libraries:

- json[2] 
- Requests[3]
- BeautifulSoup[4]

### Json[2]

The Json library was used to store data in .json format, in an organized way, similar to python 3 dictionaries. With this storage format, it is possible to have a greater ease in the implementation of machine learning techniques, the transition from dictionaries to csv datasets is easy to implement.

### Requests[3]

This library is an easy and automated way to make HTTP requests through python. It abstracts the complexities of making requests behind a nice, simple API so you can focus on interacting with services and consuming data in your app.

Throughout this article, you’ll see some of the most useful features that requests has to offer as well as how to customize and optimize those features for different situations you may come across. You’ll also learn how to use requests in an efficient way as well as how to prevent requests to external services from slowing down your application.

### BeautifulSoup[4]

With the need to encode the information coming from the request, as well as the need for an HTML Parser, this is where the need to use the BeautifulSoup library comes in, thus extracting data from all types of websites becomes an easy task.

## References

- O que é Web Scraping? Para iniciantes
\
[1]: https://www.gocache.com.br/seguranca/o-que-e-web-scraping-para-iniciantes/

- json[2]
\
[2]: https://docs.python.org/3/library/json.html

- Requests[3]
\
[3]: https://docs.python-requests.org/en/latest/

- BeautifulSoup[4]
\
[4]: https://pypi.org/project/beautifulsoup4/
