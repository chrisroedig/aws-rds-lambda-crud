from models import Climb
import controllers

def lambda_handler(event, context):
    # NOTE: requires mapping template on API gateway 
    path = event['context']['resource-path'][1:].replace("/","_")
    method = event['context']['http-method'].lower()
    params = event['body_json']
    query_params = event['params']['querystring']


def dispatch_method(method, path, params, query_params):
    # NOTE: worst router ever
    resource_name = path.split("/")[-1].title()
    method_name = method.lower()
    controller = getattr(controllers, f'{resource_name}')(params, query_params)
    getattr(controller, method_name)()
    
if __name__ == '__main__':
    dispatch_method("POST", "/climbs", {}, {})