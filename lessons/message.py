"""Class to stora a message (operator overload, union types, default parameters)."""

class Email:

    to: str
    message: str
    important: bool

    def __init__(self, recipient: str, message_text: str, importance_flag: str):
        """Constructor of an email"""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag
    
    def __str__(self) -> str:
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}"'
        return m_string



email_to_chiara: Email = Email("Chiara", "You're a great TA!", False)
print(email_to_chiara)