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
        pass
        # insert_session(*params)
    
    # 7
    elif command == "updateRelease":
        pass
        # update_release(*params)
    
    # 8
    elif command == "listReleases":
        pass
        # list_releases(*params)
    
    # 9
    elif command == "popularRelease":
        pass
        # popular_release(*params)
    
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
