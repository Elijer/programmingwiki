# Unity

### [Speeding Up Compile Times](https://www.youtube.com/watch?v=eovjb5xn8y0)


### Emulating "Seeing"
How to test if a character can "see" something?

[There's this thread](https://answers.unity.com/questions/8003/how-can-i-know-if-a-gameobject-is-seen-by-a-partic.html)

[And also this one](https://answers.unity.com/questions/720447/if-game-object-is-in-cameras-field-of-view.html)

### Vector3 Data Type
**Vector3.magnitude**
I think this takes two points and tells you how far away you are? Check the docs.

**Vector3.Dot(Vector A, Vector B**
Basically just multiplies two vectors together. If the product of all three dimensions is 0, it means that the vectors are perpendicular.

**Vector3.Cross(Vector A, Vector B**

### Worldspace vs. Local space

### 'Transform' data type
['Position, rotation and scale of an object.'](https://docs.unity3d.com/ScriptReference/Transform.html)

Every object in a scene has a transform.

### Excluding Files
In Unity, it can be super annoying to have a `.meta` file for every normal `cs` file you have.  Unity needs them, but as far as I know, I don't. VS code allows you to hide certain file types, and there are some it already hides by default, like `.git` files. First, open your settings with the hotkey `Command + ,` on mac. That's Command and the comma key. Then search `exclude` in the search bar, which will show a result with the header `files:exclude`. There will be a list of excluded files. In order to exclude `.meta` files for example, add this line to that list:
`**/*.meta`. That's it!

### Attribute Drawers
Unity has included something called AttributeDrawers, which allow you to customize the look and feel of public variables you've exposed to the Unity Inspector in the editor. Here are some quick and useful ones:
```
[Header("Vision")]

[Range(0.1f, 30.0f)] public float lineOfSight = 3.6f;

[Range(0.0f, 1.5f)] public float vertRange = 0.4f;

[Range(4.0f, 90.0f)] public float windowOfSight = 32.0f;
```
See that stuff in between the square brackets? The one with `[Header]` specifies a label for a bunch of variables, keeping them visually organized. Then the `[Range]` one specifies that instead of the default number field, you'd like to display a variable as a value on a slider that you can easily push back and forth to customize the value. This is useful because it conveniently encodes the value of the limits on either side as well. Maybe you know a value of more than say, `1400` will crash a program. Set the limit of te slider at 1000 and you can rest easy, even if you open the project a few months later.

However, sometimes you'll want to make your *OWN* attribute drawers with special characteristics. I don't know too too much about this, but I did create one really useful one according to someone elses's guidance:

```
using UnityEditor;

  

// This stuff is to create a public, non-editable (through inspector) field

public class ReadOnlyAttribute : PropertyAttribute {}

  

[CustomPropertyDrawer(typeof(ReadOnlyAttribute))]

public class ReadOnlyDrawer : PropertyDrawer {

  

public override float GetPropertyHeight(SerializedProperty property, GUIContent label){

return EditorGUI.GetPropertyHeight(property, label, true);

}

  

public override void OnGUI(Rect position, SerializedProperty property, GUIContent label){

GUI.enabled = false;

EditorGUI.PropertyField(position, property, label, true);

GUI.enabled = true;

}

}
```

Just create this file, name it something like ReadOnlyAttribute and put it in a few folder in your Assets directoy. Call it Attributes. You'll want to separate files like this so that if you ever write Assembly Directives, the editor files are already grouped together. Also for production I guess; since this is editor-only behavior, you don't want it bloated down the game you end up shipping as the player won't be using the Unity Editor to play it.

For more on creating AttributeDrawers, [here's where I found this solution.](https://forum.unity.com/threads/how-do-you-disable-inspector-editing-of-a-public-variable.142100/)