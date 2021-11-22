# phone-wordlist-generator
A python script to generate a wordlist with all possible phone numbers. The output of this should be about 100GB of space.

## Running the code

First you'll want to clone the repo to your computer

```
git clone https://github.com/RaspberryProgramming/phone-wordlist-generator
```

Then simply run the main.py file

```
python3 main.py
```

## Examples

Creating list with areacode 456

```
python3 main.py --staticnum 456 --filename 456-phones.list
```

Adding US code to numbers

```
python3 main.py --prefix +1 --filename 456-phones.list
```

## Help

```
main.py --help
usage: main.py [-h] [--filename FILENAME]
               [--staticnum STATICNUM] [--len LEN]
               [--prefix PREFIX] [--benchmark]

Creates a wordlist of phone numbers

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME   Filename to write wordlist to.
  --staticnum STATICNUM
                        First few numbers that stay
                        static. Ex: you want 123*******
                        numbers, pass 123 as argument.
  --len LEN             Full length of the phone numbers,
                        default is 10
  --prefix PREFIX       Prefix for the phone numbers, Ex:
                        +1 for US phone numbers
  --benchmark           Runs program without writing to
                        disk, used to run a benchmark.
```