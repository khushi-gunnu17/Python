# pip install pymongo

# import pymongo
from pymongo import MongoClient

from bson import ObjectId

client = MongoClient("mongodb+srv://khushigunnu17:khushigunnu17@cluster0.orjmrbm.mongodb.net/", tlsAllowInvalidCertificates = True)
# Not a good idea to include password and username in code files
# tlsAllowInvalidCertificates = True - Not a good way to handle ssl

db = client['ytmanager']

video_collection = db["videos"]

print(video_collection)

# functions now
def list_all_videos() :
    for video in video_collection.find() :
        print(f"ID : {video['_id']}, Name : {video['name']} and Time : {video['time']}")


def add_video(name, time) :
    video_collection.insert_one({"name" : name, "time" : time})


def update_video(video_id, new_name, new_time) :
    video_collection.update_one(
        {'_id' : ObjectId(video_id)},
        {"$set" : {"name" : new_name, "time" : new_time}}
    )


def delete_video(video_id) :
    video_collection.delete_one({"_id" : ObjectId(video_id)})


def main() :
    while True :
        print('\nYoutube Manager app with DB.')
        print('1. List all Youtube Videos ')
        print('2. Add a Youtube Video ')
        print('3. Update a Youtube Video ')
        print('4. Delete a Youtube Video ')
        print('5. Exit the app ')

        choice = input('Enter your choice : ')


        if choice == '1' :
            list_all_videos()

        elif choice == '2' :
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)

        elif choice == '3' :
            video_id = input("Enter video id to update. : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id, name, time)

        elif choice == '4' :
            video_id = input("Enter video id to delete. : ")
            delete_video(video_id)

        elif choice == '5' :
            break

        else :
            print("Invalid choice.")



if __name__ == '__main__' :
    main()

# BSON - in object notation