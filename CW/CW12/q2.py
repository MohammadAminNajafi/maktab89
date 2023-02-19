import sys

profile = sys.argv
if len(profile)>=3:
    try:
        assert isinstance(int(profile[3]),int)
        print(f"Welcom {profile[1]} {profile[2]} with age of {profile[3]}")
    except AssertionError:
        print("age must be a number")
    except IndexError:
        print(f"Welcom {profile[1]} {profile[2]}")
else:
    print("please enter firstname and lastname")

