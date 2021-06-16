WeightsFile  = open("weights.txt", "w+")
WeightsList = WeightsFile.readlines()



class Layer:
	def __init__(self, Neurons, Input = False)
		self.input = Input
		self.Neurons = Neurons
		self.NeuronCount = len(Neurons)
	def AppendNeuron(self, Neuron):
		self.Neurons.append(Neuron)
class Neuron:
	def __init__(self, Ineurons, WeightsIndex, layer):
		WeightsIE = len(Ineurons) + WeightsIndex
		self.weights = WeightsList[WeightsIndex:WeightsIE]
		self.Ineurons = Ineurons
		self.bias = WeightsList[WeightsIE+1]

	def __exec__(self):
		return [i() *  float(w) for i, w in zip(self.Ineurons, self.weights)]
