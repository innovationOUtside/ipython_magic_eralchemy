# ipython_magic_eralchemy
IPython magic to display ERD diagrams produced by `eralchemy`

`pip install --upgrade --no-deps git+https://github.com/innovationOUtside/ipython_magic_eralchemy.git`

Usage:

```
%load_ext eralchemy_magic


%erd --connection_string sqlite:///amagicdemo.db
```



See also: [updated eralchemy to use Crows Foot ERD style](https://github.com/psychemedia/eralchemy)