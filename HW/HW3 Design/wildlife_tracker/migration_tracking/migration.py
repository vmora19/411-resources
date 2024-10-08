from typing import Any

class Migration:
    def __init__(self,
                migration_id: int,
                current_location: str,
                start_date: str,
                ) -> None:
                self.migration_id = migration_id
                self.current_location = current_location
                self.start_date = start_date

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass