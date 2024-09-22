import time

def earliestFullBloom(plantTime:list[int], growTime:list[int]) -> int:
    """
    Calculate the earliest possible day where all seeds are blooming.
    Args:
        plantTime (list[int]): List of plant time of seeds
        growTime (list[int]): List of grow time of seeds    
    Returns:
        int: Earliest possible day where all seeds are blooming
    """
    # Combine both plantTime and growTime and sort based on growTime in descending order
    seeds = sorted(zip(plantTime, growTime), key=lambda x: -x[1])
    
    current_planting_time = 0  # Tracks the day we are planting
    latest_bloom_day = 0  # Tracks the latest bloom day
    
    for plant, grow in seeds:
        current_planting_time += plant  # Increment current day by the time it takes to plant this seed
        latest_bloom_day = max(latest_bloom_day, current_planting_time + grow)  # Calculate when this seed will bloom
    return latest_bloom_day  # Earliest possible day where all seeds are blooming

