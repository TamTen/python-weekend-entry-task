# Python weekend entry task

Author of the solution: Petr Balazy

## Description:
The Python script processes flight data from the given .csv file (in format: flight_no, origin,destination, departure, arrival, base_price, bag_price, bags_allowed)

In the processed data, the program searches for paths from the origin to the destination according to the user's input and then finds all available flights for these paths.

The result is sorted in ascending order of the total trip price and printed in json format to the standard output.

This README is only a summary, the task specifications can be found in [TASK.md](./TASK.md).

## How to run:
usage: main.py [-h] [-b [N]] [--return] file_name origin destination

### Examples how to run script (from solution folder):
python ./main.py ../example/example3.csv WUE JBN  
python -m main ../example/example3.csv WUE JBN  

python ./main.py ../example/example2.csv IUT IUQ --bags=1 --return  
python -m main ../example/example2.csv IUT IUQ --bags=1 --return  

## Program arguments:
### Positional arguments:
| Argument          | Description                                                |
|----------------|---------------------------------------------------------------|
| `file_name`    | .csv file with data.                                          |
| `origin`       | Origin airport of the trip.                                   |
| `destination`  | The final destination of the trip.                            |

### Optional arguments:
| Argument          | Description                                                |
|----------------|---------------------------------------------------------------|
| `-h, --help`   | Show help message and exit.                                   |
| `-b [N], --bags [N]`| Number of bags for trip.                                 |
| `--return`     | Include return trip.                                          |