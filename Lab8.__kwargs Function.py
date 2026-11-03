#Question 4: write a function using **kwargs to display employee information.

def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


employee_info(
    name="Ahmed",
    age=25,
    department="IT",
    salary=50000
)