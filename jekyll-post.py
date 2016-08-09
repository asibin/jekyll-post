import argparse
import datetime
import sys
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument("title", help="Post title. Only alfanumerics and dashes are allowed. Required.")
parser.add_argument("-t", "--tags", help="Comma separated list of tags. Defaults to 'blog'.")
parser.add_argument("-c", "--categories", help="Comma separated list of categories. Defaults to 'blog'.")
args = parser.parse_args()

post_template = """---
layout: post
title:  {title}
date:   {post_date}
categories: {post_categories}
tags: [{post_tags}]
---
"""


def sanitize_post_title(title):
    """
    Sanitizes post title for filename
    :param title: str: Title of blog post
    :return: str: Sanitized title containing only alafanumerics and dashes
    """
    title = title.lower().replace(' ', '-')
    if re.match('^[\w-]+$', title) is not None:
        return title
    else:
        print "Only alfanumerics and dashes are allowed"
        sys.exit(1)


def main():
    post_title = args.title

    if not args.categories:
        post_categories = "blog"
    else:
        post_categories = " ".join(args.categories.split(','))

    if not args.tags:
        post_tags = "blog"
    else:
        post_tags = ", ".join(args.tags.split(','))

    datetime_today = datetime.datetime.today()
    date_today = datetime_today.date()
    datetime_post = datetime_today.strftime("%Y-%m-%d %H:%M:%S")

    filename = "{}-{}.md".format(date_today, sanitize_post_title(post_title))
    file_path = os.path.join(os.getcwd(), "_posts", filename)

    post_header = post_template.format(title=post_title,
                                       post_date=datetime_post,
                                       post_categories=post_categories,
                                       post_tags=post_tags)

    with open(file_path, 'w') as post_file:
        post_file.write(post_header)

    print "Post: {} created!".format(filename)


if __name__ == '__main__':
    main()
