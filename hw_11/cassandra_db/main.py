"""
Main script for event log management.
"""

from uuid import UUID

from hw_11.cassandra_db.services.log_service import LogService


def main() -> None:
    """
    Run the console-based session management system.
    """

    log_service = LogService()

    while True:
        print("\nEvent Log Management:")
        print("1. Log new event")
        print("2. Get recent events by type")
        print("3. Update event metadata")
        print("4. Clean old logs")
        print("0. Exit\n")

        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nExiting program...")
            break

        if choice == "1":
            user_id = input("Enter user ID: ")
            event_type = input("Enter event type: ")
            metadata = input("Enter metadata: ")
            event = log_service.log_event(user_id, event_type, metadata)
            print(f"Event logged: {event}")

        elif choice == "2":
            event_type = input("Enter event type: ")
            events = log_service.get_recent_events(event_type)

            if events:
                for event in events:
                    print(event)
            else:
                print("No events found")

        elif choice == "3":
            event_id = input("Enter event ID: ")

            try:
                event_id = UUID(event_id)
            except ValueError:
                print("Invalid event ID")
                continue

            existing_event = log_service.get_event_by_id(event_id)

            if not existing_event:
                print("Event not found")
                continue

            new_metadata = input("Enter new metadata: ")
            log_service.update_event_metadata(event_id, new_metadata)
            print("Event metadata updated.")

        elif choice == "4":
            log_service.clean_old_logs()
            print("Old logs cleaned.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
