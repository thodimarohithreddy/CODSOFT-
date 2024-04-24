#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Task {
    string description;
    bool completed;
};
void addTask(vector<Task>& tasks, const string& description) {
    tasks.push_back({description, false});
    cout << "Task added successfully." << endl;
}

void viewTasks(const vector<Task>& tasks) {
    cout << "Tasks:" << endl;
    for (size_t i = 0; i < tasks.size(); ++i) {
        cout << i + 1 << ". " << (tasks[i].completed ? "[X] " : "[ ] ") << tasks[i].description << endl;
    }
}

void markCompleted(vector<Task>& tasks, size_t index) {
    if (index >= 1 && index <= tasks.size()) {
        tasks[index - 1].completed = true;
        cout << "Task marked as completed." << endl;
    } else {
        cout << "Invalid task number." << endl;
    }
}

void removeTask(vector<Task>& tasks, size_t index) {
    if (index >= 1 && index <= tasks.size()) {
        tasks.erase(tasks.begin() + index - 1);
        cout << "Task removed successfully." << endl;
    } else {
        cout << "Invalid task number." << endl;
    }
}

int main() {
    vector<Task> tasks;
    int choice;

    do {
        cout << "\nTo-Do List Manager" << endl;
        cout << "1. Add Task" << endl << "2. View Tasks" << endl;
        cout << "3. Mark Task as Completed" << endl << "4. Remove Task" << endl;
        cout << "5. Exit" << endl << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                cin.ignore(); // clear input buffer
                cout << "Enter task description: ";
                string description;
                getline(cin, description);
                addTask(tasks, description);
                break;
            }
            case 2:
                viewTasks(tasks);
                break;
            case 3: {
                size_t index;
                cout << "Enter the task number to mark as completed: ";
                cin >> index;
                markCompleted(tasks, index);
                break;
            }
            case 4: {
                size_t index;
                cout << "Enter the task number to remove: ";
                cin >> index;
                removeTask(tasks, index);
                break;
            }
            case 5:
                cout << "Exiting program. Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 5);

    return 0;
}
