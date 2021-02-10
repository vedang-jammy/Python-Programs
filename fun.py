def up_low(s):
    up = 0
    low = 0
    for item in s.split():
        count = 0
        while count <= len(item):
            if item[count].isupper():
                up += 1
            elif item[count].islower():
                low += 1
            else:
                pass
            count += 1
    print(f"No. of uppercase characters: {up}")
    print(f"\nNo of lowercase characters: {low}")


s = "hello I am your FriEnd"
up_low(s)
