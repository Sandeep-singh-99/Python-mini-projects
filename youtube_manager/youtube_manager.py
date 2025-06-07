
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.loads(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos,file)

def list_all_videos(video):
    for index, video in enumerate(video, start=1):
        print(f"{index}. {video['name']}, Duration:  {video['time']}")

def add_video(video):
    name = input('Enter video name: ')
    time = input("Enter video time")
    video.append({'name': name, 'time': time})
    save_data_helper(video)

def update_video(video):
    pass

def delete_video(video):
    pass

def main():
        videos = load_data()
        while True:
            print("\n Youtube Manager | choose an option")
            print("1. List a favourite videos")
            print("2. Add a youtube video")
            print("3. Update a youtube video details")
            print("4. Delete a youtube video")
            print("5. Exit the app")
            choice = input("Enter your choice: ")
            print(videos)

            match choice:
                case '1':
                    list_all_videos(videos)
                case '2':
                    add_video(videos)
                case '3':
                    update_video(videos)
                case '4':
                    delete_video(videos)
                case '5':
                    break
                case _:
                    print("Invalid choice")

if __name__ == '__main__':
    main()