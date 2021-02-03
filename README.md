# Boolean Algebra

This repository is a collection of functions practicing working with Boolean Algebra and truth tables. It is being done in conjuction with working through the *Nand to Tetris* book, but is not necessarily meant to actually program an operating system so much as to explore the underlying Boolean structures and logic.

## Notes:

**Boolean Expressions**
    x*y = x AND y
    x+y = x OR y
    ~x = NOT x

**Boolean Functions with Two Variables**
|             | x               | 0 0 1 1 |
|             | y               | 0 1 0 1 |
| :---------- | :-------------: | ------: |
| Constant 0  | 0               | 0 0 0 0 |
| And         | x * y           | 0 0 0 1 |
| x And Not y | x * ~y          | 0 0 1 0 |
| x           | x               | 0 0 1 1 |
| Not x And y | ~x * y          | 0 1 0 0 |
| y           | y               | 0 1 0 1 |
| Xor         | x * ~y + ~x * y | 0 1 1 0 |
| Or          | x + y           | 0 1 1 1 |
| Nor         | ~(x + y)        | 1 0 0 0 |
| Equivalence | x * y + ~x * ~y | 1 0 0 1 |
| Not y       | ~y              | 1 0 1 0 |
| If y then x | x + ~y          | 1 0 1 1 |
| Not x       | ~x              | 1 1 0 0 |
| If x then y | ~x + y          | 1 1 0 1 |
| Nand        | ~(x * y)        | 1 1 1 0 |
| Constant 1  | 1               | 1 1 1 1 |

