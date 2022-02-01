SELECT n.Name, n.StudentID
FROM name_table n
JOIN mark_table m ON n.StudentID=m.StudentID
-- Student ids are unique, so the query will return a single Total_marks value
WHERE m.Total_marks>(SELECT Total_marks FROM mark_table WHERE StudentID='V002');