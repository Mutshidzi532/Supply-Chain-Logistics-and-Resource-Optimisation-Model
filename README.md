# Supply-Chain-Logistics-and-Resource-Optimisation-Model
An applied mathematics project leveraging Linear Programming to optimise supply chain resource allocation. Built using Python (SciPy and NumPy) to solve complex operational constraints, minimise distribution costs, and translate complex data matrices into clear, actionable business insights.
# Logistics Optimisation & Supply Chain Resource Model

An applied mathematics and operations research project leveraging **Linear Programming** to solve complex supply chain allocation constraints, minimising distribution overheads whilst fully meeting localised dealership demand variables.

## 📊 Business Case & Focus
In heavy machinery distribution systems (such as Caterpillar's dealership network), routing equipment and spare parts efficiently from central distribution centres to specific market hubs directly impacts bottom-line operational efficiency. This system models distribution flows using deterministic mathematical programming techniques.

## 🛠️ Tech Stack & Methodologies
* **Language:** Python 3
* **Libraries:** SciPy (Optimisation module), NumPy (Data structures)
* **Mathematical Method:** Linear Programming (Simplex / HiGHS optimisation solver)

## 📈 Model Architecture
* **Objective Function:** Minimise total regional transit costs across multiple nodes.
* **Supply Constraints:** Upper bounds limiting maximum output capacity from active supply depots.
* **Demand Constraints:** Strict equality requirements ensuring dealerships receive exact resource volumes needed for operational uptime.
