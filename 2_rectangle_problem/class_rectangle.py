class Rectangle:
    def __init__(self, length: int, width: int):
        """Constructor of class Rectangle

        Args:
            length (int): Length of Rectangle
            width (int): Width or Breadth of Rectangle
        """
        self.length = length
        self.width = width

    def __iter__(self):
        """
        Create an iterator to itorate upon dictionary.

        Returns:
            _type_: return the iterator object itself
        """
        self.dimensions = [{"length": self.length}, {"width": self.width}]
        self.index = 0
        return self

    def __next__(self):
        """_summary_

        Raises:
            StopIteration: To stop iteration when iterator object reaches its length.

        Returns:
            _type_: return the next item in the sequence.
        """
        if self.index >= len(self.dimensions):
            raise StopIteration

        result = self.dimensions[self.index]
        self.index += 1
        return result


rect = Rectangle(5, 3)

for values in rect:
    print(values, end=" ")

# we can convert it into a list
# its_values = list(rect_value)
# print(its_values)
