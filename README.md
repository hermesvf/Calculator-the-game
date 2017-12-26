# Calculator: The Game
A CLI solver for the game [Calculator](https://play.google.com/store/apps/details?id=com.sm.calculateme&hl=en).

![Banner image of the app](http://www.appunwrapper.com/wp-content/uploads/2017/07/image-312-1.jpg)

## Summary ##

Calculator is a mobile game that consists of performing a number of chained operations to one number in order to get another number. This operations can be either mathematical or digit-manipulation ones.

The game currently has 200 levels. As the level increases, more operations are unlocked.

![Some levels of the app](https://i.imgur.com/9LuaQzY.png)

### Operations ###

* Addition
* Substraction
* Multiplication
* Division
* Digit replacement
* Sign change
* Shift left *(removes the last digit)*
* Reverse

## Wanna try it out? ##

1. **Clone this repo**
```
git clone https://github.com/hermesvf/Calculator-the-game.git
```

2. **Run the solver**
```
python3 solve.py 123 64 4 +2 -5 *6 /9 R A5 S X9:0
```

This is how the parameters should be entered:
```
Usage: python3 solve.py <source> <target> <steps> <op_1> [<op_2> ... <op_n>]

```
