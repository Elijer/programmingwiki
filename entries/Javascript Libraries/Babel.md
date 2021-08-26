# Wtf is Babel?
Babel is a javascript compiler or transpiler. What does it do? It takes the latest version of javascript and it converts them back to ES5 so that you can use lots of cool features in modern JS while still having full compatibility with all browsers.

If you go to babel's website, you can actually try this out by writing ES6 code or something in a code-box on the left and it will translate it into ES5 on the right.

Copying and pasting all the time is gonna suck though. So how do you make it automatic?

## Setting up Babel in a project
Let's use npm. First, initialize npm:

```javascript
npm init -y
```

Let's do an npm install of two things, the babel CLI and a babel preset.

```javascript
npm i --save-dev babel-cli babel-env-preset
```

Once the install is complete, we should see it in our **package.json** file.

These packages are what will actually let you run commands to tell babel to compile things.

Before we do that, though, we're probably going to need to do some project organization like this;

Create an `src` folder and a `js` folder. Then you can write your fancy javascript in the `src` folder and tell babel to transpile it to the `js` folder.

Creat your `index.html` file and make sure that it is linking to the javascript in your `js` folder. It will be linking to a file that doesn't exist yet, of the same name as the one that *does* exist in your `src` folder.

But we haven't told the CLI to do anything yet. To make things easier, let's create an npm command in our package.json file. For anyone not familiar with this, basically npm has a widely used feature in which you can create you own commands by simply adding them into your package.son. The default `test` script can be run by simply running the `npm test` command, and every other command that isn't test can be run with `npm run {nameOfYourScriptHere}`.

Let's create an npm command called 'build':

`build: babel src -d js`
							/			   \
					 entry            output
As you can see, we are giving babel in entry folder and an output folder. This instructs babel to take everything in our `src` folder and transpile them into new files of the same name in `js`. That's one way of doing things. If these arguments can be summarized as
"folder : folder" We could also do the following instead:

1. "folder/file : folder/file"
2. "folder : folder/file"

This second option will tell babel to take all the files in one folder and put them into a *single* compiled file as an output, which may come in handy when using ES6 modules.

When you run a `babel` command like this, through npm or through the command line or whatever, it will look for a `.babelrc` file so it nows how exactly you want it to do things.

## The BabelRC File; `.babelrc`
It's basically a json file.

Presets is one array that can be in our .babelrc jason:

```json
{
	"presets": ["env"]
}
```

Where `env` is a shortcut for saying that you want to compile everything from ES2015, ES2016 and ES2017 and the latest. So it is an abbreviation for all four of those settings:

```json
{
	"presets": ["es2015", "es2016", "es2017", "latest"]
}
```

But just saying "env" is obviously easier.

Other things we can do inside of our `.babelrc`:

Specifity targets:
`"targets: ["node": "6.10", chrome": "52"]"`
If `presets` tells babel what kind of files to transpire *from*, `targets` looks like this tells babel what to transpile them *for*.