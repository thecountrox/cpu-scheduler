import utils


def main():
    number_of_processes: int = utils.input_loop("Enter the number of processes", int)

    process_table: dict[str, list[int]] = {}
    # KEY                 : VALUE
    # process_name -> str : [arrival_time, burst_time] Both being int here

    gnatt_list: list[tuple[str, int]] = []
    # we are going to only calculate this one
    # store process name and time sequentially, when displaying we iterate through and calculate the chart on the fly using this

    for i in range(number_of_processes):
        process_name = "P" + str(i)
        arrival_time = utils.input_loop(f"[{process_name}]: Enter Arrival Time", int)
        waiting_time = utils.input_loop(f"[{process_name}]: Enter Waiting Time", int)
        process_table[process_name] = [arrival_time, waiting_time]

    utils.print_process_table(process_table)

    # SCHEDULING ALGORITHM: FCFS
    # For FCFS we have to
    # 1) sort by arrival time

    sorted_by_arrival_time = sorted(process_table.items(), key=lambda item: item[1][0])
    print(sorted_by_arrival_time)

    # 2) then process them sequentially
    gnatt_list = utils.sort_by_arrival(process_table)


if __name__ == "__main__":
    main()
