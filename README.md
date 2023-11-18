# Mutation Testing

## Introduction:
The goal of mutation testing is to assess the quality of the test suite by introducing small changes (mutations) to the code and observing how well the tests detect these changes. This process helps identify areas of weakness in the test suite and suggests improvements.

## List of defined mutation operators:
Mutation Operator 1: Addition<br>
Mutation Operator 2: Subtraction<br>
Mutation Operator 3: Multiplication<br>
Mutation Operator 4: Logical OR<br>
Mutation Operator 5: Less than<br>

## Description of applied mutations and their impact:
The Python code underwent mutation testing using a set of predefined mutation operators. These intentional faults, introduced through mutations, aimed to assess the resilience of the test suite. The mutations encompassed focusing on arithmetic and logical operators.

## Summary of mutant survival and killing:
From the utilization of Mutatest:

**Overall mutation trial summary**
 - ERROR: 33
 - DETECTED: 42
 - SURVIVED: 16
 - TOTAL RUNS: 91

**DETECTED**
 - polynomial.py: (l: 13, c: 8) - mutation from If_Statement to If_True
 - polynomial.py: (l: 13, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - polynomial.py: (l: 13, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - polynomial.py: (l: 17, c: 12) - mutation from If_Statement to If_False
 - polynomial.py: (l: 17, c: 12) - mutation from If_Statement to If_True
 - polynomial.py: (l: 17, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - polynomial.py: (l: 17, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - polynomial.py: (l: 17, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - polynomial.py: (l: 17, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - polynomial.py: (l: 17, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - polynomial.py: (l: 20, c: 12) - mutation from If_Statement to If_False
 - polynomial.py: (l: 20, c: 12) - mutation from If_Statement to If_True
 - polynomial.py: (l: 20, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - polynomial.py: (l: 20, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - polynomial.py: (l: 20, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - polynomial.py: (l: 20, c: 19) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - polynomial.py: (l: 20, c: 19) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - polynomial.py: (l: 20, c: 19) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - polynomial.py: (l: 20, c: 19) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - polynomial.py: (l: 20, c: 19) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 20, c: 19) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - polynomial.py: (l: 21, c: 16) - mutation from If_Statement to If_True
 - polynomial.py: (l: 21, c: 16) - mutation from If_Statement to If_False
 - polynomial.py: (l: 21, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - polynomial.py: (l: 21, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - polynomial.py: (l: 21, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - polynomial.py: (l: 33, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - polynomial.py: (l: 33, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - polynomial.py: (l: 33, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - polynomial.py: (l: 33, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - polynomial.py: (l: 34, c: 30) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - polynomial.py: (l: 35, c: 31) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - polynomial.py: (l: 45, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - polynomial.py: (l: 56, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - polynomial.py: (l: 56, c: 46) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - polynomial.py: (l: 65, c: 28) - mutation from <class 'ast.Pow'> to <class 'ast.Add'>

**SURVIVED**
 - polynomial.py: (l: 13, c: 8) - mutation from If_Statement to If_False
 - polynomial.py: (l: 13, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - polynomial.py: (l: 20, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - polynomial.py: (l: 21, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - polynomial.py: (l: 21, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 24, c: 39) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - polynomial.py: (l: 33, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 34, c: 30) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 43, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 44, c: 30) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - polynomial.py: (l: 56, c: 46) - mutation from <class 'ast.Mult'> to <class 'ast.FloorDiv'>
 - polynomial.py: (l: 72, c: 16) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - polynomial.py: (l: 72, c: 54) - mutation from Slice_UnboundLower to Slice_Unbounded
 - polynomial.py: (l: 83, c: 11) - mutation from <class 'ast.Mult'> to <class 'ast.Div'>
 - polynomial.py: (l: 87, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - polynomial.py: (l: 105, c: 15) - mutation from <class 'ast.Mult'> to <class 'ast.Sub'>

## Analysis of the test suite's effectiveness:
The presence of a significant number of mutants indicates potential areas where the test suite may have insufficient coverage. Analyzing the surviving mutants can provide perspectives into specific scenarios or conditions that might not be adequately addressed by the existing set of test cases.

## Recommendations for improving the test suite:
Expand the test coverage to include additional scenarios that were not sufficiently handled in the initial set of test cases.

The result:

**Overall mutation trial summary**
 - DETECTED: 56
 - SURVIVED: 11
 - ERROR: 36
 - TOTAL RUNS: 104

## Conclusion:
Based on the provided output, it is evident that the number of surviving mutants has decreased by 5. Mutation testing serves as a valuable tool for assessing the robustness of a test suite by mimicking possible defects within the code. Although the existing test suite has effectively eliminated some mutants, the presence of survivors indicates areas where further refinement is needed. Incorporating the enhancements will elevate the quality of the test suite, leading to more thorough code testing.
