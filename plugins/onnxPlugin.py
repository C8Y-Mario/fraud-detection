import onnxruntime as rt
from apama.eplplugin import EPLPluginBase, EPLAction
import numpy as np

class ApamaONNXPlugin(EPLPluginBase):
    def __init__(self, init):
        super(ApamaONNXPlugin, self).__init__(init)
        self.loadedModel = False
        self._logger = self.getLogger()
        self._logger.info("testado")

    #method to load model into onnxEngine
    @EPLAction("action<string>", "loadModel")
    def loadModel(self, modelPath):
        self.session = rt.InferenceSession(modelPath)
        self.loadedModel = True
        self._logger.info("Model %s loaded successfully", modelPath)

    
    #method that runs the model and return the outputs
    @EPLAction("action<sequence<float> > returns sequence<any>")
    def executeModel(self, inputValues):
        # Perform preprocessing on the input data
        input_array = np.array(inputValues).reshape((1, len(inputValues))).astype(np.float32)

         # Get the names of the input and output nodes of the ONNX model
        input_name = self.session.get_inputs()[0].name
        output_name = self.session.get_outputs()[0].name

         # Pass the preprocessed input data to the ONNX Runtime
        output = self.session.run([output_name], {input_name: input_array})

        #Return output
        return output[0].tolist()