# Types of SQL (Relational) Database Management Systems
- MySQL
- Postgres (PostgreSQL)
- SQLite
- GraphQL?

-----

# MySQL and Posgres
Heavier Database management systems, usually where the database is running on its own server

-----

# SQLite
Doesn't have it's own server. All data is stored as a single file, so probably the configuration is a bit simpler.

----

# SQLite Data Types
- TEXT
- INTEGER
- REAL (has decimals)
- NUMERIC (not really an integer or real number, but dates or booleans)
- BLOB (Binary large object; file, media, etc.)

-----

# MySQL Data Additional Types
- CHAR(size) (which takes an argument for how many characters should be alloted to this type)
- VARCHAR(size) (variable length, )
- SMALLINT
- INT
- BIGINT
- FLOAT
- DOUBLE

-----

# SQLite Syntax
### Creating a table
```
CREATE TABLE flights (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	origin TEXT NOT NULL,
	destination TEXT NOT NULL,
	duration INTEGER NOT NULL
)
```

### Constaints
CHECK: obey a certain condition, like make sure it's between a range of values
DEFAULT
NOT NULL
PRIMARY KEY
UNIQUE

### Empty space
You tell SQL where a line ends with the semicolon, which means that you can add blank space and line breaks wherever you want for legibility and...*style*.

### Adding Data (inserting)
```
INSERT INTO flights
(origin, destination, duration)
VALUES ("New York", "London", 415);
```
And let's just write that all on one line to see how it looks:
```
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);
```
So it's like INSERT INTO (our variable name) these fields (list the fields) using these values (list the values).

## Getting Data out
You're probably going to use a select query
`SELECT * FROM flights;`
This would return EVERYTHING form this table named flights. You're probably not going to want to do that.
`SELECT origin, destination FROM flights;`
This still selects ALL of the rows, but it only selects the origin and destination columns.
`SELECT * FROM flights WHERE id = 3;`
So this one is saying only find the flights were the id is equal to 3. So as long as the ids are unique, this should only return one row. Here's another example:
`SELECT * FROM flights WHERE origin = "New York";`
And it looks like we can note here that all commands are uppercase while all of the data indicators are lowercase.

## SQLite CLI Commands
`touch flights.sql`
This isn't part of the command line, but because SQLite is only using files to store tables, we can create a file where we will store out table this way.
`sqlite3 flights.sql`
I think this is how we actually open a sql file with SQLite, (SQLite3 in this case), so that now you are in the SQLite prompt.

Now we can go ahead and create the table in the file using the SQLite CLI tool and the normal SQL syntax that is used above in the adding data header.
```
CREATE TABLE flights (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	origin TEXT NOT NULL,
	destination TEXT NOT NULL,
	duration INTEGER NOT NULL
	);
```

Now if you type `.tables`, you will shown all of the tables in your database.

Now you could do `SELECT * FROM FLIGHTS` to see if there is any data inside of fights, which of course there isn't.

If you do have data in there and try to return it though, it'll be kinda ugly and hard to read. To format the data that gets returned, try this:

`.mode columns`
`.headers yes`

That'll make it look nicer.

Let's try to get something specific again:

`SELECT * FROM flights WHERE origin = "New York"`

### Other Types of Query
The where keyword can be used with boolean expressions.
`WHERE duration > 500;`
`WHERE duration > 500 AND destination = 'Paris';`

Or you could have used `OR`.

Then there's this one:

`SELECT * FROM flights WHERE origin IN ("New York", "Lima");`, where as long as origin is one of those two, it will be returned.

Here's some regular expression shit:

`SELECT * FROM flights WHERE origin LIKE "%a%";`

The percent sign stands as a sort of wildcard, where it represents 0 or more characters of any kind. So I guess strings that could match this would be "asparagus", "instead of the last", or just "a".

SQL also has a bunch of built-in functions for averages, sums, stuff like that. So I guess those are for getting data ABOUT your data.

### Updating Data
`UPDATE flights
	SET duration = 430
	WHERE origin = "New York"
	AND destination = "London";
`

### Deleting Data
`DELETE FROM flights WHERE destination = "Tokyo";`

### Other Clauses for data adding/deleting/whatever operations
`LIMIT`
`ORDER BY`
`GROUP BY`
`HAVING`


### Foreign Keys
'Normalizing' data apparently means to separate things out into separate tables so that the data is more organized and less redundant.

### One-to-One vs. Many-to-Many relationships
35:54 of the lecture

The solution? Use an association table. No, not arrays. One problem with this? Super hard to read...you can't just read it by looking at all these foreign keys!

Luckily, SQL has a way to make this easier. It's called a `JOIN` query.

### The Join Query

```
SELECT first, origin, destination
FROM flights JOIN passengers
ON passengers.flight_id = flights.id
```
Note: first stands for 'first name'.

So the first line is about which columns to select.
The second line is about which two tables to join.
Then third line is about what id is to be used in order to link each row from one table to a row from another table.

The "hold up" moment for me in this is that first line; it's like wait, if we're just selecting columns from multiple tables, how does that work?

But it mostly makes sense to me now. Normally you do `SELECT {fields} FROM {tableName}`. But here, where `{tableName}` would normally be, we're actually *creating* a table out of two tables. It's not super clear from the syntax what the 'order of operations' is here, but to me it looks like the join is done BEFORE the `FROM` keyword gets looked at at all by SQL. By extension of that logic, the `ON` keyword must also get looked at before the `FROM` keyword because it looks like it's probably crucial to make the join happen in the way you would want.

So that's pretty cool! For all intents and purposes, we are querying columns from a single table, even though we have actually split that table into many other tables for organizational purposes. Full circle!

There are a few types of join queries. The one above is the 'default join', or the `INNER JOIN` which can just be specified with the keyword `JOIN`. There are also these;
- `LEFT OUTER JOIN`
- `RIGHT OUTER JOIN`
- `FULL OUTER JOIN`

What's right and left here? Outer? An inner join compares two tables, analyzes them based on the conditions given, and then only returns full matches. A left outer join, I think, means that everything on the left is preserved AS WELL AS any matches it has with the right, and vice versa. And then a full outer join just return everything, even if there aren't matches.

### Query Optimation / Index
What's an index? Well it's like the one in a book. An index on a table is an additional datastructure that can be constructed, and then maintained automatically, and it allows querying to be much more efficient.

`CREATE INDEX name_index ON passengers (last)`

This index, called `name_index`, will somehow make it faster to select rows based on last name.

### Security
**Sequel Injection Attack:**
In SQL, a '--' will comment out the rest of a line. It turns out that strings can be injected in queries as if they were written straight into the CLI. So if you make your username "hacker"--" then you might end up automatically inserting this comment into a SQL command done automatically at login, and comment out the rest of the line.

How to solve this?

Well, you could escape special characters so they are only ever used as strings.

OR you could use a higher level system like Django to just make sure that nothing malicious can get into SQL.

**Race Conditions**
These can happen while queries are made to an actively changing database. You can use `transactions` to solve this proble, which lock parts of a database while that part is being written to.