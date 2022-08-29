This section contains all the matrials regarding "TESTING" of an application. We'll define some of the main operating functions.

I. test_add() --
   Addition of two numbers, to be precise integers and rationals.
   Input: user is expected to enter two numbers as per the allowed data types.
   Output: final result will be returned after performing the addition operation on the two input numbers.
   Intuition: Given A and B => result = A + B

II. test_subract() --
    Given two numbers, perform subtraction and return the result
    The same input format is expected from the user.
    Output: final result will be returned after performing the subtration operation.
    Intuition: Given A and B => result = A - B

III. test_multiply() --
      Given two numbers, compute the scaler product and return the result
      The same input format is expected from the user.
      Output: final result will be returned after performing the  operation.
      Intuition: Given A and B => result = A * B

IV. test_divide() --
      Given two numbers, compute the quotient obtained by dividing the two numbers and return the result.
      The same input format is expected from the user.
      Output: final result will be returned after performing the division operation.
      Intuition: Given A and B => result = A / B

V. test_valid_inputs() --
     This function validates, or in other words, tests if the numbers entered by the user is according to the rules.
     The same input format is expected from the user

VI. test_valid_operators() --
      Runs a check on the operators used in the arithmatic operations to see if they are used properly or not.
      The same input format is expected from the user
      The allowed operators are " + ", " - ", " * " and " / ".

VII. test_invalid_inputs() --
        This will make sure that the inputs are entered correctly. The only difference between this function and test_valid_inputs() is that the former checks for valid inputs and the later checks for invalid inputs.  
        The same input format is expected by the user.
        Output: an error message will be generated on entering incorrect inputs

VIII. test_invalid_operators() --
         Finally, this does the same job as the previous function did and the only difference between this and test_valid_operators() is that the former checks the valid ones and the latter checks the
         invalid ones.
         Output: an error message will be generated on entering incorrect operators





