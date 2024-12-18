import threading
import time


def timer(name, duration, message):
    """Function to run a timer."""
    while duration > 0:
        print(f"{name}: {message} ({duration} seconds remaining)")
        time.sleep(1)
        duration -= 1
    print(f"{name}: Timer finished!")


def main():
    # Set durations and messages for the two timers
    duration1 = 10  # Duration for Timer 1 (in seconds)
    duration2 = 7  # Duration for Timer 2 (in seconds)

    message1 = "Doing task A"
    message2 = "Working on task B"

    # Create threads for each timer
    timer1_thread = threading.Thread(target=timer, args=("Timer 1", duration1, message1))
    timer2_thread = threading.Thread(target=timer, args=("Timer 2", duration2, message2))

    # Start the threads
    timer1_thread.start()
    timer2_thread.start()

    # Wait for both threads to complete
    timer1_thread.join()
    timer2_thread.join()

    print("Both timers have finished.")


if __name__ == "__main__":
    main()
