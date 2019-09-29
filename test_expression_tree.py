from tree.expression_tree import tokenize, build_expression_tree

big = build_expression_tree(tokenize('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'))
print(big, '=', big.evaluate())