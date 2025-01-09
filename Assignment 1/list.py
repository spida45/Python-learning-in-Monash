import random

def generate_random_lists(length):
    # 生成第一个随机列表
    first_list = [random.randint(1, 100) for _ in range(length)]

    # 生成第二个随机列表
    second_list = [random.randint(1, first_list[i]) for i in range(length)]

    return first_list, second_list


# 设定列表长度
length = 5

# 生成随机列表
first_list, second_list = generate_random_lists(length)

# 打印生成的列表
print("First List:", first_list)
print("Second List:", second_list)