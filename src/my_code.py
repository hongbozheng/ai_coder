###This file is generated by AI from prompts/src/my_code.py. DO NOT MODIFY THIS FILE MANUALLY###

import requests
import json

def get_top_hacker_news(keywords):
    """
    Function to fetch the top hacker news that mention certain keywords
    :param keywords: list, keywords to search in the news
    """
    def fetch_news():
        news_list = []
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        response = requests.get(url)
        top_stories = response.json()
        for story_id in top_stories:
            story_url = (
                f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
            story_response = requests.get(story_url)
            story = story_response.json()
            if 'title' in story:
                if any(keyword in story['title'].lower() for keyword in
                    keywords):
                    news_list.append({'title': story['title'], 'url': story
                        .get('url', 'No url')})
        return news_list

    return fetch_news()