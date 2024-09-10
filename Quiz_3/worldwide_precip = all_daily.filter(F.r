worldwide_precip = all_daily.filter(F.col('ELEMENT') == 'PRCP')

worldwide_precip = worldwide_precip.withColumn("year", F.substring(F.col("DATE").cast("string"), 1, 4))

worldwide_precip = worldwide_precip.withColumn("country", F.substring(F.col("ID").cast("string"), 1, 2))




avg_measurement_by_year_country = worldwide_precip.groupBy("year", "country") \

    .agg(F.avg("VALUE").alias("avg_measurement"))


worldwide_precip.show()

avg_measurement_by_year_country.show()

avg_measurement_by_year_country.write.csv(USER_DIRECTORTY + "/rainfall_by_year_country_new.csv", header=True, mode="overwrite")

​