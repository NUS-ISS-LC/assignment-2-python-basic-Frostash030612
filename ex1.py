def find(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return[i,j]
    return None

def run_sum():
    try:
        nums_input = input("Type in the number set: ")
        nums_str_list = nums_input.replace(',', ' ').split()
        nums = [int(s) for s in nums_str_list]

        target_input = input("Type in your target: ")
        target = int(target_input)
    
    except ValueError:
        print("Please type in valid integer!")
        return
    
    print(f"\nSet input: {nums}")
    print(f"Target: {target}")

    result = find(nums, target)

    if result:
        print("Find!")
        i,j = result
        print(f"Result: {result}")
    else:
        print("Haven't find the result.")

if __name__ == "__main__":
    run_sum()