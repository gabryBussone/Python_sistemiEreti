import turtle

class Barcode:
    def __init__(self):
        self.t = turtle.Turtle()

    def draw_bar(self, color, width, height):
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(width)
            self.t.left(90)
            self.t.forward(height)
            self.t.left(90)
        self.t.end_fill()
        self.t.forward(1)

    def draw_binary_barcode(self, binary_string):
        for bit in binary_string:
            if bit == '1':
                self.draw_bar("black", 4, 100)
            else:
                self.draw_bar("white", 4, 100)

    def generate_binary_string(self, text):
        binary_string = ""
        for char in text:
            ascii_code = ord(char)
            binary_representation = format(ascii_code, '08b')
            binary_string += binary_representation
        return binary_string

    def draw_barcode(self, text):
        binary_string = self.generate_binary_string(text)
        self.draw_binary_barcode(binary_string)

def main():
    barcode_generator = Barcode()
    text_to_encode = "Hello123"
    barcode_generator.draw_barcode(text_to_encode)
    turtle.done()

if __name__ == "__main__":
    main()
