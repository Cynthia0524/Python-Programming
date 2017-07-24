### show the variable class
type(2)

### Year-Month-Day Hour:Minute:Second
strftime("%Y-%m-%d %H:%M:%S")

### evaluate input
eval()

### "x: " <-- input a number manually
imput("x: ")

### Title format the variable
  var.title()

### True represents a condition. When it is satisfied, the loop will continue
while True:
  pass


### Filter Function
[member for member in list if list["name"] == "name" ]

https://github.com/prof-rossetti/nyu-info-2335-70-201706/blob/master/notes/programming-languages/python/datatypes/lists.md

### Open .csv
|Modes|Description|
|-----|:---------:|
|'r'  |Open a file for reading. (default)|
|'w'  |Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.|
|'x'  |Open a file for exclusive creation. If the file already exists, the operation fails.|
|'a'  |Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.|
|'t'  |Open in text mode. (default)|
|'b'  |Open in binary mode.|
|'+'  |Open a file for updating (reading and writing)|

### Another way to add a row to the csv file

```shell
with open(products_path, "a", newline='') as products_file:
    writer = csv.DictWriter(products_file,fieldnames = keys)
    new_row = csv.writer(products_file)
    new_row.writerow("")
    writer.writerow(new_product)
```
