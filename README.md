# Wedding Guest List Processor

This Python program processes a structured JSON file representing a wedding guest list. It analyzes the data to generate a summary report including total guests, children, likely absences, and a breakdown by guest type and proximity level.

## 📂 Input File

The input file should be a JSON with the following structure:

```json
[
  {
    "type": "FAMILY",
    "people_by_level": [
      {
        "level": 1,
        "people": [
          {
            "name": "Alice",
            "isChild": true,
            "probably_give_up": false
          }
        ]
      }
    ]
  }
]
```

- `type`: `"FAMILY"` or `"FRIEND"`
- `level`: Proximity level (integer)
- `name`: Person's name
- `isChild`: (optional, default `false`) `true` if the guest is a child
- `probably_give_up`: (optional, `false`) `true` if the guest is likely to decline the invitation

## 🚀 How to Run

1. **Install dependencies** (if you haven't already):
   ```bash
   pip install pydantic
   ```

2. **Place your input JSON file** at the expected path:
   ```
   files/guests.json
   ```

3. **Run the program**:
   ```bash
   python main.py
   ```

4. **Outputs** will be generated in:
    - `files/output/guests_output.txt` — sorted list of unique guest names
    - `files/output/output.txt` — detailed summary report

## 📊 Output Summary

The summary file includes:
- Total number of unique guests
- Number of children
- Number of guests who will probably give up
- Number of guests who will probably attend
- Breakdown by guest type (FAMILY or FRIEND) and proximity level (1, 2, 3...)

## 🧠 Built With

- [Python 3](https://www.python.org/)
- [Pydantic](https://docs.pydantic.dev/)

## ✍️ Author

Created by [Pierre Vieira](https://github.com/PierreVieira). Feel free to reach out if you'd like to contribute or suggest improvements!
