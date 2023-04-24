class Planet:

    def __init__ (self, id, name, description, temperature):
        self.id = id
        self.name = name
        self.description = description
        self.temperature = temperature

Planet = [Planet(1, "Mercury", "smallest planet", 333),
        Planet(2, "Venus", "thick and toxic atmosphere", 867),
        Planet(3,"Earth", "our home planet", 59),
        Planet(4, "Mars", "dusty, cold, thin atmopshere", -85),
        Planet(5, "Jupiter", "largest planet in solar system", -166),
        Planet(6, "Saturn", "second largest planet in solar system", -220),
        Planet(7, "Uranus", "mostly made up of water, ammonia, and methane", -320),
        Planet(8, "Neptune", "dark, cold with supersonic winds")
]