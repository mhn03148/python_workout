def run_timing():
    number_of_run = 0
    total_run = 0
    while True:
        one_run = input('Enter 10 Km run time: ')
        if not one_run: #공백을 enter하면 break
            break
        number_of_run += 1
        total_run += float(one_run)

    average_time = total_run/ number_of_run
    print(f'Average of {average_time}, over {number_of_run} runs')

run_timing()