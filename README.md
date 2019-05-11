# gbranching
Command line utility to easily create branch names for Git from a ticket name. 

### Usage
```text
$ gbranching [-t <ticket-type>] [-n <ticket-number>] -b <branch name>
$ gbranching -b branch name 
```

### Demo
```bash
$ gbranching story 'Some new feature to implement'
story/GB-some-new-feature-to-implement

$ gbranching story 1234 'Some new feature to implement'
story/GB-1234-some-new-feature-to-implement
```
