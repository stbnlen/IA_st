from collections import Counter
from typing import List, Optional, Counter

def questions(df: List[str], aspectos: List[str], default_one: Optional[str] = None, default_two: Optional[str] = None) -> Counter:
    aspect_counts = Counter()

    unique_aspects = {aspect for aspect in aspectos}
    aspects = (x.replace(", ", ",").split(",") for x in df)
    aspect_counts.update([aspect for aspect_list in aspects for aspect in aspect_list if aspect in unique_aspects])
                
    if default_one is not None:
        aspect_counts[default_one] += 1
    if default_two is not None:
        aspect_counts[default_two] += 1

    return aspect_counts