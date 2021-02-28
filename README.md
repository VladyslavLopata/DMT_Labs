# Labs for Decision Making Theory.

## Launching
The code was written and is meant to be launched via VSCode. So firstly, grab VSCode and Python 3.
Launch VSCode, install python extensions of your chouce and open terminal.
It is recommended to have separate venv, but you should not bother with it if you don't want to.
In order to launch the Flask Server meant for serving data to your front end, you should first run the folowing command in the terminal:

> pip install -r requirements.txt -v

After requirements get installed, you can launch the Flask application by simply pressing F5 or vie Run - Start Debugging in VSCode.

## Using
After the succesful start of the Flask server, you can request any data from the server by sending th POST request to one of the following urls:

### localhost:5000/api/lab1/
Body for POST request:
```javascript
{
  "experts" : [
    {
      "name": "Expert 1",
      "grades": [5, 3]
    },
    {
      "name": "Expert 2",
      "grades": [5, 1]
    }
  ],
  "alternatives": ["A1", "A2"]
}
```
Grades array for each expert shoud be ordered correspondingly to alternatives array.

You will get the following response:

```javascript
[
  0.46,
  0.28
]
```
Grades ARE NOT ordered. The order of grades corresponds to the order of the entered alternatives.

### localhost:5000/api/lab2/
Body for POST request:
```javascript
{
    "As": ["a1", "a2", "a3", "a4"],
    "Xs": ["x1", "x2", "x3", "x4","x5"],
    "matrix": [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [1, 2, 6, 7]
    ]
}
```
You will get the following response:
```javascript
{
    "gurvizza": [
        [
            4.8,
            "a2"
        ],
        [
            4.6000000000000005,
            "a3"
        ],
        [
            2.8,
            "a1"
        ]
    ],
    "maxmax": [
        [
            7,
            "a3"
        ],
        [
            6,
            "a2"
        ],
        [
            4,
            "a1"
        ]
    ],
    "maxmin": [
        [
            3,
            "a2"
        ],
        [
            1,
            "a1"
        ],
        [
            1,
            "a3"
        ]
    ]
}
```
The arrays DO come in ranged fassion, whereas the best alternative comes first.
### localhost:5000/api/lab3/
Body for POST request:
```javascript
{
    "alternatives": ["Vasia", "Petia", "Zhora"],
    "states": ["State1", "State2", "State3"],
    "matrix": [
        [1, 2, 3],
        [2, 3, 1],
        [3, 2, 1]
    ]
}
```
Input matrix format is provided in the lab task.

You will get the following response:
```javascript
{
    "Laplasus": [
        [
            2.0,
            "Vasia"
        ],
        [
            2.0,
            "Petia"
        ],
        [
            2.0,
            "Zhora"
        ]
    ],
    "Savidge": [
        [
            2,
            "Vasia"
        ],
        [
            2,
            "Petia"
        ],
        [
            2,
            "Zhora"
        ]
    ]
}
```
For each criteria you get a list of tuples ordered from the best to the worst. Tuple consists of criteria value and alternative name.

### localhost:5000/api/lab4/

Body for POST request:
```javascript
{
    "matrix": [
        [3, 1, 2, 4],
        [2, 3, 1, 3]
    ]
}
```
You will get the following response:
```javascript
{
    "answer": [2, 3]
}
```
