def remove_vowels(input_string):
    vowels = "AEIOUaeiou"
    return "".join(char for char in input_string if char not in vowels)

# Example usage:
input_string = "Hello, World!"
result = remove_vowels(input_string)
print(result)  # Output: "Hll, Wrld!"

