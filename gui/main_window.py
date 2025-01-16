from PyQt5.QtWidgets import  QMainWindow,QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt
from backend.database_operations import get_material_data
from backend.calculations import calculate_costs
from gui.bar_plot import BarPlot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bridge Cost Comparison")
        self.setGeometry(100, 100, 900, 600)  # Set window size

        # Main layout
        layout = QHBoxLayout()

        # Left Panel: Inputs
        input_layout = QVBoxLayout()
        input_layout.setAlignment(Qt.AlignTop)

        self.span_length = QLineEdit()
        self.span_length.setPlaceholderText("Span Length (m)")
        input_layout.addWidget(QLabel("Span Length:"))
        input_layout.addWidget(self.span_length)

        self.width = QLineEdit()
        self.width.setPlaceholderText("Width (m)")
        input_layout.addWidget(QLabel("Width:"))
        input_layout.addWidget(self.width)

        self.traffic_volume = QLineEdit()
        self.traffic_volume.setPlaceholderText("Traffic Volume (vehicles/day)")
        input_layout.addWidget(QLabel("Traffic Volume:"))
        input_layout.addWidget(self.traffic_volume)

        self.design_life = QLineEdit()
        self.design_life.setPlaceholderText("Design Life (years)")
        input_layout.addWidget(QLabel("Design Life:"))
        input_layout.addWidget(self.design_life)

        self.calculate_button = QPushButton("Calculate Costs")
        self.calculate_button.clicked.connect(self.calculate_costs)
        input_layout.addWidget(self.calculate_button)

        # Add input layout to the main layout
        layout.addLayout(input_layout)

        # Center Panel: Bar Plot
        self.plot_container = QWidget()
        self.plot_layout = QVBoxLayout()
        self.plot_container.setLayout(self.plot_layout)
        layout.addWidget(self.plot_container, stretch=2)

        # Right Panel: Results Table
        self.results_table = QTableWidget(8, 3)
        self.results_table.setHorizontalHeaderLabels(["Cost Component", "Steel Bridge (₹)", "Concrete Bridge (₹)"])
        layout.addWidget(self.results_table, stretch=1)

        # Main widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate_costs(self):
        try:
            # Fetch input values
            length = float(self.span_length.text())
            width = float(self.width.text())
            traffic_volume = float(self.traffic_volume.text())
            design_life = int(self.design_life.text())

            # Fetch data from database
            steel_data = get_material_data("Steel")
            concrete_data = get_material_data("Concrete")

            # Perform calculations
            input_data = {
                "length": length,
                "width": width,
                "traffic_volume": traffic_volume,
                "design_life": design_life,
            }
            steel_costs = calculate_costs(input_data, steel_data)
            concrete_costs = calculate_costs(input_data, concrete_data)

            # Update results table
            self.update_results_table(steel_costs, concrete_costs)

            # Update bar plot
            self.update_bar_plot(steel_costs, concrete_costs)

        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Invalid input: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")

    def update_results_table(self, steel_costs, concrete_costs):
        cost_components = [
            "Construction Cost",
            "Maintenance Cost",
            "Repair Cost",
            "Demolition Cost",
            "Environmental Cost",
            "Social Cost",
            "User Cost",
            "Total Cost",
        ]

        for i, component in enumerate(cost_components):
            self.results_table.setItem(i, 0, QTableWidgetItem(component))
            self.results_table.setItem(i, 1, QTableWidgetItem(f"{steel_costs[component.lower().replace(' ', '_')]:,.2f}"))
            self.results_table.setItem(i, 2, QTableWidgetItem(f"{concrete_costs[component.lower().replace(' ', '_')]:,.2f}"))

    def update_bar_plot(self, steel_costs, concrete_costs):
        # Clear the existing plot
        for i in reversed(range(self.plot_layout.count())):
            self.plot_layout.itemAt(i).widget().deleteLater()

        # Create a new bar plot and add it to the layout
        bar_plot = BarPlot(steel_costs, concrete_costs)
        self.plot_layout.addWidget(bar_plot)
