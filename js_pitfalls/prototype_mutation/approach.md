Prototype mutation

The gotcha of this problem is that the code produces unintended side-effects.

When an object is queried for a property or method, it first checks the object itself, then
then checks it's delegate prototype, all the way down the prototype chain. The prototype chain typically ends at the Object prototype.

When using prototype delegation, the properties on the prototype will act like the defaults. When you set them on the instance, the instance overrides the value
for that instance only...except:

If you mutate an object or array on the instance, that property will be shared on the prototype.

If you instead replace the entire object or array, then the instance will override it's own value and not it's prototype's value.

SO:
If using Object.create() to do prototype delegation, try not to share any non-method data (state) with the prototype, as this is considered an anti-pattern and can lead to
the unintended side-effects demonstrated in the problem.
