# serverless CRUD API

Trying to see how far we can get without a server or any money...
Postgres REST CRUD lambda for various thing I track via a database.

## AWS Stack

* AWS RDS (postgres free tier)
* AWS lambda (python)
  * role must have `AWSLambdaVPCAccessExecutionRole`
  * must must share security group for RDS instance
* AWS API gateway 
  * mapping template, to pass along path, method and query params
  
## Application

* python 3.7
* orator - active reocrd ORM
* simple router and controller
