def dict_fruit():
    fruit_count = {}

    while True:
        fruit = input("enter a fruit: ").lower()
        if fruit == 'exit':
            break
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1

    for fruit, count in fruit_count.items():
        print(f"'{fruit}' is {count}")

dict_fruit()