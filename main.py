import cv2
from core.hand_tracker import HandTracker
from config.settings import DISPLAY_SETTINGS


class MathVisionCanvas:
    def __init__(self):
        """Initialize the application components."""
        self.cap = cv2.VideoCapture(0)
        self.hand_tracker = HandTracker()

        # Set camera resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, DISPLAY_SETTINGS['window_width'])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, DISPLAY_SETTINGS['window_height'])

    def run(self):
        """Main application loop."""
        while True:
            # Read frame from camera
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # Flip frame horizontally for selfie view
            if DISPLAY_SETTINGS['flip_image']:
                frame = cv2.flip(frame, 1)

            # Process frame with hand tracker
            frame, landmarks = self.hand_tracker.process_frame(frame)

            # Display the mode (for now just print if hand is detected)
            if landmarks is not None:
                finger_coords = self.hand_tracker.get_finger_coordinates(landmarks)
                if finger_coords:
                    # Display index fingertip position for testing
                    index_tip = finger_coords['index_tip']
                    cv2.circle(frame, (int(index_tip[0]), int(index_tip[1])),
                               10, (0, 255, 0), -1)

            # Display the frame
            cv2.imshow(DISPLAY_SETTINGS['window_name'], frame)

            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def cleanup(self):
        """Release resources."""
        self.cap.release()
        self.hand_tracker.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = MathVisionCanvas()
    try:
        app.run()
    finally:
        app.cleanup()