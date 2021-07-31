# Overview
- 'strongly-typed' language: data types must be defined, which helps avoid errors
- 'statically-typed'
- Often very object oriented
- C# is fast -- in one case, .NET CORE is up to 2,000 times faster than Node (the leading javascript server technology.)
- Unity projects, a popular 3D/2D game-making application, are written in C#

--------
<br>

# Links/Documentation:
[Microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/)

--------
<br>

# Data Types
Might be different in .NET than in Unity?

| Type     | Size (bytes)      | Descrip | Range                                 |
| -------- | ----------------- | ------- | ------------------------------------- |
| int      | 4                 |         | about 2 billion, negative to positive |
| long     | 8                 |         | really big                            |
| float    | 4                 |         |                                       |
| double   | 8                 |         |                                       |
| decimal  | 16                |         |                                       |
| char     | 2                 |         |                                       |
| bool     | 1                 |         |                                       |
| DateTime | 8                 |         |                                       |
| string   | 2 (per character) |         |                                       |

### Defining data types
Declaring:
`int myAge;`

Setting:
`myAge = 32;`

Declaring and setting together:
`int myAge = 32`

**floats, doubles, decimals**
^This order is from least precise but least memory used to most precise and most memory used. Note: when defining a decimal, you must include an `m` at the end, like this:
`decimal myDecimal = 23423.234234m`
Otherwise compiling will runan error.

### Math
If a less exact data type is added to a more exact one, the result will always be returned in the more exact data type.

However, two integers will always return an integer, and so on.

**Incrementing and decremting**
Incrementing by 1:
`++`
Decrementing by 1:
`--`
Incrementing by some other number, like 3:
`variable += 3`

### Modulo
`%`

**More complex math operations:**
-   `Math.Abs()`—will find the absolute value of a number. Example: `Math.Abs(-5)` returns 5.
-   `Math.Sqrt()`—will find the square root of a number. Example: `Math.Sqrt(16)` returns 4.
-   `Math.Floor()`—will round the given double or decimal down to the nearest whole number. Example: `Math.Floor(8.65)` returns 8.
-   `Math.Min()`—returns the smaller of two numbers. Example: `Math.Min(39, 12)` returns 12.


### Casting
There are casting functions for each variable type. For example, `(int)myDouble` will convert a double called myDouble into an int. So `(int)` is actually an operator called a "cast".

There are also methods, like `Convert.ToString()`, or `Convert.ToInt32()`

Sometimes casting will work, but it is designed to fail before it destroys any information. That's where the `Convert.ToX()` functions are useful. They are more determined.

### Checking the type of a variable
`someVariable.GetType()`: runtime
`someVariable.typeof()`: compiletime

--------
<br>

# Strings
Don't forget to escape quotes: `\"`
And use the escape slash to make a new line: `\n`
Note:  If we want to concatenate a string with something that is another data type, C# will implicitly convert that value to a string.

### Interpolation
The syntax for string interpolation is the following:
```
$"A dollar sign preceding the quotes to mark the start of the string and allowance of the interpolation of {variables} within the {string} which can contain programmatic values or, I believe, logic?"
```

### Getting Info about string:
`someWord.IndexOf()` If the substring included in the single argument exists `someWord`, its index is returned. Since positioning starts at 0, the second thing in the string will return a 1. ** If it doesn’t exist in the string the method will return a -1**. If we pass it an empty string, it will return 0. If it occurs more than once, it will return the first instance.

`someString.Length;`: returns lengths

`Substring();`

*Indexes and substrings*
`someString.IndexOf("avacoado")`: this will return the index of the start of avacado
`someString.Substring(12)`: will return everythin in the string *past* the specified index point.

`.ToUpper()`
`.ToLower()`

--------
<br>

# Logical Operators
And, or, not, equals;
```
&&
||
!
==
```

### Switch Statements:
```
string color;  
  
switch (color)  
{  
 case "blue":  
 // execute if the value of color is "blue"  
 Console.WriteLine("color is blue");  
 break;  
 case "red":  
 // execute if the value of color is "red"  
 Console.WriteLine("color is red");  
 break;  
 case "green":  
 // execute if the value of color is "green"  
 Console.WriteLine("color is green");  
 break;  
 default:  
 // execute if none of the above conditions are met  
 break;  
}
```

--------
<br>

# Classes!


--------
<br>

# Arrays
Characteristics:
- Ordered
- All share the same (declared) data type

Declared like this:
```
int[] x;  
string[] s;  
double[] d;
```

Specifying values:
`t[] plantHeights = { 3, 4, 6 };`

The 'new' keyword:
`int[] plantHeights = new int[] { 3, 4, 6 };`

'The `new` keyword signifies that we are instantiating a new array from the array class. We’ll cover classes and instantiation in another lesson, but for now you can just think of it as another way to create an array.'  -Code Academy

If you define an array and then decide to initialize it later, you *must* use the `new` keyword:

```
// Initial declaration  
int[] plantHeights;  
  
// This works  
plantHeights = new int[] { 3, 4, 6 };   
  
// This will cause an error  
// plantHeights = { 3, 4, 6 };
```

The size and type (right?) of an array is fixed, and cannot be changed for the lifespan of the array.

It is possible to initialize an array with a length without specifying values. The syntax to do is the following:
`int[] plantHeights = new int[3];`

The default values for an `int[]` array is `0`, and for a `string[]` it's `null`.

So that `plantHeights` above will end up being equal to `[0,0,0]`

### Properties of Array
Get the length of an array:
`plantHeights.Length;`

