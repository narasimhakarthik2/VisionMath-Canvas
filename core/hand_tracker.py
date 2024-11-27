"""
HandTracker class for detecting and tracking hand landmarks using MediaPipe.
"""

import mediapipe as mp
import cv2
import numpy as np
from config.settings import HAND_DETECTION_SETTINGS, DISPLAY_SETTINGS


class HandTracker:
    def __init__(self):
        """Initialize MediaPipe hands solution and settings."""
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        # Initialize MediaPipe Hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=HAND_DETECTION_SETTINGS['static_image_mode'],
            max_num_hands=HAND_DETECTION_SETTINGS['max_num_hands'],
            min_detection_confidence=HAND_DETECTION_SETTINGS['min_detection_confidence'],
            min_tracking_confidence=HAND_DETECTION_SETTINGS['min_tracking_confidence']
        )

        # Store previous landmark positions for tracking
        self.prev_landmarks = None

    def process_frame(self, frame):
        """
        Process a frame and detect hands.

        Args:
            frame (numpy.ndarray): Input frame in BGR format

        Returns:
            tuple: Processed frame and hand landmarks if detected, None otherwise
        """
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = self.hands.process(frame_rgb)

        # Store the frame dimensions
        frame_height, frame_width = frame.shape[:2]

        # If hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks
                self.draw_landmarks(frame, hand_landmarks)

                # Convert landmarks to pixel coordinates
                landmarks_px = self._convert_landmarks_to_pixel(
                    hand_landmarks, frame_width, frame_height
                )

                self.prev_landmarks = landmarks_px
                return frame, landmarks_px

        self.prev_landmarks = None
        return frame, None

    def draw_landmarks(self, frame, hand_landmarks):
        """Draw hand landmarks and connections on the frame."""
        self.mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS,
            landmark_drawing_spec=self.mp_draw.DrawingSpec(
                color=DISPLAY_SETTINGS['colors']['hand_landmarks'],
                thickness=2,
                circle_radius=2
            ),
            connection_drawing_spec=self.mp_draw.DrawingSpec(
                color=DISPLAY_SETTINGS['colors']['hand_connections'],
                thickness=1
            )
        )

    def _convert_landmarks_to_pixel(self, hand_landmarks, frame_width, frame_height):
        """Convert normalized landmarks to pixel coordinates."""
        landmarks_px = []
        for landmark in hand_landmarks.landmark:
            px = np.array([
                landmark.x * frame_width,
                landmark.y * frame_height,
                landmark.z * frame_width
            ])
            landmarks_px.append(px)

        return np.array(landmarks_px)

    def get_finger_coordinates(self, landmarks_px):
        """Get specific finger landmark coordinates."""
        if landmarks_px is None:
            return None

        return {
            'index_tip': landmarks_px[self.mp_hands.HandLandmark.INDEX_FINGER_TIP.value],
            'middle_tip': landmarks_px[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP.value],
            'index_pip': landmarks_px[self.mp_hands.HandLandmark.INDEX_FINGER_PIP.value],
            'middle_pip': landmarks_px[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP.value]
        }

    def release(self):
        """Release the MediaPipe hands object."""
        self.hands.close()