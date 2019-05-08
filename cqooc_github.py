# config
username = ''    # your username used to login
user_id = int()    # should be a integer
courseId = ''
cookie_xsid = ''    # find it in your browser after logging in
finish_time = ''    # e.g. 20181222
parentId = ''



from requests import Session

session = Session()
session.cookies['xsid'] = cookie_xsid

def fuck(courseId, sectionId, chapterId):
    endpoint = 'http://www.cqooc.com/json/learnLogs'
    payload = {
        'username': username,
        'ownerId': user_id,
        'parentId': parentId,
        'action': 0,
        'courseId': str(courseId),
        'sectionId': str(sectionId),
        'chapterId': str(chapterId),
        'category': 2,
        'time': finish_time,
    }
    #print(payload)
    return session.post(endpoint, json=payload)

def learn_course(courseId):
    endpoint = 'http://www.cqooc.com/json/chapter/lessons?courseId='+courseId
    j = session.get(endpoint).json()['data'][0]['body']
    for chapterId, sectionIds in j.items():
        for sectionId in sectionIds:
            print('learning', chapterId, sectionId)
            print(fuck(courseId, sectionId, chapterId).text)


learn_course(courseId)