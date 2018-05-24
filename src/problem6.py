"""
Final exam, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, their colleagues,
         and Aaron Kondrat.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: n=5')
    shape(5)

    print()
    print('Test 2 of shape: n=3')
    shape(3)

    print()
    print('Test 3 of shape: n=14')
    shape(14)


def shape(n):
    ####################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ####################################################################
    """
    Prints a shape with numbers on the left side of the shape,
    other numbers on the right side of the shape,
    and stars in the middle,per the pattern in the examples below.
    When the pattern calls for a number with more than one digit,
    just use the last (rightmost) digit when you print that number.

    It looks like this example for n=5:
    1 ** 54321
   12 *** 4321
  123 **** 321
 1234 ***** 21
12345 ****** 1

    And this one for n=3:
  1 ** 321
 12 *** 21
123 **** 1


And this one for n=14:
             1 ** 43210987654321
            12 *** 3210987654321
           123 **** 210987654321
          1234 ***** 10987654321
         12345 ****** 0987654321
        123456 ******* 987654321
       1234567 ******** 87654321
      12345678 ********* 7654321
     123456789 ********** 654321
    1234567890 *********** 54321
   12345678901 ************ 4321
  123456789012 ************* 321
 1234567890123 ************** 21
12345678901234 *************** 1

    :type n: int
    """
    x = 1
    seq = []
    for k in range(n):
        if x == 10:
            x = 0
        seq = seq + [x]
        x = x + 1
    for k in range(n):
        for j in range(n - k - 1):
            print(' ', end='')
        for i in range(k + 1):
            print(seq[i], end='')
        print(' ', end='')
        for h in range(k + 2):
            print('*', end='')
        print(' ', end='')
        for g in range(len(seq)-k-1, -1, -1):
            print(seq[g], end='')
        print('')


    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #          Some tests are already written for you (above).
    ####################################################################
    # IMPORTANT: In solving this problem,
    #   You must NOT use string multiplication.
    ####################################################################
    #
    # HINT:
    #   If you're having trouble with the spaces on the left,
    #   print Xs for the spaces until you figure out where the problem is
    #   (and then change the Xs back to spaces).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
