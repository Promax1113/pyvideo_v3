import praw


def get_post_list(instance: praw.Reddit, subreddit: str, mode: str = "hot", amount: int = 10) -> list:
    print(f"Fetching {mode} {amount} post(s) from {subreddit}...")
    print("Keep in mind that the NSFW posts will be removed afterwards.")
    match mode:
        case "hot":
            return [submission for submission in instance.subreddit(subreddit).hot(limit=amount)]
        case "top":
            return [submission for submission in instance.subreddit(subreddit).top(limit=amount)]
        case "rising":
            return [submission for submission in instance.subreddit(subreddit).rising(limit=amount)]
        case "new":
            return [submission for submission in instance.subreddit(subreddit).new(limit=amount)]
