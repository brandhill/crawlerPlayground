# -*- coding: utf-8 -*-

class Lotto649Result:

    # def main(self):
    #   self.first_prizes = None
    #
    # if __name__ == '__main__':
    #     main()

    def __init__(self, value):
        self.dd = value


    def set_first_prizes(self, value):
        self.first_prizes = value

    def set_term(self, value):
        self.term = value

    def set_date(self, value):
        self.date = value

    def set_draw_sequences(self, value):
        self.draw_sequences = value
