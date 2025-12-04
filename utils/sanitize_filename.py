def sanitize_filename(filename: str) -> str:
    """Remove unsafe characters from filename."""
    # Remove path separators and other unsafe characters
    unsafe_chars = ['/', '\\', '..', '<', '>', ':', '"', '|', '?', '*']
    for char in unsafe_chars:
        filename = filename.replace(char, '_')
    return filename.strip()
