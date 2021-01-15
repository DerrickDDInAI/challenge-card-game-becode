class Symbol:
    """
    Symbol has 2 attributes: color and icon
    * color: string
    * icon: string in the list [♥, ♦, ♣, ♠]
    """

    def __init__(self, color: str, icon: str):
        """
        Function that creates an instance of Symbol class
        """
        self.color = color
        self.icon = icon

    def __str__(self):
        """
        Function that prints the Symbol object's attributes 
        """
        return f"{self.color} {self.icon}"


class Card(Symbol):
    """
    Card is a child class of Symbol.
    Card has one more attribute: value
    * value: string in the list ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
    """

    def __init__(self, color: str, icon: str, value: str):
        """
        Function that creates an instance of Card class
        """
        super().__init__(color, icon)
        self.value = value

    def __str__(self):
        """
        Function that prints the Card object's attributes
        """
        return f"{self.value} {self.color} {self.icon}"


# CONSTANTS
SYMBOL_LIST = [
    Symbol("RED", "♥"),
    Symbol("RED", "♦"),
    Symbol("BLACK", "♣"),
    Symbol("BLACK", "♠"),
]
VALUE_LIST = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# if the module run is the main program, it performs the following tests
if __name__ == "__main__":
    symbol_1 = Symbol("red", "♥")
    print(symbol_1)

    card_1 = Card("black", "♥", 10)
    print(card_1)
