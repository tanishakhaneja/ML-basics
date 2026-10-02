def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

        
print_kwargs(name="tani", friend = "nitish")
print_kwargs(name="tani")
print_kwargs(name="tani", friend="nitish", bestf = "priyank")