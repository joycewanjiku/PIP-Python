def create_full_name(first_name,last_name):
    space=""
    full_name=first_name + space +last_name
    return full_name
print("Full Name:",create_full_name('Joyce Mumbi'))

def sum_three_numbers(num_one,num_two,num_three):
    sum=num_one+num_two+num_three
    return sum
print ('Sum of three numbers:',sum_three_numbers(78,89,54))


def area_of_circle(r):
    PI=3.45
    area=PI *r ** 2
    return area
print(area_of_circle(30))

def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
        print(total)
        print(sum_of_numbers(70))



    def is_even(n): 
        if n % 2 == 0:
            print('even')
            print('even')
            return True
        return False
    print(is_even(7))
    print(is_even(20))


    def find_even_numbers(n):
        even=[]
        for i in range(n+1):
            if i % 2 ==0:
                even.append(i)
                return even
            print(find_even_numbers(30))

    def calculate_age(birth_year,current_year=2023):
        age=current_year-birth_year
        return age;

    def weight_of_objects(mass,gravity=9.876):
        weight=str(mass * gravity)+ 'N'
        return weight
    print('weight of an object in Newtons:',weight_of_objects(150))
    print('weight of an object in Newtons: ',weight_of_objects(150, 1.54))

        





