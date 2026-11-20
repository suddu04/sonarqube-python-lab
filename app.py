
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def get_user_query(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    return query, (user_id,)


def calculate_total(price, quantity):
    return price * quantity


def main():
    print("Welcome to SonarQube Training Lab")

    print(divide_numbers(10, 2))

    total = calculate_total(100, 5)

    print("Total:", total)


if __name__ == "__main__":
    main()
