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

    return jobs


if __name__ == '__main__':
    print("yo")
    # Getting the jobs
    jobs = random_job_generation()

    print(jobs)

