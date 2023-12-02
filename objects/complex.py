from typing import List, Dict, Union, Any
def complex_aggregate(data: List[Dict[str, Union[str, int, float]]], agg_key: str) -> Dict[str, Dict[str, Any]]:
    result = {}
    sub_key = ""
    for entry in data:
        key = entry[agg_key]
        if key not in result:
            result[key]= {}
        for sub_key, value in entry.items():
            if sub_key == agg_key:
                continue
            if sub_key not in result[key]:
                result[key][sub_key] = {"count": 0, "sum": 0 if isinstance(value, (int, float)) else None, "unique": set()}
            result[key][sub_key]["count"] += 1
            if isinstance(value, (int, float)):
                result[key][sub_key]["sum"] += value
            result[key][sub_key]["unique"].add(value)
    for key in result:
        for sub_key in result[key]:
            result[key][sub_key]["unique"] = list(result[key][sub_key]["unique"])
    return result

data = [
    {"department": "Sales", "employee": "Alice", "sales": 150},
    {"department": "Sales", "employee": "Bob", "sales": 200},
    {"department": "HR", "employee": "Charlie", "sales": 50}
]
agg_key = "department"
print(complex_aggregate(data, agg_key))
'''
{
    "Sales": {"employee": {"count": 2, "unique": {"Alice", "Bob"}},
              "sales": {"count": 2, "sum": 350, "unique": {150, 200}}},
    "HR": {"employee": {"count": 1, "unique": {"Charlie"}},
           "sales": {"count": 1, "sum": 50, "unique": {50}}}
}
'''