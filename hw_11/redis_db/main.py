"""Main script for user session management."""

from hw_11.redis_db.session_service import SessionService


def main() -> None:
    """Run the console-based session management system."""

    session_service = SessionService()

    while True:
        print("\nUser Session Management:")
        print("1. Create session")
        print("2. Get session")
        print("3. Update session activity")
        print("4. Logout user")
        print("0. Exit\n")

        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nExiting program...")
            break

        if choice == "1":
            user_id = input("Enter user id: ")
            session = session_service.create_user_session(user_id)
            print(f"Session created: {session}")
        elif choice == "2":
            user_id = input("Enter user id: ")
            session = session_service.get_user_session(user_id)
            print(f"Active session: {session}" if session else "No active session found.")
        elif choice == "3":
            user_id = input("Enter user id: ")
            session_service.update_user_activity(user_id)
            print("Session activity updated.")
        elif choice == "4":
            user_id = input("Enter user id: ")
            session_service.logout_user(user_id)
            print("User logged out.")
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
