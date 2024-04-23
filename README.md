<h1 align="center">
GOOGLE GIRL HACKATHON 2024
</h1>
<h3 align="center">
  The provided code aims to optimize the design of a Network-on-Chip (NOC) system. The problem statement entails building and optimizing the NOC to efficiently transfer data between various components of a System-on-Chip (SoC), including a CPU, IO peripherals, and system memory.
</h3>
<br>
  
## Building the NOC:
-The code defines classes for components of the NOC system, such as MachineLearningRouter and NetworkOnChip.

-The MachineLearningRouter class initializes a machine learning model (in this case, a RandomForestClassifier) to make routing decisions within the NOC.

-The NetworkOnChip class represents the NOC itself, with methods to handle routing traffic, setting buffer sizes, updating buffer occupancy, and adjusting arbiter weights.

## Optimizing the NOC:
-The simulate_system_on_chip function simulates the behavior of the entire system over multiple iterations.

-Within each iteration, simulated data transfer occurs between the CPU and IO peripherals through the NOC.

-Machine learning models are trained using dummy data to predict routing decisions, and these models are then used to route traffic through the NOC.

-Power and buffer occupancy are measured during simulation to assess the system's performance.

-The optimize_noc_design function dynamically adjusts buffer sizes and arbiter weights based on traffic patterns and system conditions.

-Optimization checks are performed to determine if the NOC design meets predefined criteria, such as latency and bandwidth requirements.

## Iterative Refinement:
-The entire process is iterative, with each iteration refining the NOC design based on simulation results.

-Buffer sizes, arbiter weights, and other parameters are continuously adjusted to achieve optimal performance.

-If the optimization criteria are met, the process terminates; otherwise, further iterations are performed until the criteria are satisfied.

