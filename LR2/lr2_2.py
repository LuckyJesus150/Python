def sport (m,k):
    for days in range  (1, target+1):
        m=m+m*(k/100)
        if m >=target:
            print("Через", days, "днів буде вироблена норма пробігу в 50км на день")
            break
target=50
