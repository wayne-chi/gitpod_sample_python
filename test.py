try:
    import psycopg2
    print ("import successful")
except Exception as e:
    print (e)
    print("import failed")