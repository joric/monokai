# Colorer Schemes

Monokai-like Far Manager color schemes

![python](misc/solution.png)

## Installation

### HRC

```
copy *.hrc %FARHOME%\Plugins\FarColorer\base\auto\
```

### HRD

```
copy *.hrd %FARHOME%\Plugins\FarColorer\base
copy *.xml %FARHOME%\Plugins\FarColorer\base

```

* Open editor file, press F11, select Far Colorer, Configure, Main settings
* Set "Users file of color styles" to `%FARHOME%\Plugins\FarColorer\base\catalog-user.xml`
* Select "Monokai" in schemes.

Reload colorer with F11, Far Colorer, Reload in editor after editing/copying the files (or restart Far).

### Color settings

With conemu you can use monokai colors both in a console and in an RGB mode. Console is recommended.

* Use `Far.exe /import far-colors.farconfig` to import color settings
* Copy/paste conemu-colors.xml to conemu xml (you should try conemu)

It's also possible to adjust console colors in the Far Manager application shortcut.

## Whitespace

Note that whitespace color is buggy in the stock colorer in the RGB mode,
it uses inverted (RGB->BGR) `def:Text` colors. You may download patched colorer
with `def:Whitespace` support in the [releases](https://github.com/joric/colorer-schemes/releases) section.
My schemes already support this feature.
You don't really need it though, default whitespace color in 16-color mode looks fine.

