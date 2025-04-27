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
```

**Zrzut ekranu:**
![exercise-01](./screenshots/exercise-01.png)

## exercise-02
**Treść zadania:**  
Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.

**Zapytanie SQL:**
```sql

SELECT island, species
FROM penguins
LIMIT 11 OFFSET 49;
```

**Zrzut ekranu:**
![exercise-02](./screenshots/exercise-02.png)