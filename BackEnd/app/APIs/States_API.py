from Backend.app import application,db
from Backend.app.Models import States
from flask import request
import uuid


@application.route('/api/states')
def get_all_states():
    states = States.query.all()
    if states:
        state_list=[]
        for state in states:
            print(f'state name: {state.state_name}')
            state_dict={}
            state_dict['state_code']=state.state_code
            state_dict['state_name']=state.state_name
            state_dict['country']=state.country
            state_list.append(state_dict)
        return {"states": state_list}
    else:
        return {"message": "No states Available"}

@application.route('/api/state', methods=['POST'])
def add_state():
    body = request.json
    state = States(
        uuid.uuid4(),
        body['state_name'],
        body['country']
    )
    db.session.add(state)
    db.session.commit()
    return {"message": "New state added successfully"}