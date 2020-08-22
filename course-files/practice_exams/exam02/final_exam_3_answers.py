restaurants = restaurants = [
    {
        "id": "0b6AU869xq",
        "name": "Kabul House",
        "rating": 4.5,
        "price": "$$",
        "review_count": 854
    }, {
        "id": "CJWVmhX7gSP",
        "name": "Ovo Frito Cafe",
        "rating": 4.5,
        "price": "$$",
        "review_count": 265
    }, {
        "id": "x9-IcWixbknu",
        "name": "Soulwich",
        "rating": 4.5,
        "price": "$",
        "review_count": 551
    }, {
        "id": "8J3tKkFkf6q",
        "name": "Andy's Frozen Custard",
        "rating": 4.5,
        "price": "$",
        "review_count": 346
    }
]


def print_header(message):
    print()
    print('*' * (len(message) + 4))
    print('*', message, '*')
    print('*' * (len(message) + 4))


def q1():
    print_header('Question 1')
    result = 6 % 4 
    print(result, type(result))

    result = False and True
    print(result, type(result))

    my_list = [{'red': 5}, {'blue': 2}, {'pink': 9}, {'violet': 12}]
    result = my_list.pop(3)
    print(result, type(result))
    print(my_list, type(my_list))

    a = 'trace'
    b = 'no'
    result = a[-1] + b[0] + a[0:3] + b[0] + a[3:5]
    print(result, type(result))
    

def q2():
    print_header('Question 2')
    my_list = ['red', 'yellow', 'turquoise', 'violet', 'pink']
    for i in range(0, 13, 3):
        print(my_list[i % len(my_list)])

def q3a():
    print_header('Question 3a')
    for c in 'rhino':
        print(c)

def q3b():
    print_header('Question 3b')
    names = ['frida', 'emma', 'ravi', 'shu', 'jonas']
    p = len(names)
    while p > 0:
        print(names[p - 1])
        p -= 1

def q4():
    print_header('Question 4')
    a = True
    b = False
    c = True

    if a and b:
        print('dog')
    elif a:
        print('cat')
    if b or not a:
        print('squirrel')
    else:
        print('chicken')
    if not b and c:
        print('giraffe')
    if a and not c:
        print('lion')
    elif c:
        print('penguin')
    elif not a:
        print('rabbit')
    print('skunk')

def q5():
    print_header('Question 5')
    
    def foo(a:float, b:float):
        return a - 2 * b

    def bar(a:float, b:float):
        return b // a

    x = bar(3, 2 + 2)
    y = foo(bar(2, 3), foo(1, 2))
    print(x)
    # print('bar(2, 3)', bar(2, 3))
    # print('foo(1, 2)', foo(1, 2))
    print(y)


def q6():
    print_header('Question 6')
    
    def get_restaurant_ids(businesses):
        restaurant_ids = []
        for business in businesses:
            restaurant_ids.append(business['id'])
        return restaurant_ids
    print(get_restaurant_ids(restaurants))


def q7():
    print_header('Question 7')
    
    def get_average_num_reviews(businesses):
        review_sum = 0
        for business in businesses:
            review_sum += business['review_count']
        return review_sum / len(businesses)
    print(get_average_num_reviews(restaurants))

def q8():
    print_header('Question 8')

    a = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    b = {}
    c = 2
    while len(b) < 4:
        e = c % len(a)
        b[a[e]] = c
        c += len(b)
    
    print(b)
    print(c)

def ec():
    print_header('Extra Credit')

    statuses = [
        'Freshling', 'Sophomore', 'Junior', 'Senior', 'Auditor', 
        'Masters Student', 'PhD Student', 'Other'
    ]
    num = 1
    for status in statuses:
        print(num, '-', status)
        num += 1
    
    while True:
        status = input('Enter your student status (1-8): ')
        try:
            status_num = int(status) - 1
            if status_num >= 0 and status_num < len(statuses):
                user_student_status = statuses[status_num]
                break
            else:
                print('Please enter a number from 1-8')
        except:
            print('Please enter a number')
    
    print('Your student status is:', user_student_status)



    

q1()
q2()
q3a()
q3b()
q4()
q5()
q6()
q7()
q8()
ec()