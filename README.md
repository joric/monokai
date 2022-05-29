# Colorer Schemes


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
* Check "TrueMod enabled"
* Select "Monokai (RGB)" in TrueMod schemes.

Reload colorer with F11, Far Colorer, Reload in editor after editing/copying the files (or restart Far).

## Whitespace

Note that whitespace is buggy in the stock colorer.
It uses inverted (RGB->BGR) `def:Text` colors and can't be redefined.
You may download patched colorer with `def:Whitespace` support in the releases section.
My schemes already support this feature.
