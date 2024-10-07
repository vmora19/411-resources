from typing import Any, Optional

class Animal:

    def __init__(self,
                age: Optional[int],
                animal_id: int) -> None:
        self.age = age
        self.animal_id = animal_id
    
    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass
