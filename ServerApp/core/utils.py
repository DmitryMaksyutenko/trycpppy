def user_to_string(obj) -> str:
    """Create string based on User model fields and values."""
    return f"username={obj.username}" + \
        f" first_name={obj.first_name}" + \
        f" last_name={obj.last_name} email={obj.email}"
