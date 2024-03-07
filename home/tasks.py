from bucket import bucket



# TODo: can be async?
def all_bucket_objects_task():
    result = bucket.get_objects()
    return result