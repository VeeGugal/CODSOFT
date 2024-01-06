class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("OOPS!!!!......There are No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}'Successfully added to the to-do list.")
   

    def remove_task(self, task_index):
        try:
            task_removed = self.tasks.pop(task_index - 1)
            print(f"Task '{task_removed}'Successfully removed from the to-do list.")
        except IndexError:
            print("Oooops!!!!.......Invalid task index. Please try again.")


    
def main():
    to_do_list = ToDoList()

    while True:
        print("\nChoose one from below given Options:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Enter your choice in between (1-4): ")

        if choice == '1':
            to_do_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '3':
            to_do_list.display_tasks()
            task_index = int(input("Enter the task index to remove the respective task: "))
            to_do_list.remove_task(task_index)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Option you have selected is invalid. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
