# Overview
- 'strongly-typed' language: data types must be defined, which helps avoid errors
- 'statically-typed'
- Often very object oriented
- C# is fast -- in one case, .NET CORE is up to 2,000 times faster than Node (the leading javascript server technology.)
- Unity projects, a popular 3D/2D game-making application, are written in C#

# Links/Documentation:
[Microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/)

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

**Math**
If a less exact data type is added to a more exact one, the result will always be returned in the more exact data type.

However, two integers will always return an integer, and so on.

**Incrementing and decremting**
Incrementing by 1:
`++`
Decrementing by 1:
`--`
Incrementing by some other number, like 3:
`variable += 3`

**Modulo**
`%`

**More complex math operations:**
-   `Math.Abs()`—will find the absolute value of a number. Example: `Math.Abs(-5)` returns 5.
-   `Math.Sqrt()`—will find the square root of a number. Example: `Math.Sqrt(16)` returns 4.
-   `Math.Floor()`—will round the given double or decimal down to the nearest whole number. Example: `Math.Floor(8.65)` returns 8.
-   `Math.Min()`—returns the smaller of two numbers. Example: `Math.Min(39, 12)` returns 12.


##### Casting
There are casting functions for each variable type. For example, `(int)myDouble` will convert a double called myDouble into an int. So `(int)` is actually an operator called a "cast".

There are also methods, like `Convert.ToString()`, or `Convert.ToInt32()`

Sometimes casting will work, but it is designed to fail before it destroys any information. That's where the `Convert.ToX()` functions are useful. They are more determined.

**Checking the type of a variable**
`someVariable.GetType()`: runtime
`someVariable.typeof()`: compiletime

### Strings
Don't forget to escape quotes: `\"`
And use the escape slash to make a new line: `\n`
Note:  If we want to concatenate a string with something that is another data type, C# will implicitly convert that value to a string.

**String Interpolation**
The syntax for string interpolation is the following:
```
$"A dollar sign preceding the quotes to mark the start of the string and allowance of the interpolation of {variables} within the {string} which can contain programmatic values or, I believe, logic?"
```

*Getting Info about string:*
`someWord.IndexOf()` If the substring included in the single argument exists `someWord`, its index is returned. Since positioning starts at 0, the second thing in the string will return a 1. ** If it doesn’t exist in the string the method will return a -1**. If we pass it an empty string, it will return 0. If it occurs more than once, it will return the first instance.

`someString.Length;`: returns lengths

`Substring();`

*Indexes and substrings*
`someString.IndexOf("avacoado")`: this will return the index of the start of avacado
`someString.Substring(12)`: will return everythin in the string *past* the specified index point.

`.ToUpper()`
`.ToLower()`

### Logical Operators
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

### Arrays
[Array Overview by microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

Example One

```
class TestArraysClass
{
    static void Main()
    {
        // Declare a single-dimensional array of 5 integers.
        int[] array1 = new int[5];

        // Declare and set array element values.
        int[] array2 = new int[] { 1, 3, 5, 7, 9 };

        // Alternative syntax.
        int[] array3 = { 1, 2, 3, 4, 5, 6 };

        // Declare a two dimensional array.
        int[,] multiDimensionalArray1 = new int[2, 3];

        // Declare and set array element values.
        int[,] multiDimensionalArray2 = { { 1, 2, 3 }, { 4, 5, 6 } };

        // Declare a jagged array.
        int[][] jaggedArray = new int[6][];

        // Set the values of the first array in the jagged array structure.
        jaggedArray[0] = new int[4] { 1, 2, 3, 4 };
    }
}
```

Example 2

```
string sentence = "Hwello";

char[] charArr = sentence.ToCharArray();

foreach (char ch in charArr)

{

Console.WriteLine(ch);

}
```

### Object and Class (and type?)
[microsoft](https://www.javatpoint.com/c-sharp-object-and-class)
`Student s1 = new Student();//creating an object of Student`
In this example, Student is the type and s1 is the reference variable that refers to the instance of Student class.

## Defining Methods/Functions


# Useful Functions, Basic
`capitalize()`
`square()`
`Substring()`
`IndexOf()`
