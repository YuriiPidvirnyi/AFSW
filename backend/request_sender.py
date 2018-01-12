import json
import requests
from config import HEADERS, URI, PORT, RESOURCES


def main():
    request_type, user_input = "get_als", "10007"
    # request_type, user_input = "get_gup", "20000,20002"
    request_type, user_input = "get_mba", "10246,10575"
    # request_type, user_input = "get_ir", "10175,10042".split(",")
    # request_type, user_input = "get_likes", "10033,10062,10371,10746,10963".split(",")
    # request_type, user_input = "get_subscr", "10196"
    # request_type, user_input = "get_followers", "10196"
    # request_type, user_input = "get_shared", "10196,10001".split(",")
    # request_type, user_input = "get_updates", "10196,10001".split(",")
    print(send_get_request(request_type, user_input))

    # request_type = "put_event"
    # template = {"event": "Create", "eventTime": "2017-10-05T15:13:34.694517Z", "userId": "ADMIN",
    #             "targetEntityType": "PROJECT", "targetEntityId": "10000", "properties": {"groups": "SMLP"}}
    # print(send_put_request(template, request_type))


def send_put_request(template=None, request_type=None):
    payload = json.dumps(template, indent=4, sort_keys=True)
    url = URI + PORT + RESOURCES[request_type]
    response = requests.put(url, data=payload, headers=HEADERS)
    if not response.status_code == 200:
        return response.text + ":\t" + str(response.status_code)
    return response, payload


def send_get_request(request_type=None, user_input=None):
    url = URI + PORT + RESOURCES[request_type][0]
    query_keys = RESOURCES[request_type][1:]
    if user_input:
        if len(query_keys) == 2:
            if len(user_input) > 2:
                modified = user_input[0:1]
                modified.append(",".join(user_input[1:]))
                querystring = dict(zip(query_keys, modified))
                req = requests.Request('GET', url, headers=HEADERS, params=querystring)
                prepared = req.prepare()
                pretty_print_get_request(prepared)
                response = requests.get(url, headers=HEADERS, params=querystring)
                try:
                    response_json = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
                    return response_json
                except:
                    return response.text + ":\t" + str(response.status_code)
            else:
                querystring = dict(zip(query_keys, user_input))
                req = requests.Request('GET', url, headers=HEADERS, params=querystring)
                prepared = req.prepare()
                pretty_print_get_request(prepared)
                response = requests.get(url, headers=HEADERS, params=querystring)
                try:
                    response_json = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
                    return response_json
                except:
                    return response.text + ":\t" + str(response.status_code)
        elif len(query_keys) == 3:
            if len(user_input) > 2:
                modified = user_input[0:1]
                modified.append(",".join(user_input[1:-1]))
                modified.append(",".join(user_input[-1]))
                querystring = dict(zip(query_keys, modified))
                req = requests.Request('GET', url, headers=HEADERS, params=querystring)
                prepared = req.prepare()
                pretty_print_get_request(prepared)
                response = requests.get(url, headers=HEADERS, params=querystring)
                try:
                    response_json = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
                    return response_json
                except:
                    return response.text + ":\t" + str(response.status_code)
            else:
                querystring = dict(zip(query_keys, user_input))
                req = requests.Request('GET', url, headers=HEADERS, params=querystring)
                prepared = req.prepare()
                pretty_print_get_request(prepared)
                response = requests.get(url, headers=HEADERS, params=querystring)
                try:
                    response_json = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
                    return response_json
                except:
                    return response.text + ":\t" + str(response.status_code)
        else:
            query_key = "".join(query_keys)
            querystring = {query_key: user_input}
            req = requests.Request('GET', url, headers=HEADERS, params=querystring)
            prepared = req.prepare()
            pretty_print_get_request(prepared)
            response = requests.get(url, headers=HEADERS, params=querystring)
            try:
                response_json = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
                return response_json
            except:
                return response.text + ":\t" + str(response.status_code)
    else:
        required_param = RESOURCES[request_type][1]
        return "'{}' request parameter is required".format(required_param)


def pretty_print_get_request(req):
    print('{}\n{}\n{}\n\n{}'.format(
        '\n-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        "body: {}\n".format(req.body)
    ))


if __name__ == '__main__':
    main()
