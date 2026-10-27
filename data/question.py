import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = '123456'

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn

# DATE_TRUNC ile ay bazlı kayıt sayılarını listele
def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT DATE_TRUNC('month', e.enrollment_date), COUNT(*) AS count_
FROM students AS s
JOIN enrollments AS e
ON s.Student_id=e.student_id
JOIN courses as c
ON c.course_id=e.course_id
GROUP BY DATE_TRUNC('month',e.enrollment_date)
ORDER BY DATE_TRUNC('month',e.enrollment_date);
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# DATE_PART ile sadece kayıtların yıl bilgisini al
def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""SELECT DATE_PART('year', enrollment_date) from enrollments;""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Tüm öğrencilerin yaşlarının toplamını dönen bir sql sorgusu yaz.
def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT SUM(age) from students;
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Tüm kurs sayısını bul
def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(course_id) from courses;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Yaşı ortalama yaştan büyük olan öğrencileri getir
def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM students
WHERE age> (SELECT AVG(age) FROM students)
ORDER BY student_id;
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kursun en eski kayıt tarihini bul
def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    
SELECT c.course_id, MIN(e.enrollment_date) as first_enrollment
FROM students as s
JOIN enrollments as e
ON s.student_id=e.student_id
JOIN courses as c
ON c.course_id=e.course_id
GROUP BY c.course_id
ORDER BY c.course_id;
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kurs için öğrencilerin ortalama yaşlarını bulun. 
# Sorgu course_name ve ortalama yaş(avg_age) değerlerini dönmelidir.
def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT c.course_name, AVG(s.age) as avg_age
FROM students as s
JOIN enrollments as e
ON s.student_id=e.student_id
JOIN courses as c
ON c.course_id=e.course_id
GROUP BY c.course_id
ORDER BY c.course_id;
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# En genç öğrencinin yaşını getiren sorguyu yazınız.
def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT MIN(age) from students;
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Her derse kayıt olmuş öğrenci sayısını bulunuz.
def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT c.course_name, COUNT(s.student_id) as student_count
FROM students as s
JOIN enrollments as e
ON s.student_id=e.student_id
JOIN courses as c
ON c.course_id=e.course_id
GROUP BY c.course_id
ORDER BY c.course_id;
""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#Tüm kayıt olunmuş derslerin sadece isimlerini getirinz.
def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT c.course_name
FROM students as s
JOIN enrollments as e
ON s.student_id=e.student_id
JOIN courses as c
ON c.course_id=e.course_id
GROUP BY c.course_name
ORDER BY c.course_name;

""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