[Array Overview by microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

### Accessing Values
`array[index]`

### Methods for Arrays
1) `Array.Sort(yourArray)`
2) `Array.IndexOf(yourArray, specificValue)`
If the value appears more than once in an array, it returns only the first occurrence within the specified range. If it cannot find the value, it returns the lower bound of the array, minus 1 (since most arrays start at 0, it’s usually -1).
3) `Array.Find()`
Where IndexOf() returns just one index, Find() actually returns the value of the result. It also seems to only return one value though, rather than all matches.

### Copying Methods for Arrays
1) .Clone();
`string[] summerStrutCopy = (string[])summerStrut.Clone();`
2) .Copy();
```
int leng = summerStrut.Length;
[] summerStrutCopy = new string[leng];
Array.Copy(summerStrut, summerStrutCopy, leng);
```

1) `Array.CopyTo()`
2) `Array.ConstrainedCopy()`
3) `Array.ConvertAll()`

**Note on what a 'Predicate' is:**
A predicate is a method that takes one input and outputs a boolean.

### Avoiding Loops
Based on what CodeAcademy has taught me, I may be using cumbersome loops too frequently when `Find()` and `IndexOf()` can be used instead much more easily.

--------
<br>

# Object and Class (and type?)
[microsoft](https://www.javatpoint.com/c-sharp-object-and-class)
`Student s1 = new Student();//creating an object of Student`
In this example, Student is the type and s1 is the reference variable that refers to the instance of Student class.

--------
<br>

# Defining Methods/Functions
[Code Academy Cheatsheet Here](https://www.codecademy.com/learn/learn-c-sharp/modules/csharp-methods/cheatsheet)
### Making parameters optional
In the following method, the punctation parameter has been made optional by using the equal sign to make it equal to a default value.
```
static void YourMethodName(string message, string punctuation = "."){  
 Console.WriteLine(message + punctuation);  
}
```

### Using Parameters by Name
`someFunction(parameterName: data);`
Named parameters can be listed in any order.

Positional arguments (non-named) arguments (also known as parameters) can be used with named arguments, but the positional arguments must come before the named arguments.

### Method Overloading
Basically, you can just write fucntions with the same name and different parameters. Because the amount of parameters taken is what makes the function unique, these funtions will actually function as functions with separate functionality, *even though* they share the same name. I'm assuming that this won't work if you declare two functions with the same name *and* the same number and type of parameters, *in the same order*. One will probably overwrite the other.

### Arguments/Parameters:
Values passed to a method are called _arguments_. When defined in the method, they are _parameters_.

### Method Output
1) *Method Declaration: Return Type*
When a method is declared, it must announce the type of value it will return. The first line of a function is called a *_method declaration_*, and it has a few parts. Let's look at this:
`static void mooseMethod(){}`
The name of the method is  'mooseMethod', but that leaves two other terms, `static`, and `void`. The second word defines the *return type* of the function. Void means *nothing* will be returned. Otherwise, you would specify `string`, `int`, `double`, etc.
<br>

2) *Method Declaration: Access Modifiers*
Static, Public, etc.

### The 'Out' Keyword
Here's how it looks in action:
`public static bool TryParse (string s, out int result);`
What's happening? Well, the out keyword is, in a complex way, allowing us to sort of recieve *two* return values, even though methods can only return one as a rule.

In this case, we're recieving one in the normal way, and we're returning the other through a variable called `result`.

When writing a method with out parameters, remember that the `out` parameter(s?) must be set to a value before the method ends.


--------
<br>

# Alternate Expressions
### Shortcuts for defining methods:
- expression-bodied definitions
- lambda expressions

Expression-bodied definitions use the `=>` arrow. They remove curly braces and the return keyword. The following function:
```
bool IsEven(int num)  
{  
 return num % 2 == 0;  
}
```

Becomes this instead:
 
`bool isEven(int num) => num % 2 == 0;`

### Passing Methods as arguments into functions
This is allowed in C#. When passed as arguments, do *not* include the `()` at the end. Just write them like a normal variable.

### Lamba Expressions
A lambda expression is a type of anonymous function that is used as soon as it is defined.

Example:
`bool hasEvenNumber = Array.Exists(numbers, (int num) => num % 2 == 0 );`

Abstract Example:
`(input-parameters) => expression`

Uses:
- fat arrow
- no curly braces (usually)
- no semi-colon (usually)

Unless you *do* want to use more than one expression (line)! Then you can use curly braces and semi-colons.

### Lambda Craziness
- Apparently sometimes the type keyword in the beginning of a Lamba can be omitted in cases where it is implied...da fuck
- And also you can omit parentheses when there is only one parameter/argument

Example:
`bool hasEvenNumbers = Array.Exists(numbers, num => num % 2 == 0 );`


--------
<br>


# Loops
```
for (int i = 0; i < 15; i++)  
{  
 AddAlien();  
}
```
Concise summary:
```
while loop: while(){..}
do...while loop: do{...}while();
for loop: for(int i=0; i<x; i++){}
foreach loop: foreach(int item in list){}
jump statements: break, continue, return
```


Types of loops:
1. while
2. do...while
3. for
4. foreach

### While loop can be useful for keymapping:
```
while (spacebar == "down")  
{  
RiseUp();  
}
```


### Jump Statements: Continue, break, return
Break stops the loop.
Continue stops the current iteration of the loop and continues to the next loop iteration.
Return also stops the loop.

"You should only use `return` if you need to exit a method, because it will break out of **all** loops. If you only want to break out of one loop and not exit a method, use `break`." - Codeacademy


---------
<br>

# Useful Functions, Basic
`capitalize()`
`square()`
`Substring()`
`IndexOf()`

--------
<br>