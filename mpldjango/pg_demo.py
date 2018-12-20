import psycopg2
import matplotlib.pyplot as plt


conn = psycopg2.connect(database="udd")
cur = conn.cursor()

query = """
select to_char(date AT TIME ZONE 'UTC', 'HH24'), count(*)
  from upload_history
  where to_char(date, 'YYY') = '2018'
  group by 1
  order by 1"""

cur.execute(query)
data = cur.fetchall()

cur.close()
conn.close()

hours, uploads = zip(*data)

plt.plot(hours, uploads)
plt.xlim(0, 23)
plt.xticks(range(0, 23, 2))
plt.grid()

plt.title("Debian packages uploads per hour in 2018")
plt.xlabel("Hour (in UTC)")
plt.ylabel("No. of uploads")

