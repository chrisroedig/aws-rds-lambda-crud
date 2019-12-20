# serverless CRUD API

Trying to see how far we can get without a server or any money...

**Experiment: I would not recomend using any of this for a real/serious application**

The main purpose is to have a simple way to put day-to-day things into a PG database via a conventional REST API.

## AWS Stack

* AWS RDS (postgres free tier)
* AWS lambda (python)
  * role must have `AWSLambdaVPCAccessExecutionRole`
  * must must share security group for RDS instance
* AWS API gateway 
  * mapping template to pass along path, method and query params
  
## Application

* python 3.7
* orator - active reocrd ORM
* simple router and controller
