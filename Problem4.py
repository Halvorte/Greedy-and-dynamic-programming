'''
Problem 4. Job scheduling
Generate a random dataset with at least 50 jobs. Each job should have a profit and a deadline no later than 40. Find the maximum profit under the constraints of the deadlines for all jobs.
'''
import random

# Function to create the 50 jobs with random profit and deadline
def random_job_generation():
    jobs = []
    for i in range(50):
        profit = random.randint(0, 20)
        deadline = random.randint(1,40)
        dictionary = {
            'Job' : f'J{i+1}',
            'Profit' : profit,
            'Deadline' : deadline
        }
        jobs.append(dictionary)
    # Return a list of all the jobs
    return jobs


# Funciton to assign jobs to the latest possible slot.
def assign_jobs(sorted_jobs):
    schedule = [None] * 41
    print(schedule)

    for i in sorted_jobs:
        deadline = i['Deadline']

        for j in range(deadline):
            if schedule[deadline - j] is None:
                if (deadline - j) > 0:
                    schedule[deadline - j] = i
                    break


    profit = 0
    for k in schedule:
        if k is None:
            pass
        else:
            print(k)
            profit += k['Profit']

    print(profit)
    print(schedule)



if __name__ == '__main__':
    print("yo")
    # Getting the jobs
    jobs = random_job_generation()
    print(jobs)

    # Sort jobs in order of profit
    sorted_jobs = sorted(jobs, key=lambda x: x['Profit'], reverse=True)
    print(sorted_jobs)

    # Assign the jobs to a timeslot and print all the jobs
    assign_jobs(sorted_jobs)