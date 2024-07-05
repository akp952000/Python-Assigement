# Write a Python program to monitor the health of the CPU.

import psutil  # Importing the psutil library to gather system data
import time  # Importing the time library to manage delay intervals

def check_cpu_usage(threshold):
    """
    Continuously monitors the CPU load and triggers an alert if it surpasses a defined limit.
    
    Args:
        threshold (float): The CPU load percentage limit for triggering an alert.
    """
    print("Monitoring CPU usage...")
    
    try:
        while True:
            # Fetching the current CPU usage as a percentage
            current_usage = psutil.cpu_percent(interval=1)
            
            # If the current CPU usage exceeds the threshold, print an alert message
            if current_usage > threshold:
                print(f"Warning! CPU load has exceeded the limit: {current_usage}%")
            
            # Pause for a second before the next reading
            time.sleep(1)
    
    except KeyboardInterrupt:
        # Gracefully handle user interruption
        print("\nMonitoring interrupted by user.")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define the CPU usage limit for triggering alerts
    cpu_limit = 80
    
    # Begin monitoring the CPU usage
    check_cpu_usage(cpu_limit)
