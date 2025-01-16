from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class BarPlot(FigureCanvas):
    def __init__(self, steel_costs, concrete_costs):
        self.fig = Figure(figsize=(5, 3))
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

        # Data preparation
        components = [
            "Construction Cost",
            "Maintenance Cost",
            "Repair Cost",
            "Demolition Cost",
            "Environmental Cost",
            "Social Cost",
            "User Cost",
            "Total Cost",
        ]
        steel_values = [steel_costs[component.lower().replace(" ", "_")] for component in components]
        concrete_values = [concrete_costs[component.lower().replace(" ", "_")] for component in components]

        # Plotting
        x = range(len(components))
        self.ax.bar(x, steel_values, width=0.4, label="Steel", align="center")
        self.ax.bar([i + 0.4 for i in x], concrete_values, width=0.4, label="Concrete", align="center")
        self.ax.set_xticks([i + 0.2 for i in x])
        self.ax.set_xticklabels(components, rotation=45, ha="right")
        self.ax.set_title("Cost Comparison")
        self.ax.legend()

        self.draw()
