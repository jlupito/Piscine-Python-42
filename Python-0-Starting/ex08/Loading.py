import sys

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    counter = 1
    for item in lst:
        percent_completed = counter / total * 100
        progress_bar_length = 55
        filled_length = int(progress_bar_length * counter / total)
        bar = "█" * filled_length + " " * (progress_bar_length - filled_length)
        sys.stdout.write(f"\r{percent_completed:.0f}%|{bar}| {counter}/{total}")
        sys.stdout.flush()
        counter += 1
        yield item
    print()