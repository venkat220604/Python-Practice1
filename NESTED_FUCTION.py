def outer():
    print("I am outer")
    def inner():
        print("I am Inner")
    inner()
outer()