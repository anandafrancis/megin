from task_api import TaskAPI
from datetime import datetime

def main():
    # Initialize TaskAPI instance
    task_api = TaskAPI(uri="mongodb://localhost:27017/", db_name="task_manager", collection_name="samples_t")

    # Create tasks with additional fields
    task_id_1 = task_api.create_task("DS4300 HW6", "Mongo Project", datetime(2024, 4, 9), "High")
    task_id_2 = task_api.create_task("DS4400 HW4", "Graph Project", datetime(2024, 4, 19), "Medium")

    # Print all tasks
    samples_t = task_api.get_all_tasks()
    print("All Tasks:")
    for task in samples_t:
        print(task)

    # Generate and print schedule
    schedule = task_api.generate_schedule()
    print("\nSchedule:")
    for days_remaining, samples_t in schedule.items():
        print(f"Days remaining: {days_remaining}")
        for task in samples_t:
            print(task)

if __name__ == "__main__":
    main()