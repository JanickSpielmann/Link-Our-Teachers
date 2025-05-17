WITH WordCount AS (
    SELECT
        unnest(string_to_array("Beschreibung", ' ')) AS Word
    FROM event
)
SELECT 
    c.name AS Word, 
    COUNT(*) AS WordCount,
    c.latitude,
    c.longitude
FROM WordCount wc
INNER JOIN cities c ON wc.Word = c.name
GROUP BY c.name, c.latitude, c.longitude
ORDER BY WordCount DESC;