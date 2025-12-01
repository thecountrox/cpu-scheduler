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


def main():
    # Input handling:

    number_of_processes: int = input_loop("Enter the number of processes", int)

    process_table = {}
    # KEY                 : VALUE
    # process_name -> str : [arrival_time, burst_time] Both being int here

    for i in range(number_of_processes):
        process_name = "P" + str(i)
        arrival_time = input_loop(f"[{process_name}]: Enter Arrival Time", int)
        waiting_time = input_loop(f"[{process_name}]: Enter Waiting Time", int)
        process_table[process_name] = [arrival_time, waiting_time]
    print_process_table(process_table)


if __name__ == "__main__":
    main()
