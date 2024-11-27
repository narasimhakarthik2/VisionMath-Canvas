# Hand Detection Settings
HAND_DETECTION_SETTINGS = {
    'max_num_hands': 1,  # Maximum number of hands to detect
    'min_detection_confidence': 0.7,  # Minimum confidence value for hand detection
    'min_tracking_confidence': 0.7,  # Minimum confidence value for hand tracking
    'static_image_mode': False,  # Set to False for video streaming
}

# Gesture Detection Settings
GESTURE_SETTINGS = {
    'finger_tap_threshold': 0.05,  # Maximum distance between fingers to register as a tap
    'tap_duration_frames': 5,  # Number of frames finger tap must be held
    'min_gesture_confidence': 0.8,  # Minimum confidence for gesture detection
}

# Mode Settings
MODE_SETTINGS = {
    'modes': ['DRAW', 'WRITE', 'ERASE'],  # Available modes in the application
    'default_mode': 'DRAW',  # Starting mode
    'mode_switch_delay': 10,  # Frames to wait before allowing another mode switch
}

# Visualization Settings
DISPLAY_SETTINGS = {
    'window_name': 'MathVision Canvas',
    'window_width': 1280,
    'window_height': 720,
    'flip_image': True,  # Mirror the image horizontally

    # Colors in BGR format
    'colors': {
        'hand_landmarks': (121, 22, 76),  # Color for hand landmarks
        'hand_connections': (245, 129, 66),  # Color for connections between landmarks
        'mode_text': (255, 255, 255),  # Color for mode display text
        'drawing_color': (0, 255, 0),  # Color for drawing lines
    },

    # Text settings
    'font_scale': 1,
    'font_thickness': 2,
    'mode_display_position': (30, 50)  # Position to display current mode
}

# Drawing Settings
DRAWING_SETTINGS = {
    'line_thickness': 2,
    'min_drawing_distance': 5,  # Minimum pixel distance to draw new line segment
    'smoothing_factor': 0.5,  # Factor for smoothing drawing (0-1)
}