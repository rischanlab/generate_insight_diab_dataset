#!/usr/bin/python
import psycopg2 as pg

def config_data(db):
	conn = pg.connect(dbname=db, user= "postgres", password="xx")
	cur = conn.cursor()
	return cur