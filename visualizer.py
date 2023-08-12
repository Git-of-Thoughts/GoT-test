import matplotlib.pyplot as plt

class Visualizer:
    def plot_dca_return(self, dca_return):
        plt.figure(figsize=(10, 6))
        plt.title('DCA Strategy Return')
        plt.plot(dca_return)
        plt.show()

    def plot_sensitivity_results(self, sensitivity_results):
        plt.figure(figsize=(10, 6))
        plt.title('Sensitivity Analysis Results')
        plt.plot(sensitivity_results)
        plt.show()
