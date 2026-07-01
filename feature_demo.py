def calculate_average(numbers):
    """
    计算列表的平均值

    参数:
        numbers: 数字列表

    返回:
        列表的平均值。如果列表为空，返回 0。
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 示例用法
if __name__ == "__main__":
    # 测试示例
    test_list = [10, 20, 30, 40, 50]
    avg = calculate_average(test_list)
    print(f"列表: {test_list}")
    print(f"平均值: {avg}")

    # 测试空列表
    empty_list = []
    print(f"\n空列表平均值: {calculate_average(empty_list)}")

    # 测试小数
    float_list = [1.5, 2.5, 3.5]
    print(f"小数列表平均值: {calculate_average(float_list)}")