from .core import count_in_list


def init_function():
    sample_list = ["frog", "dog", "cat", "dog", "dog", "cat"]
    print(count_in_list(sample_list, "dog"))
