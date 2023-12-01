data = [
    {"id": 1, "value": 42, "category": "A"},
    {"id": 2, "value": 58, "category": "B"},
    {"id": 3, "value": 73, "category": "A"},
    {"id": 4, "value": 90, "category": "C"},
    {"id": 5, "value": 64, "category": "B"}
]

total = sum(item["value"] for item in data)

print(total)