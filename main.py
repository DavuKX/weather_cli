from Calendar import Calendar


def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Input cannot be empty. Please try again.")


def get_valid_search_type():
    valid_search_types = ["date", "name", "description"]
    while True:
        search_type = input("Enter search type (date/name/description): ").lower()
        if search_type in valid_search_types:
            return search_type
        else:
            print("Invalid search type. Please choose from date, name, or description.")


def main():
    calendar = Calendar()

    while True:
        print("\nCalendar CLI Interface")
        print("1. Add Event")
        print("2. Delete Event")
        print("3. Search Events")
        print("4. View All Events")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = get_non_empty_input("Enter date (YYYY-MM-DD): ")
            time = get_non_empty_input("Enter time (HH:MM): ")
            title = get_non_empty_input("Enter title: ")
            description = get_non_empty_input("Enter description: ")
            calendar.add_event(date, time, title, description)
        elif choice == "2":
            search_type = get_valid_search_type()
            search_param = get_non_empty_input("Enter search parameter: ")
            search_results = calendar.search_events(search_type, search_param)

            if not search_results:
                print("No events found.")
                continue

            print("Search results:")
            for index, event in enumerate(search_results, start=1):
                print(f"{index}.")
                event.display()
                print("\n")

            delete_choice = input("Enter the number of the event to delete or 'c' to cancel: ")

            if delete_choice.isdigit():
                delete_choice = int(delete_choice)

                if 1 <= delete_choice <= len(search_results):
                    confirm = input("Are you sure you want to delete this event? (y/n): ")

                    if confirm.lower() == "y":
                        event_to_delete = search_results[delete_choice - 1]
                        calendar.delete_event(event_to_delete)
                else:
                    print("Invalid event number.")
            elif delete_choice.lower() == "c":
                print("Delete operation canceled.")
            else:
                print("Invalid choice.")
        elif choice == "3":
            search_type = get_valid_search_type()
            search_param = get_non_empty_input("Enter search parameter: ")
            calendar.search_events(search_type, search_param)
        elif choice == "4":
            calendar.view_all_events()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
