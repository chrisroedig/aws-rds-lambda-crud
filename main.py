import psycopg2
import logging
import traceback
import settings
from os import environ


endpoint=environ.get('ENDPOINT')
port=environ.get('PORT')
dbuser=environ.get('DBUSER')
password=environ.get('DBPASSWORD')
database=environ.get('DATABASE')

query="SELECT * FROM climbs LIMIT 2"

logger=logging.getLogger()
logger.setLevel(logging.INFO)

def insert(p):
  "INSERT INTO public.climbs ( "|
  "location_type, route_ref, rope_style, yds_grade_posted, yds_grade_estimated, completed, falls, takes, created_at, updated_at, notes) 
VALUES('gym', '200', 'lead', '5.10', NULL, true, 6, 2, '2019-12-19 20:05', '2019-12-19 20:05', '');
"
'%(location_type)s',
'%(route_ref)s',
'%(rope_style)s',
'%(yds_grade_posted)s',
'%(yds_grade_estimated)s',
%(completed)i,
%(falls)i,
%(takes)i,
'%(created_at)s',
'%(updated_at)s',
'%(notes)s'
" % params_dict

def make_connection():
    conn_str="host={0} dbname={1} user={2} password={3} port={4}".format(
        endpoint,database,dbuser,password,port)
    conn = psycopg2.connect(conn_str)
    conn.autocommit=True
    return conn 


def log_err(errmsg):
    logger.error(errmsg)
    return {"body": errmsg , "headers": {}, "statusCode": 400,
        "isBase64Encoded":"false"}

logger.info("Cold start complete.") 

def handler(event,context):

    try:
        cnx = make_connection()
        cursor=cnx.cursor()

        try:
            cursor.execute(query)
        except:
            return log_err ("ERROR: Cannot execute cursor.\n{}".format(
                traceback.format_exc()) )

        try:
            results_list=[]
            for result in cursor: results_list.append(result)
            print(results_list)
            cursor.close()

        except:
            return log_err ("ERROR: Cannot retrieve query data.\n{}".format(
                traceback.format_exc()))


        return {"body": str(results_list), "headers": {}, "statusCode": 200,
        "isBase64Encoded":"false"}

    
    except:
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(
            traceback.format_exc()))


    finally:
        try:
            cnx.close()
        except:
            pass


if __name__== "__main__":
    handler(None,None)
