# 2D Robotic Arm Simulation

This project simulates a 2D robotic arm using Python. The simulation allows users to visualize the movement of a robotic arm with two segments, providing insights into basic kinematics and robotic motion.

## Overview

The 2D robotic arm consists of two segments of fixed lengths. The arm's movement is controlled by two joint angles, allowing it to reach various positions in a 2D plane. The simulation is implemented using Matplotlib for visualization and NumPy for mathematical calculations.

## Installation

To run this project, you need to have Python installed on your machine. You can install the required dependencies using pip. Follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/2d-robotic-arm-simulation.git
   cd 2d-robotic-arm-simulation
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the simulation, execute the following command in your terminal:

```
python src/simulation.py
```

This will start the 2D robotic arm simulation, displaying the arm's movement in a graphical window.

## Testing

To ensure the correctness of the kinematics calculations, unit tests are provided. You can run the tests using:

```
pytest tests/test_kinematics.py
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
