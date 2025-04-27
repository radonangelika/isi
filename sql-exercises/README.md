# SQL Exercises - Core Features

## exercise-01
**Treść zadania:**  
Write a SQL query to select the sex and body mass columns from the little_penguins in that order, sorted such that the largest body mass appears first.

**Zapytanie SQL:**
```sql
SELECT
    sex,
    body_mass_g
FROM
    little_penguins
ORDER BY
    body_mass_g DESC;

**Zrzut ekranu:**
![exercise-01](./screenshots/exercise-01.png)
