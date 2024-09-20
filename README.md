# Flow Control - Extra Challenge
Below are a set of additional challenges on flow control

These are deliberatly a challenge, so do not be discouraged if you struggle - perservere and seek help when you need it

You are free to use all control structures we have looked at - for, while, if, match

Some challenges will impose specific limitations/rules to add to the overall challenge - these are generally designed to prevent you from finding "shortcuts" and to allow you to develop the core skills we are focused on

But - always remember that in real software development, taking shortcuts is always encouraged (as long as its not at the expense of quality!)

## Challenge 1 - Sort the Names

Your starter code is a function that will read in a list of names and store it in the variable "start_list"

Each item of the list will be a string of the form "firstName lastName", for example:
```
    ["Geoff Jefferson", "Gerogina Georgeson"]
```
and so on

Your task is to write a program that will rearrange the list to sort the names by the length of the surnames, in ascending order - if two surnames are of equal length then they should be sorted in alphabetical order, for example:

```
    task_1([
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
    ]) ➞ ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]
```

<span style="color: red; font-weight: bold;">Restriction - you may not use ANY pre-defined/built in sorting function in Python, such as the sort() function</span>

## Challenge 2 - Repeating Numbers

For this code you have a function that once again reads in a list of strings

For this one, each item in the list will simply be a single, lower case character

You may assume all lists used will follow this rule

You are going to "compress" the list into a string of letters and numbers according to the following rules:
* If the number of repeating characters is 1, append the string with only this character
* If the number of repeating characters is > 1, append the string with the character and the number of repeats as a digit

For example:
```
task_2(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

task_2(["a"]) ➞ "a"
```

As an additional challenge, if the same character is repeated but not sequentially (i.e. they are not next to each other) the output string should reflect this and maintain the origional order, for example:

```
task_2(["a", "b", "a", "c", "a", "d", "a", "a"]) ➞ "abacabada2"
```
Your code should also return an empty string if the list is empty

## Challenge 3 - The Very Expensive Staircase

There is a staicase which is very expensive to climb, you must pay an integer amount for each step you stop on!

Your code will read in a list of integers - you may assume all integers are above or equal 0

These integers are the price of each step, starting at step 1

When climbing this staircase, you may climb one or two steps each "turn" then pay the cost of the step you are on

You will write a program that works out the minimum cost of climbing a given staircase based on the list of prices given

Remember that you may climb one or two steps each time

*NOTE* - the top "step" (i.e. the final item in a list) is **NOT** the top...it is the final step on the staircase, the top would be going beyond the end of the list - this means that the final payment is calculated when you reach either the final list item (list[-1]), or the second-to-last (list[-2])

Examples are shown below:

```
climbing_stairs([0, 2, 2, 1]) ➞ 2

climbing_stairs([0, 2, 3, 2]) ➞ 3

climbing_stairs([10, 15, 20]) ➞ 15

climbing_stairs([0, 0, 0, 0, 0, 0]) ➞ 0
```