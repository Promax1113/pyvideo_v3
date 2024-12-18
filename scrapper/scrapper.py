import praw


def get_post_list(
    instance: praw.Reddit,
    subreddit: str,
    mode: str = "hot",
    time_filter: str = "all",
    amount: int = 10,
) -> list:
    print(
        f"\nFetching {amount} {f'{mode} of {time_filter}' if mode == 'top' else mode} post(s) from {subreddit}..."
    )
    print("Keep in mind that the NSFW posts will be removed afterwards.\n")
    match mode:
        case "hot":
            return list(instance.subreddit(subreddit).hot(limit=amount))
        case "top":
            return list(
                instance.subreddit(subreddit).top(time_filter=time_filter, limit=amount)
            )
        case "rising":
            return list(instance.subreddit(subreddit).rising(limit=amount))

        case "new":
            return list(instance.subreddit(subreddit).new(limit=amount))
