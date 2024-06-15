value = "value"

print(value.upper())  # VALUE
print(value)  # value (strings are immutable)
print(value.lower())  # value
print(value.capitalize())  # Value
print("value".capitalize())  # Value
print(value.islower())  # True
print(value.isupper())  # False
print(value.istitle())  # False
print(value.isdigit())  # False
print(value.isalpha())  # True
print(value.isalnum())  # True
print(value.startswith("val"))  # True
print(value.endswith("ue"))  # True
print(value.find("ue"))  # 3
print(value[0])  # v

for ch in value:
    print(ch)
