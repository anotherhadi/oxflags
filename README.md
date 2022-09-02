# 0xFlags  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">

A Handy Package to Parse Command-Line Arguments

# Installation :

From pip :

```bash
pip3 install oxflags
```

From source :

```bash
git clone https://github.com/0x68616469/oxflags/
```

### Requirements :

[oxansi](https://github.com/0x68616469/oxansi/)
[oxtables](https://github.com/0x68616469/oxtables/)
(downloaded automatically with pip)

# Example :

```python
from oxflags import Flag

flag = Flag(description="A Handy Package to Parse Command-Line Arguments, made by @0x68616469")

flag.new(short="-e", full="--example", type="string", default="Default string", help="Description/Usage")
flag.new(full="--age", required=True, type="int", default=None)
flag.new(short="-y", full="--yes", type="bool")

flag.parse()

print(f"Example: {flag.example}")
print(f"Age : {flag.age}")
print(f"Yes : {flag.yes}")

# $ python3 test.py --age 10 -y
# Example: Default string
# Age : 10
# Yes : True
```

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/0x68616469)