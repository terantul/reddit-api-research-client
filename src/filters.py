def apply_filters(posts):
    def is_valid(post):
        title = post["data"].get("title", "")
        if len(title.split()) < 3:
            return False
        if "bot" in title.lower() or "promo" in title.lower():
            return False
        return True

    return [post for post in posts if is_valid(post)]