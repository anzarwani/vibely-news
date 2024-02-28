import feedparser

def fetch_news_from_rss(feed_url, num_articles=5):
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries[:num_articles]:
        news_dict = {
            'headline': entry.title,
            'text': entry.summary,
            'link': entry.link
        }
        articles.append(news_dict)

    return articles

'''if __name__ == "__main__":
    feed_url = 'https://feeds.skynews.com/feeds/rss/home.xml'
    num_articles = 5
    news_articles = fetch_news_from_rss(feed_url, num_articles)'''

    #print("Fetched News Articles:")
    #for idx, article in enumerate(news_articles, 1):
        #print(f"Article {idx}:")
        #print(f"Headline: {article['headline']}")
        #print(f"Text: {article['text']}")
        #print(f"Link: {article['link']}")
        #print()
