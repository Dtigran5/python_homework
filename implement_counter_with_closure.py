def create_counter(value=0):
    counter_value = value

    def increment(amount=1):
        nonlocal counter_value
        counter_value += amount
        print(f"Counter incremented by {amount}. Current value: {counter_value}")

    def decrement(amount=1):
        nonlocal counter_value
        counter_value -= amount
        print(f"Counter decremented by {amount}. Current value: {counter_value}")

    def get_counter_value():
        print(f"Current counter value: {counter_value}")

    return increment, decrement, get_counter_value

counter_increment, counter_decrement, get_value = create_counter(5)

get_value()  # Output: Current counter value: 5

counter_increment()  # Output: Counter incremented by 1. Current value: 6
counter_increment(3)  # Output: Counter incremented by 3. Current value: 9

counter_decrement()  # Output: Counter decremented by 1. Current value: 8
counter_decrement(2)  # Output: Counter decremented by 2. Current value: 6

get_value()  # Output: Current counter value: 6

