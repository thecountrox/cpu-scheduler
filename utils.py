def input_loop(message: str, type: type):
    while True:
        try:
            var = type(input(message + ": "))
            break
        except ValueError:
            print("Invalid input!")

    return var


def print_process_table(process_table: dict[int, int]):
    print("==== Process Table ====")
    print(" Pid    [AT, BT]")
    for key, value in process_table.items():
        print(f" {key} --> {value}")
    print("=======================")
    print("Legend \nAT = Arrival Time\nBT = Burst Time")
    print("=======================")


def generate_gnatt_chart():
    pass


def sort_by_arrival(process_table: dict[str, list[int]]):
    lis = sorted(process_table.items(), key=lambda item: item[1][0])
    return [
        (process_name, burst_time) for process_name, [arrival_time, burst_time] in lis
    ]
