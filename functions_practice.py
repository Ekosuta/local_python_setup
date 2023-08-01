def hello():
    print("hello there")

def pack(first, last, age):
    return [first, last, age]
profile = pack('elvin', 'kosuta', 19)

lunch = ['eggs', 'salad', 'pasta']
def eat_lunch(lunch):
    print(f"First I eat {lunch[0]}. Next I eat {lunch[1]}. Lastly I eat {lunch[2]}")

hello()
print(profile)
eat_lunch(lunch)