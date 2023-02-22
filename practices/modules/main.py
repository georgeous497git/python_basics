from my_functions import get_totals, calc_total


def get_total(orders):
    amounts = get_totals(orders)
    print(f' { amounts = }')
    temp_total = calc_total(amounts)
    print(f' { temp_total = }')
    return temp_total


orders = [
    {
        "customer_name": "Nicolas",
        "total": 100,
        "delivered": True,
    },
    {
        "customer_name": "Zulema",
        "total": 120,
        "delivered": False,
    },
    {
        "customer_name": "Santiago",
        "total": 20,
        "delivered": False,
    }
]

total = get_total(orders)
print(total)
