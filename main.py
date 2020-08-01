import os
from dotenv import load_dotenv
from instabot import Bot
import re
import random
import argparse


def check_if_user_exists(username):
    user_id = bot.get_user_id_from_username(username)
    return bool(user_id)


def get_right_commenters(comments):
    right_commenters = []
    for comment in comments:
        comment_text = comment['text']
        commenter_user_id = comment['user_id']
        mentioned_usernames = re.findall(r'@(\w+)', comment_text)
        for mentioned_username in mentioned_usernames:
            if_user_id_true = check_if_user_exists(mentioned_username)
            if if_user_id_true:
                right_commenters.append(str(commenter_user_id))
    return right_commenters


def get_liked_and_followed(media_likers,
                           right_commenters_id,
                           followers_of_media_author):
    commenters_who_liked = set(media_likers) & set(right_commenters_id)
    commenters_who_followed = set(commenters_who_liked)\
                              & set(followers_of_media_author)
    return list(commenters_who_followed)

def get_winner(commenters_who_followed):
    winner_id = random.choice(commenters_who_followed)
    winner_username = bot.get_username_from_user_id(winner_id)
    return winner_username


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description='Takes three arguments.'
                    '1. Media URL'
                    '2. Media authors username'
                    '3. friends_mentions_number ')

    parser.add_argument('url',
                        type=str,
                        help='The url of instagram post')
    parser.add_argument('username',
                        type=str,
                        help='The Instagram post authors username')
    return parser


if __name__ == '__main__':
    load_dotenv()
    instagram_username = os.getenv('INSTAGRAM_USERNAME')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD')
    bot = Bot()
    bot.login(username=instagram_username,
              password=instagram_password)

    parser = get_argument_parser()
    args = parser.parse_args()
    media_url = args.url
    media_authors_username = args.username

    media_id = bot.get_media_id_from_link(media_url)
    comments = bot.get_media_comments(media_id)
    media_likers = bot.get_media_likers(media_id)
    followers_of_media_author = bot.get_user_followers(media_authors_username)

    right_commenters_id = get_right_commenters(comments)
    commenters_who_followed = get_liked_and_followed(media_likers,
                                                     right_commenters_id,
                                                     followers_of_media_author)

    winner = get_winner(commenters_who_followed)

    print('The Winner is:> ' + winner)
