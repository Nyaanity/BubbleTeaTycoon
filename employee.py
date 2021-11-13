import names


class Employee:
    """A class representing an employee."""

    def __init__(self):
        """Initialize."""
        self.name = names.get_full_name()

    def __repr__(self):
        return f'<Employee name={self.name}>'
    
    def __str__(self):
        return self.name