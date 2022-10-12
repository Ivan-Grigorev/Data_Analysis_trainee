import random
import pyspark
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import mean, stddev, round as _round, udf


import pandas as pd

from datetime import datetime, date
from faker import Faker


# sc = pyspark.SparkContext()
#
#
# def inside(p):
#     x, y = random.random(), random.random()
#     return x * x + y * y < 1
#
#
# NUM_SAMPLES = 10 ** 7
# count = sc.parallelize(range(NUM_SAMPLES)).filter(inside).count()
# approx_pi = (4.0 * count / NUM_SAMPLES)
# print(f"Pi is roughly {approx_pi}")

spark_session = SparkSession.builder.getOrCreate()
fake = Faker()

users_df = spark_session.createDataFrame(
    [
        Row(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(),
            address=fake.address(),
            salary=random.randint(2000, 15000),
            age=random.randint(25, 40),
            city=fake.city()
        )
        for _ in range(10)
    ]
)

# users_df.show()

# users_df.select(
#     mean('age').alias('average age'),
#     _round(stddev('age'), 2).alias('age stddev')
# ).show()

# users_df.corr('age', 'salary')

# users_df.groupBy('city').avg('age').show()

# users_df.groupBy('city').avg().show()

# users_df.agg({'age': 'avg'}).show()

# users_df.groupBy('city').agg({'age': 'avg'}).show()


@udf('float')
def amount_net(amount_gross: float) -> float:
    return amount_gross * 0.19


# users_df.select(amount_net(users_df.salary).alias('salary_net')).show()

# users_df.select('*', amount_net(users_df.salary).alias('salary_net')).show()

# users_df_pd = users_df.toPandas()
# print(users_df_pd)

users_df.createOrReplaceTempView('Users')
result = spark_session.sql('Select city, avg(age) From Users Group By city')
result.rdd.saveAsTextFile('results')
