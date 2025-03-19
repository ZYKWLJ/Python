list=[1,2,3,4,5]
if 0 in list:
    print("0 in list return")
elif 1 in list:
    print("0 not in list and i in the list")

def func(num):
    match num:
        case 1:
            print("1")
        case 2:
            print("2")
        case _:
            print("other")
func(1)
func(2)
func(3)
