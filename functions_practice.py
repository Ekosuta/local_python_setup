def hello():
    print("hello there")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_lunch)):
            if i == 0:
                print(f"First I eat {my_lunch[0]}")
            else:
                print(f"Next I eat {my_lunch[i]}")

hello()
print(pack('one', 'two', 'three'))
eat_lunch([])
eat_lunch(['eggs', 'salad'])