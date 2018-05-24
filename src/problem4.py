"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Aaron Kondrat.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    pig1 = Pig(78)
    pig2 = Pig(28)

    print('The weight of the first pig is 78 lbs.')
    print('The weight of the first pig is', pig1.get_weight(), 'lbs.')

    print('The weight of the second pig is 28 lbs.')
    print('The weight of the second pig is', pig2.get_weight(), 'lbs.')

    pig1.eat(22)
    print('The first pig now weighs 100 lbs.')
    print('The first pig now weighs', pig1.get_weight(), 'lbs.')

    pig2.eat_for_a_year()
    print('The second pig now weighs 66823 lbs.')
    print('The second pig now weighs', pig2.get_weight(), 'lbs.')

    # print('The heavier pig is the other pig.')
    # print('The heavier pig is the', pig1.heavier_pig(pig2), '.')

    pig3 = pig1.new_pig(pig2)
    print('The weight of the third pig is', pig2.get_weight(), 'lbs.')
    print('The weight of the third pig is', pig3.get_weight(), 'lbs.')


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        self.weight = weight
        # DONE: Implement and test this method.

    def get_weight(self):
        """ Returns this Pig's weight. """
        return self.weight
        # DONE: Implement and test this method.

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        self.weight = self.weight + pounds_of_slop
        # DONE: Implement and test this method.

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        for k in range(365):
            self.eat(k + 1)
        # DONE: Implement and test this method.

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        if self.weight > other_pig.weight:
            return self
        else:
            return other_pig
        # DONE: Implement and test this method.

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        new_pig = Pig(self.heavier_pig(other_pig).get_weight())
        return new_pig
        # DONE: Implement and test this method.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
