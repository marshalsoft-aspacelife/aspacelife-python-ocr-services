class SaveVideoFileResponseClass:
    """
    This class is defining the structure File object.
    """
    def __init__(self, filename: str, filepath: str, filesize: int):
        self.filename = filename
        self.filepath = filepath
        self.filesize = filesize
