import boto3
import os
from typing import Optional

# Get AWS authentication credentials from environment variables
aws_profile = os.environ.get("AWS_PROFILE")
aws_region = os.environ.get("AWS_REGION", "ap-northeast-1")  # Default is Tokyo region

# Initialize ECS client
def get_ecs_client():
    """
    Create and return a boto3 ECS client with the proper authentication credentials.
    Uses AWS_PROFILE environment variable if set, otherwise uses default credentials.
    """
    session = boto3.Session(
        profile_name=aws_profile,
        region_name=aws_region
    )
    return session.client('ecs')

# Utility function to chunk a list into smaller batches
def chunk_list(lst, chunk_size):
    """
    Split a list into smaller chunks of a specified size.
    
    Args:
        lst: The list to split
        chunk_size: The size of each chunk
        
    Returns:
        A list of lists, where each inner list is a chunk of the original list
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
