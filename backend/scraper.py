import feedparser

def fetch_business_news():
    feed = feedparser.parse("https://news.ycombinator.com/rss")

    news = []
    for entry in feed.entries:
        title = entry.title.lower()
        if "business" in title or "startup" in title:
            news.append(entry.title)

    return news[:5]
