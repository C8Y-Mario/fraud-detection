from apama.eplplugin import EPLPluginBase, EPLAction
import csv

class DataLoaderPlugin(EPLPluginBase):
    def __init__(self, init):
        super(DataLoaderPlugin, self).__init__(init)
        self.loadedModel = False
        self._logger = self.getLogger()
        self._logger.info("DataLoaderPlugin initialized")

    # method to load model into onnxEngine
    @EPLAction("action<string> returns sequence<dictionary<string, any>>", "loadCsv")
    def loadCsv(self, modelPath):
        self._logger.info("Model %s loaded successfully", modelPath)
        json_objects = []

        # Open the CSV file
        with open(modelPath, mode='r', newline='') as file:
            # Create a CSV reader object
            reader = csv.DictReader(file)

            # Iterate over the rows in the CSV file and convert them into JSON objects
            for row in reader:
                json_objects.append(row)
        return json_objects