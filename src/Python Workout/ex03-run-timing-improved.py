def run_timing():
    """Write a function (run_timing) that asks how long it took for you
to run 10 km. The function continues to ask how long (in minutes)
it took for additional runs, until the user presses Enter. At that
point, the function exits--but only after calculating and displaying
the average time that the 10 km runs took."""
    total_duration = 0
    count = 0

    while True:
        duration = input("Enter your 10k time: ")
        if not duration:
            break
        else:
            try:
                total_duration += float(duration)
                count += 1
            except ValueError as e:
                print("Hey! That's not a valid number.")
    print(f"Average of {total_duration / count} in {count} runs.")

run_timing()
