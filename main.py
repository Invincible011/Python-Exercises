class Phone:
    # How to create the phones attributes
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f'{self.brand} is calling {phone_number}')

    def __str__(self) -> str:
        return f'Brand: {self.brand}, Price: {self.price}'



# Creating the Actual Instance
iphone = Phone('Iphone-XR', 400)
one_plus = Phone('One Plus-3T', 500)

# Generating each Properties and Behaviors On Constructors
print(iphone.brand, iphone.price)  # Property
print(one_plus.brand, one_plus.price)  # Property
print()

# Objects: iphone and one_plus
iphone.call('07067485969')  # Behavior
one_plus.call('09034861241')  # Behavior
print()
print(iphone)
print(one_plus)