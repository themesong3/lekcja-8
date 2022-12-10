countries = [
    {"France": 67236432},
    {"Poland": 738753},
    {"USA": 758932},
    {"Germany": 649350},
    {"Turkey": 6233580}
]

for c in countries:
    for k, v in c.items():
        print(f"{k}: {v}")