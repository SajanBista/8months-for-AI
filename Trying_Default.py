messy_dict = {
    "numbers": [1, 2, 3, {"nested": (4, 5, 6)}, set([7, 8, 9])],
    True: {
        "name": "John",
        "data": [None, False, 3.14],
        "mixed": ("a", 1, [1, 2], {"x": 100}),
    },
    (1, "tuple"): {"lists": [[1], [2, 2], [3, 3, 3]], "dict": {"a": 1, "b": {"c": 3}}},
    None: "exists",
    42: [lambda x: x * 2, {1, 2, 3}, {"key": []}],
}

# Test print to verify it works
print(messy_dict)
print(messy_dict[True]["mixed"][3]["x"])  # Access nested value
print(messy_dict[(1, "tuple")]["lists"][2])  # Access nested list
