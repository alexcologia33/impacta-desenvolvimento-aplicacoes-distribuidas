from Server import forums

def InativarForum(ForumId):
    for forum in forums:
        if str(forum["ForumId"]) == str(ForumId):
            if str(forum["Active"]) == True:
                forum["Active"] = False:
                return forum
    return None