import praw


from security import get_key_and_name
from scrapper import get_post_list
from setup import setup



if __name__ == "__main__":
    name, key = get_key_and_name()
    config = setup()

    ins = praw.Reddit(client_id=name, client_secret=key, user_agent="scrapper")
    submissions: list = []

    # TODO Make a small user inteface that asks which subreddit and all that stuff.
    for post in get_post_list(instance=ins, subreddit=config["name"], time_filter=config["top_filter"], mode=config["mode"]):
        if post.over_18:
            continue
        submissions.append({"title": post.title, "submission": post})
        print(f"Title: {post.title}")
