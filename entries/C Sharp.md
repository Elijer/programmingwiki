# Overview
- 'strongly-typed' language: data types must be defined, which helps avoid errors
- 'statically-typed'
- Often very object oriented
- C# is fast -- in one case, .NET CORE is up to 2,000 times faster than Node (the leading javascript server technology.)
- Unity projects, a popular 3D/2D game-making application, are written in C#

# Links

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

### Arrays
[Array Overview by microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

`class TestArraysClass
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
}`

### Object and Class (and type?)
[microsoft](https://www.javatpoint.com/c-sharp-object-and-class)
`Student s1 = new Student();//creating an object of Student`
In this example, Student is the type and s1 is the reference variable that refers to the instance of Student class.

# Functions, Basic
`capitalize()`
`square()`
