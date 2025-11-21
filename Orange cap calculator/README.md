# Orange Cap Calculator – Mini Python Project

This project calculates the **total runs scored** by each cricket player across multiple test matches and determines the player who wins the **Orange Cap** (highest run scorer).

It uses Python dictionaries to store player statistics and processes them using a custom function.

---

## Features

- Stores match-wise run data inside a nested dictionary  
- Calculates **total runs** scored by each player  
- Finds the **highest run scorer**  
- Returns the player's name and total score  
- Easy to extend for multiple matches and players  

---

## Python Concepts Used

- Dictionary traversal  
- Nested dictionary access  
- Conditional checks (`if-else`)  
- Function with return value  
- Loops (`for` loop)

---

## Code Explanation

- `orange_cap(d)`  
  - Accepts match data as a dictionary  
  - Calculates cumulative runs into `total` dictionary  
  - Determines the highest scorer using comparison logic  
  - Returns a tuple: `(top_player_name, top_score)`

Example dictionary format:
```python
{
 "test1": {"Player1": score, "Player2": score},
 "test2": {"Player1": score, "Player3": score}
}
