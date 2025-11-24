# Face Editor
class FaceEditor:
    def __init__(self, widget=None, parameters=None, add_action=None):
        self.data = {}
        self.widget = widget or {}
        self.parameters = parameters or {}
        self.add_action = add_action or (lambda action, params: None)

        # Default parameters for a face
        self.default_parameters = [
            'Human-Face', 2.50, 0.00, 0.00, 0, 0, 0, 0.00, 0.00, 1.00, 0.00, 0.00, 0.00, 0,
            0.00, 0.00, 0.00, 0.00, 0.00
        ]

        # Map parameter names to widget keys
        # Mappatura dei nomi dei widget agli indici dei parametri
        self.parameter_map = {
            "FaceEditorTypeTextSel": 0,
            "CropScaleSlider": 1,
            "EyesOpenRatioSlider": 2,
            "LipsOpenRatioSlider": 3,
            "HeadPitchSlider": 4,
            "HeadYawSlider": 5,
            "HeadRollSlider": 6,
            "XAxisMovementSlider": 7,
            "YAxisMovementSlider": 8,
            "ZAxisMovementSlider": 9,
            "MouthPoutingSlider": 10,
            "MouthPursingSlider": 11,
            "MouthGrinSlider": 12,
            "LipsCloseOpenSlider": 13,
            "MouthSmileSlider": 14,
            "EyeWinkSlider": 15,
            "EyeBrowsDirectionSlider": 16,
            "EyeGazeHorizontalSlider": 17,
            "EyeGazeVerticalSlider": 18
        }

        self.default_named_parameters = {name: self.default_parameters[index] for name, index in self.parameter_map.items()}

    def add_parameters(self, frame_number, face_id, parameters):
        if frame_number not in self.data:
            self.data[frame_number] = {}
        self.data[frame_number][face_id] = parameters

    def get_parameters(self, frame_number, face_id):
        return self.data.get(frame_number, {}).get(face_id, None)

    def get_named_parameters(self, frame_number, face_id):
        """
        Restituisce una lista di tuple (nome_parametro, valore) per un dato frame e face_id.
        """
        parameters = self.get_parameters(frame_number, face_id) or self.default_parameters

        # Crea un dizionario con i nomi dei parametri come chiavi e i loro valori
        named_parameters = {name: parameters[index] for name, index in self.parameter_map.items()}

        return named_parameters

    def are_parameters_default(self, parameters):
        """
        Verifica se i parameters forniti sono uguali a self.default_parameters.
        """
        return parameters == self.default_parameters

    def are_named_parameters_default(self, named_parameters):
        """
        Verifica se i named_parameters forniti sono uguali a self.default_parameters.
        """
        return named_parameters == self.default_named_parameters

    def get_all_parameters_for_frame(self, frame_number):
        return self.data.get(frame_number, {})

    def reset_parameters_for_face_id(self, frame_number, face_id):
        if frame_number in self.data and face_id in self.data[frame_number]:
            self.data[frame_number][face_id] = self.default_parameters.copy()

    def remove_all_parameters_for_frame(self, frame_number):
        if frame_number in self.data:
            self.data[frame_number] = {}

    def remove_all_data(self):
        self.data = {}

    def apply_max_face_id_to_widget(self, frame_number, value):
        if self.widget and self.parameters and self.add_action:
            if self.widget['FaceEditorIDSlider'].set_max(value, False):
                self.apply_changes_to_widget_and_parameters(frame_number, self.widget['FaceIDSlider'].get())

                return True

            return False

    def apply_changes_to_widget_and_parameters(self, frame_number, face_id):
        parameters = self.get_parameters(frame_number, face_id) or self.default_parameters
        self.parameters['FaceEditorIDSlider'] = face_id
        self.widget.get('FaceEditorIDSlider', {}).set(face_id, request_frame=False)

        for i, param_key in enumerate(self.parameter_map):
            value = parameters[i]
            if param_key in self.widget:
                self.widget[param_key].set(value, request_frame=False)
            self.parameters[param_key] = value

        self.add_action('parameters_face_editor', self.parameters)