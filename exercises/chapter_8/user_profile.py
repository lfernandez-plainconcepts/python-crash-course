def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing user profile information."""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

# Example usage
user_profile = build_profile('john', 'doe', age=30, location='new york')
print(user_profile)