import datetime
import sys
import re
import os

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
    post_title = raw_input("Please input post title: ")
    post_categories = raw_input("Please input post categories (optional): ")
    post_tags = raw_input("Please input post tags (optional): ")

    if post_categories == '':
        post_categories = "blog"

    if post_tags == '':
        post_tags = "blog"
    else:
        post_tags = ", ".join(post_tags.split(" "))

    datetime_today = datetime.datetime.today()
    date_today = datetime_today.date()
    datetime_post = datetime_today.strftime("%Y-%m-%d %H:%M:%S")

    filename = "_{}-{}.md".format(date_today, sanitize_post_title(post_title))
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
