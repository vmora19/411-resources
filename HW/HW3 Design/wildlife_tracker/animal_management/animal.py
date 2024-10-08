from typing import Any, Optional

class Animal:

    def __init__(self,
                age: Optional[int],
                animal_id: int,
                health_status: Optional[str],
                species: str) -> None:
        self.age = age or None
        self.animal_id = animal_id
        self.species = species
        self.health_status = health_status or None
    
    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass
