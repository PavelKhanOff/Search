def aggregate_all(data):
    courses = []
    lessons = []
    posts = []
    users = []
    for obj in data:
        if obj['_index'] == 'courses':
            courses.append(obj['_source'])
        if obj['_index'] == 'lessons':
            lessons.append(obj['_source'])
        if obj['_index'] == 'posts':
            posts.append(obj['_source'])
        if obj['_index'] == 'users':
            users.append(obj['_source'])
    response = {
        "courses": courses,
        "lessons": lessons,
        "posts": posts,
        "users": users
                }
    return response

def aggregate(es_data,page,size, count):
    data={}
    for obj in es_data:
        index = obj['_index']
        if index not in data:
            data[index]=[]
        data[index].append(obj['_source'])
    response = {}
    response['data']=data
    response['meta']={
        "current_page": page,
        "per_page": size,
        "total_items": count,
    }
    return response

