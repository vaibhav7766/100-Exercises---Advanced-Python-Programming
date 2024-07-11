def clean_hashtags(input_file, output_file, length):
    with open("hashtags.txt", "r") as file:
        content = file.read()
    hashtags = content.split()
    short_hashtags = [hashtag for hashtag in hashtags if len(hashtag) <= length + 1]
    result = sorted(set(short_hashtags))
    with open(output_file, "w") as file:
        for hashtag in result:
            file.write(hashtag + "\n")