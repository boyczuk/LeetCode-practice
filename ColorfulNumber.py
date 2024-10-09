def test_colorfulNumber():
    test_cases = [
        (7, True),     # Colorful
        (23, True),    # Colorful
        (22, False),   # Not Colorful
        (324, True),   # Colorful
        (326, False),  # Not Colorful
        (3245, True),  # Colorful
        (2233, False), # Not Colorful
        (121, False),  # Not Colorful
        (204, False),  # Not Colorful
        (987, True)    # Colorful
    ]
    
    for i, (input_val, expected_output) in enumerate(test_cases, start=1):
        print(f"Test Case {i}: Input = {input_val}")
        result = colorfulNumber(input_val)
        if result == expected_output:
            print("Output: Passed")
        else:
            print("Output: Not Passed")
        print()

def colorfulNumber(number):
    subarr = []
    arr = str(number)
    for i in range(len(arr)):
        # Each should clump i number together
        for j in range(i+1, len(arr) + 1):
            subarr.append(arr[i:j])

    productMap = {}
    for subpart in subarr:
        product = 1
        for s in subpart:
            product *= int(s)
        if product in productMap:
            return False
        productMap[product] = s

    return True





if __name__ == "__main__":
    test_colorfulNumber()
