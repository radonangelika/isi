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

Napisz zapytanie SQL, które wybiera kolumny island oraz species z wierszy od 50 do 60 włącznie z tabeli penguins. Wynik powinien zawierać 11 wierszy.
**Zapytanie SQL:**
```sql

SELECT island, species
FROM (
    SELECT island, species
    FROM penguins
    LIMIT 11 OFFSET 49 
);
```

**Zrzut ekranu:**
![exercise-02](./screenshots/exercise-02.png)

## exercise-03
**Treść zadania:**  
Modify your query to select distinct combinations of island and species from the same rows and compare the result to what you got in part 1.

Zmień zapytanie, aby wybierało unikatowe kombinacje island i species z tych samych wierszy i porównaj wynik z częścią pierwszą.
**Zapytanie SQL:**
```sql

SELECT DISTINCT island, species
FROM (
    SELECT island, species
    FROM penguins
    LIMIT 11 OFFSET 49
);
```

**Zrzut ekranu:**
![exercise-03](./screenshots/exercise-03.png)


## exercise-04
**Treść zadania:**  
Write a query to select the body masses from penguins that are less than 3000.0 grams.

Napisz zapytanie SQL, które wybiera masy ciała (body_mass_g) pingwinów ważących mniej niż 3000.0 gramów.
**Zapytanie SQL:**
```sql

SELECT DISTINCT island, species
FROM (
    SELECT island, species
    FROM penguins
    LIMIT 11 OFFSET 49
);
```

**Zrzut ekranu:**
![exercise-04](./screenshots/exercise-04.png)

## exercise-05
**Treść zadania:**  
Write another query to select the species and sex of penguins that weight less than 3000.0 grams. This shows that the columns displayed and those used in filtering are independent of each other.

Napisz kolejne zapytanie, które wybiera gatunek (species) i płeć (sex) pingwinów ważących mniej niż 3000.0 gramów.
**Zapytanie SQL:**
```sql

SELECT species, sex
FROM penguins
WHERE body_mass_g < 3000.0;
);
```

**Zrzut ekranu:**
![exercise-05](./screenshots/exercise-05.png)


## exercise-06
**Treść zadania:**  
Use the not operator to select penguins that are not Gentoos.

Użyj operatora NOT, aby wybrać pingwiny, które nie są gatunku Gentoo.

**Zapytanie SQL:**
```sql

SELECT *
FROM penguins
WHERE NOT species = 'Gentoo';
```

**Zrzut ekranu:**
![exercise-06](./screenshots/exercise-06.png)

## exercise-07
**Treść zadania:**  
SQL's or is an inclusive or: it succeeds if either or both conditions are true. SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on Torgersen Island but not both.

Napisz zapytanie, które wybiera pingwiny, które są: samice (sex = 'FEMALE') lub znajdują się na wyspie Torgersen (island = 'Torgersen') ale nie oba warunki jednocześnie (czyli wyłączna alternatywa, tzw. XOR).

**Zapytanie SQL:**
```sql

SELECT *
FROM penguins
WHERE (sex = 'FEMALE' OR island = 'Torgersen')
  AND NOT (sex = 'FEMALE' AND island = 'Torgersen');
```

**Zrzut ekranu:**
![exercise-07](./screenshots/exercise-07.png)

## exercise-08
**Treść zadania:**  
Write a single query that calculates and returns:

A column called what_where that has the species and island of each penguin separated by a single space.
A column called bill_ratio that has the ratio of bill length to bill depth.
You can use the || operator to concatenate text to solve part 1, or look at 


Napisz jedno zapytanie, które zwraca:

Kolumnę what_where, zawierającą gatunek (species) i wyspę (island) każdego pingwina, połączone pojedynczą spacją.

Kolumnę bill_ratio, zawierającą stosunek długości dzioba (bill_length_mm) do jego głębokości (bill_depth_mm).

**Zapytanie SQL:**
```sql
SELECT 
    species || ' ' || island AS what_where,
    bill_length_mm / bill_depth_mm AS bill_ratio
FROM 
    penguins;
```

**Zrzut ekranu:**
![exercise-08](./screenshots/exercise-08.png)