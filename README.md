# gbranching
Command line utility to easily create branch names for Git from a ticket name. 

### Usage
```text
$ gbranching [-t <ticket-type>] [-n <ticket-number>] title
$ gbranching title 
```

### Demo
```bash
$ gbranching -t story 'Some new feature to implement'
story/GB-some-new-feature-to-implement

$ gbranching -t story -n 1234 'Some new feature to implement'
story/GB-1234-some-new-feature-to-implement
```

### Make it Executable
```bash
pyinstaller -F gbranching/__init__.py -n gbranching --distpath ./bin
```
