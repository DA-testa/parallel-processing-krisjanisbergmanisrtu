# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = []  # n counters which will decrease count in each m cycle
    for thread in range (int(n)):
        val = data[thread]
        val = int(val) - 1
        threads.append([val, 0]) # Adds counter and saved time when it started count

    i = 1  # time counter that will increment
    job_index = 0

    while len(output) < int(m):
        for threadIndex in range(int(n)):
            if threads[threadIndex][0] == 0:  # if job reaches execution timeout
                # output.append([getattr(threads[threadIndex]), i]) # then add it to results
                output.append([threadIndex, threads[threadIndex][1]])  # then add it to results

                job_index = +1  # look at next job

                threads[threadIndex][0] = int(data[job_index])  # put next job in this thread (puts the timer in thread)
                threads[threadIndex][1] = i

            else:  # Else decrease time left in job
                threads[threadIndex][0] -= 1

        i += 1
    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    m_n = input()
    m_n = m_n.split(' ')
    # n - thread count 
    # m - job count
    n = m_n[0]
    m = m_n[1]

    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = input()
    data = data.split(' ')

    # TODO: create the function
    result = parallel_processing(n, m, data)

    # TODO: print out the results, each pair in it's own line
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
