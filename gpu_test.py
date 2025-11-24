import onnxruntime as ort

providers = ort.get_available_providers()
print("Available providers:", providers)

sess = ort.InferenceSession("det_10g.onnx", providers=["CPUExecutionProvider"])
print("Session initialized successfully.")