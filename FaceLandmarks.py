# Face Landmarks
class FaceLandmarks:
    def __init__(self, widget = {}, parameters = {}, add_action = {}):
        self.data = {}
        self.widget = widget
        self.parameters = parameters
        self.add_action = add_action

    def add_landmarks(self, frame_number, face_id, landmarks):
        if frame_number not in self.data:
            self.data[frame_number] = {}
        self.data[frame_number][face_id] = landmarks

    def get_landmarks(self, frame_number, face_id):
        return self.data.get(frame_number, {}).get(face_id, None)

    def get_all_landmarks_for_frame(self, frame_number):
        return self.data.get(frame_number, {})


    def remove_all_landmarks_for_frame(self, frame_number):
        if frame_number in self.data:
            self.data[frame_number] = {}

    def remove_all_data(self):
        self.data = {}

    def apply_max_face_id_to_widget(self, frame_number, value):
        if self.widget and self.parameters and self.add_action:
            if self.widget['FaceIDSlider'].set_max(value, False):
                self.apply_changes_to_widget_and_parameters(frame_number, self.widget['FaceIDSlider'].get())

                return True

            return False

    def apply_changes_to_widget_and_parameters(self, frame_number, face_id):
        if self.widget and self.parameters and self.add_action:
            landmarks = self.data.get(frame_number, {}).get(face_id, None)
            if landmarks is not None:
                self.widget['FaceIDSlider'].set(face_id, request_frame=False)
                self.parameters['FaceIDSlider'] = face_id

                self.widget['EyeLeftXSlider'].set(landmarks[0][0], request_frame=False)
                self.parameters['EyeLeftXSlider'] = landmarks[0][0]

                self.widget['EyeLeftYSlider'].set(landmarks[0][1], request_frame=False)
                self.parameters['EyeLeftYSlider'] = landmarks[0][1]

                self.widget['EyeRightXSlider'].set(landmarks[1][0], request_frame=False)
                self.parameters['EyeRightXSlider'] = landmarks[1][0]

                self.widget['EyeRightYSlider'].set(landmarks[1][1], request_frame=False)
                self.parameters['EyeRightYSlider'] = landmarks[1][1]

                self.widget['NoseXSlider'].set(landmarks[2][0], request_frame=False)
                self.parameters['NoseXSlider'] = landmarks[2][0]

                self.widget['NoseYSlider'].set(landmarks[2][1], request_frame=False)
                self.parameters['NoseYSlider'] = landmarks[2][1]

                self.widget['MouthLeftXSlider'].set(landmarks[3][0], request_frame=False)
                self.parameters['MouthLeftXSlider'] = landmarks[3][0]

                self.widget['MouthLeftYSlider'].set(landmarks[3][1], request_frame=False)
                self.parameters['MouthLeftYSlider'] = landmarks[3][1]

                self.widget['MouthRightXSlider'].set(landmarks[4][0], request_frame=False)
                self.parameters['MouthRightXSlider'] = landmarks[4][0]

                self.widget['MouthRightYSlider'].set(landmarks[4][1], request_frame=False)
                self.parameters['MouthRightYSlider'] = landmarks[4][1]

            else:
                self.widget['FaceIDSlider'].set(1, request_frame=False)
                self.parameters['FaceIDSlider'] = 1

                self.widget['EyeLeftXSlider'].set(0, request_frame=False)
                self.parameters['EyeLeftXSlider'] = 0

                self.widget['EyeLeftYSlider'].set(0, request_frame=False)
                self.parameters['EyeLeftYSlider'] = 0

                self.widget['EyeRightXSlider'].set(0, request_frame=False)
                self.parameters['EyeRightXSlider'] = 0

                self.widget['EyeRightYSlider'].set(0, request_frame=False)
                self.parameters['EyeRightYSlider'] = 0

                self.widget['NoseXSlider'].set(0, request_frame=False)
                self.parameters['NoseXSlider'] = 0

                self.widget['NoseYSlider'].set(0, request_frame=False)
                self.parameters['NoseYSlider'] = 0

                self.widget['MouthLeftXSlider'].set(0, request_frame=False)
                self.parameters['MouthLeftXSlider'] = 0

                self.widget['MouthLeftYSlider'].set(0, request_frame=False)
                self.parameters['MouthLeftYSlider'] = 0

                self.widget['MouthRightXSlider'].set(0, request_frame=False)
                self.parameters['MouthRightXSlider'] = 0

                self.widget['MouthRightYSlider'].set(0, request_frame=False)
                self.parameters['MouthRightYSlider'] = 0


            self.add_action('parameters', self.parameters)
