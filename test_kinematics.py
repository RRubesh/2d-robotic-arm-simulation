import pytest
import numpy as np
from src.simulation import calculate_positions

def test_calculate_positions():
    # Test case 1: Both angles are zero
    theta1 = 0
    theta2 = 0
    expected = ((0, 0), (5.0, 0.0), (8.0, 0.0))
    result = calculate_positions(np.radians(theta1), np.radians(theta2))
    assert result == expected

    # Test case 2: First angle is 90 degrees, second angle is 0 degrees
    theta1 = 90
    theta2 = 0
    expected = ((0, 0), (0.0, 5.0), (0.0, 5.0 + 3.0))
    result = calculate_positions(np.radians(theta1), np.radians(theta2))
    assert result == expected

    # Test case 3: First angle is 45 degrees, second angle is 45 degrees
    theta1 = 45
    theta2 = 45
    expected_x = 5 * np.cos(np.radians(theta1)) + 3 * np.cos(np.radians(theta1 + theta2))
    expected_y = 5 * np.sin(np.radians(theta1)) + 3 * np.sin(np.radians(theta1 + theta2))
    expected = ((0, 0), (5 * np.cos(np.radians(theta1)), 5 * np.sin(np.radians(theta1))),
                (expected_x, expected_y))
    result = calculate_positions(np.radians(theta1), np.radians(theta2))
    assert np.isclose(result[2], expected[2]).all()

    # Test case 4: Negative angles
    theta1 = -90
    theta2 = -45
    expected = ((0, 0), (0.0, -5.0), (3.0, -5.0 + 3.0 * np.sin(np.radians(-45))))
    result = calculate_positions(np.radians(theta1), np.radians(theta2))
    assert np.isclose(result[2], expected[2]).all()