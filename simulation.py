
import matplotlib.pyplot as plt
import numpy as np

# --- Configuration ---
L1 = 5  # Length of the first segment
L2 = 3  # Length of the second segment

# --- Functions ---

def calculate_positions(theta1_rad, theta2_rad):
    """Calculates the coordinates of the robotic arm joints."""
    x0, y0 = 0, 0
    x1 = L1 * np.cos(theta1_rad)
    y1 = L1 * np.sin(theta1_rad)
    x2 = x1 + L2 * np.cos(theta1_rad + theta2_rad)
    y2 = y1 + L2 * np.sin(theta1_rad + theta2_rad)
    return (x0, y0), (x1, y1), (x2, y2)

def plot_arm(positions):
    """Clears the current plot and draws the arm in a new position."""
    (x0, y0), (x1, y1), (x2, y2) = positions
    
    plt.clf()  # Clear the previous plot
    plt.plot([x0, x1, x2], [y0, y1, y2], '-o', linewidth=4, markersize=10, color='blue', label='Robotic Arm')
    
    # Set plot properties
    max_reach = L1 + L2
    plt.xlim(-max_reach - 1, max_reach + 1)
    plt.ylim(-max_reach - 1, max_reach + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Animated 2D Robotic Arm Simulation")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()

# --- Main Execution ---
if __name__ == "__main__":
    plt.ion()  # Turn on interactive mode for animation
    fig = plt.figure(figsize=(8, 8))

    try:
        # Animation loop
        for angle in np.linspace(0, 360, 180):  # Animate over a full circle
            # Define joint angles that change over time
            theta1_deg = angle
            theta2_deg = 45 * np.sin(np.radians(angle * 2))  # Elbow moves back and forth

            # Convert angles to radians
            theta1_rad = np.radians(theta1_deg)
            theta2_rad = np.radians(theta2_deg)

            # Calculate and plot
            joint_positions = calculate_positions(theta1_rad, theta2_rad)
            plot_arm(joint_positions)
            
            # Display coordinates in console
            (x0, y0), (x1, y1), (x2, y2) = joint_positions
            print(f"End Effector at angle {angle:.1f}°: ({x2:.2f}, {y2:.2f})", end='\r')

            plt.pause(0.01)  # Pause for a short duration to create animation effect

    except KeyboardInterrupt:
        print("\nAnimation stopped by user.")
    finally:
        plt.ioff()  # Turn off interactive mode
        print("\nSaving final position...")
        plt.savefig("robotic_arm_final_position.png")
        plt.show()  # Show the final plot until closed