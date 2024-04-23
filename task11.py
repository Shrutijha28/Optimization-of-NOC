import numpy as np

class Particle:
    def __init__(self, dim, min_values, max_values):
        self.position = np.random.uniform(min_values, max_values, dim)
        self.velocity = np.zeros(dim)
        self.best_position = self.position
        self.best_score = float('inf')

    def update_velocity(self, global_best_position, inertia_weight, cognitive_weight, social_weight):
        self.velocity = inertia_weight * self.velocity \
                        + cognitive_weight * np.random.rand() * (self.best_position - self.position) \
                        + social_weight * np.random.rand() * (global_best_position - self.position)

    def update_position(self):
        self.position += self.velocity

def particle_swarm_optimization(dim, num_particles, num_iterations, min_values, max_values, fitness_function):
    particles = [Particle(dim, min_values, max_values) for _ in range(num_particles)]
    global_best_position = np.zeros(dim)
    global_best_score = float('inf')

    for _ in range(num_iterations):
        for particle in particles:
            score = fitness_function(particle.position)
            if score < particle.best_score:
                particle.best_score = score
                particle.best_position = particle.position

            if score < global_best_score:
                global_best_score = score
                global_best_position = particle.position

        for particle in particles:
            particle.update_velocity(global_best_position, 0.5, 0.5, 0.5)
            particle.update_position()

    return global_best_position

# Define the evaluate_performance function
def evaluate_performance(parameters):
    # Example: Simulate NOC performance using the parameters and return a single fitness score
    # Example calculation for latency
    latency = parameters[0] * 0.5 + parameters[1] * 0.3
    # You can add more complex calculations based on the problem statement
    # For now, let's return the latency as the fitness score
    return latency

# Example usage
optimized_parameters = particle_swarm_optimization(
    dim=2,
    num_particles=10,
    num_iterations=100,
    min_values=[0, 0],
    max_values=[100, 100],
    fitness_function=evaluate_performance
)
print("Optimized parameters:", optimized_parameters)
