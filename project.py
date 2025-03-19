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
            print("Wrong. Should be python3 project.py import [file_name]")
        else:
            import_data(params[0])
    
    # 2
    elif command == "insertViewer":
        pass
        # insert_viewer(*params)
    
    # 3
    elif command == "addGenre":
        pass
        # add_genre(*params)

    # 4
    elif command == "deleteViewer":
        pass
        # delete_viewer(*params)
    
    # 5
    elif command == "insertMovie":
        pass
        # insert_movie(*params)
    
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
