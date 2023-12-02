from typing import List, Dict, Union

def aggregate_scores(data: List[Dict[str, Union[str, int]]]) -> Dict[str, int]:
    result = {}
    for item in data:
        name = item["name"]
        score = item["score"]
        result[name] = result.get(name, 0) + score
    print(result)
aggregate_scores([
    {"name": "Charlie", "score": 12},
    {"name": "Delta", "score": 9},
    {"name": "Charlie", "score": 8}
]) 
