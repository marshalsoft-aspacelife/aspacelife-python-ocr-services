class KafkaResponseClass :
    """
    This class is defining the structure File object.
    """
    def __init__(self, postId: str, resourceId: str, resourceType: str,status:str,resourceTextBody:str):
        self.postId = postId
        self.resourceId = resourceId
        self.resourceType = resourceType
        self.status = status
        self.resourceTextBody = resourceTextBody