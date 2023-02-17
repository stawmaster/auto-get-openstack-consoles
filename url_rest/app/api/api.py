import json




def read_consoles():
    
    with open('data/consoles.json') as stream:
        consoles = json.load(stream)

    return consoles

def replace_placeholders(template,**kwargs):
    return template.format(**kwargs)

def check_args(template_id,**placeholders):
    with open('data/templates.json') as stream:
        templates = json.load(stream)

    for template in templates:
        if(template['template_id'] == template_id):
            if (template['number_of_placeholders'] == len(placeholders)):
                return True
            else:
                print('wrong number of placeholders')
                return False
        
    print('non existant id, template unavailable')
    return False

def replace_args(template_id,**placeholders):
    if(check_args(template_id,**placeholders)==False):
        return False
    else:
        with open('data/templates.json') as stream:
            templates = json.load(stream)

        for template in templates:
            if(template['template_id']==template_id):
                finalstr=replace_placeholders(template['string'],**placeholders)
        return finalstr

def respond(payload):
    with open('data/templates.json') as stream:
        templates = json.load(stream)
    
    tid = payload['template_id']
    placeholders = payload['arguments']

    # print('CALL OK')

    for template in templates:
        if template['template_id'] == tid:
            if(check_args(tid, **placeholders)):
                # print('check OK')
                return replace_args(tid,**placeholders)