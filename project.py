import sys
from functions import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 project.py <function> [params]")
        return

    # command should always be import, insertViewer, etc...
    command = sys.argv[1]

    # the parameters are everything after the initial command.
    params = sys.argv[2:]
    #print(sys.argv) 

    # 1
    if command == "import":
        if len(params) != 1:
            print("Fail")
        else:
            result = import_data(params[0])
            print(result)
    
    # 2
    elif command == "insertViewer":
        if len(params) != 12:
            print("Fail")
        else:
            uid = int(params[0])
            email = params[1]
            nickname = params[2]
            street = params[3]
            city = params[4]
            state = params[5]
            zip_code = params[6]
            genres = params[7]
            joined_date = params[8]
            first_name = params[9]
            last_name = params[10]
            subscription = params[11]

            result = insert_viewer(uid, email, nickname, street, city, state, zip_code, genres, joined_date, first_name, last_name, subscription)
            print(result)
    
    # 3
    elif command == "addGenre":
        if len(params) != 2:
            print("Fail")
        else:
            uid = int(params[0])
            genre = params[1]
            result = add_genre(uid, genre)
            print(result) 

    # 4
    elif command == "deleteViewer":
        if len(params) != 1:
            print("Fail")
        else:
            uid = int(params[0])
            result = delete_viewer(uid)
            print(result)
    
    # 5
    elif command == "insertMovie":
        if len(params) != 2:
            print("Fail")
        else:
            rid = int(params[0])
            website_url = params[1]
            result = insert_movie(rid, website_url)
            print(result)
    
    # 6 
    elif command == "insertSession":
        if len(params) != 8:
            print("Fail")
        else:
            try:
                sid = int(params[0])
                uid = int(params[1])
                rid = int(params[2])
                ep_num = int(params[3])
                initiate_at = params[4].strip('"')
                leave_at = params[5].strip('"')
                quality = params[6]
                device = params[7]
                result = insert_session(sid, uid, rid, ep_num, initiate_at, leave_at, quality, device)
                print(result)
            except ValueError:
                print("Fail")
    
    # 7
    elif command == "updateRelease":
        if len(params) != 2:
            print("Fail")
        else:
            rid = int(params[0])
            title = params[1].strip('"')
            result = update_release(rid, title)
            print(result)
        
    # 8
    elif command == "listReleases":
        if len(params) != 1:
            print("Fail")
        else:
            uid = int(params[0])
            result = list_releases(uid)
            if result == "Fail":
                print("Fail")
    
    # 9
    elif command == "popularRelease":
        if len(params) != 1:
            print("Fail")
        else:
            N = int(params[0])
            result = popular_release(N)
            if result == "Fail":
                print("Fail")
    
    # 10
    elif command == "releaseTitle":
        pass

    # 11
    elif command == "activeViewer":
        pass

    # 12
    elif command == "videosViewed":
        pass

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
